from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()

# Replace 'dataset/username/dataset-name' with the desired dataset path from Kaggle
dataset_path = 'datasets/stoicstatic/face-recognition-dataset/'

# Provide the dataset path and set the download path
api.dataset_download_files(dataset_path, path='scripts/data_acquisition/data', unzip=True)