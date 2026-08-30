"""
Script to download the Google Play Store datasets from Kaggle using kagglehub
"""

import shutil
from pathlib import Path
import kagglehub


def download_data():
    print("Authenticating with Kaggle...")
    kagglehub.login()

    print("Downloading Google Play Store dataset...")
    path = kagglehub.dataset_download(
        "lava18/google-play-store-apps"
    )

    # Project directories
    project_root = Path(__file__).resolve().parent
    raw_data_dir = project_root / "data" / "raw"

    # Create data/raw if it does not exist
    raw_data_dir.mkdir(parents=True, exist_ok=True)

    # Find CSV files downloaded from Kaggle
    csv_files = list(Path(path).glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            "No CSV files found in the downloaded dataset"
        )

    # Copy all CSV files to data/raw
    for source_file in csv_files:
        destination_file = raw_data_dir / source_file.name
        shutil.copy2(source_file, destination_file)
        print(f"Success! Dataset saved to: {destination_file}")


if __name__ == "__main__":
    download_data()