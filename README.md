# UBS-CDE-ML-Course / Custom NFI dataset 
This repository includes all necessary scripts to reproduce a custom dataset 
based on the national forest invetory data of Germany. 

## Prerequisites 
The dataset is generated using different filedatabses that can be downloaded 
from the servers of the Thuenen Institut. Since the most databases are distributed 
as Microsoft Acces filedatabases the scripts are only tested on a Windows machine. 
This makes sure that the necessary ODB drivers are preinstalled. 


## Download of the databases 
Using your prefered shell that allows to execute Python scripts navigate to the 
repository and the scripts folder. Use the following command to download 
all files from here.

```
python downloads_dbs.py --config '../configs/download.yaml'
```
After that you will find all filedatabses in the ``datasets`` directory. 

## Dataset creation 

Next, we create the dataset. For this run the following command, again in the 
``scripts`` directory: 

```
python create_bwi_ml_dataset.py
```

You will find the dataset in the ``datasets`` directory as well. 
