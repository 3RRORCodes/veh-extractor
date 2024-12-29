# Vehicle Extractor

This script is designed to categorize vehicle folders based on their names into specific categories (police, EMS, fire, or others) and generate output in Lua format. It was created for personal use to suit specific needs, so it might not work perfectly for others unless you have similar requirements. You are free to use or modify it as needed.

## How to Install and Run

### Prerequisites
- **Python**: Ensure Python is installed on your system. If not, follow these steps to install it:

  1. Download Python from the [official Python website](https://www.python.org/downloads/).
  2. Run the installer and select the option to add Python to your PATH.
  3. Complete the installation process.

- **Required Files**:
  - `vehicle_extractor.py`
  - `run.bat`

### Installation and Usage

1. Clone or download this repository to your local machine.
2. Place all your vehicle folders in a single directory.
3. Run the script:
   - Open the command line and navigate to the folder containing the files.
   - Execute the `run.bat` file or directly run the script with the following command:
     ```bash
     python vehicle_extractor.py <path-to-your-vehicle-directory>
     ```
   Replace `<path-to-your-vehicle-directory>` with the full path to the directory containing your vehicle folders.

### Output
The script generates:
- Categorized vehicle files in Lua format.
- Output files are saved in the `output` folder created in the same directory as the script.

### Notes
- The script processes folder names and categorizes them based on predefined patterns (e.g., "police", "ems").
- If errors occur during processing, they will be logged in the console.
- This script was tailored to specific requirements, so it may need adjustments for other use cases.

## Disclaimer
This script was made for personal use. While others are free to use and modify it, it may not work out-of-the-box for different requirements or setups.
