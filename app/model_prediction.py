import numpy as np
import pandas as pd
from flask import Flask, request,render_template
from app import logging
import pickle
import os

class ModelPrediction(object):
    def __init__(self):
        self.loaded_model = pickle.load(open(f'{os.getcwd()}/model/adult_model.pickle', 'rb'))
        
    def predict(self, form_data_dict):
        logging.info(form_data_dict)
        
        to_predict_list = list(form_data_dict.values()) 
        logging.info(to_predict_list)
        
        to_predict_list = list(map(int, to_predict_list))
        logging.info(to_predict_list)
        
        to_predict = np.array(to_predict_list).reshape(1, 12)
        logging.info(to_predict)
        
        prediction_result = self.loaded_model.predict(to_predict)
        
        prediction = None
        if int(prediction_result) == 1:
            prediction = 'Income is more than 50K'
        else:
            prediction = 'Income is less than 50K'
        return prediction