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
from datetime import datetime
import os
import selectors
import numpy as np
import pandas as pd
import re
import argparse
import datetime

# Outline:
# Crawl through folders using os.walk()
# Identify nesting of year, month, date.
# For each 'terminal' folder containing no sub-folders, add a line to the CSV for a potential deposit,
# including staff name and date in the title, and folder names eg pMito240_00, pMito240_01
#
# Deposit metadata fields: deposit_title, deposit_description, contains_perso_data = 'FALSE' etc
#

# Initialisation of global variables

# Parse the Command-Line Interface (CLI) arguments
CLI_arg_parser = argparse.ArgumentParser(
    description='Please answer the following questions to help us prepare your deposits for your vault...')
CLI_arg_parser.ArgumentParser(fromfile_prefix_chars='@')
CLI_arg_parser.add_argument(
    'year_flag', type=bool, help='Do you have folders named after and corresponding to one year e.g. \'2021\'?')

CLI_arg_parser.add_argument(
    'CSV_flag', type=bool, help='Do you want to create a list of metadata for suggested deposits in a CSV file?')
CLI_arg_parser.add_argument(
    'index_flag', type=bool, help='Do you want to create an index file so you can add it to your vault?')

# Do you want to deposit one deposit per staff member per year?
# Do you want us to create an index file (to be archived alongside the data in DataVault) for each deposit and/or an index file for the whole vault?
# In the index files, would you like us to list empty folders (including nested sub???directories) and label them ???Empty????
# Do you want the index and/or list of deposits to be made with the assumption that where there is a logfile, the deposit will consist of the contents of the folder containing the logfile, and where there is no logfile, the deposit will be the folder named after the date DD-Mmm-YYYY? And/or should we assume there is one deposit per person per year, and that we compile the info from the logfiles into the index for that deposit?

args = CLI_arg_parser.parse_args()

# DATA STRUCTURE - Holding the deposit field names in a list
fields = ["PathToFiles", "Logfile", "DepositTitle", "DepositDescription" ] 

# Holding the rows in a dataframe, where the fields are the columns, 
# and each row is a deposit
metadata = pd.DataFrame(columns = fields)

# Holding the details of experiments drawn from files, which may be combined together in deposits, 
# and should all be listed in the index file
experimental_details_fields = ["Microscrope_name", "Expt_description", "Omero_project", "Omero_tags"]
experiments = pd.DataFrame(column = )

# Configuration
# Optionally edit / comment / uncomment the following lines to set the specified variables
# add a deposit title prefix to give the project name eg 'physiology'
deposit_title_prefix = "" 
# deposit_title_prefix = "<<PREFIX??? replace me in the script>> "
# add a sample ID to all deposit descriptions (I think species should be in vault description rather than here - PW).
deposit_description_prefix = ""
# deposit_description_prefix = "Sample ID:??? Equipment make and model??? etc ... "
# If splitting by year, use this list of years which will be matched against folder names
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
            "2020", "2021", "2022", "2023", "2024", "2025"]

# If splitting by staff names, use this list of names which will be matched against folder names
staff_names = ["Pauline", "Ivan", "Tomasz",
               "Andrew", "Manuel", "Nahuel", "Andy"]

# If splitting by date in the folder name...
# Swain lab dated folders DD-Mmm-YYYY eg 23-Jan-2017
date_folder_pattern = "[0-9][0-9]-[a-zA-Z][a-zA-Z][a-zA-Z]-[0-9][0-9][0-9][0-9]"

# If finding logfiles, configure the filename patter to identify logfiles
# Swain lab logfiles when present, end in 'log.txt'.
logfile_pattern = "log.txt$"
log_experiment = "Experiment details:\n"
log_microscope = "Microscope name is:"

# Location from which to start walking through directories/folders
top_level_directory = "."

# Location where output file is saved
outputpath = "./"

# Mandatory variables - not to be amended for configuration purposes
# Output file
output_file = outputpath + "deposits_metadata.CSV"


def parse_logfile():
    metadata.at[rownum, 'Logfile'] = filenm
           metadata.at[rownum, 'DepositTitle'] = deposit_title_prefix + \
               person_name + " (" + year_name + ") " + current_folder
            metadata.at[rownum, 'DepositDescription'] = "Data generated by team member: " + \
                person_name + " in folder: " + root + ". "

             metadata.at[rownum, 'PathToFiles'] = root
              logfile_relative_path = root + "\\" + filenm
               with open(logfile_relative_path, "r") as logfile:
                    logfile_lines = logfile.readlines()
                    logfile.close()
                for idx, microscope_line in enumerate(logfile_lines):
                    if re.search(log_microscope, microscope_line):
                        metadata.at[rownum,
                                    'DepositDescription'] += logfile_lines[idx].rstrip() + ". "

                if log_experiment in logfile_lines:
                    details_index = logfile_lines.index(log_experiment)
                    experiment_details = ""
                    for x in range(0, 9):
                        detail = logfile_lines[details_index + x].rstrip()
                        experiment_details += detail + " "
                    metadata.at[rownum,
                                'DepositDescription'] += experiment_details

def add_one_deposit_metadata():


def make_csv():
    metadata.to_csv(output_file, index_label="Index")



def make_index(): 
    date_stamp = datetime.datetime.now().strftime("%Y-%m-%d")
    index_file = open('index_file_for_vault_compiled_' + datetime.datetime + '.txt', "w")




def main():

    

     
    rownum = 0
    for root, directory_names, filenames in os.walk(top_level_directory):
        # identify the person if any 
        person_name = ""
        year_name = ""
        for person in staff_names:
            if person in root: 
                person_name = person    
        # identify the year if any 
        for year in years: 
            if ("\\" + year + "\\") in root or ("/" + year + "/") in root:
                year_name = year 
        # identify the date if any
        current_folder = os.path.basename(root)
        for filenm in filenames:

            if re.search( logfile_pattern , filenm) :
                
                parse_logfile()
                                              
                rownum += 1 
                continue
            
            rownum += 1 
        
    make_csv()

if __name__=='__main__':
     main()