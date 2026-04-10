import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
matches=pd.read_csv("archive/IPL_Matches_2008_2022.csv")
print(matches.shape)
print(matches.columns.tolist())
print(matches.head())
# Most match wins by team
wins = matches['WinningTeam'].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=wins.values, y=wins.index, palette='viridis')
plt.title('Top 10 Teams by Match Wins (2008-2022)')
plt.xlabel('Number of Wins')
plt.ylabel('Team')
plt.tight_layout()
plt.show()
#  Toss impact on match result
matches['toss_match_win'] = matches['TossWinner'] == matches['WinningTeam']

toss_impact = matches['toss_match_win'].value_counts()
labels = ['Won Toss and the Match', 'Won Toss but not the Match']

plt.figure(figsize=(6,6))
plt.pie(toss_impact.values, labels=labels, autopct='%1.1f%%', colors=['#4CAF50','#FF5252'])
plt.title('Does Winning the Toss Help Win the Match?')
plt.show()
#  Top 5 Player of the Match
potm = matches['Player_of_Match'].value_counts().head(5)

plt.figure(figsize=(10,5))
sns.barplot(x=potm.index, y=potm.values, palette='magma')
plt.title('Top 5 Player of the Match Winners (2008-2022)')
plt.xlabel('Player')
plt.ylabel('Number of Awards')
plt.tight_layout()
plt.show()
# Highest scoring pitches
balls = pd.read_csv("archive/IPL_Ball_by_Ball_2008_2022.csv")

venue_map = matches[['ID','Venue']]
balls = balls.merge(venue_map, left_on='ID', right_on='ID')

venue_runs = balls.groupby('Venue')['batsman_run'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=venue_runs.values, y=venue_runs.index, palette='rocket')
plt.title('Top 10 Highest Run-Scoring Venues (2008-2022)')
plt.xlabel('Total Runs Scored')
plt.ylabel('Venue')
plt.tight_layout()
plt.show()