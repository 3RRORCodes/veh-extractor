# Vehicle Extractor (WIP)

This tool is made for **FiveM** server developers. It helps with organizing vehicle data by scanning folders, identifying vehicles, and categorizing them based on their names. It is still a **work in progress** (WIP), and more features will be added soon!

---

## What It Does
- Scans a folder of vehicles and organizes them into categories like police, EMS, fire, and others.
- Generates Lua files with the categorized vehicle data.
- Useful for creating organized vehicle data for your FiveM server.

---

## How to Use

### Prerequisites
- **Python**: Make sure Python is installed. If not:
  1. Download Python from [python.org](https://www.python.org/downloads/).
  2. Install it and check the option to add Python to your PATH.

### Steps
1. Place the script (`vehicle_extractor.py`) and the batch file (`run.bat`) in a folder.
2. Add your vehicle folders into a directory.
3. Run the batch file or use this command in the terminal:
   ```bash
   python vehicle_extractor.py <path-to-your-vehicle-directory>
   ```
   Replace `<path-to-your-vehicle-directory>` with the folder where your vehicle files are stored.
4. The output will be saved in an `output` folder created by the script.

---

## TODO Features (Coming Soon!)
- Extract vehicle names from model files.
- Extract data from `.meta` files.
- Create framework-ready vehicle data for:
  - QBCore
  - QBX
  - ESX

---

## Important Notes
- This script was made for personal use based on specific needs. Others are free to use it, but it might not work perfectly for everyone.
- It’s still a work in progress, so expect improvements and new features over time!

---

## Disclaimer
This script is made for **personal use** and designed with specific requirements in mind. While anyone can use or modify it, some adjustments may be needed to suit different needs.
