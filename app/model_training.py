from sklearn.linear_model import LogisticRegression
import pickle
import os
import logger
from app import logging

class ModelTraining(object):
    def __init__(self, x_train_set, y_train_set):
        self.model = LogisticRegression()
        self.x_train_set = x_train_set
        self.y_train_set = y_train_set
        
    def __training_model(self):
        try:
            self.model.fit(self.x_train_set, self.y_train_set)
            logging.info(self.x_train_set.columns)
            logging.info("Model trained successfully")
        except Exception as e:
            logging.error(f"Error while training model: {str(e)}")
            raise Exception(f"Error while training model : {str(e)}")
        
    def __serializing_model(self, model_name, model_path):
        try:
            logging.info(f'{os.getcwd()}/{model_path}/{model_name}.pickle')
            serialized_model_path = open(f'{os.getcwd()}/{model_path}/{model_name}.pickle', "wb")
            pickle.dump(self.model, serialized_model_path)
            logging.info("Model saved successfully")
        except Exception as e:
            logging.error(f"Error saving model : {str(e)}")
            raise Exception("Error saving model", str(e))
            
    def model_training_pipeline(self, model_name, model_path):
        try:
            self.__training_model()
            self.__serializing_model(model_name, model_path)
            logging.info("Model training pipeline completed successfully")
        except Exception as e:
            logging.error(f"Error in training model pipeline : {str(e)}")
            raise Exception("Error in training model pipeline : ", str(e))