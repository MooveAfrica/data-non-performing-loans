import pandas as pd
from datetime import datetime, timedelta

def create_week_calendar(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """
    Create a DataFrame with week starts and ends for a given date range.
    
    Args:
        start_date (datetime): Start date of the calendar
        end_date (datetime): End date of the calendar
        
    Returns:
        pd.DataFrame: DataFrame containing week starts, ends, and week numbers
    """
    # Create a DataFrame with week starts
    week_starts = pd.date_range(start=start_date, end=end_date, freq='W-MON')
    week_ends = week_starts + timedelta(days=6)
    
    # Create the calendar DataFrame
    calendar_df = pd.DataFrame({
        'week_start': week_starts,
        'week_end': week_ends,
        'week_number': range(1, len(week_starts) + 1)
    })
    
    # Format dates for better readability
    calendar_df['week_start'] = pd.to_datetime(calendar_df['week_start'].dt.strftime('%Y-%m-%d'))
    calendar_df['week_end'] = pd.to_datetime(calendar_df['week_end'].dt.strftime('%Y-%m-%d'))
    
    return calendar_df 