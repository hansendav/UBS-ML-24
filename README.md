# UBS-CDE-ML-Course / Custom NFI dataset 
This repository includes all necessary scripts to reproduce a custom dataset 
based on the national forest invetory data of Germany. 

## Prerequisites 
The dataset is generated using different MS Access and SQLite filedatabases that can be downloaded 
from the servers of the [Thünen Institut](https://bwi.info/Download/de/). It is thus necessary
to run the following scripts on a machine that has drivers for both filesystems (esp. ODBC for 
Mircosoft Access) installed. 


## Download of the databases 
Using your prefered shell that allows to execute Python scripts navigate to the 
repository and the scripts folder. Use the following command to download 
all files from here.

```
python downloads_dbs.py --config '../configs/download.yaml'
```
You will now find all filedatabses in the ``datasets`` directory. 

## Dataset creation 

Next, we create the dataset. Run the following command, again in the 
``scripts`` directory: 

```
python create_bwi_ml_dataset.py
```

You will find the dataset in the ``datasets`` directory as well. 

## Documentation 
\[Under construction]
You can find a summary and explanation of the features in the ``documentation`` directory. 
