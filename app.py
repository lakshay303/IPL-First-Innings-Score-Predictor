import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="IPL First Innings Score Predictor",page_icon="🏏",layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

@st.cache_resource
def load_model():
    return joblib.load("ipl_score_predictor.pkl")

df=load_data()
model=load_model()

st.sidebar.title("🏏 IPL Score Predictor")
st.sidebar.info("Predict the first innings score using a trained Random Forest pipeline.")

st.title("🏏 IPL First Innings Score Predictor")

batting=sorted(df['batting_team'].dropna().unique())
bowling=sorted(df['bowling_team'].dropna().unique())
venues=sorted(df['venue'].dropna().unique())
batsmen=sorted(df['batsman'].dropna().unique())
bowlers=sorted(df['bowler'].dropna().unique())

c1,c2=st.columns(2)
with c1:
    batting_team=st.selectbox("Batting Team",batting)
    venue=st.selectbox("Venue",venues)
    batsman=st.selectbox("Batsman",batsmen)
    runs=st.number_input("Current Runs",0,300,70)
    overs=st.number_input("Overs Completed",5.0,20.0,10.0,0.1)
    striker=st.number_input("Striker Runs",0,200,30)
with c2:
    bowling_team=st.selectbox("Bowling Team",[t for t in bowling if t!=batting_team] or bowling)
    bowler=st.selectbox("Bowler",bowlers)
    wickets=st.number_input("Wickets",0,10,2)
    runs_last_5=st.number_input("Runs in Last 5 Overs",0,100,40)
    wickets_last_5=st.number_input("Wickets in Last 5 Overs",0,5,1)
    non_striker=st.number_input("Non-Striker Runs",0,200,20)

if st.button("Predict Score",use_container_width=True):
    inp=pd.DataFrame({
        "batting_team":[batting_team],
        "bowling_team":[bowling_team],
        "venue":[venue],
        "batsman":[batsman],
        "bowler":[bowler],
        "runs":[runs],
        "wickets":[wickets],
        "overs":[overs],
        "runs_last_5":[runs_last_5],
        "wickets_last_5":[wickets_last_5],
        "striker":[striker],
        "non-striker":[non_striker]
    })
    try:
        pred=model.predict(inp)[0]
        st.success(f"🏏 Predicted First Innings Score: {round(pred)}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.markdown("---")
st.caption("Developed by Lakshay Verma | AI & ML Internship Project")
