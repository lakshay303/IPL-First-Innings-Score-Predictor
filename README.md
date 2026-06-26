# 🏏 IPL First Innings Score Predictor

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge\&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge\&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A Machine Learning web application that predicts the **final first innings score** in an IPL match based on the current match situation using historical IPL data.

Developed as part of my **AI & Machine Learning Internship**.

---

# 📑 Table of Contents

* Project Overview
* Features
* Technologies Used
* Machine Learning Workflow
* Model Performance
* Project Structure
* Installation
* Usage
* Screenshots
* Future Improvements
* Author

---

# 📌 Project Overview

This project predicts the expected **final first innings score** during an IPL match.

The prediction is based on several match parameters including:

* 🏏 Batting Team
* 🎯 Bowling Team
* 🏟 Venue
* 👤 Batsman
* 🎳 Bowler
* 📈 Current Runs
* ❌ Wickets Lost
* ⏱ Overs Completed
* 🔥 Runs in Last 5 Overs
* 💥 Wickets Lost in Last 5 Overs
* 🏏 Striker Runs
* 🤝 Non-Striker Runs

The application uses a trained **Random Forest Regression** model to estimate the final score.

---

# 🚀 Features

* 🏏 Predict IPL First Innings Score
* 🤖 Machine Learning based prediction
* 📊 Random Forest Regression model
* 🔄 Data preprocessing using Pipeline
* 🎯 One-Hot Encoding
* 📈 Standard Scaling
* 🌐 Interactive Streamlit Web App
* 💻 User-friendly interface

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

# 📂 Project Structure

```text
IPL_First_Innings_Score_Predictor/
│
├── app.py
├── data.csv
├── ipl_score_predictor.pkl
├── IPL_First_Innings_Score_Predictor.ipynb
├── requirements.txt
├── README.md
└── images/
```

---

# ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Streamlit App Development
9. Deployment

---

# 📊 Model Performance

| Metric   |                   Value |
| -------- | ----------------------: |
| Model    | Random Forest Regressor |
| MAE      |                   ~3.40 |
| R² Score |                   ~0.95 |

The model demonstrates excellent predictive performance on the evaluation dataset.

---

# ▶️ Installation

Clone the repository:

```bash
git clone <your-github-repository-link>
```

Move into the project folder:

```bash
cd IPL_First_Innings_Score_Predictor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 📱 Usage

1. Select the batting team.
2. Select the bowling team.
3. Choose the venue.
4. Enter the current match statistics.
5. Click **Predict Score**.
6. View the predicted first innings score.

---

# 📷 Screenshots

Add screenshots after deploying the application.

```markdown

## Prediction Result

![Result](images/result.png)
```

---

# 🎯 Future Improvements

* 🏆 Match Winner Prediction
* 📈 Win Probability Prediction
* 🌐 Live IPL API Integration
* 📊 Interactive Visualizations
* 📱 Mobile-Friendly UI
* 📋 Team Performance Analytics

---

# 📌 Disclaimer

This project is developed for educational and learning purposes. Predictions are based on historical IPL data and should not be considered exact match outcomes.

---

# 👨‍💻 Author

**Lakshay Verma**

AI & Machine Learning Intern

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.
