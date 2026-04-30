# Data Analysis Projects

This repository is a growing portfolio of practical data analysis projects using SQL, Python, exploratory data analysis, dashboard development, and business-oriented communication.

The goal of this portfolio is to demonstrate the complete analytical workflow: understanding a business problem, preparing data, performing analysis, creating visual outputs, documenting the process clearly, and communicating insights in a professional way.

---

## Skillset

Across these projects, I explore and demonstrate the following tasks:

- Data cleaning and transformation using SQL and Python
- Exploratory data analysis for business decision-making
- Creation of analysis-ready datasets and summary tables
- Dashboard development with Python, Dash, and Plotly
- Marketing campaign analysis and classification modelling
- Sales and profit performance analysis
- Data retrieval and SQL/Python workflow development
- Database connection management using environment variables
- Clear documentation of workflows, assumptions, and reproducibility steps
- Communication of technical results for technical and non-technical readers

---

## Repository Structure

```text
data_analysis/
├── README.md
├── Market_Campaign_Analysis/
│   ├── README.md
│   ├── EDA_campaign_analysis.ipynb
│   └── ML_prediction_analysis.ipynb
├── Sales_Profit_Analysis/
│   ├── README.md
│   ├── Sales_data_analysis.ipynb
│   └── Sales_data_deep_analysis.ipynb
├── global_onlinestore/
│   ├── README.md
│   ├── data_cleaning.sql
│   ├── eda_views.sql
│   ├── analysis_dataset.sql
│   ├── dash_app.py
│   └── dash_v2.py
├── nyc_taxi_sql_py_analysis/
│   └── ongoing project
└── docs/
    └── documentation_style_guide.md
```

---

## Projects

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

### Sales and Profit Analysis

The `Sales_Profit_Analysis` project focuses on analysing business performance through sales, profit, and related commercial metrics. It uses notebook-based analysis to explore patterns in revenue, profitability, and possible areas of loss or underperformance.

The project covers:

- Loading and inspecting sales/profit data in Python notebooks
- Performing exploratory data analysis on business performance metrics
- Comparing revenue and profitability across useful business dimensions
- Identifying high-performing and low-performing areas
- Exploring the difference between high sales and actual profitability
- Creating visual summaries to support business interpretation
- Documenting findings in a way that is clear for portfolio reviewers and business stakeholders

For the full project documentation, see [`Sales_Profit_Analysis/README.md`](Sales_Profit_Analysis/README.md).

---

### Market Campaign Analysis

The `Market_Campaign_Analysis` project explores marketing campaign data to understand customer response behaviour and campaign effectiveness. It combines exploratory data analysis with a machine-learning prediction workflow for identifying patterns related to campaign response.

The project covers:

- Exploring customer and campaign data through EDA
- Analysing campaign response distribution and class imbalance
- Comparing responders and non-responders across available features
- Preparing data for machine-learning classification
- Building and evaluating prediction models for campaign response
- Using classification metrics such as precision, recall, F1 score, and model comparison outputs
- Connecting model results back to business questions around targeting and campaign prioritisation

For the full project documentation, see [`Market_Campaign_Analysis/README.md`](Market_Campaign_Analysis/README.md).

---

### NYC Taxi SQL and Python Analysis *(Ongoing)*

The `nyc_taxi_sql_py_analysis` project is an ongoing data analysis and data-engineering-style project focused on working with NYC taxi trip data using SQL and Python. The project is intended to demonstrate scalable data retrieval, structured transformations, and analysis workflows using modern analytical tools.

The project covers:

- Reading large public taxi datasets without relying only on local CSV downloads
- Using SQL and Python together for data exploration and transformation
- Working with Parquet-style analytical data workflows
- Building staging and cleaned tables for analysis
- Tracking data loading or transformation steps as part of a reproducible pipeline
- Preparing analysis-ready datasets for taxi trip patterns, time-based trends, and operational questions
- Developing a project structure that shows data engineering foundations alongside data analysis skills

This project is still in progress and will be expanded as the pipeline, analysis queries, and documentation mature.

---

### Report Data Analysis

The `report_data_analysis` folder is intended for report-style analysis work, where the final output is not only code but also a clear written explanation of findings, assumptions, limitations, and recommendations.

The project area covers:

- Structuring analysis around a clear question or reporting objective
- Cleaning and preparing data for written analysis
- Creating visual summaries for reports
- Translating exploratory findings into written insights
- Documenting assumptions and limitations
- Communicating analytical results for non-technical readers
- Building portfolio-ready reports that show both analysis and communication skill

For the full project documentation, see [`report_data_analysis/README.md`](report_data_analysis/README.md).

---

## Technical Stack

| Area | Tools |
|---|---|
| Programming | Python, SQL |
| Database | MySQL, DuckDB-style analytical workflows |
| Data Analysis | pandas, SQL queries, Jupyter Notebook |
| Dashboarding | Dash, Plotly |
| Database Connection | SQLAlchemy, PyMySQL |
| Environment Management | python-dotenv, Conda or virtual environments |
| Version Control | Git, GitHub |
| Documentation | Markdown, project README files, documentation style guide |

---

## How to Use This Repository

### 1. Clone the repository

```bash
git clone https://github.com/ElihleN/data_analysis.git
cd data_analysis
```

### 2. Review the project documentation

Start with the project-level README files. They explain the purpose of each project, the workflow, the expected inputs, and how to reproduce or extend the analysis.

### 3. Run project files in order

For SQL-to-dashboard projects, the usual workflow is:

1. Prepare the database and clean the imported data.
2. Create reusable SQL views and summary tables.
3. Connect the dashboard script to the database.
4. Run the dashboard locally.

For notebook-based projects, the usual workflow is:

1. Open the main notebook.
2. Review the data loading and cleaning steps.
3. Run the exploratory analysis sections.
4. Review the visualisations and interpretations.
5. Read the final findings or recommendations.

---

## Documentation Approach

The documentation in this repository follows a technical documentation style:

- Start with the purpose and business context.
- Explain the workflow before showing implementation details.
- Document assumptions, inputs, outputs, and dependencies.
- Provide reproducible setup instructions where possible.
- Use clear headings and concise explanations.
- Separate business interpretation from technical implementation.

For documentation standards used in this repository, see [`docs/documentation_style_guide.md`](docs/documentation_style_guide.md).

---

## Portfolio Value

This repository presents practical analytics workflows rather than isolated code snippets. It shows the ability to move from raw data to cleaned data, from cleaned data to analysis-ready outputs, and from analysis-ready outputs to reporting, dashboards, or business recommendations.

The work is especially relevant for roles involving:

- Data analysis
- Business intelligence
- Analytics engineering support
- Data-driven reporting
- Junior machine learning or data science preparation
- Technical documentation for analytical systems

---

## Next Improvements

Planned improvements for this portfolio include:

- Adding screenshots of dashboard outputs
- Adding sample result summaries for each project
- Creating a `requirements.txt` file for easier environment setup
- Adding more project-level README files as new projects are added
- Adding a short case-study summary for each completed analysis
- Expanding the ongoing NYC taxi SQL/Python analysis documentation

---

## Author

Maintained by [ElihleN](https://github.com/ElihleN).

This portfolio reflects an applied approach to data analysis: clean the data carefully, structure the workflow clearly, document the process professionally, and communicate insights in a way that supports decision-making.
