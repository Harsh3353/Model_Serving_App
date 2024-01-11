# Model Serving Service

This repository contains a simple Flask-based model serving service that allows you to train a logistic regression model and make predictions using form data. The service has two endpoints: `/training` for model training and `/home` for making predictions.

## Getting Started

### Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- Flask
- pandas
- scikit-learn

You can install the required Python packages using the following command:

```bash
pip install flask pandas scikit-learn
```

### Running the Code

To run the server, execute the following command in your terminal:

```bash
python3 server.py
```

The server will start, and you can access the endpoints at the following URLs:

- Training Endpoint: `http://127.0.0.1:8080/training` (GET request)
- Form Endpoint: `http://127.0.0.1:8080/home` (GET request)
- Prediction Endpoint: `http://127.0.0.1:8080/prediction` (POST request)

## Endpoints

### Training Endpoint (`/training`)

- **Method:** GET
- **Description:** Trains a logistic regression model using a provided CSV dataset.
- **Dataset:** The dataset file should be named `dataset.csv`.
- **Model File:** The trained model is saved as `logistic_regression_model.joblib`.
- **Response:** JSON response with a message indicating successful training and the model's accuracy.

### Prediction Endpoint (`/prediction`)

- **Method:** POST
- **Description:** Makes predictions using the trained logistic regression model.
- **Input:** Form data is used for input.
- **Model:** The trained model is loaded from `logistic_regression_model.joblib`.
- **Response:** HTML page is renderd showing model's response.

## Example Usage

### Training the Model

```bash
curl http://127.0.0.1:8080/training
```

### Making Predictions

```bash
curl -X POST -d "feature1=value1&feature2=value2" http://127.0.0.1:8080/prediction
```

Replace `feature1`, `feature2`, etc., and `value1`, `value2`, etc., with the actual features and values for prediction.

## Contributors

- Harsh Dusane

Feel free to contribute by forking the repository and creating pull requests. If you encounter any issues or have suggestions, please open an issue.

Happy modeling and serving!
