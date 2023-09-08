import json
# Define the tabular data
tabular_data = [
    ["particulars", "Uom", "qty", "rate per unit", "disc%", "Net rate per unit", "net amount"],
    ["repair 128-LH fender Dent", "0", "1", "5,500", "0", "5,500", "5,500"],
    ["Repair-143-RH Fender paint", "job", "1", "9,000", "0", "9,000", "9,000"],
    ["Repair-122-LH Rear Door paint", "0", "1", "9,500", "0", "9,500", "9,500"],
    ["repair115-Rear Bumper Dent", "0", "1", "8,000", "0", "8,000", "8,000"],
    ["repair112-Fitting charge", "job", "1", "1,500", "0", "1,500", "1,500"],
    ["77260M82P00-5PK-Guard-AssyPR fender Splash-L", "pcs", "1", "1,226", "0", "1,226", "1,226"],
    ["77280M82P00-5PK-Guard-Assy-RR Bumper side", "pcs", "1", "312", "0", "312", "312"],
    ["Dt204-Double Tape", "pcs", "1", "1,000", "0", "1,000", "1,000"]
]

# Extract the headers and rows
headers = tabular_data[0]
rows = tabular_data[1:]

# Converting the tabular data into a list of dictionaries
data_list = []
for row in rows:
    data_dict = {}
    for i in range(len(headers)):
        data_dict[headers[i]] = row[i]
    data_list.append(data_dict)

# Define the output JSON file path
output_file_path = "output.json"

# Write the JSON data to the file
with open(output_file_path,"w") as json_file:
    json.dump(data_list, json_file, indent=4)

print(f"JSON data {output_file_path}")
