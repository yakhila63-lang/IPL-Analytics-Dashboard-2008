import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🏏 IPL Analytics Dashboard - 2008 Season")

df = pd.read_csv("matches_2008.csv")

team = st.sidebar.selectbox("Team", ["All"] + sorted(set(df.team1) | set(df.team2)))
d = df if team == "All" else df[(df.team1 == team) | (df.team2 == team)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Matches", len(d))
c2.metric("Teams", 8)
c3.metric("Venues", df.venue.nunique())
c4.metric("Champion", "Rajasthan Royals")

fig1 = px.bar(d.winner.value_counts(), title='Wins by Team')
fig2 = px.pie(d, names='toss_decision', title='Toss: Bat vs Field', hole=.4)

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.dataframe(d)
