import pandas as pd
import logger
from app.dataloader import DatasetLoader
import numpy as np
from app import logging

class DatasetCleaner(object):
    def __init__(self, datasetloader: DatasetLoader):
        logging.info(f"DatasetLoader : {datasetloader}")
        self.dataset_loader = datasetloader
        
    def execute_cleaning_pipeline(self):
        try:
            self.__checking_duplicates()
            self.__dataset_cleaning()
            self.__removing_outliers_from_dataset()
            self.__converting_objects_to_categorical_codes()
            logging.info("Successfully completed executing data cleaning pipeline")
        except Exception as e:
            logging.error(f"Error executing cleaning pipeline : {str(e)}")
            raise Exception("Error executing cleaning pipeline", str(e))
            
    def __checking_duplicates(self):
        try:
            dataset = self.dataset_loader.get_dataset()
            logging.info(dataset)
            dataset.drop_duplicates(inplace=True)
            self.dataset_loader.set_dataset(dataset)
        except Exception as e:
            logging.error(f"Error removing duplicates from dataset : {str(e)}")
            raise Exception("Error removing duplicates from dataset", str(e))
            
    def __dataset_cleaning(self):
        try:
            dataset = self.dataset_loader.get_dataset()
            dataset = dataset.drop(columns=['fnlwgt', 'education-no. of years'], axis=1)
            dataset.workclass = dataset.workclass.str.replace('?', 'Unk')
            dataset.occupation = dataset.occupation.str.replace('?', 'Unk')
            dataset['native-country'] = dataset['native-country'].str.replace('?', 'Unk')
            self.dataset_loader.set_dataset(dataset)
        except Exception as e:
            logging.error(f"Error cleaning dataset and saving it : {str(e)}")
            raise Exception("Error cleaning dataset and saving it", str(e))
    
    def __remove_outlier(self, col):
        sorted(col)
        Q1,Q3=np.percentile(col,[25,75])
        IQR=Q3-Q1
        lower_range= Q1-(1.5 * IQR)
        upper_range= Q3+(1.5 * IQR)
        return lower_range, upper_range
        
    def __removing_outliers_from_dataset(self):
        try:
            dataset = self.dataset_loader.get_dataset()
            for column in dataset.columns:
                if dataset[column].dtype != 'object': 
                    lr,ur=self.__remove_outlier(dataset[column])
                    dataset[column]=np.where(dataset[column]>ur,ur,dataset[column])
                    dataset[column]=np.where(dataset[column]<lr,lr,dataset[column])
                    
            self.dataset_loader.set_dataset(dataset)
        except Exception as e:
            logging.error(f"Error removing outliers from dataset : {str(e)}")
            raise Exception("Error removing outliers from dataset", str(e))
                
    def __converting_objects_to_categorical_codes(self):
        try:
            dataset = self.dataset_loader.get_dataset()
            for feature in dataset.columns: 
                if dataset[feature].dtype == 'object':
                    dataset[feature] = pd.Categorical(dataset[feature]).codes
                    
            self.dataset_loader.set_dataset(dataset)
        except Exception as e:
            logging.error(f"Error converting objects to categorical codes : {str(e)}")
            raise Exception("Error converting objects to categorical codes", str(e))