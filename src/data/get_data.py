"""
This script gets the dataset from kaggle.com through the kaggle api and unpacks the .zip file.
"""

from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import os

api = KaggleApi()
api.authenticate()

# Gets the absolute path to the data folder.
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '..', '..', 'data', '')

api.competition_download_file('jigsaw-unintended-bias-in-toxicity-classification', 'all_data.csv', path=filename)

zf = ZipFile(filename + 'all_data.csv.zip')
zf.extractall(filename)
zf.close()

os.remove(filename + 'all_data.csv.zip')
