# Python script to create a custom dataset for machine learning tasks 
# based on the filedatabases of National Forest Inventory (bwi.info)
# Usage: python create_bwi_ml_dataset.py 
# Author: David Hansen 
# Date: 27/09/2024



import os 
import sqlalchemy as sa
from sqlalchemy import create_engine
import pandas as pd 

import yaml

import helper_functions as hf


# Extract soil features workflow 
def extract_soil_features(config):
    
    # Setup database connection 
    path = os.path.join(config['data_dir'],
                        config['datasets']['soil'])
    engine = sa.create_engine(hf.get_conn_url_from_path(path))

    # Extract soild data
    df_soilprofiles = hf.query_to_df(engine,
                                    config['query_dir']['soil'], # config file
                                    'leitprofil') # query name in config file
    df_soils = hf.query_to_df(engine,
                                         config['query_dir']['soil'],
                                         'kartiereinheiten')
    df_fieldcapacity = hf.query_to_df(engine,
                                config['query_dir']['soil'],
                                'feldkapazitaet')

    # Calculate custom soil features: ADepth, NumHTypes
    add_features = hf.calculate_custom_features_from_groups(df_soilprofiles,
                                    group_by_column=['LAND', 'SOEH_KRZ', 'SOEH_VAR'],
                                    process_function=hf.get_ADepth_HTypes_from_profile,
                                    column_names=['ADepth', 'NumHTypes'])
    
    df_soilprofiles_unique = df_soilprofiles.iloc[:, :3].drop_duplicates().reset_index(drop=True)
    add_features= add_features.reset_index(drop=True)

    df_soilprofiles_features = pd.concat([df_soilprofiles_unique, add_features], axis=1)
    
    # Merge soil dfs into one final df
    df_soils = pd.merge(df_soils,
                        df_soilprofiles_features,
                        on=['LAND', 'SOEH_KRZ', 'SOEH_VAR'],
                        how='inner')
    df_soils = pd.merge(df_soils,
                        df_fieldcapacity,
                        on=['TNR', 'ENR', 'SOEH_NR'],
                        how='inner')

    # Dispose soil engine
    engine.dispose()
    print('Soil features extracted successfully')
    return df_soils

def extract_climate_features(config):

    # Setup database connection 
    path = os.path.join(config['data_dir'],
                        config['datasets']['climate'])
    engine = sa.create_engine(hf.get_conn_url_from_path(path)) 

    bioclim =  hf.query_to_df(engine,
                           config['query_dir']['climate'],
                           'bioclim_variables')
    bioclim = bioclim[(bioclim['year_first'] == 1991) & (bioclim['year_last'] == 2000)]
    bioclim.rename(columns={'tnr': 'Tnr',
                            'enr': 'Enr'},
                            inplace=True)
    
    print('Climate features extracted successfully')
    return bioclim


def extract_forest_features(config):

    # Setup database connection
    path = os.path.join(config['data_dir'],
                        config['datasets']['bwi_2002'])
    engine = sa.create_engine(hf.get_conn_url_from_path(path)) 

    # Extract data from database
    df_ecke = hf.query_to_df(engine,
                             config['query_dir']['bwi_2002'],
                             'ecke')
    df_tab = hf.query_to_df(engine,
                            config['query_dir']['bwi_2002'],
                            'tab')
    df_tree = hf.query_to_df(engine,
                             config['query_dir']['bwi_2002'],
                             'bwi_2002_baeume')
    df_bestand = hf.query_to_df(engine,
                                config['query_dir']['bwi_2002'],
                                'bestand')
    df_wzp = hf.query_to_df(engine,
                            config['query_dir']['bwi_2002'],
                            'wzp')
    df_bestock = hf.query_to_df(engine,
                                config['query_dir']['bwi_2002'],
                                'bestock')

    engine.dispose()

    # Setup database connection
    path = os.path.join(config['data_dir'],
                        config['datasets']['bwi_change'])
    engine = sa.create_engine(hf.get_conn_url_from_path(path))

    df_change = hf.query_to_df(engine,
                               config['query_dir']['bwi_change'],
                               'b23_baeume_m_s')
    
    engine.dispose()

    # Merge forest features into df 
    df = pd.merge(df_ecke, df_tab, on='Tnr', how='inner')
    df = pd.merge(df_tree, df, on=['Tnr', 'Enr'], how='inner')
    df = pd.merge(df, df_bestand, on=['Tnr', 'Enr'], how='inner')
    df = pd.merge(df, df_wzp, on=['Tnr', 'Enr', 'Bnr'], how='inner')
    df = pd.merge(df, df_bestock, on=['Tnr', 'Enr'], how='inner')
    df = pd.merge(df, df_change, on=['Tnr', 'Enr', 'Bnr'], how='inner')

    print('Forest features extracted successfully')
    return df

def main():
    
    with open('../configs/dataset_creation.yaml') as file:
        config = yaml.full_load(file)

    df_soil = extract_soil_features(config)
    df_climate = extract_climate_features(config)
    df_trees = extract_forest_features(config)


    # Merge tree and soil data
    df_soil.rename(columns={'TNR': 'Tnr',
                                    'ENR': 'Enr'}, inplace=True)

    df = pd.merge(df_trees, df_soil,
                  on=['Tnr', 'Enr'],
                  how='inner')
    
    df = pd.merge(df, df_climate,
                  on=['Tnr', 'Enr'],
                  how='inner')
    
    # Filter only one soilprofile to avoid duplicate instances
    df = df[df['SOEH_NR'] == 1] 

    # Filter duplicates 
    hf.check_for_duplicates(df, delete_duplicates=True)

    output_path = os.path.join(config['data_dir'], config['name'] + '.csv')
    if os.path.exists(output_path):
        print(f"File {output_path} already exists. Please rename the file or delete the existing one.")
    else:
        df.to_csv(output_path, index=False)
        print(f"Dataset generated with {df.shape[0]} instances and {df.shape[1]} features\n"
            f"Dataset saved to {output_path}")

if __name__ == '__main__':
    main()