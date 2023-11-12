import pandas as pd

# Define the file paths for the two CSV files
def merge_files(file1_path, file2_path):
    # Read the data from both CSV files
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Concatenate the dataframes to merge the records
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Define the file path for the merged CSV file
    merged_file_path = 'unpackers/output/output.xlsx'

    # Write the merged data to a new CSV file
    # merged_df.to_csv(merged_file_path, index=False)
    merged_df.to_excel(merged_file_path, index=False)

    print(f"Merged data saved to '{merged_file_path}'")