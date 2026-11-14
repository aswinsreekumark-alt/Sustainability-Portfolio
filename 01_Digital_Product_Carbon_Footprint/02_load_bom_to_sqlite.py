from pathlib import Path
import sqlite3
import pandas as pd

# --------------------------------------------------
# 1. Define project folders and file paths
# --------------------------------------------------

project_folder = Path(__file__).resolve().parent.parent

input_file = (
    project_folder
    / "04_cleaned_data"
    / "Cleaned_Motor_BOM.xlsx"
)

database_folder = project_folder / "06_SQL"
database_folder.mkdir(exist_ok=True)

database_file = database_folder / "Motor_PCF_Database.db"

# --------------------------------------------------
# 2. Load the cleaned BOM from Excel
# --------------------------------------------------

bom = pd.read_excel(
    input_file,
    sheet_name="Cleaned_BOM"
)

# Clean column names
bom.columns = bom.columns.astype(str).str.strip()

# Remove accidental duplicate ID column if identical
if "Component_ID2" in bom.columns and "Component_ID" in bom.columns:
    if bom["Component_ID2"].equals(bom["Component_ID"]):
        bom = bom.drop(columns=["Component_ID2"])

# Remove completely empty rows
bom = bom.dropna(how="all")

# --------------------------------------------------
# 3. Load the material summary
# --------------------------------------------------

materials = pd.read_excel(
    input_file,
    sheet_name="Material_Summary"
)

materials.columns = materials.columns.astype(str).str.strip()
materials = materials.dropna(how="all")

# --------------------------------------------------
# 4. Store both datasets in SQLite
# --------------------------------------------------

with sqlite3.connect(database_file) as connection:

    bom.to_sql(
        "motor_bom",
        connection,
        if_exists="replace",
        index=False
    )

    materials.to_sql(
        "material_summary",
        connection,
        if_exists="replace",
        index=False
    )

    # --------------------------------------------------
    # 5. Validate the database
    # --------------------------------------------------

    component_count = pd.read_sql_query(
        "SELECT COUNT(*) AS total_components FROM motor_bom",
        connection
    )

    total_mass = pd.read_sql_query(
        """
        SELECT SUM(Component_Mass_kg) AS total_mass_kg
        FROM motor_bom
        """,
        connection
    )

    material_count = pd.read_sql_query(
        "SELECT COUNT(*) AS total_materials FROM material_summary",
        connection
    )

# --------------------------------------------------
# 6. Display results
# --------------------------------------------------

print("\nSQL DATABASE CREATED SUCCESSFULLY")
print("----------------------------------")

print("Components stored:", component_count.iloc[0, 0])
print("Materials stored:", material_count.iloc[0, 0])
print("Total BOM mass:", round(total_mass.iloc[0, 0], 2), "kg")

print("\nDatabase saved at:")
print(database_file)

# Basic validation
assert component_count.iloc[0, 0] == 10, "Unexpected component count"
assert abs(total_mass.iloc[0, 0] - 38.50) < 0.001, "Mass validation failed"

print("\nVALIDATION PASSED")