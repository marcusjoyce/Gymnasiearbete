"""
This script gets the dataset from kaggle.com through the kaggle api and unpacks the .zip file.
"""

from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import os

api = KaggleApi()
api.authenticate()

api.competition_download_file('jigsaw-unintended-bias-in-toxicity-classification', 'all_data.csv', path='././data/')

zf = ZipFile('././data/all_data.csv.zip')
zf.extractall('././data/')
zf.close()

os.remove('././data/all_data.csv.zip')
