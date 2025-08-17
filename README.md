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
---
│
---
├── Airline_datacleaning.py        # Python script for cleaning data
---
├── Airlinemetrics.sql          # SQL queries for KPIs & dashboards
---
└── screenshots/             # Dashboard images for README reference
---
---
## How to Run

1. Data Cleaning using Python
```
python Airline_datacleaning.py
```
 - Removes null/missing values & Prepares dataset for SQL and Power BI

2. Load into SQL

- Import the cleaned CSV into MySQL or PostgreSQL.

Run queries from sql/metrics.sql to generate metrics for dashboards.

3. Visualization in Power BI

- Import the cleaned dataset.

- Build dashboards using the metrics generated from SQL queries.

---
## Results & Insights

### Dashboard 1: Customer Profile Analysis

![Dashboard 1 Screenshot](screenshots/picture1.jpg)

**Positive Insights:**
- Equal gender distribution (50:50) shows inclusivity.
- High number of loyal customers across all classes indicates strong customer relationships.
- Business travel dominates (70:30 ratio vs personal), suggesting airlines play a vital role in professional engagement.
- Younger customers (22–25) show strong loyalty, while economy travel remains accessible for mass adoption.

**Negative Insights:**
- Disloyalty peaks in the 38–42 age group, signaling dissatisfaction in this demographic.
- Decline in loyalty among older customers, requiring retention strategies.

**Comments:**
- Airlines should enhance loyalty programs for older customers while targeting improvements for middle-aged travelers.

---

### Dashboard 2: Travel Experience Rating Insights

![Dashboard 2 Screenshot](picture2.jpg)

**Positive Insights:**
- Onboarding, baggage handling, cleanliness, seat comfort, and inflight entertainment all received 4–5 star ratings.
- These reflect strong operational standards, attention to detail, and comfort.

**Negative Insights:**
- Wi-Fi service received only a 2-star rating, showing a major gap.
- Over 50% of customers expressed neutral/dissatisfied sentiment, highlighting unmet expectations.

**Comments:**
- Improving connectivity and addressing dissatisfaction are key to maintaining competitiveness.

---

### Dashboard 3: Flight Performance Analysis

![Dashboard 3 Screenshot](picture3.jpg)

**Positive Insights:**
- Departure and arrival delays decrease as flight distance increases, showing efficiency in long-haul flights.
- Economy class analysis reveals opportunities for punctuality improvements.

**Negative Insights:**
- Inflight and onboard services decline as flight distance increases, impacting long-haul satisfaction.
- Economy class experiences the highest delays, both in departure and arrival.

**Comments:**
- Airlines must ensure consistent service quality across distances and streamline processes for Economy passengers.

