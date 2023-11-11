import pandas as pd


def normalise_xls(original_excel_path):
    # Read the original Excel file (change the file extension if it's a .xls file)
    df = pd.read_excel(original_excel_path)

    # Define the desired column order
    desired_order = ['Name', 'Date', 'Heartrate', 'Blood Pressure', 'Sleep']

    # Reorder the columns
    df_reordered = df[desired_order]

    # Save the reordered DataFrame to a new Excel file
    new_excel_path = 'xlsNormal.csv'
    df_reordered.to_csv(new_excel_path, index=False)

    print("New Excel file created successfully.")
