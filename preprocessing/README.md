# Documentation - prepare_deposits_for_vault.py 
# v0.2 One deposit-per-date (DD-Mmmm-YYYY)
This python script crawls through a hierarchically-organised set of folders 
to compile suggested descriptive metadata about the data files contained therein 
for use in depositing the files into the Edinburgh DataVault. 
The file outputs the metadata in a CSV file. 

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

## Directory / folder structure
This version, 0.2, finds any directory whose name contains a string that looks like a date, and compiles metadata for one deposit corresponding to all the nested sub-directories in that directory. It therefore lists far fewer suggested deposits than v0.1, which listed every directory containing files (v0.2 suggests a deposit fo rthe day, which may contain many directories containing files). The pattern searched for reflects the practice of the Swain group, that folders for a given date are named 'DD-Mmm-YYYY'. Thus any string starting with two numerals, followed by a dash, three letters, another dash and four numerals will match. Should such a match be an error, the user may manually adjust the output file accordingly, to suit their own approach to depositing the data. 

This script also breaks down the data according to staff member name and year. So two folders of the same date but under the name of different staff members will be treated correctly as separate deposits. 

## Configuration 
The user can modify the list of staff names to be matched by editing the variable assignment in the initialisation section of the code. 
