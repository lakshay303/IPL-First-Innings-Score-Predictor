import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="🏏 IPL First Innings Score Predictor",
    page_icon="🏏",
    layout="wide"
)

# ----------------------------------------------------
# Custom CSS
# ----------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
    color: #FF4B4B;
}

.stButton>button {
    width:100%;
    background-color:#FF4B4B;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stSuccess{
    font-size:22px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Load Model
# ----------------------------------------------------
@st.cache_resource
def load_objects():

    preprocessor = joblib.load("preprocessor.pkl")
    model = joblib.load("model.pkl")

    return preprocessor, model


preprocessor, model = load_objects()

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()
required_columns = [
    "venue",
    "batting_team",
    "bowling_team",
    "batsman",
    "bowler",
    "runs",
    "wickets",
    "overs",
    "runs_last_5",
    "wickets_last_5",
    "striker",
    "non-striker"
]

missing = [c for c in required_columns if c not in df.columns]

if missing:
    st.error(f"Missing columns in data.csv: {missing}")
    st.stop()

# ----------------------------------------------------
# Extract Dropdown Values
# ----------------------------------------------------

teams = sorted(df["batting_team"].unique())

venues = sorted(df["venue"].unique())

batsmen = sorted(df["batsman"].unique())

bowlers = sorted(df["bowler"].unique())

# ----------------------------------------------------
# Title
# ----------------------------------------------------

st.title("🏏 IPL First Innings Score Predictor")

st.markdown(
"""
Predict the final **First Innings Score**
using Machine Learning.

Fill the current match situation below.
"""
)

st.divider()

# ----------------------------------------------------
# Team Selection
# ----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    batting_team = st.selectbox(
        "Batting Team",
        teams
    )

with col2:

    bowling_team = st.selectbox(
        "Bowling Team",
        [team for team in teams if team != batting_team]
    )

# ----------------------------------------------------
# Venue
# ----------------------------------------------------

venue = st.selectbox(
    "Venue",
    venues
)

st.divider()
# ----------------------------------------------------
# Player Selection
# ----------------------------------------------------

col3, col4 = st.columns(2)

with col3:

    batsman = st.selectbox(
        "Batsman",
        batsmen
    )

with col4:

    bowler = st.selectbox(
        "Bowler",
        bowlers
    )

st.divider()

# ----------------------------------------------------
# Match Statistics
# ----------------------------------------------------

col5, col6 = st.columns(2)

with col5:

    runs = st.number_input(
        "Current Runs",
        min_value=0,
        max_value=300,
        value=80
    )

    wickets = st.number_input(
        "Wickets Lost",
        min_value=0,
        max_value=10,
        value=2
    )

    overs = st.number_input(
        "Overs Completed",
        min_value=0.0,
        max_value=20.0,
        value=10.0,
        step=0.1
    )

    runs_last_5 = st.number_input(
        "Runs in Last 5 Overs",
        min_value=0,
        max_value=100,
        value=45
    )

with col6:

    wickets_last_5 = st.number_input(
        "Wickets in Last 5 Overs",
        min_value=0,
        max_value=10,
        value=1
    )

    striker = st.number_input(
        "Striker Runs",
        min_value=0,
        max_value=200,
        value=35
    )

    non_striker = st.number_input(
        "Non-Striker Runs",
        min_value=0,
        max_value=200,
        value=20
    )

st.divider()

predict = st.button("🏏 Predict Final Score")
# ----------------------------------------------------
# Prediction
# ----------------------------------------------------

if predict:

    # Basic Validation
    if overs > 20:
        st.error("Overs cannot exceed 20.")
        st.stop()

    if wickets > 10:
        st.error("Wickets cannot exceed 10.")
        st.stop()

    if batting_team == bowling_team:
        st.error("Batting Team and Bowling Team cannot be the same.")
        st.stop()

    # Create Input DataFrame
    input_df = pd.DataFrame({

    "venue": [venue],
    "batting_team": [batting_team],
    "bowling_team": [bowling_team],
    "batsman": [batsman],
    "bowler": [bowler],
    "runs": [runs],
    "wickets": [wickets],
    "overs": [overs],
    "runs_last_5": [runs_last_5],
    "wickets_last_5": [wickets_last_5],
    "striker": [striker],
    "non-striker": [non_striker]

})

    # Transform
    input_processed = preprocessor.transform(input_df)
    # Convert sparse matrix to dense if needed
    try:
    input_processed = input_processed.toarray()
except AttributeError:
    pass

    # Predict
    prediction = model.predict(input_processed)[0]

    prediction = int(round(prediction))

    st.divider()

    st.markdown("## 🏆 Predicted First Innings Score")

    st.success(
        f"🏏 Expected Score : **{prediction} Runs**"
    )

    st.info(
        f"📊 Prediction Range : **{prediction-5} - {prediction+5} Runs**"
    )

    st.balloons()

    st.divider()

    st.markdown(
        """
        ### 📌 Disclaimer

        This prediction is generated using a Machine Learning model trained
        on historical IPL data. Actual match outcomes may vary depending
        on match situations and player performances.
        """
    )

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div style='text-align:center'>

Developed with ❤️ by <b>Lakshay Verma</b>

AI & Machine Learning Intern

</div>
""",
unsafe_allow_html=True
)