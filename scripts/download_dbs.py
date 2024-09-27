# Python script to download and extract zip files from URLs listed in a config file.
# Usage: python download_dbs.py --config_file config.yml
# Config file should be in YAML format and contain the following
# dest_folder: path to the folder where the zip files will be downloaded and extracted
# urls: a dictionary of key-value pairs where key is the name of the extracted folder and value is the URL to download the zip file
# Author: David Hansen 
# Date: 27/09/2024

import os
import requests
import zipfile
import argparse
import yaml

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def extract_zip(file_path, extract_to, new_name):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        for file_info in zip_ref.infolist():
            extracted_file_path = os.path.join(extract_to, file_info.filename)
            new_file_path = os.path.join(extract_to, new_name + os.path.splitext(file_info.filename)[1])
            os.rename(extracted_file_path, new_file_path)

def main(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    
    dest_folder = config.get('dest_folder', './downloads') # default to ./downloads if dest_folder is not specified
    urls = config.get('urls', {})
    
    if not urls:
        raise ValueError("No URLs specified in the config file.")
    
    for key, url in urls.items():
        url = url.strip()
        if url:
            print(f"Downloading {url}")
            zip_path = download_file(url, dest_folder)
            print(f"Extracting {zip_path}")
            extract_zip(zip_path, dest_folder, key)
            os.remove(zip_path)
            print(f"Finished processing {url}")

    print(f"Download and extraction complete. Files saved to {dest_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and extract zip files from URLs listed in a config file.')
    parser.add_argument('--config_file', type=str, required=True, help='Path to the config file containing URLs and destination folder')
    args = parser.parse_args()
    config_file = args.config_file
    main(config_file)