import os
import logging
from typing import Optional
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RedshiftConnection:
    def __init__(self, min_conn: int = 1, max_conn: int = 10):
        """
        Initialize Redshift connection pool.
        
        Args:
            min_conn (int): Minimum number of connections in the pool
            max_conn (int): Maximum number of connections in the pool
        """
        # Load environment variables
        load_dotenv()
        
        # Database connection parameters
        self.db_params = {
            'host': os.getenv('REDSHIFT_HOST'),
            'port': os.getenv('REDSHIFT_PORT', '5439'),
            'database': os.getenv('REDSHIFT_DATABASE'),
            'user': os.getenv('REDSHIFT_USER'),
            'password': os.getenv('REDSHIFT_PASSWORD'),
            'sslmode': 'require'
        }
        
        # Connection pool
        self.pool = None
        self.min_conn = min_conn
        self.max_conn = max_conn
        
        # Initialize connection pool
        self._initialize_pool()
    
    def _initialize_pool(self) -> None:
        """Initialize the connection pool."""
        try:
            self.pool = pool.SimpleConnectionPool(
                self.min_conn,
                self.max_conn,
                **self.db_params
            )
            logger.info("Successfully initialized Redshift connection pool")
        except Exception as e:
            logger.error(f"Failed to initialize connection pool: {str(e)}")
            raise
    
    def get_connection(self) -> Optional[psycopg2.extensions.connection]:
        """
        Get a connection from the pool.
        
        Returns:
            Optional[psycopg2.extensions.connection]: Database connection or None if failed
        """
        try:
            if self.pool:
                return self.pool.getconn()
            else:
                logger.error("Connection pool not initialized")
                return None
        except Exception as e:
            logger.error(f"Failed to get connection: {str(e)}")
            return None
    
    def return_connection(self, conn: psycopg2.extensions.connection) -> None:
        """
        Return a connection to the pool.
        
        Args:
            conn (psycopg2.extensions.connection): Connection to return
        """
        try:
            if conn and self.pool:
                self.pool.putconn(conn)
        except Exception as e:
            logger.error(f"Failed to return connection: {str(e)}")
    
    def execute_query(self, query: str, params: tuple = None) -> Optional[pd.DataFrame]:
        """
        Execute a query and return results as a pandas DataFrame.
        
        Args:
            query (str): SQL query to execute
            params (tuple, optional): Query parameters
            
        Returns:
            Optional[pd.DataFrame]: Query results as a pandas DataFrame or None if failed
        """
        conn = None
        try:
            conn = self.get_connection()
            if not conn:
                return None
            
            # Use pandas read_sql to directly convert query results to DataFrame
            df = pd.read_sql(query, conn, params=params)
            return df
                
        except Exception as e:
            logger.error(f"Failed to execute query: {str(e)}")
            return None
        finally:
            if conn:
                self.return_connection(conn)
    
    def execute_many(self, query: str, params_list: list) -> bool:
        """
        Execute the same query with different parameters.
        
        Args:
            query (str): SQL query to execute
            params_list (list): List of parameter tuples
            
        Returns:
            bool: True if successful, False otherwise
        """
        conn = None
        try:
            conn = self.get_connection()
            if not conn:
                return False
            
            with conn.cursor() as cur:
                cur.executemany(query, params_list)
                conn.commit()
                return True
                
        except Exception as e:
            logger.error(f"Failed to execute batch query: {str(e)}")
            if conn:
                conn.rollback()
            return False
        finally:
            if conn:
                self.return_connection(conn)
    
    def close_pool(self) -> None:
        """Close all connections in the pool."""
        try:
            if self.pool:
                self.pool.closeall()
                logger.info("Successfully closed all connections in the pool")
        except Exception as e:
            logger.error(f"Failed to close connection pool: {str(e)}")

def summarize_dataframe(df):
    """
    Create a comprehensive summary of a DataFrame where rows are column names
    and columns are summary statistics.
    
    Args:
        df (pd.DataFrame): Input DataFrame to summarize
        
    Returns:
        pd.DataFrame: Summary DataFrame with column statistics
    """
    # Initialize summary dictionary
    summary_dict = {}
    
    # Get basic column information
    summary_dict['data_type'] = df.dtypes
    summary_dict['non_null_count'] = df.count()
    summary_dict['null_count'] = df.isnull().sum()
    summary_dict['null_percentage'] = (df.isnull().sum() / len(df) * 100).round(2)
    summary_dict['unique_values'] = df.nunique()
    summary_dict['unique_percentage'] = (df.nunique() / len(df) * 100).round(2)
    
    # Get numeric column statistics
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) > 0:
        numeric_stats = df[numeric_cols].describe()
        summary_dict.update({
            'mean': numeric_stats.loc['mean'],
            'std': numeric_stats.loc['std'],
            'min': numeric_stats.loc['min'],
            '25%': numeric_stats.loc['25%'],
            '50%': numeric_stats.loc['50%'],
            '75%': numeric_stats.loc['75%'],
            'max': numeric_stats.loc['max']
        })
    
    # Get categorical column statistics
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(categorical_cols) > 0:
        categorical_stats = df[categorical_cols].describe()
        summary_dict.update({
            'mode': categorical_stats.loc['top'],
            'freq': categorical_stats.loc['freq']
        })
    
    # Create DataFrame from summary dictionary
    summary_df = pd.DataFrame(summary_dict)
    
    # Fill NaN values with appropriate placeholders
    summary_df = summary_df.fillna({
        'mean': 'N/A',
        'std': 'N/A',
        'min': 'N/A',
        '25%': 'N/A',
        '50%': 'N/A',
        '75%': 'N/A',
        'max': 'N/A',
        'mode': 'N/A',
        'freq': 'N/A'
    })
    
    # Round numeric columns to 2 decimal places
    numeric_summary_cols = ['mean', 'std', 'min', '25%', '50%', '75%', 'max', 
                          'null_percentage', 'unique_percentage']
    for col in numeric_summary_cols:
        if col in summary_df.columns:
            summary_df[col] = pd.to_numeric(summary_df[col], errors='ignore')
            if summary_df[col].dtype in ['int64', 'float64']:
                summary_df[col] = summary_df[col].round(2)
    
    return summary_df

# Example usage
if __name__ == "__main__":
    # Create a .env file with these variables:
    # REDSHIFT_HOST=your-cluster.region.redshift.amazonaws.com
    # REDSHIFT_PORT=5439
    # REDSHIFT_DATABASE=your_database
    # REDSHIFT_USER=your_username
    # REDSHIFT_PASSWORD=your_password
    
    try:
        # Initialize connection
        redshift = RedshiftConnection()
        
        # Example query
        query = "SELECT * FROM information_schema.tables LIMIT 5"
        results = redshift.execute_query(query)
        
        if results is not None:
            print(results)
        
        # Example batch insert
        insert_query = "INSERT INTO example_table (column1, column2) VALUES (%s, %s)"
        params_list = [('value1', 'value2'), ('value3', 'value4')]
        success = redshift.execute_many(insert_query, params_list)
        
        if success:
            print("Batch insert successful")
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
    finally:
        # Close the connection pool
        redshift.close_pool() 