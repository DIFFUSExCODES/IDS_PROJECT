Machine Learning Based Intrusion Detection System

Overview

This project implements a Machine Learning-based Intrusion Detection System (IDS) for network security using the NSL-KDD dataset. The objective is to detect malicious network activity by distinguishing normal traffic from network attacks and to evaluate the performance of different machine learning algorithms on a standardized benchmark dataset.

The project follows a structured machine learning workflow that includes data exploration, preprocessing, model development, performance evaluation, and comparative analysis. In later stages, the project will be extended with model explainability techniques and a web-based interface for interactive predictions.

Objectives

* Perform exploratory data analysis on the NSL-KDD dataset.
* Preprocess network traffic data for machine learning.
* Build a binary intrusion detection model to classify network traffic as either normal or malicious.
* Compare the performance of multiple machine learning algorithms.
* Analyze model performance using standard classification metrics.
* Extend the project with explainability and deployment features.

Dataset

The project uses the NSL-KDD dataset, an improved version of the KDD Cup 1999 dataset designed for evaluating intrusion detection systems. The dataset removes many redundant records present in the original dataset while maintaining a diverse collection of normal and malicious network traffic.

Training and testing are performed using the official NSL-KDD train-test split.

Machine Learning Models

The following models are implemented and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* LightGBM

Additional models may be included as the project progresses.

Evaluation Metrics

Model performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Future versions will also include:

* ROC-AUC
* Precision-Recall Curve
* Cross Validation
* Feature Importance Analysis
* SHAP Explainability

Project Structure

.
├── data
│   ├── external
│   ├── interim
│   ├── processed
│   └── raw
│
├── models
│
├── notebooks
│
├── references
│
├── reports
│   └── figures
│
├── src
│   ├── modeling
│   ├── dataset.py
│   ├── features.py
│   ├── plots.py
│   └── config.py
│
├── README.md
└── LICENSE

Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* LightGBM
* Matplotlib
* Jupyter Notebook

Current Status

The project is under active development.

Completed:

* Dataset collection
* Exploratory Data Analysis
* Data preprocessing
* Binary classification pipeline
* Initial model comparison

Planned:

* Hyperparameter optimization
* Explainable AI using SHAP
* Multi-class intrusion detection
* Flask-based web application
* Research paper and project report

License

This project is intended for academic and educational purposes.
