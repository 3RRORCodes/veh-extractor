import os
import sys
from typing import List
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# ANSI Color codes for prettier console output
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

@dataclass
class VehicleCategory:
    name: str
    vehicles: List[str]
    patterns: List[str]

    def matches(self, folder_name: str) -> bool:
        lower_name = folder_name.lower()
        return any(pattern in lower_name for pattern in self.patterns)

def colored_print(color: str, message: str) -> None:
    print(f"{color}{message}{Colors.RESET}")

def print_success(message: str) -> None:
    colored_print(Colors.GREEN, message)

def print_error(message: str) -> None:
    colored_print(Colors.RED, message)

def print_info(message: str) -> None:
    colored_print(Colors.BLUE, message)

class VehicleExtractor:
    def __init__(self, directory: str):
        self.directory = directory
        self.categories = [
            VehicleCategory("police", [], ["pol", "police", "cop", "patrol"]),
            VehicleCategory("ems", [], ["ems", "ambulance", "paramedic", "medical"]),
            VehicleCategory("fire", [], ["fire", "fd", "rescue"]),
            VehicleCategory("other", [], [])
        ]
        self.stats = {"total": 0, "processed": 0, "errors": 0}
        self.output_dir = self._create_output_dir()

    def _create_output_dir(self) -> str:
        output_dir = os.path.join(os.path.dirname(__file__), "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_dir

    def process_directory(self) -> None:
        print_info(f"Starting processing of directory: {self.directory}")
        print_info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        try:
            for folder_name in os.listdir(self.directory):
                self.stats["total"] += 1
                folder_path = os.path.join(self.directory, folder_name)
                
                if not os.path.isdir(folder_path):
                    continue

                self._categorize_vehicle(folder_name)
                self.stats["processed"] += 1

            self._generate_output_files()
            self._print_statistics()

        except Exception as e:
            print_error(f"Critical error: {str(e)}")
            self.stats["errors"] += 1

    def _categorize_vehicle(self, folder_name: str) -> None:
        categorized = False
        for category in self.categories[:-1]:  # Exclude 'other' category
            if category.matches(folder_name):
                category.vehicles.append(folder_name)
                categorized = True
                break
        
        if not categorized:
            self.categories[-1].vehicles.append(folder_name)  # Add to 'other' category

    def _generate_output_files(self) -> None:
        try:
            # Generate timestamp and source directory info
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            source_dir_name = Path(self.directory).name
            base_filename = f"{source_dir_name}_{timestamp}"

            # Generate Lua output
            lua_content = f"-- Extracted Vehicles - By 3RROR#0278\n-- Source Directory: {self.directory}\n-- Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            for category in self.categories:
                if category.vehicles:  # Only include categories with vehicles
                    variable_name = f"{category.name}Vehicles"
                    vehicles_str = ",\n    ".join(f'"{v}"' for v in sorted(category.vehicles))
                    lua_content += f"local {variable_name} = {{\n    {vehicles_str}\n}}\n\n"

            # Save Lua file
            self._save_file(f"{base_filename}.lua", lua_content)
        except Exception as e:
            print_error(f"Error generating output files: {str(e)}")
            self.stats["errors"] += 1

    def _save_file(self, filename: str, content: str) -> None:
        try:
            output_file = os.path.join(self.output_dir, filename)
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            with open(output_file, "w", encoding='utf-8') as file:
                file.write(content)
            print_success(f"Successfully created {filename}")
        except Exception as e:
            print_error(f"Error saving {filename}: {str(e)}")
            self.stats["errors"] += 1

    def _print_statistics(self) -> None:
        print_info("\nProcessing Statistics:")
        print(f"Total items found: {self.stats['total']}")
        print(f"Successfully processed: {self.stats['processed']}")
        print(f"Errors encountered: {self.stats['errors']}")
        
        for category in self.categories:
            print(f"{category.name.title()} vehicles: {len(category.vehicles)}")

def main():
    # Only use command line arguments
    if len(sys.argv) < 2:
        print_error("No directory provided. Please provide a directory path as an argument.")
        sys.exit(1)

    directory = sys.argv[1].strip()
    
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print_error("Invalid directory. Please provide a valid folder path.")
        sys.exit(1)

    extractor = VehicleExtractor(directory)
    extractor.process_directory()

if __name__ == "__main__":
    main()
