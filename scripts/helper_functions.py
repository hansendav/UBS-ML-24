# Various helper functions for the create_bwi_ml_dataset.py script
# Author: David Hansen 
# Date: 27/09/2024

import os 
import sqlalchemy as sa 
import pandas as pd 
from sqlalchemy import create_engine

import yaml

import warnings

def get_conn_url_from_path(file_path):
    """Returns a connection URL for filedatabases 
    based on the database file path. (To be used within a SQLAlchemy Engine.)
    ---
    Included databases: MSAccess (*.mdb, *.accdb) + SQLite
    """
    ext = os.path.splitext(file_path)[1]

    if ext in ['.mdb', '.accdb']:
        connection_string = (
            rf"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};"
            rf"DBQ={file_path};"
            rf"ExtendedAnsiSQL=1;" # to support DECIMAL(m, n) columns in Access
        )

        # Create URL without usr and pwd 
        connection_url = sa.engine.URL.create(
        "access+pyodbc",
        query={"odbc_connect": connection_string}
        )
    elif ext == '.sqlite':
        connection_url = rf"sqlite:///{file_path}"

    return connection_url


def get_ADepth_HTypes_from_profile(df_profile):
    """Returns the depth of the A horizons and
    """
    df = df_profile[['HORIZONT', 'TIEFE_OG', 'TIEFE_UG']]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        df['HORIZONT'] = df['HORIZONT'].apply(lambda x: x[0])
        df['DEPTH'] = df['TIEFE_UG'] - df['TIEFE_OG']
        df.drop(['TIEFE_OG', 'TIEFE_UG'], axis=1, inplace=True)
    
    num_htypes = df['HORIZONT'].value_counts().shape[0]
    As = df[df['HORIZONT'] == 'A']
    ADepth=0 
    for depth in As[As['HORIZONT'] == 'A']['DEPTH']:
        ADepth += depth

    return ADepth, num_htypes

def calculate_custom_features_from_groups(df, group_by_column, process_function, column_names):
    """
    Groups the DataFrame by the specified column and applies a processing function to each group.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    group_by_column (str): The column name to group by.
    process_function (function): The function to apply to each group.

    Returns:bioclim =  query_to_df(engine, config['query_dir']['climate'], 'bioclim_variables')
bioclim = bioclim[(bioclim['year_first'] == 2001) & (bioclim['year_last'] == 2010)]
bioclim.rename(columns={'tnr': 'Tnr',
                                    'enr': 'Enr'}, inplace=True)
    pd.DataFrame: A DataFrame with the processed results.
    """
    # Group the DataFrame by the specified column
    grouped = df.groupby(group_by_column)

    # Initialize a list to store the results
    results = []

    # Iterate over each group
    for group_df in grouped:
        # Apply the processing function to the group
        output = process_function(group_df[-1])
        results.append(output)
    
    return pd.DataFrame(results, columns=column_names)


def query_to_df(engine, config, key_to_query): 
    with open(config) as file:
        config_queries = yaml.full_load(file)
    query = config_queries[key_to_query]
    formatted_query = query.replace('\n', ' ').replace('  ', ' ')
    df = pd.read_sql(formatted_query, engine)

    return df

def instanciate_engine(dataset_config_key):
    path = os.path.join(config['data_dir'], config['datasets'][dataset_config_key])
    return sa.create_engine(get_conn_url_from_path(path))

def check_for_duplicates(df, delete_duplicates=False):
    num_duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {num_duplicates}")

    if delete_duplicates:
        df.drop_duplicates(inplace=True)
        print("Duplicates removed.")