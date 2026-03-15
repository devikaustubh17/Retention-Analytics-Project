# User Retention Analytics Project

## Project Overview
This project analyzes user retention and churn behavior for a simulated online learning platform.  
Using Python and data analytics techniques, the project explores engagement patterns and builds a predictive churn model.

## Objectives
- Simulate user activity data
- Analyze cohort-based retention
- Explore engagement metrics
- Build a churn prediction model

## Dataset Features
- user_id
- signup_date
- lessons_completed
- weekly_sessions
- churn_probability
- churned

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Analysis Performed
## Visualizations

### Cohort Retention Analysis
Retention rates were calculated based on signup month cohorts.

![Cohort Retention](visuals/cohort_retention.png)

### Engagement vs Churn
User engagement metrics were compared with churn outcomes.

![Engagement Scatter](visuals/engagement_scatter.png)

## Churn Prediction Model
A logistic regression model was trained using:

- Lessons completed
- Weekly sessions

Model Accuracy: 0.71


Example prediction:

User behavior:
- Lessons completed: 3
- Weekly sessions: 1

Predicted churn probability:54.45%


## Project Structure
Retention_Analytics_Project

1. project2.py
2. user_dataset.csv
3. README.md
4. visuals
 4.1 cohort_retention.png
 4.2engagement_scatter.png
5. report

## Key Insights
- Higher weekly engagement reduces churn risk
- Cohort retention varies across signup periods
- Logistic regression provides a baseline churn prediction model
