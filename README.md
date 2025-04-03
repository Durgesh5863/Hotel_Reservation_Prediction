# Hotel Reservation Prediction System

## Overview
This project is a machine learning-based system for predicting hotel reservation cancellations. It implements a complete ML pipeline from data ingestion to model deployment with a web interface for real-time predictions.

## Features
- Automated data ingestion from Google Cloud Storage
- Data preprocessing and feature engineering
- Model training using LightGBM with hyperparameter tuning
- MLflow integration for experiment tracking
- Flask web application for real-time predictions
- Containerized deployment with Docker
- CI/CD pipeline using Jenkins

## Project Structure
```
├── artifacts/               # Directory for storing pipeline artifacts
│   ├── models/             # Trained model files
│   ├── processed/          # Processed datasets
│   └── raw/                # Raw datasets
├── config/                 # Configuration files
│   ├── config.yaml         # Main configuration parameters
│   ├── model_params.py     # Model hyperparameters
│   └── paths_config.py     # File path configurations
├── custom_jenkins/         # Custom Jenkins configuration
├── logs/                   # Application logs
├── notebook/               # Jupyter notebooks for exploration
├── pipeline/               # ML pipeline implementation
│   └── training_pipeline.py # Main pipeline orchestration
├── src/                    # Source code
│   ├── data_ingestion.py   # Data download and splitting
│   ├── data_preprocessing.py # Feature engineering and preprocessing
│   ├── model_training.py   # Model training and evaluation
│   ├── logger.py           # Logging configuration
│   └── custom_exception.py # Custom exception handling
├── static/                 # Static files for web app
├── templates/              # HTML templates for web app
├── utils/                  # Utility functions
├── application.py          # Flask web application
├── Dockerfile              # Docker configuration
├── Jenkinsfile             # Jenkins pipeline configuration
├── requirements.txt        # Python dependencies
└── setup.py                # Package setup configuration
```

## Installation

### Prerequisites
- Python 3.7+
- Google Cloud SDK (for data ingestion from GCS)
- Docker (for containerized deployment)

### Local Setup
1. Clone the repository
   ```
   git clone https://github.com/Durgesh5863/hotel-reservation-prediction.git
   cd hotel-reservation-prediction
   ```

2. Create and activate a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -e .
   ```

4. Run the training pipeline
   ```
   python pipeline/training_pipeline.py
   ```

5. Start the web application
   ```
   python application.py
   ```

### Docker Deployment
1. Build the Docker image
   ```
   docker build -t hotel-reservation-prediction:latest .
   ```

2. Run the container
   ```
   docker run -p 8080:8080 hotel-reservation-prediction:latest
   ```

## Usage

### Web Application
Access the web application at http://localhost:8080 after starting the application. Enter the required information in the form to get a prediction on whether a hotel reservation is likely to be canceled.

### Training Pipeline
The training pipeline consists of three main components:
1. **Data Ingestion**: Downloads data from Google Cloud Storage and splits it into training and test sets
2. **Data Preprocessing**: Handles categorical encoding, feature selection, and data balancing
3. **Model Training**: Trains a LightGBM model with hyperparameter tuning and logs metrics with MLflow

## CI/CD Pipeline
The project includes a Jenkins pipeline configuration that:
1. Clones the repository
2. Sets up a virtual environment and installs dependencies
3. Builds and pushes a Docker image to Google Container Registry
4. Deploys the application to Google Cloud Run

## Model Information
The prediction model uses LightGBM with hyperparameter tuning via RandomizedSearchCV. The model is trained to predict whether a hotel reservation will be canceled based on features such as lead time, price, arrival date, and special requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
