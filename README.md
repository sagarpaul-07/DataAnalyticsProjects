# 📊 Marketing Analytics — End-to-End Data Analytics Project

An end-to-end **Marketing Analytics project** designed to analyze customer behavior, marketing engagement, customer journeys, conversion performance, online activity, product performance, and customer feedback.

The project combines **SQL, Python, and Power BI** to transform raw marketing and customer data into an interactive analytical solution and actionable business insights.

---

## 📌 Project Overview

The objective of this project is to understand how customers interact with a business across different stages of the marketing and purchasing journey.

The analysis focuses on:

* Customer demographics and segmentation
* Customer journey and conversion behavior
* Product-level conversion performance
* Online engagement and website activity
* Views, clicks, and engagement patterns
* Customer reviews and ratings
* Customer sentiment
* Marketing performance over time
* Identification of opportunities for improving conversion and customer experience

The project follows an end-to-end analytics workflow:

```text
Raw Data
   ↓
Data Cleaning & Preparation
   ↓
SQL Server
   ↓
Data Transformation & Analysis
   ↓
Python
   ↓
Sentiment Analysis
   ↓
Power BI Data Model
   ↓
Interactive Dashboard
   ↓
Business Insights & Recommendations
```

---

# 🎯 Business Objectives

The project was developed to answer important marketing and business questions such as:

1. How effectively are visitors converting into customers?
2. Which products have the highest and lowest conversion rates?
3. How does customer behavior change across the customer journey?
4. Which months or periods show stronger marketing performance?
5. How are views and clicks distributed across products and channels?
6. Which products generate higher customer engagement?
7. What does customer feedback reveal about the overall customer experience?
8. What is the distribution of positive, neutral, and negative customer sentiment?
9. Which products receive stronger customer ratings?
10. What areas could be improved to increase conversion and customer satisfaction?

---

# 🛠️ Tools & Technologies

| Technology           | Purpose                                                     |
| -------------------- | ----------------------------------------------------------- |
| **SQL Server**       | Data storage, querying, cleaning and transformation         |
| **SQL**              | Data extraction, joins, filtering, aggregation and analysis |
| **Python**           | Data processing and customer review analysis                |
| **Pandas**           | Data manipulation and preprocessing                         |
| **NLTK**             | Natural Language Processing                                 |
| **VADER**            | Customer review sentiment analysis                          |
| **Power BI Desktop** | Data modeling, DAX and dashboard development                |
| **DAX**              | Measures, KPIs and analytical calculations                  |
| **PowerPoint**       | Project documentation and business presentation             |
| **GitHub**           | Version control and project portfolio                       |

---

# 🗂️ Project Structure

The repository is organized into separate sections for each stage of the analytics workflow.

```text
Marketing-Analytics/
│
├── README.md
│
├── SQL/
│   ├── Customer_Analysis.sql
│   ├── Product_Analysis.sql
│   ├── Customer_Journey_Analysis.sql
│   ├── Engagement_Analysis.sql
│   └── Conversion_Analysis.sql
│
├── Python/
│   ├── Sentiment_Analysis.py
│   └── Data_Processing.py
│
├── PowerBI/
│   ├── Marketing_Analytics.pbix
│   │
│   └── Dashboard_Screenshots/
│       ├── Overview.png
│       ├── Conversion_Analysis.png
│       ├── Online_Analysis.png
│       └── Customer_Analysis.png
│
├── Presentations/
│   ├── Marketing_Analytics_Project.pptx
│   └── Marketing_Analytics_Summary.pptx
│
└── Video/
    └── Dashboard_Walkthrough.mp4
```

> **Note:** File names can be changed to match the actual names used in the repository.

---

# 📂 Dataset

The project uses multiple datasets representing different aspects of the customer and marketing ecosystem.

The data covers areas such as:

* Customer information
* Geography
* Product information
* Customer journeys
* Engagement data
* Customer reviews
* Ratings
* Views and clicks
* Purchase/conversion activity

The datasets are combined and transformed to create an analytical model suitable for Power BI.

---

# 🧹 Data Preparation & Cleaning

Before building the dashboard, the data was reviewed and prepared for analysis.

Key preparation activities included:

* Removing unnecessary columns
* Handling duplicate fields
* Filtering irrelevant records
* Standardizing categorical values
* Preparing customer and product attributes
* Combining relevant datasets
* Creating calculated fields
* Preparing customer journey data
* Preparing review data for sentiment analysis
* Validating relationships between datasets

SQL Server was primarily used for structured data preparation and analytical queries.

---

# 🗄️ SQL Analysis

SQL was used as the foundation of the data analysis process.

The SQL analysis includes:

### Customer Analysis

Analysis of:

* Customer demographics
* Age groups
* Gender
* Geographic information
* Customer characteristics

### Product Analysis

Analysis of:

* Product categories
* Product performance
* Product-level engagement
* Product-level conversion
* Product ratings

### Customer Journey Analysis

The customer journey data was used to understand how customers move through different stages of interaction.

Examples include:

```text
Customer
   ↓
View
   ↓
Click
   ↓
Engagement
   ↓
Purchase
```

This allows conversion performance to be evaluated at different stages of the customer journey.

### Engagement Analysis

SQL was also used to analyze:

* Views
* Clicks
* Engagement
* Content types
* Marketing interactions

---

# 🐍 Python Analysis

Python was used to extend the analysis beyond traditional SQL queries.

The primary Python workflow focused on **customer review and sentiment analysis**.

### Libraries Used

```python
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
```

### Sentiment Analysis

The **VADER SentimentIntensityAnalyzer** from NLTK was used to analyze customer reviews.

The sentiment analysis classifies customer feedback into categories such as:

* Positive
* Neutral
* Negative

This helps convert unstructured customer feedback into structured analytical information.

### Python Workflow

```text
Customer Reviews
       ↓
Text Processing
       ↓
VADER Sentiment Analysis
       ↓
Sentiment Score
       ↓
Sentiment Category
       ↓
SQL / Power BI
       ↓
Customer Insights
```

---

# 📊 Power BI Dashboard

The final analytical solution was developed using **Microsoft Power BI**.

The dashboard contains four major analytical sections:

---

# 1️⃣ Overview

The **Overview** page provides a high-level summary of marketing performance.

It contains KPI cards and visualizations covering areas such as:

* Conversion Rate
* Views
* Clicks
* Customer/transaction metrics
* Average rating
* Monthly performance
* Product conversion
* Views and clicks
* Product ratings

### Key Visuals

The page includes:

* KPI cards
* Monthly trend analysis
* Conversion rate by product
* Views and clicks by month
* Product rating analysis
* Interactive slicers
* Product/category filters
* Month-based filtering

The Overview page is designed to provide a quick understanding of overall marketing performance.

---

# 2️⃣ Conversion Analysis

The **Conversion Analysis** page focuses specifically on the customer conversion journey.

It analyzes how users move from initial interaction toward purchase.

### Key Metrics

* Conversion Rate
* Customer Journey stages
* Conversion by month
* Conversion by product
* Journey-level performance

### Key Visualizations

The dashboard uses:

* Customer journey funnel
* Conversion trend
* Conversion rate by product
* Product-level comparisons
* Interactive filtering

This page helps identify where customers are converting successfully and where potential drop-offs may occur.

---

# 3️⃣ Online Analysis

The **Online Analysis** page focuses on website/online engagement.

Key metrics include:

* Views
* Clicks
* Likes/engagement
* Product-level online activity
* Monthly engagement
* Relationship between online interactions and conversion

### Key Visualizations

The page includes:

* KPI cards
* Product-level data table
* Views/clicks analysis
* Monthly trends
* Engagement comparisons
* Scatter/correlation-style visual analysis

This allows online customer behavior to be compared against marketing and conversion performance.

---

# 4️⃣ Customer Analysis / Reviews

The **Customer Analysis** page focuses on customer feedback and sentiment.

The analysis combines:

* Customer reviews
* Ratings
* Sentiment
* Review categories
* Product-level customer feedback

### Key Metrics

Examples include:

* Average Rating
* Sentiment distribution
* Review volume
* Product ratings
* Positive/negative feedback

### Key Visualizations

The page contains:

* Sentiment distribution
* Rating analysis
* Customer review table
* Product-level sentiment analysis
* Rating distribution
* Review-level details

This page helps identify customer satisfaction patterns and potential product/service issues.

---

# 🎛️ Interactive Dashboard Features

The Power BI dashboard was designed to be interactive rather than static.

### Navigation

The dashboard contains navigation buttons allowing users to move between:

```text
Overview
   ↓
Conversion Analysis
   ↓
Online Analysis
   ↓
Customer Analysis
```

### Slicers

Interactive filters allow users to analyze the data based on different dimensions such as:

* Product
* Category
* Month
* Customer attributes
* Other available business dimensions

### Dynamic KPIs

The KPI cards dynamically update based on the selected filters.

This allows users to move from:

**Overall performance → specific product → specific period → detailed analysis**

---

# 📐 Power BI & DAX

DAX was used to create analytical measures and dynamic KPIs.

Examples of measures used in the project include:

### Total Views

```DAX
Total Views =
SUM(Customer_Journey[Views])
```

### Total Purchases

```DAX
Total Purchases =
CALCULATE(
    COUNTROWS(Customer_Journey),
    Customer_Journey[Action] = "Purchase"
)
```

### Conversion Rate

```DAX
Conversion Rate =
DIVIDE(
    [Total Purchases],
    [Total Views],
    0
)
```

> The exact measure names and table/column names may vary depending on the final Power BI model.

Other DAX calculations were used for:

* Monthly analysis
* Product-level performance
* Customer metrics
* Ratings
* Engagement
* Dynamic KPI cards

---

# 📅 Calendar / Time Intelligence

A dedicated calendar table was created to support time-based analysis.

The calendar enables:

* Year analysis
* Month analysis
* Month sorting
* Monthly trends
* Time-based slicers
* Period comparisons

The calendar structure supports chronological month ordering rather than alphabetical ordering.

---

# 🔗 Data Model

The Power BI model combines the major analytical entities required for the dashboard.

Conceptually:

```text
                 ┌─────────────┐
                 │  Customers  │
                 └──────┬──────┘
                        │
                        │
                 ┌──────▼──────┐
                 │   Journey   │
                 └──────┬──────┘
                        │
             ┌──────────┼──────────┐
             │          │          │
             ▼          ▼          ▼
        Engagement   Products   Reviews
             │          │          │
             └──────────┼──────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   Power BI  │
                 └─────────────┘
```

The final model allows customer behavior, product information, engagement and reviews to be analyzed together.

---

# 📈 Key Analytical Areas

The project provides analysis across several important marketing dimensions.

### Customer Behavior

Understand how customers interact with products and marketing touchpoints.

### Conversion Performance

Identify conversion rates across:

* Products
* Months
* Customer journey stages

### Online Engagement

Analyze relationships between:

* Views
* Clicks
* Engagement
* Conversion

### Product Performance

Compare products based on:

* Conversion
* Engagement
* Ratings
* Customer feedback

### Customer Satisfaction

Analyze:

* Ratings
* Reviews
* Sentiment
* Product-level customer experience

---

# 💡 Business Insights

The dashboard is designed to help answer questions such as:

### Conversion

* Which products have stronger conversion performance?
* Where are potential customer journey drop-offs occurring?
* How does conversion change over time?

### Engagement

* Which products attract the most views?
* Which products generate higher click activity?
* Does higher online engagement correspond with stronger conversion?

### Customer Experience

* Which products receive the highest ratings?
* Which products receive more negative feedback?
* What is the overall sentiment of customer reviews?
* Which products may require further investigation?

### Marketing Performance

* Which periods perform better?
* Which products should receive greater marketing attention?
* Where are opportunities to improve customer conversion?

---

# 🎯 Potential Business Recommendations

Based on the analysis, the dashboard can be used to support decisions such as:

### 1. Optimize Low-Conversion Products

Products generating significant traffic but relatively low conversion can be investigated for:

* Pricing
* Product positioning
* Product information
* Customer experience
* Call-to-action effectiveness

### 2. Focus on High-Performing Products

Products demonstrating strong conversion and engagement can be evaluated for additional marketing investment.

### 3. Investigate Customer Sentiment

Products with lower ratings or negative sentiment can be investigated further to identify recurring customer concerns.

### 4. Improve the Customer Journey

High drop-off points in the journey can be targeted with improvements to:

* Website experience
* Product pages
* Checkout process
* Marketing messaging

### 5. Use Engagement as an Early Indicator

Views and clicks can be monitored alongside conversion to identify products that attract attention but fail to translate engagement into purchases.

---

# 🖥️ Dashboard Preview

## Overview

![Marketing Analytics Overview]([Dashboard/Screenshot 2026-08-20 002248.png](https://github.com/sagarpaul-07/DataAnalyticsProjects/blob/ae844e1baf98d690e42063473f81e62289174182/Dashboard/Screenshot%202026-08-20%20002248.png))

The Overview page provides a high-level summary of marketing performance through KPIs, trends, product analysis and interactive filtering.

---

## Conversion Analysis

![Conversion Analysis]([Dashboard/Screenshot 2026-08-20 002308.png](https://github.com/sagarpaul-07/DataAnalyticsProjects/blob/ae844e1baf98d690e42063473f81e62289174182/Dashboard/Screenshot%202026-08-20%20002308.png))

The Conversion Analysis page evaluates customer journey performance and product-level conversion.

---

## Online Analysis

![Online Analysis]([PowerBI/Dashboard_Screenshots/Online_Analysis.png)](https://github.com/sagarpaul-07/DataAnalyticsProjects/blob/ae844e1baf98d690e42063473f81e62289174182/Dashboard/Screenshot%202026-08-20%20002358.png)

The Online Analysis page focuses on views, clicks, engagement and online customer behavior.

---

## Customer Analysis

![Customer Analysis]([PowerBI/Dashboard_Screenshots/Customer_Analysis.png](https://github.com/sagarpaul-07/DataAnalyticsProjects/blob/ae844e1baf98d690e42063473f81e62289174182/Dashboard/Screenshot%202026-08-20%20002413.png))

The Customer Analysis page combines customer ratings, reviews and sentiment analysis.

---

# 🎥 Dashboard Walkthrough

A dashboard walkthrough video is included in the repository to demonstrate:

* Dashboard navigation
* Interactive slicers
* KPI changes
* Conversion analysis
* Online analysis
* Customer review analysis
* Interactive Power BI functionality

```text
Video/
└── Dashboard_Walkthrough.mp4
```

> For GitHub repositories, consider hosting a compressed version of the video or linking to a YouTube/LinkedIn demonstration if the video file becomes too large for GitHub.

---

# 📑 Project Documentation

The project also includes PowerPoint presentations documenting the project and its findings.

```text
Presentations/
│
├── Marketing_Analytics_Project.pptx
└── Marketing_Analytics_Summary.pptx
```

The presentations provide additional information about:

* Business problem
* Analytical approach
* Tools used
* Data analysis
* Dashboard
* Findings
* Recommendations

---

# 🚀 End-to-End Workflow

The complete project workflow can be summarized as:

```text
                    DATA SOURCES
                         │
                         ▼
                ┌─────────────────┐
                │ Data Preparation│
                └────────┬────────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ SQL Server  │
                  └──────┬──────┘
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
        SQL Analysis          Python Analysis
              │                     │
              │              Sentiment Analysis
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                  ┌─────────────┐
                  │   Power BI  │
                  └──────┬──────┘
                         │
                         ▼
                 Interactive Dashboard
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      Conversion      Online        Customer
       Analysis      Analysis       Analysis
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                 Business Insights
                         │
                         ▼
                  Recommendations
```

---

# 🧠 Skills Demonstrated

This project demonstrates practical experience in:

### Data Analytics

* Exploratory data analysis
* Business problem solving
* KPI development
* Trend analysis
* Customer behavior analysis

### SQL

* SELECT statements
* Filtering
* Aggregations
* GROUP BY
* CASE statements
* JOINs
* Data transformation
* Analytical queries

### Python

* Pandas
* Data preprocessing
* Natural Language Processing
* Sentiment analysis
* VADER
* Data integration

### Power BI

* Data modeling
* DAX
* Calculated measures
* KPI cards
* Interactive slicers
* Page navigation
* Drill/filter-based analysis
* Time-based analysis
* Dashboard design
* Data storytelling

### Business Analytics

* Conversion analysis
* Customer journey analysis
* Marketing performance
* Customer satisfaction
* Product performance
* Actionable recommendations

---

# 📌 Project Highlights

✅ End-to-end analytics workflow

✅ SQL-based data preparation and analysis

✅ Python-based customer sentiment analysis

✅ Interactive Power BI dashboard

✅ Customer journey and conversion analysis

✅ Online engagement analysis

✅ Product performance analysis

✅ Customer review and rating analysis

✅ Dynamic KPI cards

✅ Interactive slicers

✅ Multi-page dashboard navigation

✅ Business-focused insights and recommendations

---

# 🔮 Future Improvements

Potential future enhancements include:

* Add automated data refresh
* Add additional marketing channel analysis
* Implement customer segmentation
* Build customer lifetime value analysis
* Add cohort analysis
* Add retention/churn analysis
* Add predictive conversion modeling
* Integrate real-time or scheduled data pipelines
* Add advanced NLP for review topic extraction
* Develop a Power BI Service deployment
* Add automated reporting

---

# 📚 Repository Contents

| Folder           | Contents                                      |
| ---------------- | --------------------------------------------- |
| `SQL/`           | SQL queries and analytical scripts            |
| `Python/`        | Python data processing and sentiment analysis |
| `PowerBI/`       | Power BI dashboard and screenshots            |
| `Presentations/` | Project presentations                         |
| `Video/`         | Dashboard walkthrough                         |
| `README.md`      | Project documentation                         |

---

# 👨‍💻 Author

**Sagar Paul**

Data Analytics Portfolio Project

### Skills

`SQL` `Python` `Power BI` `DAX` `Pandas` `NLTK` `VADER` `Data Analytics` `Marketing Analytics` `Data Visualization`

---

# ⭐ Conclusion

This project demonstrates how multiple analytics technologies can be combined to transform raw customer and marketing data into a structured business intelligence solution.

The combination of:

**SQL → Python → Sentiment Analysis → Power BI → Business Insights**

provides an end-to-end approach to understanding customer behavior, marketing performance, conversion, online engagement and customer satisfaction.

---

## ⭐ If you found this project useful

Feel free to explore the SQL scripts, Python analysis, Power BI dashboard and project documentation included in this repository.

If you have suggestions or feedback, I'd be happy to hear them.
