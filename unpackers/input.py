# THIS FILE IS ONLY FOR TESTING HL7 PARSING AND CSV EXPORT
# DO NOT INCLUDE THIS FILE IN ANY FINAL SUBMISSION

import hl7
import csv

# Your original HL7 content
hl7_content = """MSH|^~\&|SNDAPP|SNDFAC|RCVAPP|RCVFAC|20220101120000||ORU^R01|MSG00001|P|2.4|
PID|1|12345|12345|Lee^David||19800101|M|20220101|
OBX|1|NM|HR^Heart Rate|1|75|bpm|||F|||20220101120000|
OBX|2|NM|BP^Blood Pressure|1|120/80|mmHg|||F|||20220101120000|
OBX|3|ST|SLP^Sleep|1|7|h|||F|||20220101120000"""

# Split the HL7 content into individual segments
hl7_segments = hl7_content.split('\n')

# Manually remove the MSH segment
if hl7_segments[0].startswith('MSH'):
    hl7_segments = hl7_segments[1:]

# Initialize an empty list to store parsed segments
parsed_segments = []

# Reconstruct the MSH segment and parse each segment
for segment in hl7_segments:
    # Skip empty lines
    if segment:
        msh_segment = "MSH|" + segment[0:]  # Reconstruct the MSH segment
        parsed_segment = hl7.parse(msh_segment)
        parsed_segments.append(parsed_segment)

# Extract PID and OBX segments directly
pid_segments = [segment for segment in parsed_segments if str(segment[0][2]) == 'PID']
obx_segments = [segment for segment in parsed_segments if str(segment[0][2]) == 'OBX']

for segment in pid_segments:
    print(segment)

# Combine the extracted segments into a list
exported_segments = pid_segments + obx_segments

# Define the desired order of fields for CSV export
csv_field_order = ['SegmentID', 'Name', 'Field2', 'Field3', ...]  # Replace with actual field names

# Create a list of dictionaries for CSV export
csv_data = []
for segment in exported_segments:
    csv_row = {'SegmentID': segment[0][0]}
    for i, field_value in enumerate(segment[1:], start=1):
        csv_row[f'Field{i}'] = field_value
    csv_data.append(csv_row)

# Save the CSV data to a file
csv_path = 'export.csv'
with open(csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=csv_field_order)
    csv_writer.writeheader()
    csv_writer.writerows(csv_data)

print(f"CSV file '{csv_path}' created successfully.")
