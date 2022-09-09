# Documentation - prepare_deposits_for_vault.py 
This python script crawls through a hierarchically-organised set of folders 
to compile descriptive metadata about the data files contained therein 
for use in depositing the files into the Edinburgh DataVault. 
The file outputs the metadata in a CSV file. 

The script should be run from the top directory of the directory structure. 

## Running this script in Windows 
It is assumed the files are on a DataStore area, either a homespace or a group shared area, 
already mapped as a network drive. 
The script uses NumPy and Pandas packages in Python, which can be installed on their own or as part of Anaconda. 

If using the Anaconda prompt, navigate to the directory with the cd command. 
You will need to include "/D" to make it change directory. Then carry on with cd till you reach the folder. 
 

