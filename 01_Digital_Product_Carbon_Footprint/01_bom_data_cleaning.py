from pathlib import Path
import pandas as pd

# Project folders
project_folder = Path(__file__).resolve().parent.parent

input_file = (
    project_folder
    / "02_Raw_BOM_Data"
    / "Motor_Engineering_BOM.xlsx"
)

output_folder = project_folder / "04_cleaned_data"
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "Cleaned_Motor_BOM.xlsx"

# Read the original BOM
df = pd.read_excel(
    input_file,
    sheet_name="Motor_Engineering_BOM"
)

original_rows = len(df)

# Remove completely empty rows and columns
df = df.dropna(how="all").dropna(axis=1, how="all")

# Remove the extra ID column if it duplicates Component_ID
if "Component_ID2" in df.columns:
    if (
        "Component_ID" in df.columns
        and df["Component_ID2"].equals(df["Component_ID"])
    ):
        df = df.drop(columns=["Component_ID2"])

# Required columns
required_columns = [
    "Component_ID",
    "Component_Name",
    "Material",
    "Quantity",
    "Unit",
    "Component_Mass_kg",
    "Data_Source",
    "Data_Type"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

# Clean text fields
text_columns = [
    "Component_ID",
    "Component_Name",
    "Material",
    "Unit",
    "Manufacturing_Process",
    "Data_Source",
    "Data_Type",
    "Notes"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].apply(
            lambda x: x.strip() if isinstance(x, str) else x
        )

# Convert numeric fields
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)

df["Component_Mass_kg"] = pd.to_numeric(
    df["Component_Mass_kg"], errors="coerce"
)

# Check missing and duplicate values
missing_values = df[required_columns].isna().sum().sum()

duplicate_ids = df["Component_ID"].duplicated().sum()

invalid_mass = (
    df["Component_Mass_kg"].isna()
    | (df["Component_Mass_kg"] <= 0)
).sum()

invalid_quantity = (
    df["Quantity"].isna()
    | (df["Quantity"] <= 0)
).sum()

non_kg_units = (
    df["Unit"].str.lower() != "kg"
).sum()

# Calculate total BOM mass
total_mass = df["Component_Mass_kg"].sum()

# Summarise mass by material
material_summary = (
    df.groupby("Material", as_index=False)
    ["Component_Mass_kg"]
    .sum()
)

material_summary = material_summary.rename(
    columns={"Component_Mass_kg": "Total_Mass_kg"}
)

# Create quality-check report
quality_checks = pd.DataFrame({
    "Check": [
        "Original BOM rows",
        "Cleaned BOM rows",
        "Missing required values",
        "Duplicate component IDs",
        "Invalid component masses",
        "Invalid quantities",
        "Rows with non-kg units",
        "Total BOM mass (kg)"
    ],
    "Result": [
        original_rows,
        len(df),
        missing_values,
        duplicate_ids,
        invalid_mass,
        invalid_quantity,
        non_kg_units,
        round(total_mass, 2)
    ]
})

# Export results
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df.to_excel(
        writer, sheet_name="Cleaned_BOM", index=False
    )
    material_summary.to_excel(
        writer, sheet_name="Material_Summary", index=False
    )
    quality_checks.to_excel(
        writer, sheet_name="Quality_Checks", index=False
    )

# Display results
print("\nBOM CLEANING COMPLETED")
print("----------------------")
print(f"Original rows: {original_rows}")
print(f"Cleaned rows: {len(df)}")
print(f"Total BOM mass: {total_mass:.2f} kg")
print(f"Duplicate component IDs: {duplicate_ids}")
print(f"Invalid component masses: {invalid_mass}")
print(f"Invalid quantities: {invalid_quantity}")
print(f"Rows with non-kg units: {non_kg_units}")
print(f"\nOutput saved to: {output_file}")