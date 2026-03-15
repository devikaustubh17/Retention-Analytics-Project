from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

print("Project Started")

# -----------------------------
# Step 1: Define number of users
# -----------------------------

num_users = 5000

# -----------------------------
# Step 2: Create user IDs
# -----------------------------

user_ids = np.arange(1, num_users + 1)

# -----------------------------
# Step 3: Generate random signup dates
# -----------------------------

start_date = datetime(2025, 1, 1)

signup_dates = [
    start_date + timedelta(days=np.random.randint(0,180))
    for _ in range(num_users)
]

# -----------------------------
# Step 4: Simulate engagement
# -----------------------------

lessons_completed = np.random.poisson(lam=4, size=num_users)

weekly_sessions = np.random.poisson(lam=2, size=num_users)

# -----------------------------
# Step 5: Simulate churn probability
# -----------------------------

churn_probability = 1 - (0.1*lessons_completed + 0.15*weekly_sessions)

churn_probability = np.clip(churn_probability,0.1,0.9)

# -----------------------------
# Step 6: Simulate churn outcome
# -----------------------------

churned = np.random.binomial(1,churn_probability)

# -----------------------------
# Step 7: Build DataFrame
# -----------------------------

df = pd.DataFrame({
    "user_id":user_ids,
    "signup_date":signup_dates,
    "lessons_completed":lessons_completed,
    "weekly_sessions":weekly_sessions,
    "churn_probability":churn_probability,
    "churned":churned
})

# -----------------------------
# Step 8: Print sample data
# -----------------------------

print(df.head())

# -----------------------------
# Step 9: Save dataset
# -----------------------------

df.to_csv("user_dataset.csv",index=False)

print("Dataset saved as user_dataset.csv")

# -----------------------------
# Step 10: Calculate retention
# -----------------------------

retention_rate = 1 - df["churned"].mean()

print("\n30-Day Retention Rate:")
print(retention_rate)

# -----------------------------
# Step 11: Cohort analysis
# -----------------------------

# Convert signup_date to datetime
df["signup_date"] = pd.to_datetime(df["signup_date"])

# Create signup month column
df["signup_month"] = df["signup_date"].dt.to_period("M")

# Calculate retention by cohort
cohort_retention = 1 - df.groupby("signup_month")["churned"].mean()

print("\nCohort Retention by Signup Month:")
print(cohort_retention)

# -----------------------------
# Step 12: Plot cohort retention
# -----------------------------

plt.figure(figsize=(8,5))

cohort_retention.plot(
    kind="line",
    marker="o"
)

plt.title("Cohort Retention by Signup Month")
plt.xlabel("Signup Month")
plt.ylabel("Retention Rate")

plt.grid(True)
plt.savefig("visuals/cohort_retention.png")
plt.show()

# -----------------------------
# Step 13: Engagement vs churn
# -----------------------------

correlation = df[["lessons_completed","weekly_sessions","churned"]].corr()

print("\nCorrelation Matrix:")
print(correlation)

# -----------------------------
# Step 14: Engagement vs Churn Analysis
# -----------------------------

correlation_matrix = df[["lessons_completed", "weekly_sessions", "churned"]].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# -----------------------------
# Step 15: Engagement vs Churn Visualization
# -----------------------------

plt.figure(figsize=(12,5))

# Plot 1: Lessons Completed vs Churn
plt.subplot(1,2,1)
plt.scatter(df["lessons_completed"], df["churned"], alpha=0.3)
plt.xlabel("Lessons Completed")
plt.ylabel("Churned")
plt.title("Lessons Completed vs Churn")

# Plot 2: Weekly Sessions vs Churn
plt.subplot(1,2,2)
plt.scatter(df["weekly_sessions"], df["churned"], alpha=0.3)
plt.xlabel("Weekly Sessions")
plt.ylabel("Churned")
plt.title("Weekly Sessions vs Churn")

plt.tight_layout()
plt.savefig("visuals/engagement_scatter.png")
plt.show()

# -----------------------------
# Step 16: Logistic Regression Churn Prediction
# -----------------------------

features = df[["lessons_completed","weekly_sessions"]]
target = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nChurn Prediction Model Accuracy:")
print(accuracy)

# -----------------------------
# Step 17: Predict churn for a new user
# -----------------------------

sample_user = pd.DataFrame([[3,1]], columns=["lessons_completed","weekly_sessions"])

probability = model.predict_proba(sample_user)[0][1]

print("\nSample User Behaviour:")
print("Lessons Completed:", sample_user["lessons_completed"].iloc[0])
print("Weekly Sessions:", sample_user["weekly_sessions"].iloc[0])
print("\nPredicted Churn Probability:")
print(round(probability*100,2), "%")