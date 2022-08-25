# Extract metadata for DataVault from Swain Lab microscopy logfiles
# Pauline Ward 2022 
# Not to be used for personal data because of the additional metadata that requires 
# Write to a CSV file to be used manually or by the prepare_deposits python script 
import os

# Deposit metadata fields: deposit_title, deposit_description, contains_perso_data = 'FALSE',  
# 
def main():
output_file = open("deposits_metadata.CSV", w+)
output_file.write("this is output \n")
output_file.close() 
if __name__=='__main__':
    main()