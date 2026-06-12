# Network Threat Analysis

A cybersecurity and machine learning project focused on identifying malicious network sessions through exploratory data analysis, threat scoring, anomaly detection, and machine learning classification.

## Project Overview

This project analyzes network session data to determine which characteristics are most strongly associated with malicious activity.

The workflow includes:

* Exploratory Data Analysis (EDA)
* Threat Scoring
* Anomaly Detection
* Machine Learning Classification
* Feature Importance Analysis

## Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-Learn
* Git
* GitHub

## Dataset

The dataset contains 9,537 network sessions and 11 features related to authentication behavior, network activity, and reputation metrics.

Target Variable:

* attack_detected

## Key Findings

### Strong Indicators

* IP Reputation Score
* Failed Login Attempts
* Login Attempts

### Weak Indicators

* Network Packet Size
* Unusual Time Access

## Threat Scoring Results

A custom threat scoring system was developed to prioritize suspicious sessions.

Average Threat Score:

* Non-Attack: 6.79
* Attack: 9.63

The top 10 highest-scoring sessions were all labeled as attacks.

## Machine Learning Results

Model:

* Logistic Regression

Performance:

* Accuracy: 73.9%
* Precision: 74%
* Recall: 65%
* F1 Score: 69%

## Repository Structure

network-threat-analysis/

├── data/

├── images/

├── main.py

├── analysis_notes.md

├── requirements.txt

└── README.md

## Future Improvements

* Additional feature engineering
* More advanced machine learning models
* Real-time monitoring dashboard
* Hyperparameter optimization
* Cross-validation testing

## Author

Anthony Villagomez

Bachelor of Science in Computer Science
