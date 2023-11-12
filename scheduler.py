from unpackers import hl7normaliser
from unpackers import xlsxnormaliser
from unpackers import csvnormaliser
from unpackers import merger

# check for files in input folder
# foreach file in input folder, check the file extension and run appropriate files for it
# in each file normalise the data into csv format and save it in output folder
# run the normalise file if number of output files > 1 and merge every record into 1 file
# output that as "masterNormalised.csv" in main folder
# take the normalised file and put it in powerapps somehow
# integrate this code into powerapps???

input_hl7_path = 'unpackers/input/input.hl7'
output_hl7_path = 'unpackers/output/hl7Normal.csv'

input_excel_path = 'unpackers/input/input.xlsx'
output_excel_path = 'unpackers/output/xlsxNormal.csv'

input_csv_path = 'unpackers/input/input.csv'
output_csv_path = 'unpackers/output/csvNormal.csv'


csvnormaliser.normalise_csv(input_csv_path, output_csv_path)
xlsxnormaliser.normalise_xls(input_excel_path, output_excel_path)
hl7normaliser.normalise_hl7(input_hl7_path, output_hl7_path)

merger.merge_files(output_csv_path, output_excel_path)

# For hl7 you need to do a lot of reformatting here before adding the data to the csv file
