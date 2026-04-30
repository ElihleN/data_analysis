# Data Analysis Portfolio

A professional portfolio of data analysis projects that demonstrate practical skills in SQL, Python, data cleaning, exploratory data analysis, dashboard development, and business-oriented communication.

This repository is designed to show not only technical ability, but also the ability to document analytical workflows clearly. Each project is written so that another analyst, recruiter, or technical reviewer can understand the business question, the data preparation process, the analytical approach, and the final output.

---

## Portfolio Focus

This repository highlights the following skills:

- Data cleaning and transformation using SQL
- Exploratory data analysis for business decision-making
- Creation of analysis-ready datasets and summary tables
- Dashboard development with Python, Dash, and Plotly
- Database connection management using environment variables
- Clear documentation of workflows, assumptions, and reproducibility steps
- Communication of technical results for non-technical stakeholders

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

Detailed instructions are included inside each project folder.

---

## Documentation Approach

The documentation in this repository follows a technical documentation style:

- Start with the purpose and business context.
- Explain the workflow before showing implementation details.
- Document assumptions, inputs, outputs, and dependencies.
- Provide reproducible setup instructions.
- Use clear headings and concise explanations.
- Separate business interpretation from technical implementation.

This makes the repository easier to review and also demonstrates communication skills that are important in data analysis, machine learning, and technical documentation roles.

---

## Portfolio Value

This repository presents a practical analytics workflow rather than isolated code snippets. It shows the ability to move from raw data to cleaned data, from cleaned data to analysis-ready outputs, and from analysis-ready outputs to interactive reporting.

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

---

## Author

Maintained by [ElihleN](https://github.com/ElihleN).

This portfolio reflects an applied approach to data analysis: clean the data carefully, structure the workflow clearly, document the process professionally, and communicate insights in a way that supports decision-making.
