import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
matches = pd.read_csv("data/matches.csv")

# -------------------------------
# 1. Most Successful Teams
# -------------------------------
team_wins = matches['winner'].value_counts()

plt.figure(figsize=(14,7))
team_wins.plot(kind='bar')

plt.title("Most Successful IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig("teams.png")
plt.show()

# Insight:
# Mumbai Indians and Chennai Super Kings are the most dominant teams.


# -------------------------------
# 2. Toss Impact
# -------------------------------
toss_win = matches[matches['toss_winner'] == matches['winner']]

percentage = (len(toss_win) / len(matches)) * 100

print("Toss win → Match win %:", percentage)

# Insight:
# Toss has around 50% impact and does not guarantee victory.


# -------------------------------
# 3. Matches per Season
# -------------------------------
matches_per_season = matches['season'].value_counts().sort_index()

plt.figure(figsize=(10,5))
matches_per_season.plot(marker='o')

plt.title("Matches per Season")
plt.xlabel("Season")
plt.ylabel("Matches")

plt.tight_layout()

plt.savefig("season.png")
plt.show()


# -------------------------------
# 4. Top Venues
# -------------------------------
venues = matches['venue'].value_counts().head(8)   # 👈 reduced to 8 for clarity

plt.figure(figsize=(14,7))
venues.plot(kind='bar')

plt.title("Top IPL Venues")
plt.xlabel("Venue")
plt.ylabel("Matches Played")

plt.xticks(rotation=60, ha='right')
plt.tight_layout()

plt.savefig("venues.png")
plt.show()

# Insight:
# Some venues consistently host more matches, indicating popularity.