# UBS-CDE-ML-Course / Custom NFI dataset 
This repository includes all necessary scripts to reproduce a custom dataset 
based on the national forest invetory data of Germany. 

## Prerequisites 
The dataset is generated using different filedatabses that can be downloaded 
from the servers of the Thuenen Institut. Since the most databases are distributed 
as Microsoft Acces filedatabases the scripts are only tested on a Windows machine. 
This makes sure that the necessary ODB drivers are preinstalled. 


# Download of the databases 
Using your prefered shell that is allows to execute Python navigate to the 
repository and the scripts folder. Use the following command to download 
all files.

```
python downloads_dbs.py --config config.yaml
```

You will find the databases in the created datasets folder of the repository. 

# Dataset creation 
