# User Retention Analytics Report

## 1. Introduction

User retention is a key metric for online platforms because it measures how well a product keeps its users engaged over time. High churn rates indicate that users stop using the platform early, which can affect long-term growth.

This project analyzes simulated user activity data to understand retention patterns and predict churn behavior using machine learning.

---

## 2. Dataset Description

The dataset was synthetically generated to simulate activity on an online learning platform.

Features include:

- **user_id** – Unique identifier for each user
- **signup_date** – Date the user joined the platform
- **lessons_completed** – Number of lessons completed
- **weekly_sessions** – Number of sessions per week
- **churn_probability** – Simulated likelihood of churn
- **churned** – Binary indicator of whether the user churned

The dataset contains **5000 simulated users**.

---

## 3. Cohort Retention Analysis

Cohort analysis groups users based on their signup month and measures how many remain active over time.

### Key Observations

- Retention rates vary slightly across different signup cohorts.
- Some cohorts show stronger retention, suggesting differences in user engagement patterns.
- Overall retention remains around **64–67% across cohorts**.

This analysis helps identify **periods where user engagement was stronger or weaker**.

---

## 4. Engagement vs Churn Analysis

User engagement was analyzed using two key metrics:

- Lessons completed
- Weekly sessions

### Insights

- Users with **higher weekly sessions** tend to have lower churn probability.
- Users who complete **more lessons** are more likely to stay active on the platform.
- Lower engagement levels correlate strongly with higher churn risk.

These findings suggest that improving user engagement can directly improve retention.

---

## 5. Churn Prediction Model

A **Logistic Regression model** was trained to predict churn probability using the following features:

- lessons_completed
- weekly_sessions

### Model Performance

Model accuracy: **0.71**

This indicates the model correctly predicts churn behavior **71% of the time** on the test dataset.

### Example Prediction

User behavior:

Lessons completed: 3  
Weekly sessions: 1  

Predicted churn probability: **54.45%**

---

## 6. Key Insights

- Increased user engagement significantly reduces churn probability.
- Cohort analysis helps identify retention patterns across signup periods.
- Logistic regression provides a simple baseline model for churn prediction.

---

## 7. Conclusion

This project demonstrates how data analytics and machine learning can be used to understand user retention and predict churn behavior.

Businesses can use these insights to:

- Identify at-risk users
- Improve engagement strategies
- Increase long-term user retention.

Future improvements could include more advanced models such as **Random Forest or Gradient Boosting** to improve churn prediction accuracy.