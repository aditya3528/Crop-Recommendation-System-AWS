# Crop Recommendation System Using AWS & Machine Learning

This repository contains the code and resources for the *Crop Recommendation System deployed on AWS* project. The system uses machine learning algorithms to recommend the most suitable crops based on soil parameters such as temperature, moisture, pH, and nutrient levels (Nitrogen, Phosphorus, Potassium).

The project is integrated with AWS services like SageMaker, S3, and EC2 for model training, deployment, and scalability.

## Overview

As the global population grows, sustainable and efficient food production becomes increasingly critical. This project presents a cloud-based solution for real-time soil parameter analysis and crop recommendations. Using machine learning, we provide farmers with actionable insights to enhance productivity and resource management.

## Key Features:
- Real-time monitoring of soil parameters
- Crop and fertilizer recommendations
- Integration with AWS SageMaker for model training and deployment
- Scalable architecture using AWS EC2 and S3 for data storage
- Web interface for real-time interaction

## Technologies Used
- *Amazon SageMaker*: For model training, hyperparameter tuning, and deployment.
- *Amazon S3*: For data storage of large soil datasets and machine learning artifacts.
- *Amazon EC2*: For hosting the web application.
- *Amazon Route 53*: For DNS management and domain mapping.

## Machine Learning Algorithms:
1. *Multilayer Perceptron (MLP)*: A type of neural network used for classification tasks.
2. *Light Gradient Boosting Machine (LightGBM)*: An efficient gradient boosting algorithm for large datasets.
3. *Adaptive Boosting (AdaBoost)*: An ensemble method that combines multiple weak classifiers.
4. *Categorical Boosting (CatBoost)*: A gradient boosting algorithm specialized for categorical data.
5. *Extremely Randomized Trees (Extra Trees)*: A tree-based ensemble method that enhances model robustness.
6. *Gradient Boosting*: An ensemble technique that builds models sequentially to minimize errors.
7. *K-Nearest Neighbors (KNN)*: A non-parametric algorithm that classifies data based on proximity to neighbors.
8. *Extreme Gradient Boosting (XGBoost)*: A highly efficient gradient boosting algorithm for predictive tasks.
9. *Logistic Regression*: A linear model used for binary classification tasks.
10. *Support Vector Machine (SVM)*: A supervised learning model for classification and regression.
11. *Naive Bayes*: A probabilistic classifier based on Bayes' theorem, assuming independence among predictors.
12. *Decision Tree*: A tree-structured classifier that splits data into branches based on feature values.
13. *Random Forest*: An ensemble method that constructs multiple decision trees and merges them to get a more accurate and stable prediction.

## Website Links:
- *Deployed on AWS*: http://www.croprecommendatation.shop/login
- *Deployed on Render*: https://aws-paper.onrender.com/ (Alternative if AWS Instance Stops working)

## Website ScreenShots:
![Homepage Screenshot](ScreenShots/homepage.jpg)

![Homepage Inputs Screenshot](ScreenShots/homepage_inputs.jpg)

![Results Screenshot](ScreenShots/results.jpg)
