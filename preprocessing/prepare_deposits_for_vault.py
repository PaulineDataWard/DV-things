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
import asyncore 
import os
import selectors
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
    # add a deposit title prefix to give the project name eg 'physiology' 
    deposit_title_prefix = "<<PREFIX??? replace me in the script>> "
    # add a sample ID to all deposit descriptions (I think species should be in vault description rather than here - PW). 
    deposit_description_prefix = "Sample ID:??? Equipment make and model??? etc ... " 
    # If splitting by year, use this list of years which will be matched against folder names 
    years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
    year_name = ""

    # If splitting by staff names, use this list of names which will be matched against folder names
    staff_names = ["Pauline", "Ivan", "Tomasz", "Andrew", "Manuel", "Nahuel", "Andy"]
    person_name = ""

    ## Location where output file is saved
    outputpath = "./" 

    ## Location from which to start walking through directories/folders
    top_level_directory = "."

    ## Holding the field names in a list
    fields = ["PathToFiles", "No. of files", "DepositTitle", "DepositDescription"] 

    # Holding the rows in a dataframe, where the fields are the columns
    metadata = pd.DataFrame(columns = fields)

    # Output file
    output_file = outputpath + "deposits_metadata.CSV"
    
    rownum = 0
    for root, directory_names, filenames in os.walk(top_level_directory):
        # identify the person if any 
        for person in staff_names:
            if person in root: 
                person_name = person    
        # identify the year if any 
        for year in years: 
            if year in root:
                year_name = year 
        if (len(filenames) > 0): 

                    metadata.at[rownum, 'DepositTitle'] = deposit_title_prefix + person_name + ": " + year_name + " \"" + os.path.basename(root) + "\" from \'" + root + "\'"
                    metadata.at[rownum, 'DepositDescription'] = deposit_title_prefix + "Data generated by team member: " + person_name + " in the year: " + str(year_name) + ". Deposit contains " + str(len(filenames)) + " files that were stored in " + root + ". Metadata compiled automatically by prepare_deposits_for_vault.py."
                    metadata.at[rownum, 'PathToFiles'] = root 
                    metadata.at[rownum, 'No. of files'] = len(filenames)
                    # Output a list of sub-directories and numbers of files contained in each
                    # print (root, len(filenames) , "files")

                    rownum += 1
    metadata.to_csv(output_file, index_label="Index")

if __name__=='__main__':
     main()