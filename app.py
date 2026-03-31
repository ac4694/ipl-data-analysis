import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="IPL Dashboard", layout="wide")

st.title("🏏 IPL Advanced Dashboard")

# Load data
matches = pd.read_csv("data/matches.csv")

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("Filters")

# Season filter
seasons = sorted(matches['season'].dropna().unique())
selected_season = st.sidebar.selectbox("Select Season", ["All"] + list(seasons))

# Team filter
teams = sorted(set(matches['team1']).union(set(matches['team2'])))
selected_team = st.sidebar.selectbox("Select Team", ["All"] + teams)

# Apply filters
filtered = matches.copy()

if selected_season != "All":
    filtered = filtered[filtered['season'] == selected_season]

if selected_team != "All":
    filtered = filtered[
        (filtered['team1'] == selected_team) |
        (filtered['team2'] == selected_team)
    ]

# -------------------------------
# METRICS
# -------------------------------
st.subheader("📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Matches", len(filtered))
col2.metric("Teams", filtered['team1'].nunique())
col3.metric("Venues", filtered['venue'].nunique())

# -------------------------------
# TEAM WINS (Interactive)
# -------------------------------
st.subheader("🏆 Most Successful Teams")

team_wins = filtered['winner'].value_counts().reset_index()
team_wins.columns = ['Team', 'Wins']

fig1 = px.bar(team_wins, x='Team', y='Wins', title="Team Wins")
st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# PIE CHART (Win Distribution)
# -------------------------------
st.subheader("🥧 Win Distribution")

fig2 = px.pie(team_wins.head(5), names='Team', values='Wins',
              title="Top 5 Teams Win Share")

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# TOSS IMPACT
# -------------------------------
st.subheader("🎲 Toss Impact")

toss_win = filtered[filtered['toss_winner'] == filtered['winner']]
percentage = (len(toss_win) / len(filtered)) * 100 if len(filtered) > 0 else 0

st.metric("Toss Win → Match Win %", f"{percentage:.2f}%")

# -------------------------------
# MATCHES PER SEASON
# -------------------------------
st.subheader("📅 Matches per Season")

season_data = matches['season'].value_counts().sort_index().reset_index()
season_data.columns = ['Season', 'Matches']

fig3 = px.line(season_data, x='Season', y='Matches', markers=True)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------------
# TOP VENUES
# -------------------------------
st.subheader("🏟️ Top Venues")

venues = filtered['venue'].value_counts().head(8).reset_index()
venues.columns = ['Venue', 'Matches']

fig4 = px.bar(venues, x='Venue', y='Matches')

st.plotly_chart(fig4, use_container_width=True)

# -------------------------------
# DATA TABLE
# -------------------------------
st.subheader("📄 Raw Data")

if st.checkbox("Show Data"):
    st.dataframe(filtered)