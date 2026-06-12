# Network Threat Analysis - Research Notes

## Project Objective

The objective of this project was to explore network activity data and determine whether characteristics such as login behavior, reputation scores, and network traffic could be used to identify malicious sessions.

---

## Dataset Overview

Rows: 9,537

Columns: 11

Target Variable:

* attack_detected

Features:

* network_packet_size
* protocol_type
* login_attempts
* session_duration
* encryption_used
* ip_reputation_score
* failed_logins
* browser_type
* unusual_time_access

---

## Exploratory Data Analysis

### Attack Distribution

Non-Attack Sessions: 5,273

Attack Sessions: 4,264

The dataset was relatively balanced, making it suitable for classification analysis.

---

### Failed Login Analysis

Average Failed Logins

* Non-Attack: 1.18
* Attack: 1.94

Finding:
Attack sessions showed approximately 64% more failed login attempts than non-attack sessions.

---

### Login Attempt Analysis

Average Login Attempts

* Non-Attack: 3.54
* Attack: 4.64

Finding:
Attack sessions exhibited roughly 31% more login attempts.

---

### Reputation Score Analysis

Average Reputation Score

* Non-Attack: 0.298
* Attack: 0.373

Finding:
The reputation score behaved differently than initially expected and warrants further investigation.

---

### Unusual Time Access

Average Unusual Time Access

* Non-Attack: 0.147
* Attack: 0.153

Finding:
Minimal difference observed between attack and non-attack sessions.

---

## Threat Scoring

Threat Score Formula

Threat Score =
(2 × Failed Logins)

* Login Attempts
* (3 × Unusual Time Access)

Results:

Average Threat Score

* Non-Attack: 6.79
* Attack: 9.63

Finding:
Attack sessions exhibited approximately 42% higher threat scores.

The top 10 highest-scoring sessions were all labeled as attacks.

---

## Anomaly Detection

Packet Size Threshold:

897.19

Anomalies Identified:

232 sessions

Anomaly Attack Rate:

43.1%

Overall Attack Rate:

44.7%

Finding:
Packet size anomalies were not strongly associated with attack activity.

---

## Machine Learning Model

Model:
Logistic Regression

Features:

* failed_logins
* login_attempts
* ip_reputation_score
* unusual_time_access
* network_packet_size

Target:

* attack_detected

Train/Test Split:
80/20

---

## Model Performance

Accuracy:
73.9%

Precision (Attack):
74%

Recall (Attack):
65%

F1 Score (Attack):
69%

---

## Confusion Matrix

True Negatives: 848

False Positives: 194

False Negatives: 304

True Positives: 562

---

## Feature Importance

1. ip_reputation_score (3.145)
2. failed_logins (0.924)
3. login_attempts (0.381)
4. unusual_time_access (0.040)
5. network_packet_size (-0.00012)

---

## Conclusions

Key indicators associated with attack activity:

* IP Reputation Score
* Failed Logins
* Login Attempts

Indicators with limited predictive value:

* Network Packet Size
* Unusual Time Access

A Logistic Regression model achieved 73.9% accuracy and successfully identified meaningful attack patterns within the dataset.
