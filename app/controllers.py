import logger
from app.dataloader import DatasetLoader
from app.dataset_cleaning import DatasetCleaner
from app.splitting_dataset import DatasetSplitter
from app.model_training import ModelTraining
from app.model_prediction import ModelPrediction
from app import logging, app, jsonify, render_template, request
import os

@app.route('/home')
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        logging.info(f'Error rendering home page : {str(e)}')
        return jsonify({'error' : 'Not able to load Home page'})
    
@app.route('/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        model_prediction_object  = ModelPrediction()
        prediction_result = model_prediction_object.predict(form_data)
        return render_template("result.html", prediction = prediction_result) 
    

@app.route('/training', methods=['GET'])
def training_model():
    try:
        dataset_loader = DatasetLoader()
        logging.info(f"DatasetLoader : {dataset_loader}")
        logging.info(f"Dataset : {dataset_loader.get_dataset()}")
        
        dataset_cleaner = DatasetCleaner(dataset_loader)
        dataset_cleaner.execute_cleaning_pipeline()
        
        dataset_splitter = DatasetSplitter(dataset_loader.get_dataset(), 'salary')
        dataset_splitter.splitting_for_training_testing()
        logging.info("Dataset splitting is successful")
        
        model_training_object = ModelTraining(dataset_splitter.get_x_train_set(), dataset_splitter.get_y_train_set())
        logging.info(f"Model training object : {model_training_object}")
        logging.info(f"X Train set : {model_training_object.x_train_set}")
        logging.info(f"Y Train set : {model_training_object.y_train_set}")
        
        model_training_object.model_training_pipeline('adult_model', '/model')
        
        return jsonify({'message': 'Model is trained successfully'})
        
    except Exception as e:
        logging.error(f'Error training model : {str(e)}')
        return jsonify({'error': 'Error training model'})
        
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Ping successful'})