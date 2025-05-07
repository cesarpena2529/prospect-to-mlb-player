# prospect-to-mlb-player
Predicting MLB success using minor league statistics and machine learning (Capstone 2024)
⚾ MLB Player Success Predictor

Predicting whether a minor league baseball player will become a successful MLB player based on their AA and AAA performance. This was developed as my 2024 AI/ML capstone project.

📌 Project Overview

This project analyzes minor league data from 2006–2024 and predicts the likelihood of MLB success using:

Standard and advanced hitting statistics

WAR (Wins Above Replacement) as the success label

Machine learning classification models

We define success as accumulating 2+ career WAR in MLB.

🧱 Key Components

minor_league_combined.csv: Raw AA/AAA player data

War-archeive-2006-2024.csv: MLB WAR stats from Baseball Reference

merge_fuzzy_war.py: Script to match minor league names to MLB WAR data using fuzzy matching

minor_league_grouped_fuzzy_labeled.csv: Final dataset, grouped per player and labeled for success

model_training.ipynb: Notebook for training classifiers

api_backend.py (optional): FastAPI endpoint for live predictions

🔍 Features Used

Rate stats (AVG, OBP, SLG, OPS, BB%, K%, ISO, BABIP, wRC+)

Volume stats (AB, H, HR, SO, BB, RBI, SB)

Level: AA vs AAA

🧠 ML Model

Planned/implemented:

Logistic Regression

Random Forest / XGBoost

SHAP analysis for explainability

Target: MLB_success → Boolean (True if 2+ WAR)

🎯 Future Features

Player profile input form

Predictive simulation: "What if this player improves X stat?"

Visualization dashboard

📂 How to Run

Clone the repo

Run merge_fuzzy_war.py to prepare the dataset

Train model using model_training.ipynb

(Optional) Launch API with api_backend.py

🙌 Acknowledgments

Baseball Reference

Fangraphs

Sean Lahman Baseball Database

thefuzz for fuzzy name matching

🧠 Author

This project was developed by [Your Name] as part of a 2024 AI capstone. Open to contributions, feedback, or collaboration!

