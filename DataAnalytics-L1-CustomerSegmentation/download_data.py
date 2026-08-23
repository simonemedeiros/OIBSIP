"""
Script to download the Retail Sales dataset from Kaggle using kagglehub.
"""

import kagglehub

def download_data():
	print("Authenticating with Kaggle...")
	# This will explicitly handle authentication
	kagglehub.login()

	print("Downloading Retail Sales dataset...")
	# Download the latest version of the dataset
	path = kagglehub.dataset_download("noopurbhatt/retail-sales-dataset")

	print(f"Sucess! Path to dataset files: {path}")

if __name__ == "__main__":
	download_data()
