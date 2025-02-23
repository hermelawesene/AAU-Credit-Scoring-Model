# Advanced XAI Project: Credit Score Modeling

## Introduction

Addis Ababa University Business Enterprise (AAUBE) aims to enhance financial decision-making in the Ethiopian market. This project focuses on developing an advanced credit scoring model to predict financial distress among borrowers and applying Explainable AI (XAI) techniques to ensure transparency and fairness.

## Data Preprocessing

### Dataset Overview

The dataset consists of 250,000 borrower records with features categorized into:

- Demographics (e.g., age, income, employment status)
- Financial History (e.g., credit utilization, payment history, outstanding debt)
- Loan Information (e.g., loan amount, loan purpose)
- Target Variable: Financial distress (binary: 1 = distress, 0 = no distress)

### Data Cleaning

- **Handling Missing Values:** Imputation techniques such as mean/median imputation for numerical features and mode imputation for categorical features were applied.
- **Encoding Categorical Variables:** Label encoding and one-hot encoding were used for categorical attributes.
- **Feature Scaling:** Standardization and normalization were applied where necessary.

### Exploratory Data Analysis (EDA)

- Correlation heatmaps were generated to understand feature relationships.
- Distribution plots revealed class imbalance (handled via SMOTE).
- Outlier detection was performed using the IQR method.

## Model Development

### Model Selection & Training

Three machine learning models were developed:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting (XGBoost)

### Hyperparameter Optimization

- Grid search and random search were employed for hyperparameter tuning.
- Cross-validation ensured model generalizability.

### Model Evaluation

Performance metrics included:

- AUC-ROC Curve: Primary evaluation metric.
- Precision, Recall, F1-score: Assessed model effectiveness.
- Confusion Matrix: Evaluated misclassifications.

Best-performing model: XGBoost with an AUC-ROC of 0.89.

## Explainability Analysis

### Feature Importance Analysis

- **SHAP (Shapley Additive Explanations):** Identified key features influencing predictions, such as credit utilization and income stability.
- **LIME (Local Interpretable Model-agnostic Explanations):** Provided local explanations for individual predictions.

### Partial Dependence Plots (PDPs)

- Visualized the effect of independent variables (e.g., higher outstanding debt increased distress probability).

### Counterfactual Explanations

- Generated actionable insights, such as increasing monthly savings to improve creditworthiness.

## Ethical Considerations

### Bias Analysis

- Identified potential biases in gender and income-based lending.
- Mitigation strategies included fairness-aware ML techniques.

### Fairness in Credit Scoring

- Implemented disparate impact analysis to ensure equal treatment across demographics.

## Final Recommendations

- **Enhancing Model Transparency:** Deploy XAI dashboards for real-time model interpretability.
- **Bias Mitigation:** Continuously monitor and adjust fairness metrics.
- **Improved Credit Decisions:** Utilize XAI insights to educate borrowers on improving credit scores.

## Conclusion

This project successfully developed an accurate and explainable credit scoring model using advanced XAI techniques. The findings contribute to fairer and more transparent lending decisions in Ethiopia.

## Summary

- Key findings from the model
- Explainability insights from SHAP, LIME, and PDP
- Ethical considerations and fairness improvements

## Contributors

- Hanna Samuel - GSR/4634/17
- Hiwot Teshome - GSR/3420/17
- Hermela Wesene - GSR/1047/17
