# 📊 Netflix Data Analysis (EDA)

## Project Overview

This project performs **exploratory data analysis (EDA)** on the Netflix Movies and TV Shows dataset using **Python, Pandas, and Matplotlib**. The goal is to understand the structure of the dataset, handle missing values, and analyze trends in Netflix content over time.

The analysis focuses on content distribution, yearly content addition, and basic summary statistics, while keeping the approach simple and beginner-friendly.

---

## Dataset

* **Name:** Netflix Movies and TV Shows
* **Format:** CSV
* **Key Columns:**

  * `type` – Movie or TV Show
  * `release_year` – Year the content was released
  * `date_added` – Date when the content was added to Netflix
  * `country` – Country of production
  * `rating` – Content rating

---

## Data Cleaning & Preparation

* Checked data types and missing values using Pandas
* Filled missing categorical values (`director`, `cast`, `country`, `rating`) with `"Unknown"`
* Removed rows with missing `date_added`
* Cleaned and converted `date_added` to datetime format
* Extracted `year_added` for time-based analysis

---

## Analysis Performed

* Year-wise analysis of content added to Netflix
* Comparison of Movies vs TV Shows
* Identification of peak content addition year
* Summary statistics of release years by content type

---

## Visualizations

* Line plot showing content added per year
* Bar chart comparing Movies and TV Shows

---

## Tools Used

* Python
* Pandas
* Matplotlib

---

## Key Insights

* Netflix content additions increased steadily until **2019**, after which a decline is observed
* Movies significantly outnumber TV Shows on Netflix
* The dataset includes both older and recent content
---

## Learning Outcomes

* Gained hands-on experience with real-world data cleaning
* Learned to work with datetime data in Pandas
* Applied groupby and aggregation for analysis
* Created basic but meaningful visualizations

---
## Dataset Source

Netflix Movies and TV Shows dataset (public Kaggle dataset).
Used strictly for educational and learning purposes.

---
