# Data Analysis Projects

In these projects I explore practical data analysis  in SQL, Python through data cleaning, exploratory data analysis, dashboard development, and business-oriented communication. This is a learning project imitating real-world data analysis collection.  
---

##Skillset

In the collection, I explore the follolwing tasks:

- Data cleaning and transformation using SQL
- Exploratory data analysis for business decision-making
- Creation of analysis-ready datasets and summary tables
- Dashboard development with Python, Dash, and Plotly
- Database connection management using environment variables
- Clear documentation of workflows, assumptions, and reproducibility steps
- Communication of technical results
  
---

## Repository Structure

```text
data_analysis/
├── README.md
├── Market_Campaign_Analysis
│   ├── README.md
│   ├── EDA_campaign_analysis.ipynb
│   ├── ML_prediction_analysis.ipynb
├── Sales_Profit_Analysis
│   ├── README.md
│   ├── Sales_data_analysis.ipynb
│   ├── Sales_data_deep_analysis.ipynb
├── global_onlinestore/
│   ├── README.md
│   ├── data_cleaning.sql
│   ├── eda_views.sql
│   ├── analysis_dataset.sql
│   ├── dash_app.py
│   └── dash_v2.py
└── docs/
    └── documentation_style_guide.md
```

---

## Current Project

### Global Online Store Analytics

The `global_onlinestore` project demonstrates an end-to-end analytics workflow for a global retail dataset. It includes database preparation, SQL-based cleaning, business analysis, creation of reusable views, analysis-ready datasets, and an interactive Python dashboard.

The project covers:

- Importing and preparing raw sales data in MySQL
- Converting text-heavy imported columns into typed analytical fields
- Checking missing values, duplicate rows, and basic data quality issues
- Building summary datasets for country-level, monthly, and customer-level analysis
- Creating reusable SQL views for category, region, segment, customer, product, and shipping analysis
- Connecting Python to MySQL securely using `.env` variables
- Building an interactive Dash dashboard for business performance exploration

For the full project documentation, see [`global_onlinestore/README.md`](global_onlinestore/README.md).

---

## Technical Stack

| Area | Tools |
|---|---|
| Programming | Python, SQL |
| Database | MySQL |
| Data Analysis | pandas |
| Dashboarding | Dash, Plotly |
| Database Connection | SQLAlchemy, PyMySQL |
| Environment Management | python-dotenv |
| Version Control | Git, GitHub |

---

## How to Use This Repository

### 1. Clone the repository

```bash
git clone https://github.com/ElihleN/data_analysis.git
cd data_analysis
```

### 2. Review the project documentation

Start with the project-level README files. They explain the purpose of each project, the workflow, the expected inputs, and how to reproduce the analysis.

### 3. Run project files in order

For SQL-to-dashboard projects, the usual workflow is:

1. Prepare the database and clean the imported data.
2. Create reusable SQL views and summary tables.
3. Connect the dashboard script to the database.
4. Run the dashboard locally.


---

## Documentation Approach


---

## Portfolio Value

Th
---

## Author

Maintained by [ElihleN](https://github.com/ElihleN).

This portfolio reflects an applied approach to data analysis: clean the data carefully, structure the workflow clearly, document the process professionally, and communicate insights in a way that supports decision-making.
