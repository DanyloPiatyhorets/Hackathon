import hl7
import csv
from io import StringIO

hl7_message = open('input/input.hl7').read()

parsed_message = hl7.parse(hl7_message)

csv_data = []
for segment in parsed_message:
    csv_row = [segment[0][0]]  # Segment ID
    for field in segment[1:]:
        csv_row.extend(field)
    csv_data.append(csv_row)

# Write to CSV file
csv_output = StringIO()
csv_writer = csv.writer(csv_output)
csv_writer.writerows(csv_data)

# Print CSV content
csv_output.seek(0)
csv_content = csv_output.read()
print(csv_content)

# for segment in parsed_message:
#     segment_id = segment[21]
#     print(f"Segment: {segment_id}")
#     for field in segment[0]:
#         print(f"Field: {field[0]} - Value: {field[0]}")
#
# # Accessing specific fields
# heart_rate = parsed_message.segment('OBX')[0][5][0].value
# blood_pressure = parsed_message.segment('OBX')[1][5][0].value
#
# print(f"Heart Rate: {heart_rate}")
# print(f"Blood Pressure: {blood_pressure}")