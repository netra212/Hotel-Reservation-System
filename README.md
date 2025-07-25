# 🏨 Hotel Reservation System

A machine learning-based project designed to predict whether a hotel booking will be canceled or not. This solution helps hotels optimize **revenue**, **target marketing efforts**, and **detect fraudulent behavior** — improving decision-making and profitability.

---

## 📌 Problem Statement

To build a predictive model that classifies whether a customer will **cancel** a hotel booking based on their reservation details.

---

## 🎯 Target Audience

The primary audience is **hotels** and **hospitality businesses** aiming to improve booking reliability, increase revenue, and reduce operational disruptions due to cancellations.

---

## 💼 Real-World Use Cases

### 1. Revenue Management
Allows smart overbooking by predicting cancellations in advance.  
**Example**: If the system predicts *Arun* will cancel his booking for Room A509, the hotel can allow *Rahul* to book the same room — minimizing revenue loss.

### 2. Targeted Marketing
Enables hotels to provide **personalized offers** (e.g., free dinner, spa access) to customers who are likely to cancel, increasing retention.

### 3. Fraud Detection
Detects and flags users with a pattern of frequent cancellations, helping hotels reduce fraudulent or disruptive behavior.

---

## Preject Workflow

![Overview of Project Workflow](/Images/Project-Workflow.png)

---

## 📊 Dataset

**Source**: Kaggle - Hotel Booking Dataset  
The dataset includes the following key features:

| Column Name                     | Description                             |
|--------------------------------|-----------------------------------------|
| `Booking_ID`                   | Unique ID for each booking              |
| `no_of_adults`                 | Number of adults                        |
| `no_of_children`               | Number of children                      |
| `no_of_weekend_nights`        | Weekend nights booked                   |
| `no_of_week_nights`           | Weekday nights booked                   |
| `type_of_meal_plan`           | Selected meal plan                      |
| `required_car_parking_space`  | Parking required (1) or not (0)         |
| `room_type_reserved`          | Type of room reserved                   |
| `lead_time`                   | Days between booking and check-in       |
| `arrival_year/month/date`     | Arrival date                            |
| `market_segment_type`         | Booking source                          |
| `repeated_guest`              | Is the guest a repeat visitor?          |
| `no_of_previous_cancellations`| Previous cancellations by customer       |
| `no_of_previous_bookings_not_canceled` | Previous successful bookings   |
| `avg_price_per_room`          | Average cost per room                   |
| `no_of_special_requests`      | Any special requests made               |
| `booking_status`              | Target variable: `Canceled` / `Not_Canceled` |

---
## 📷 Model Output & UI

## 🛠️ CI/CD Deployment Pipeline

This project is fully automated using **Jenkins + Docker + GCP Cloud Run**. Below are the visual results of successful CI/CD execution and cloud deployment.

### ✅ Successful Jenkins Pipeline Execution

### 🚀 CI-CD Pipeline success

![CI CD Pipeline success](/Images/CI-CD-pipeline-success.png)

### 🚀 GCP Dashboard

![GCP Console](/Images/deployed_containers.png)

### 🚀 Google Cloud Run Deployment

![GCP Cloud Run Deployment Screenshot](/Images/deployed_project.png)

---

### 🎯 MLflow Tracking UI
Track experiments, models, and metrics:

![MLflow Dashboard](/Predictions/mlflow_dataset1.png)
![](/Predictions/mlflow_model_parameters.png)
![](/Predictions/mlflow_accuracy.png)

---

### 🧾 Live UI: Hotel Booking Predictor

> Users input booking details to get cancellation predictions.

![Model Prediction](/Predictions/PredictionImage1.png)
![](/Predictions/PredictionImage2.png)

---

## 📈 Model Performance

| Metric     | Score |
|------------|-------|
| ✅ Accuracy | **88.08%** |
| 🎯 Precision | **86.63%** |
| 🔄 Recall    | **90.05%** |
| 🧠 F1 Score  | **88.31%** |

_Model: LightGBM + Hyperparameter Tuning_

---

## 🛠️ Environment Setup (macOS/Linux)

To keep dependencies isolated and reproducible, use a virtual environment.

### 📦 Create and Activate Virtual Environment

```bash
# Step 1: Navigate to your project directory
cd /path/to/Hotel-Reservation-System

# Step 2: Create a virtual environment
python3 -m venv .venv

# Step 3: Activate the virtual environment
source .venv/bin/activate

# Step 4: Upgrade pip
pip install --upgrade pip

# Step 5: Install dependencies
pip install -r requirements.txt
```

## 🧠 Tech Stack

- **Programming Language**: Python, HTML, CSS (front-end)
- **Data Analysis & Processing**: Pandas, NumPy
- **Modeling**: Scikit-learn, XGBoost, Random Forest, Logistic Regression
- **Visualization**: Matplotlib, Seaborn
- **Version Control**: Git, GitHub

---

## 🚀 How to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/netra212/Hotel-Reservation-System.git
    cd Hotel-Reservation-System
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the notebook or script to train the model and view results:
    ```bash
    jupyter notebook hotel_reservation_prediction.ipynb

    python app.py
    ```

---