import pandas as pd


def normalise_csv(original_csv_path):
    # Read the original CSV file
    df = pd.read_csv(original_csv_path)

    # Define the desired column order
    desired_order = ['Name', 'Date', 'Heartrate', 'Blood Pressure', 'Sleep']

    # Reorder the columns
    df_reordered = df[desired_order]

    # Save the reordered DataFrame to a new CSV file
    new_csv_path = 'csvNormal.csv'
    df_reordered.to_csv(new_csv_path, index=False)

    print("New CSV file created successfully.")
