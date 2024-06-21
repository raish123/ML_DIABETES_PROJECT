# Diabetes Dataset

## Overview

This repository contains a dataset related to diabetes, which includes various medical predictor variables and one target variable, Outcome. The dataset is useful for predictive modeling and machine learning applications, particularly in the context of health and medical data analysis.

## Dataset Description

The dataset consists of 9 columns, each representing a specific medical measurement or demographic information. The target variable, Outcome, indicates whether the individual has diabetes (1) or not (0). Below is a detailed description of each feature:

### Features

- **Pregnancies**: Number of times the individual has been pregnant.
- **Glucose**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
- **BloodPressure**: Diastolic blood pressure (mm Hg).
- **SkinThickness**: Triceps skin fold thickness (mm).
- **Insulin**: 2-Hour serum insulin (mu U/ml).
- **BMI**: Body mass index (weight in kg/(height in m)^2).
- **DiabetesPedigreeFunction**: Diabetes pedigree function (a function that scores likelihood of diabetes based on family history).
- **Age**: Age of the individual (years).
- **Outcome**: Class variable (0 or 1) indicating whether the individual has diabetes (1) or not (0).

## Data Summary

- **Total Records**: 2000
- **Positive Cases (Outcome = 1)**: 768
- **Negative Cases (Outcome = 0)**: 1232

## Usage

This dataset can be used for:

- Exploratory Data Analysis (EDA)
- Training machine learning models for diabetes prediction
- Statistical analysis and research in the field of medical data

## Project Structure

- **notebooks/**: Jupyter notebooks for data exploration, preprocessing, and model training.
- **source/**: Source code for the project including data processing scripts and model implementation.
- **models/**: Saved models and their weights.
- **reports/**: Generated reports and analysis.
- **README.md**: Project overview and documentation.

## Installation

To run this project, you need to have Python installed along with the necessary libraries. You can install the required libraries using the following command:

```bash
pip install -r requirements.txt