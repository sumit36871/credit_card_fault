# Credit Card Fraud Detection Project

## Overview
This project is an end-to-end Machine Learning pipeline designed to detect credit card fraud. It handles data validation, preprocessing, training, and prediction through an API powered by Flask.

## Features
- **Automated Data Validation**: Ensures correct file format, schema, and handles missing values.
- **Dynamic Clustering**: Uses K-Means to group similar data.
- **Model Tuning**: Selects the best-performing model for each cluster.
- **REST API Integration**: Supports `/train` and `/predict` routes for user interaction.
- **Error Logging**: Captures errors and logs them for debugging.

## Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, XGBoost
- **Data Handling**: pandas, numpy
- **Deployment**: Gunicorn, Flask-CORS

## File Structure
```
├── main.py                   # Flask app entry point
├── test.py                   # Test script for training/prediction
├── trainingModel.py          # Model training pipeline
├── predictFromModel.py       # Prediction pipeline
├── training_Validation_Insertion.py  # Data validation for training
├── prediction_Validation_Insertion.py # Data validation for prediction
├── schema_training.json      # Schema definition for training data
├── schema_prediction.json    # Schema definition for prediction data
├── requirements.txt          # List of dependencies
└── Procfile                  # Deployment configuration
```

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repo_url>
   cd <project_directory>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate       # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python main.py
   ```

## API Endpoints
- **`/train`** (POST): Triggers data validation and model training.
  - Request Body: `{ "filepath": "path/to/training/data" }`
  - Response: `Training successful!!`

- **`/predict`** (POST): Runs data validation and prediction.
  - Request Body: `{ "filepath": "path/to/prediction/data" }`
  - Response: `Prediction File created at path/to/output.csv`

## Logs and Output
- **Logs:** Stored in `Training_Logs/` and `Prediction_Logs/`.
- **Predictions:** Saved as `Prediction_Output_File/Predictions.csv`.

## Error Handling
Common errors like incorrect file formats, missing columns, or invalid data are logged with detailed messages.

## Future Enhancements
- Add real-time data drift detection and auto-retraining.
- Enhance API with more detailed error messages.
- Build a frontend UI for easier file upload and model monitoring.

---

Happy fraud detecting! 🚀

