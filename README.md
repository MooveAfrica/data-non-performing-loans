# Data Science Project

This repository contains a structured data science project following best practices.

## Project Structure

```
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external      <- Data from third party sources
│   ├── interim       <- Intermediate data that has been transformed
│   ├── processed     <- The final, canonical data sets for modeling
│   └── raw          <- The original, immutable data dump
│
├── docs             <- Documentation and reports
│
├── notebooks        <- Jupyter notebooks for exploration and analysis
│   └── 01_exploratory_data_analysis.ipynb
│
├── requirements.txt <- Project dependencies
│
├── sql             <- SQL-related files
│   ├── queries     <- SQL query files
│   └── schemas     <- Database schema definitions
│
├── src             <- Source code for use in this project
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and make predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results visualizations
│       └── visualize.py
│
└── tests            <- Test files 