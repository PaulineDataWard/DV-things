# Extract metadata for DataVault from Swain Lab microscopy logfiles
# Pauline Ward 2022 
# Not to be used for personal data because of the additional metadata that requires 
# Write to a CSV file to be used manually 
# This script is designed to be mostly adaptable for re-use by the BioRDM team, running the code usually from Windows environment. 
# Swain Lab folders are nested with levels for: 
# lab member first name; year; month (3-letter code camel case); date (DD-Mmm-YYYY)...
# .. experimental condition? ; position pos1 etc(?). 
# Not all Swain lab data has an accompanying logfile. Some folders have multiple .log files, others multiple .txt files. 
# In some cases one line in the file commences with 'Experiment description: '. 
#  
from asyncore import write
import os
from selectors import DevpollSelector
# need to fix cannot find the pandas module issue
import numpy as np
import pandas as pd 

# Outline: 
# Crawl through folders using os.walk() 
# Identify nesting of year, month, date. 
# For each 'terminal' folder containing no sub-folders, add a line to the CSV for a potential deposit, 
# including staff name and date in the title, and folder names eg pMito240_00, pMito240_01
# 
# Deposit metadata fields: deposit_title, deposit_description, contains_perso_data = 'FALSE' etc 
# 

def main():
    # Initialisation

    # Optionally uncomment the following lines to set the specified variables
    # arg: add a deposit title prefix to give the project name eg 'physiology' 
    deposit_title_prefix = "PREFIX???"
    # arg: add a sample ID to all deposit descriptions (I think species should be in vault description rather than here - PW). 
    deposit_description_prefix = "Sample ID:??? Equipment make and model??? etc ... " 



    ## Location where output file is saved
    outputpath = "./" 

    ## Location from which to start walking through directories/folders
    top_level_directory = "./"

    ## Holding the field names in a list
    fields = ["Index", "DepositTitle", "DepositDescription", "PathToFiles", "No. of files", "Name of first file"] 

    # Holding the rows in a dataframe, where the fields are the columns
    metadata = pd.DataFrame()
    metadata.set_index(fields)

    # Output file
    output_file = open( outputpath + "deposits_metadata.CSV", "w")
    
    for root, directory_names in walk.os(top_level_directory):
        metadata[PathToFiles] = root 

        
    metadata.to_csv(output_file)
    output_file.close() 

if __name__=='__main__':
     main()