# AI-Powered Real-Time Fake News Verification

## Overview

This project combines Machine Learning and Google's Fact Check API to detect fake news and verify claims in real time.

## Features

- Fake News Detection using NLP
- TF-IDF Feature Extraction
- Logistic Regression Model
- Google Fact Check API Integration
- Confidence Score
- Streamlit Dashboard

## Tech Stack

- Python
- Pandas
- Scikit-Learn
- NLP
- Streamlit
- Google Fact Check API

## Project Structure

AI-Fake-News-Verification/

├── app.py

├── train_model.py

├── fact_checker.py

├── model.pkl

├── vectorizer.pkl

├── Fake.csv

├── True.csv

├── requirements.txt

└── README.md

## Installation

pip install -r requirements.txt

## Train Model

python train_model.py

## Run Application

".venv/Scripts/python.exe" -m streamlit run app.py