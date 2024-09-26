# Python script to download and extract zip files from URLs listed in a config file.
# Usage: python download_dbs.py --config_file config.yml
# Config file should be in YAML format and contain the following
# dest_folder: path to the folder where the zip files will be downloaded and extracted
# urls: a dictionary of key-value pairs where key is the name of the extracted folder and value is the URL to download the zip file


import os 
import sqlalchemy as sa 
import pandas as pd 
from sqlalchemy import create_engine, text
import matplotlib.pyplot as plt
import warnings
import yaml
import argparse

import helper_functions as hf

def main(config_file):

    with open('../configs/dataset_creation.yaml') as file:
    config = yaml.full_load(config_file)

    # Setup soil database connection
    path = os.path.join(config['data_dir'], config['datasets']['soil'])
    engine = sa.create_engine(get_conn_url_from_path(path))

    # Extract soild data
    df_leitprofile = hf.query_to_df(engine, config['query_dir']['soil'], 'leitprofil')
    df_kartiereinheiten = query_to_df(engine, config['query_dir']['soil'], 'kartiereinheiten')
    df_feldkap = query_to_df(engine, config['query_dir']['soil'], 'feldkapazität')

    # Calculate custom soil features: ADepth, NumHTypes
    add_features = calculate_custom_features_from_groups(df_leitprofile,
                                    group_by_column=['LAND', 'SOEH_KRZ', 'SOEH_VAR'],
                                    process_function=get_ADepth_HTypes_from_profile,
                                    column_names=['ADepth', 'NumHTypes'])
    df_leitprofile_unique = df_leitprofile.iloc[:, :3].drop_duplicates().reset_index(drop=True)
    add_features= add_features.reset_index(drop=True)

    df_leitprofile_features = pd.concat([df_leitprofile_unique, add_features], axis=1)
    
    # Merge soil dfs into one final df
    df_kartiereinheiten = pd.merge(df_kartiereinheiten, df_leitprofile_features, on=['LAND', 'SOEH_KRZ', 'SOEH_VAR'], how='inner')
    df_kartiereinheiten = pd.merge(df_kartiereinheiten, df_feldkap, on=['TNR', 'ENR', 'SOEH_NR'])

    # Dispose soil engine
    engine.dispose()

    # Setup bwi_2002 databse connection
    path = os.path.join(config_file['data_dir'], config_file['datasets']['bwi_2002'])
    engine = sa.create_engine(get_conn_url_from_path(path))

