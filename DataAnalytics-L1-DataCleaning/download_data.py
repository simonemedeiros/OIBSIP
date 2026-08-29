"""
Script to download the dirty dataset from Kaggle using kagglehub
"""

import shutil
from pathlib import Path
import kagglehub

def download_data():
	print("Authenticating with Kaggle...")
	kagglehub.login()

	print("Downloading dirty dataset...")
	path = kagglehub.dataset_download(
		"joannanplkrk/dirty-data-to-clean-whats-wrong-with-this-dataset"
	)

	# Project directories
	project_root = Path(__file__).resolve().parent
	raw_data_dir = project_root / "data" / "raw"

	# Create data/raw if it does not exist
	raw_data_dir.mkdir(parents=True, exist_ok=True)

	# Find CSV files downloaded from kaggle
	csv_files = list(Path(path).glob("*.csv"))

	if not csv_files:
		raise FileNotFoundError("No CSV file found in the downloaded dataset.")

	# Copy the first CSV file to data/raw
	source_file = csv_files[0]
	destination_file = raw_data_dir / source_file.name

	shutil.copy2(source_file, destination_file)

	print(f"Sucess! Dataset saved to: {destination_file}")

if __name__ == "__main__":
	download_data()
