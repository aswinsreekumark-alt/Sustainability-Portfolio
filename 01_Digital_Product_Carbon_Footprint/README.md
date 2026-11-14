# Digital Product Carbon Footprint & BOM-to-PCF Automation

## 1. Project Overview

This project demonstrates an illustrative cradle-to-gate Product Carbon Footprint (PCF) assessment of a 5.5 kW industrial three-phase induction motor.

The objective is to demonstrate how engineering Bill of Materials (BOM) data can be transformed into structured environmental data and used for product-level carbon footprint modelling.

The project combines BOM data cleaning, environmental dataset mapping, life cycle assessment (LCA), database management, sensitivity analysis and Power BI visualisation.

**Project status:** Demonstration model using simulated BOM data and illustrative manufacturing assumptions. Results are not manufacturer-verified.

## 2. Project Objectives

- Develop a structured engineering BOM for an industrial electric motor.
- Clean and validate BOM data using Python and Pandas.
- Store structured BOM records in an SQLite database.
- Map BOM materials to relevant ecoinvent environmental datasets.
- Build a product system in openLCA.
- Calculate climate change impacts using IPCC 2021 GWP100.
- Evaluate the influence of manufacturing electricity assumptions.
- Present results through a Power BI dashboard.

## 3. Methodology and Scope

| Parameter | Description |
|---|---|
| Product | 5.5 kW three-phase induction motor |
| Functional unit | 1 motor |
| Assessment boundary | Intended cradle-to-gate |
| BOM components | 10 |
| Total BOM mass | 38.5 kg |
| Background database | ecoinvent 3.9.1 |
| System model | Cut-off |
| Impact assessment method | IPCC 2021 |
| Impact category | Climate change, GWP100 |
| Electricity geography | Germany (DE) |

The current model includes upstream material supply and one aggregated illustrative manufacturing electricity input. It does not represent a complete, verified factory production inventory.

## 4. Technical Workflow

**Engineering BOM → Python Data Cleaning → SQLite Database → Environmental Dataset Mapping → openLCA Modelling → Power BI Dashboard**

### Stage 1 — BOM Data Preparation
- Developed a simulated 10-component motor BOM.
- Organised component identifiers, material classifications, quantities and masses.
- Documented illustrative manufacturing process assumptions.

### Stage 2 — Python Data Cleaning
- Used Python and Pandas to clean and validate BOM records.
- Checked missing values, duplicate component IDs, invalid quantities and mass consistency.
- Generated a cleaned BOM workbook and quality-check results.

### Stage 3 — SQL Database
- Created an SQLite database to store structured BOM information.
- Organised component-level records and material summaries.

### Stage 4 — Environmental Dataset Mapping
- Reviewed ecoinvent 3.9.1 Cut-off datasets.
- Mapped BOM materials to selected background datasets.
- Documented geographical coverage, data quality, proxies and assumptions.
- Used low-alloyed steel as a provisional proxy for electrical steel where a suitable dataset was not identified.

### Stage 5 — Life Cycle Assessment
- Built a foreground motor assembly process and product system in openLCA 2.5.
- Linked material inputs to background market datasets.
- Applied IPCC 2021 GWP100 to calculate climate change impacts.

### Stage 6 — Electricity Sensitivity and Visualisation
- Added an illustrative 10 kWh manufacturing electricity input using the German medium-voltage electricity market dataset.
- Evaluated low, base and high electricity scenarios.
- Developed a Power BI dashboard to present the modelled footprint and material contributions.

## 5. Key Results

### Modelled Product Carbon Footprint

| Result | Value |
|---|---:|
| Material supply contribution | 170.22 kg CO₂-eq |
| Illustrative electricity consumption | 10 kWh |
| Electricity contribution | 4.71 kg CO₂-eq |
| **Base modelled footprint** | **174.93 kg CO₂-eq/motor** |

### Material Contribution to Carbon Footprint

| Material | GWP (kg CO₂-eq) |
|---|---:|
| Aluminium | 84.09 |
| Low-alloyed steel | 44.52 |
| Copper | 34.32 |
| ABS | 3.72 |
| Epoxy resin insulator | 1.52 |
| Polypropylene | 1.15 |
| Unalloyed steel | 0.90 |

Aluminium, steel and copper represent the main contributors to the modelled material-supply footprint.

### Manufacturing Electricity Sensitivity

| Scenario | Electricity (kWh/motor) | Total GWP (kg CO₂-eq/motor) |
|---|---:|---:|
| Low | 5 | 172.58 |
| Base | 10 | 174.93 |
| High | 20 | 179.64 |

These are illustrative scenarios, not measured factory energy consumption or industry benchmarks.

## 6. Tools and Technologies

- **LCA:** openLCA 2.5, ecoinvent 3.9.1
- **Impact assessment:** IPCC 2021 GWP100
- **Data processing:** Python, Pandas
- **Database:** SQLite, SQL
- **Data management:** Microsoft Excel
- **Visualisation:** Microsoft Power BI

## 7. Project Files

| File | Description |
|---|---|
| `Motor_Engineering_BOM.xlsx` | Original illustrative engineering BOM |
| `Cleaned_Motor_BOM.xlsx` | Cleaned BOM and quality checks |
| `01_bom_data_cleaning.py` | Python BOM cleaning script |
| `02_load_bom_to_sqlite.py` | SQLite database loading script |
| `Motor_PCF_Database.db` | Structured BOM database |
| `Environmental_Dataset_Register.xlsx` | Environmental dataset register and BOM mapping |
| `Motor_PCF_IPCC2021_GWP100_Results.xlsx` | Initial openLCA results |
| `Motor_PCF_IPCC2021_GWP100_With_Electricity.xlsx` | openLCA results including illustrative electricity |
| `PCF_Calculation_Summary.md` | Calculation methodology, results and limitations |
| `Digital_Product_Carbon_Footprint_Dashboard.pbix` | Interactive Power BI dashboard |
| `Digital_Product_Carbon_Footprint_Dashboard.pdf` | Dashboard PDF report |

## 8. Assumptions and Limitations

- The motor BOM is simulated and is not manufacturer-supplied.
- Manufacturing electricity consumption is an illustrative assumption, not measured data.
- The electrical-steel stator and rotor cores are represented using a low-alloyed steel proxy.
- Plastic and insulation material selections are provisional assumptions.
- Individual manufacturing operations, scrap and material losses, packaging, and other factory inputs are not fully represented.
- The model should be treated as a preliminary demonstration rather than a verified product carbon footprint or Environmental Product Declaration.

## 9. Key Learning Outcomes

- Engineering BOM data structuring and validation.
- Python-based environmental data preparation.
- SQL database development and data management.
- Environmental dataset selection and mapping.
- Product-level LCA modelling in openLCA.
- GWP100 impact assessment and contribution analysis.
- Sensitivity analysis and Power BI reporting.
- Documentation of data quality, assumptions and modelling limitations.

## 10. Project Deliverables

- [Power BI Dashboard PDF](Digital_Product_Carbon_Footprint_Dashboard.pdf)
- [PCF Calculation Summary](PCF_Calculation_Summary.md)
- [Initial openLCA Results](Motor_PCF_IPCC2021_GWP100_Results.xlsx)
- [openLCA Results with Electricity](Motor_PCF_IPCC2021_GWP100_With_Electricity.xlsx)

The interactive `.pbix` dashboard can be opened using Microsoft Power BI Desktop.

---

**Project Focus:** Product Sustainability | Product Carbon Footprinting | Life Cycle Assessment | Environmental Data Analytics | BOM Automation
