import pandas as pd
import json

# Input JSON file
input_path = "jsontobeconvertedintotable.json"
# Output Excel file
output_path = "output.xlsx"

# Load JSON array
with open(input_path, "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel(output_path, index=False)

print("Excel file created:", output_path)
