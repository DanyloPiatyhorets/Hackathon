from unpackers import hl7normaliser
from unpackers import xlsxnormaliser
from unpackers import csvnormaliser

# check for files in input folder
# foreach file in input folder, check the file extension and run appropriate files for it
# in each file normalise the data into csv format and save it in output folder
# run the normalise file if number of output files > 1 and merge every record into 1 file
# output that as "masterNormalised.csv" in main folder
# take the normalised file and put it in powerapps somehow
# integrate this code into powerapps???

original_hl7_path = 'unpackers/input/input.hl7'
original_excel_path = 'unpackers/input/input.xlsx'
original_csv_path = 'unpackers/input/input.csv'

csvnormaliser.normalise_csv(original_csv_path)
xlsxnormaliser.normalise_xls(original_excel_path)
hl7normaliser.normalise_hl7(original_hl7_path)

# For hl7 you need to do a lot of reformatting here before adding the data to the csv file
