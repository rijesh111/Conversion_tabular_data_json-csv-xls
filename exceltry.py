import openpyxl

# Define the tabular data
tabular_data = [
    ["particulars", "Uom", "qty", "rate per unit", "disc%", "Net rate per unit", "net amount"],
    ["repair 128-LH fender Dent", "", "1", "5,500", "", "5,500", "5,500"],
    ["Repair-143-RH Fender paint", "job", "1", "9,000", "", "9,000", "9,000"],
    ["Repair-122-LH Rear Door paint", "", "1", "9,500", "", "9,500", "9,500"],
    ["repair115-Rear Bumper Dent", "", "1", "8,000", "", "8,000", "8,000"],
    ["repair112-Fitting charge", "job", "1", "1,500", "", "1,500", "1,500"],
    ["77260M82P00-5PK-Guard-AssyPR fender Splash-L", "pcs", "1", "1,226", "", "1,226", "1,226"],
    ["77280M82P00-5PK-Guard-Assy-RR Bumper side", "pcs", "1", "312", "", "312", "312"],
    ["Dt204-Double Tape", "pcs", "1", "1,000", "", "1,000", "1,000"]
]

# Create a new Excel workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Populate the sheet with the tabular data
for row_data in tabular_data:
    sheet.append(row_data)

# Define the output Excel file path
output_file_path = "output.xlsx"

# Save the workbook to the Excel file
workbook.save(output_file_path)

print(f"Excel data has been written to {output_file_path}")
