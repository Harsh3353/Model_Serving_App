import os
import pandas as pd
from . import variables as envars
from app import logging

class DatasetLoader(object):
    def __init__(self):
        self.__load()
    
    def get_dataset(self):
        try:
          return self.dataset
        except Exception as e:
            logging.error(f"Error fetching dataset : {str(e)}")
            raise Exception("Error fetching dataset", str(e))
    
    def set_dataset(self, new_dataset):
        try:
            self.dataset = new_dataset
        except Exception as e:
            logging.error(f"Error setting dataset : {str(e)}")
            raise Exception("Error setting dataset", str(e))
    
    def __load(self):
        try:
            self.set_dataset(pd.read_csv(envars.DATASET_PATH))
            logging.info("Dataset loaded successfully")
        except Exception as e:
            logging.error(f"Error loading dataset :{str(e)}")
            raise Exception("Error loading dataset", str(e))
        