# Product Carbon Footprint Calculation Summary

## Project
**Digital Product Carbon Footprint (PCF) & BOM-to-PCF Automation**  
Illustrative 5.5 kW industrial three-phase induction motor.

## Purpose and status
This is a demonstration PCF model built using a simulated bill of materials (BOM) and illustrative manufacturing assumptions. It is not a manufacturer-verified product carbon footprint.

## Goal and scope
- **Functional unit:** one motor
- **Intended boundary:** cradle-to-gate
- **Modelled stages:** upstream supply of the 10 BOM material inputs, plus one aggregated illustrative manufacturing-electricity input
- **Impact category:** climate change, GWP100
- **Impact assessment method:** IPCC 2021
- **Background database:** ecoinvent 3.9.1, Cut-off system model
- **Electricity geography:** Germany (DE), medium-voltage market dataset

## Modelled results

| Result | Value |
|---|---:|
| Upstream material-supply GWP | 170.22 kg CO₂-eq per motor |
| Illustrative manufacturing electricity | 10 kWh per motor |
| Electricity contribution at 10 kWh | 4.71 kg CO₂-eq per motor |
| **Base modelled total** | **174.93 kg CO₂-eq per motor** |

The base total is the material-supply result plus the modelled 10 kWh electricity input.

## Material contribution to the material-supply result

| Material / dataset grouping | GWP contribution (kg CO₂-eq) |
|---|---:|
| Aluminium | 84.09453 |
| Low-alloyed steel | 44.52053 |
| Copper | 34.32252 |
| ABS | 3.72038 |
| Epoxy resin insulator, SiO₂ | 1.51508 |
| Polypropylene | 1.14818 |
| Unalloyed steel | 0.89846 |
| **Total** | **170.21967** |

The low-alloyed steel dataset is used as a proxy for the electrical-steel stator and rotor cores because a suitable electrical-steel dataset was not identified in the selected ecoinvent database. This is a documented data limitation.

## Electricity sensitivity

The electricity scenarios are illustrative assumptions, not measured factory data or industry benchmarks. Using the modelled electricity factor of approximately 0.471264 kg CO₂-eq/kWh:

| Scenario | Electricity (kWh/motor) | Modelled total (kg CO₂-eq/motor) |
|---|---:|---:|
| Low | 5 | 172.58 |
| Base | 10 | 174.93 |
| High | 20 | 179.64 |

These scenario totals are calculated from the material-supply result plus the corresponding electricity burden. Check that the High scenario in the Power BI source data is set to **20 kWh** before presenting it; a 15 kWh input would produce a different total.

## Key assumptions and limitations
1. The 10-component BOM is simulated and illustrative, not supplied or verified by a motor manufacturer.
2. The 10 kWh manufacturing electricity input is an aggregated placeholder. It is not based on measured factory energy consumption.
3. The electricity input represents an illustrative manufacturing-energy contribution; individual process energy, factory overheads, and production-line allocation have not been separately modelled.
4. Scrap rates, material losses, recycling allocation details beyond the selected ecoinvent Cut-off model, packaging, transport to the factory, and other manufacturing inputs may be incomplete or excluded.
5. Electrical steel is represented using a low-alloyed steel proxy. This may not represent the actual grade or production route.
6. Plastic and insulation material selections are provisional assumptions based on the illustrative BOM.
7. Results should therefore be described as **preliminary modelled results for a demonstration project**, not a verified product environmental declaration or supplier-specific PCF.

## Tools and workflow
Excel BOM → Python/Pandas cleaning and validation → SQLite database → environmental dataset mapping → openLCA product system and IPCC 2021 GWP100 calculation → Power BI dashboard.

## Recommended portfolio wording
“Developed an illustrative cradle-to-gate PCF model for a 5.5 kW induction motor using a simulated 10-component BOM. Cleaned and validated BOM data with Python, stored structured records in SQLite, mapped materials to ecoinvent 3.9.1 Cut-off datasets, and modelled GWP100 in openLCA using IPCC 2021. The preliminary base result is 174.93 kg CO₂-eq per motor, including an illustrative 10 kWh manufacturing-electricity assumption. Documented dataset proxies, assumptions, limitations, and electricity sensitivity scenarios.”
