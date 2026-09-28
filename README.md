# Business Operations Analytics

## ðŸ“Š Project Overview

**Business Operations Analytics** is an end-to-end data analytics project developed to analyze business sales and operational performance using **Python, SQL, Excel, and Power BI**.

The project takes a small business transaction dataset through the complete analytics workflow:

**Data Loading â†’ Exploratory Analysis â†’ Advanced Analysis â†’ SQL Analysis â†’ Excel Reporting â†’ Power BI Dashboard**

The objective is to transform raw operational data into meaningful business insights that can support sales and operational decision-making.

---

## ðŸŽ¯ Business Objectives

The project analyzes key business questions including:

* What are the overall sales and order volumes?
* What is the average order value?
* Which regions generate the most sales?
* Which product categories contribute most to revenue?
* How are sales distributed across sales representatives?
* What is the distribution of order statuses?
* Which products and business areas require further attention?
* How can business data be transformed into actionable reports and dashboards?

---

# ðŸ—‚ï¸ Repository Structure

```text
Logistics_Analytics_AI/
â”‚
â”œâ”€â”€ Excel/
â”‚   â””â”€â”€ Business_Operations_Analytics.xlsx
â”‚
â”œâ”€â”€ PowerBI/
â”‚   â””â”€â”€ Business_Operations_Analytics.pbix
â”‚
â”œâ”€â”€ PYTHON/
â”‚   â”œâ”€â”€ 01_load_data.py
â”‚   â”œâ”€â”€ 02_eda.py
â”‚   â””â”€â”€ 03_advanced_eda.py
â”‚
â”œâ”€â”€ SQL/
â”‚   â”œâ”€â”€ 07_setup_sqlite.py
â”‚   â”œâ”€â”€ business_operations.db
â”‚   â”œâ”€â”€ business_operations.sqbpro
â”‚   â””â”€â”€ business_operations.sql
â”‚
â””â”€â”€ README.md
```

---

# ðŸ“ Project Components

## ðŸ Python

The Python analysis is organized into three scripts.

### `01_load_data.py`

Responsible for:

* Loading the business operations dataset
* Inspecting the dataset
* Displaying rows and columns
* Checking the initial structure of the data

### `02_eda.py`

Performs Exploratory Data Analysis including:

* Business KPIs
* Sales by region
* Sales by category
* Sales by sales representative
* Order-status analysis

### `03_advanced_eda.py`

Performs deeper analysis of the business data, including additional trends and operational insights.

Python analysis was performed using **Pandas** and related data-analysis functionality.

---

# ðŸ—„ï¸ SQL Analysis

The project uses **SQLite** for database analysis.

The SQL folder contains:

### `07_setup_sqlite.py`

Used to create and prepare the SQLite database.

### `business_operations.db`

SQLite database containing the project data.

### `business_operations.sql`

SQL script containing the database/query work used for the project.

### `business_operations.sqbpro`

SQLiteStudio project file associated with the database.

SQL analysis demonstrates:

* Data querying
* Filtering
* Aggregation
* GROUP BY
* ORDER BY
* Business KPI calculations
* Regional analysis
* Category analysis
* Sales representative analysis
* Order-status analysis

---

# ðŸ“— Excel Analysis

The Excel component is located at:

```text
Excel/Business_Operations_Analytics.xlsx
```

Excel was used for business reporting and analysis.

The workbook supports analysis of:

* Sales performance
* Order information
* Regional performance
* Category performance
* Sales representative performance
* Operational metrics

---

# ðŸ“Š Power BI Dashboard

The Power BI dashboard is located at:

```text
PowerBI/Business_Operations_Analytics.pbix
```

The dashboard provides an interactive business view of the dataset.

The analysis includes areas such as:

* Total Sales
* Total Orders
* Average Order Value
* Total Quantity Sold
* Regional Sales
* Category Sales
* Sales Representative Performance
* Order Status

The `.pbix` file can be opened using **Microsoft Power BI Desktop**.

---

# ðŸ“Œ Dataset

The project contains **45 business orders**.

The dataset includes the following fields:

```text
order_id
order_date
customer
region
sales_rep
product
category
quantity
unit_price
total_sale
status
Calculated_sales
Sale_check
```

### Important data fields

| Field              | Description                                      |
| ------------------ | ------------------------------------------------ |
| `order_id`         | Unique order identifier                          |
| `order_date`       | Date of the order                                |
| `customer`         | Customer associated with the order               |
| `region`           | Business/sales region                            |
| `sales_rep`        | Sales representative                             |
| `product`          | Product sold                                     |
| `category`         | Product category                                 |
| `quantity`         | Quantity sold                                    |
| `unit_price`       | Price per unit                                   |
| `total_sale`       | Recorded sales value                             |
| `status`           | Order status                                     |
| `Calculated_sales` | Sales calculated from quantity Ã— unit price      |
| `Sale_check`       | Validation between calculated and recorded sales |

---

# ðŸ“ˆ Business KPIs

The analysis produced the following key metrics:

| KPI                 |        Result |
| ------------------- | ------------: |
| Total Orders        |        **45** |
| Total Sales         | **12,581.46** |
| Average Order Value |    **279.59** |
| Total Quantity Sold |       **168** |

### KPI interpretation

The dataset contains **45 orders** generating total sales of **12,581.46**, with an average order value of approximately **279.59**.

---

# ðŸŒŽ Sales by Region

| Region  |        Sales |
| ------- | -----------: |
| South   | **4,362.62** |
| East    | **3,797.05** |
| West    | **2,235.97** |
| Midwest | **2,185.82** |

The analysis shows differences in sales contribution across the four regions.

---

# ðŸ·ï¸ Sales by Category

| Category          |        Sales |
| ----------------- | -----------: |
| Electronics       | **6,598.72** |
| Office Supplies   | **2,656.70** |
| Furniture         | **2,393.79** |
| Shipping Supplies |   **932.25** |

The analysis provides visibility into how different product categories contribute to total sales.

---

# ðŸ‘¥ Sales by Sales Representative

| Sales Representative |        Sales |
| -------------------- | -----------: |
| Sara Khan            | **4,111.40** |
| James O'Brien        | **3,997.03** |
| Tom Alvarez          | **3,224.37** |
| Maria Chen           |   **626.97** |
| Priya Nair           |   **621.69** |

This analysis can be used to monitor sales contribution by representative and identify areas requiring further business investigation.

---

# ðŸ“¦ Order Status Analysis

| Status    | Orders |
| --------- | -----: |
| Completed | **35** |
| Returned  |  **5** |
| Pending   |  **3** |
| Cancelled |  **2** |

The order-status analysis provides an overview of the current state of transactions and can support operational monitoring.

---

# ðŸ” Analysis Workflow

The project follows this workflow:

```text
              Raw Business Data
                     â”‚
                     â–¼
              Data Loading
                     â”‚
                     â–¼
            Data Exploration
                     â”‚
                     â–¼
          Exploratory Data Analysis
                     â”‚
                     â–¼
            Advanced Analysis
                     â”‚
             â”Œâ”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”
             â–¼               â–¼
           SQL             Excel
             â”‚               â”‚
             â””â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
                     â–¼
              Power BI
                     â”‚
                     â–¼
            Business Insights
```

---

# ðŸ§® Data Validation

The project includes validation of calculated sales.

The dataset contains:

```text
Calculated_sales
Sale_check
```

The calculated sales value is based on:

```text
Quantity Ã— Unit Price
```

The `Sale_check` field is used to compare the calculated value against the recorded `total_sale`.

This helps verify the consistency of the transaction-level sales data before performing business analysis.

---

# ðŸ’¡ Business Insights

The analysis provides visibility into several areas of business performance:

### Sales Performance

Total sales across the 45 transactions were **12,581.46**, with an average order value of **279.59**.

### Regional Performance

Sales vary across the four regions, providing an opportunity for management to investigate regional differences in revenue contribution.

### Category Performance

The category analysis shows different levels of contribution to overall sales across Electronics, Office Supplies, Furniture, and Shipping Supplies.

### Sales Representative Performance

Sales contribution varies considerably across representatives, allowing management to investigate factors such as customer allocation, product mix, territory, and sales activity.

### Order Operations

Most orders in the dataset have a **Completed** status, while returned, pending, and cancelled orders represent additional operational categories that can be monitored.

---

# ðŸ› ï¸ Technologies Used

| Technology       | Purpose                                 |
| ---------------- | --------------------------------------- |
| **Python**       | Data analysis and EDA                   |
| **Pandas**       | Data manipulation and analysis          |
| **SQL / SQLite** | Database analysis and querying          |
| **Excel**        | Business reporting and analysis         |
| **Power BI**     | Interactive dashboard and visualization |
| **SQLiteStudio** | SQLite database management              |

---

# â–¶ï¸ How to Run the Project

## Python

Navigate to the Python folder:

```powershell
cd PYTHON
```

Run the scripts in sequence:

```powershell
python 01_load_data.py
python 02_eda.py
python 03_advanced_eda.py
```

Make sure Python and the required data-analysis libraries are installed.

---

## SQL

The SQL component uses SQLite.

The database is available at:

```text
SQL/business_operations.db
```

The SQL script is available at:

```text
SQL/business_operations.sql
```

The database can be opened using SQLite-compatible database software such as SQLiteStudio.

---

## Excel

Open:

```text
Excel/Business_Operations_Analytics.xlsx
```

---

## Power BI

Open:

```text
PowerBI/Business_Operations_Analytics.pbix
```

using Microsoft Power BI Desktop.

---

# ðŸŽ“ Skills Demonstrated

This project demonstrates practical skills in:

* Data Analysis
* Exploratory Data Analysis
* Business Analytics
* Data Validation
* Python
* Pandas
* SQL
* SQLite
* Excel
* Power BI
* KPI Analysis
* Sales Analysis
* Regional Analysis
* Category Analysis
* Sales Representative Analysis
* Operational Reporting
* Data Visualization
* Business Insight Generation

---

# ðŸ“Œ Project Outcome

This project demonstrates an end-to-end business analytics workflow using multiple industry-relevant tools.

The same business dataset was analyzed through **Python, SQL, Excel, and Power BI**, demonstrating the ability to:

```text
Load Data
    â†“
Analyze Data
    â†“
Validate Data
    â†“
Query Data
    â†“
Create Reports
    â†“
Build Dashboard
    â†“
Generate Business Insights
```

The project is designed to demonstrate practical, hands-on data analytics skills relevant to **Data Analyst, MIS Analyst, Reporting Analyst, and Business Analyst** roles.

---

## ðŸ‘¤ Author

**Ketan Mhamunkar**

Aspiring Data Analyst | Business Analytics | MIS & Reporting

**Skills:**
Python | SQL | Excel | Power BI | Data Analysis | Business Analytics

