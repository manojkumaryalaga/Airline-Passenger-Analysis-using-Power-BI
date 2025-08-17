## Introduction
This project analyzes customer demographics, travel experiences, and flight performance to uncover insights that influence passenger satisfaction. Using SQL, Python, and Power BI, we identify both strengths and areas for improvement in airline services, offering actionable recommendations for enhancing customer experience and loyalty.

---

## 📊 Dataset

[Airline Passenger Satisfaction dataset on Kaggle](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)


Rows: 25,977

Columns include:

- ID, Gender, Customer Type, Age, Type of Travel, Class, Flight Distance, Inflight Wi-Fi service, Departure/Arrival time convenient, Ease of Online booking, Gate location, Food and drink, Online boarding, Seat comfort, Inflight entertainment, On-board service, Leg room service, Baggage handling, Check-in service, Inflight service, Cleanliness, Departure Delay in Minutes, Arrival Delay in Minutes, 
Satisfaction. 

---

## ⚙️ Tech Stack

- Python (Pandas,NumPy): Data cleaning & preprocessing
- SQL (MySQL/PostgreSQL): Querying metrics for insights
- Power BI: Visualization & dashboard building
- GitHub: Version control & project showcase

---

## 📁 Project Structure
Airline-Passenger-Experience-Analysis/

***
│─ Airline_datacleaning.py        # Python script for cleaning data
***
│─ Airlinemetrics.sql          # SQL queries for KPIs & dashboards
***
├─ screenshots/             # Dashboard images for README reference
***
├─ README.md
***

---
## How to Run

1. Data Cleaning using python
python Airline_datacleaning.py

(Removes null/missing values
Prepares dataset for SQL and Power BI)

2. Load into SQL

Import cleaned CSV into MySQL/PostgreSQL
Run queries from sql/metrics.sql

3. Visualization in Power BI

Import cleaned dataset
Build dashboards using available metrics

---

