import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load and clean data
df = pd.read_csv(r"C:\Users\ved49\Downloads\Python_Dataset.csv")
df.dropna(subset=["pollutant_min", "pollutant_max", "pollutant_avg"], inplace=True)

# 1. Line Plot - Pollution trend for one state
state = df['state'].value_counts().idxmax()
state_data = df[df['state'] == state].sort_values("last_update")
plt.figure(figsize=(10, 5))
plt.plot(state_data["last_update"], state_data["pollutant_avg"])
plt.title(f"Pollution Trend in {state}")
plt.xlabel("Date")
plt.ylabel("Pollutant Avg")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar Chart - Avg pollution per state (top 10)
state_avg = df.groupby("state")["pollutant_avg"].mean().sort_values(ascending=False).head(10)
state_avg.plot(kind="bar", title="Top 10 Polluted States",color = 'mediumpurple', figsize=(10, 5))
plt.ylabel("Average Pollution")
plt.tight_layout()
plt.show()

# 3. Histogram - Pollutant Average Distribution
sns.histplot(df["pollutant_avg"], bins=30, kde=True)
plt.title("Pollutant Average Distribution")
plt.tight_layout()
plt.show()

# 4. Pie Chart - Pollutant ID distribution 
pollutant_dist = df["pollutant_id"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(pollutant_dist, labels=pollutant_dist.index, autopct="%1.1f%%")
plt.title("Pollutant Type Share")
plt.tight_layout()
plt.show()

# 5. Scatter Plot - Geo location by pollution (State-wise)
for state in df['state'].unique():
    state_df = df[df['state'] == state]
    fig = px.scatter(state_df, x="longitude", y="latitude", color="pollutant_avg",
                     title=f"Pollution by Location in {state}", hover_data=["city", "pollutant_id"])
    fig.show()


# 6. Box Plot - Pollution spread by pollutant (State-wise)
plt.figure(figsize=(12, 8))  
sns.boxplot(x="state", y="pollutant_avg", hue="pollutant_id", data=df)
plt.title("Pollution Levels by State and Pollutant Type")
plt.xticks(rotation=45, ha="right")  
plt.tight_layout()
plt.show()


# 7. Heatmap - Correlation (overall)
plt.figure(figsize=(6, 5))
sns.heatmap(df[["pollutant_min", "pollutant_max", "pollutant_avg"]].corr(), annot=True, cmap="coolwarm")
plt.title("Pollutant Correlation")
plt.tight_layout()
plt.show()

# 8. Pair Plot (Overall)
sns.pairplot(df[["pollutant_min", "pollutant_max", "pollutant_avg"]])
plt.suptitle("Relationship Among Pollutant Values", y=1.02)
plt.tight_layout()
plt.show()
