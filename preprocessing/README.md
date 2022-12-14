# Documentation - prepare_deposits_for_vault.py 
Pauline Ward 2022 

## Purpose
Extract metadata for DataVault from Swain Lab microscopy logfiles

Not to be used for personal data because of the additional metadata that requires 

This script is designed to be mostly adaptable for re-use by the BioRDM team, running the code usually from Windows environment. 

This python script crawls through a hierarchically-organised set of folders to compile suggested descriptive metadata about the data files contained therein for use in depositing the files into the Edinburgh DataVault. The file outputs the metadata in a CSV file. 

## Input

Swain Lab folders are nested with levels for: 
lab member first name; year; month (3-letter code camel case); date (DD-Mmm-YYYY)...
.. experimental condition? ; position pos1 etc(?). 
Not all Swain lab data has an accompanying logfile. Some folders have multiple .log files, others multiple .txt files. 
In some cases one line in the file commences with 'Experiment description: '. 

## How to use
As of September 2022, the user still needs to manually add each deposit to the vault, manually selecting the folder containing the files. The CSV is intended as a guide. 

The script should be copied to a suitable place and run from the top directory of the directory structure. 

## Running this script in Windows 
It is assumed the files are on a DataStore area, either a homespace or a group shared area, 
already mapped as a network drive. 
The script uses NumPy and Pandas packages in Python, which can be installed on their own or as part of Anaconda. 

If using the Anaconda prompt, navigate to the directory with the cd command. 
You will need to include "/D" to make it change directory. Then carry on with cd till you reach the folder. Example command from Anaconda prompt or Windows powershell: 
cd /D S:
cd theme-of-interest\project-of-interest\

If you have a large number of directories you might want to run this script in the background. See your Windows / Linux docs for how to do so. 

Example command to run the script from the Anaconda prompt on Windows in DataStore area: 
python ..\prepare_deposits_for_vault.py

The output will be found in S:\theme-of-interest\project-of-interest\deposits_metadata.CSV