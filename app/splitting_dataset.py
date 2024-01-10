from sklearn.model_selection import train_test_split
from app import logging

class DatasetSplitter(object):
    def __init__(self, dataset, column_name):
        self.X_set = dataset.drop(column_name, axis=1)
        self.Y_set = dataset[[column_name]]
        self.X_train = None
        self.Y_train = None
        
    def splitting_for_training_testing(self):
        logging.info(self.X_set)
        logging.info(self.Y_set)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X_set, self.Y_set, test_size=0.2, random_state=1)
        logging.info(self.X_train)
        logging.info(self.Y_train)
        
        
    def get_x_train_set(self):
        return self.X_train
    
    def get_y_train_set(self):
        return self.Y_train
        
    
        