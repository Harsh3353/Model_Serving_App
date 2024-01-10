import os
from app import logging

DATASET_PATH = os.getcwd()+'/dataset/adult.csv'
logging.info(f'Dataset Path : {DATASET_PATH}')