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
import os

# Crawl through folders 
# Identify nesting of year, month, date. 
# For each 'terminal' folder containing no sub-folders, add a line to the CSV for a potential deposit, 
# including staff name and date in the title, and folder names eg pMito240_00, pMito240_01
# 
# Deposit metadata fields: deposit_title, deposit_description, contains_perso_data = 'FALSE' etc 
# arg: add a deposit title prefix to give the project name eg 'physiology' 
# arg: add a sample ID to all deposit descriptions (I think species should be in vault description). 
# arg: add an equipment make and model to all deposit descriptions. 
# 
#def main():
    output_file = open("deposits_metadata.CSV", w+)
    output_file.write("this is output \n")
    output_file.close() 
#if __name__=='__main__':
#    main()