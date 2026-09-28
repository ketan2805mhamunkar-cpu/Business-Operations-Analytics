import pandas as pd

# -----------------------------------
# STEP 5 - ADVANCED EDA
# -----------------------------------

# Load data
file_path = rfile_path = r"C:\Users\Ketan\OneDrive\Desktop\Logistics_Analytics_AI\EXCEL\Business_Operations_Analytics.xlsx"

df = pd.read_excel(file_path)

print("\n========== ADVANCED EDA ==========\n")

# -----------------------------------
# 1. Sales by Product
# -----------------------------------

product_sales = (
    df.groupby("product")["total_sale"]
    .agg(["sum", "count"])
    .sort_values("sum", ascending=False)
)

print("1. SALES BY PRODUCT")
print(product_sales)


# -----------------------------------
# 2. Quantity Sold by Product
# -----------------------------------

product_quantity = (
    df.groupby("product")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n2. QUANTITY SOLD BY PRODUCT")
print(product_quantity)


# -----------------------------------
# 3. Sales by Customer
# -----------------------------------

customer_sales = (
    df.groupby("customer")["total_sale"]
    .sum()
    .sort_values(ascending=False)
)

print("\n3. SALES BY CUSTOMER")
print(customer_sales)


# -----------------------------------
# 4. Sales by Region
# -----------------------------------

region_sales = (
    df.groupby("region")["total_sale"]
    .agg(["sum", "count", "mean"])
    .sort_values("sum", ascending=False)
)

print("\n4. SALES BY REGION")
print(region_sales)


# -----------------------------------
# 5. Sales by Category
# -----------------------------------

category_sales = (
    df.groupby("category")["total_sale"]
    .agg(["sum", "count", "mean"])
    .sort_values("sum", ascending=False)
)

print("\n5. SALES BY CATEGORY")
print(category_sales)


# -----------------------------------
# 6. Region + Category Analysis
# -----------------------------------

region_category = pd.pivot_table(
    df,
    values="total_sale",
    index="region",
    columns="category",
    aggfunc="sum",
    fill_value=0
)

print("\n6. REGION + CATEGORY SALES")
print(region_category)


# -----------------------------------
# 7. Sales by Sales Representative
# -----------------------------------

sales_rep = (
    df.groupby("sales_rep")["total_sale"]
    .agg(["sum", "count", "mean"])
    .sort_values("sum", ascending=False)
)

print("\n7. SALES BY SALES REPRESENTATIVE")
print(sales_rep)


# -----------------------------------
# 8. Status Analysis
# -----------------------------------

status_analysis = (
    df.groupby("status")["total_sale"]
    .agg(["sum", "count", "mean"])
    .sort_values("sum", ascending=False)
)

print("\n8. STATUS ANALYSIS")
print(status_analysis)


# -----------------------------------
# 9. Return Rate
# -----------------------------------

total_orders = len(df)

returned_orders = (df["status"] == "Returned").sum()

return_rate = (returned_orders / total_orders) * 100

print("\n9. RETURN RATE")
print(f"Total Orders   : {total_orders}")
print(f"Returned Orders: {returned_orders}")
print(f"Return Rate    : {return_rate:.2f}%")


# -----------------------------------
# 10. Average Order Value
# -----------------------------------

average_order_value = df["total_sale"].mean()

print("\n10. AVERAGE ORDER VALUE")
print(f"Average Order Value: {average_order_value:.2f}")


# -----------------------------------
# 11. Top 5 Orders
# -----------------------------------

top_orders = (
    df[["order_id", "customer", "region", "product", "total_sale", "status"]]
    .sort_values("total_sale", ascending=False)
    .head(5)
)

print("\n11. TOP 5 ORDERS")
print(top_orders)


# -----------------------------------
# 12. Final Summary
# -----------------------------------

print("\n========== STEP 5 COMPLETED ==========")

print(f"Total Sales       : {df['total_sale'].sum():.2f}")
print(f"Total Orders      : {len(df)}")
print(f"Average Order     : {df['total_sale'].mean():.2f}")
print(f"Returned Orders   : {returned_orders}")
print(f"Return Rate       : {return_rate:.2f}%")

# -----------------------------------
# STEP 6 - TIME-BASED SALES ANALYSIS
# -----------------------------------

print("\n========== STEP 6: TIME ANALYSIS ==========\n")

# Convert Order Date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# -----------------------------------
# 1. Sales by Date
# -----------------------------------

daily_sales = (
    df.groupby("order_date")["total_sale"]
    .sum()
    .sort_index()
)

print("1. DAILY SALES")
print(daily_sales)


# -----------------------------------
# 2. Orders by Date
# -----------------------------------

daily_orders = (
    df.groupby("order_date")["order_id"]
    .count()
    .sort_index()
)

print("\n2. DAILY ORDERS")
print(daily_orders)


# -----------------------------------
# 3. Monthly Sales
# -----------------------------------

df["month"] = df["order_date"].dt.to_period("M")

monthly_sales = (
    df.groupby("month")["total_sale"]
    .sum()
    .sort_index()
)

print("\n3. MONTHLY SALES")
print(monthly_sales)


# -----------------------------------
# 4. Monthly Orders
# -----------------------------------

monthly_orders = (
    df.groupby("month")["order_id"]
    .count()
    .sort_index()
)

print("\n4. MONTHLY ORDERS")
print(monthly_orders)


# -----------------------------------
# 5. Monthly Average Order Value
# -----------------------------------

monthly_aov = (
    df.groupby("month")["total_sale"]
    .mean()
    .sort_index()
)

print("\n5. MONTHLY AVERAGE ORDER VALUE")
print(monthly_aov)


# -----------------------------------
# 6. Best Sales Day
# -----------------------------------

best_sales_day = daily_sales.idxmax()
best_sales_value = daily_sales.max()

print("\n6. BEST SALES DAY")
print(f"Date  : {best_sales_day}")
print(f"Sales : {best_sales_value:.2f}")


# -----------------------------------
# 7. Lowest Sales Day
# -----------------------------------

lowest_sales_day = daily_sales.idxmin()
lowest_sales_value = daily_sales.min()

print("\n7. LOWEST SALES DAY")
print(f"Date  : {lowest_sales_day}")
print(f"Sales : {lowest_sales_value:.2f}")


print("\n========== STEP 6 COMPLETED ==========")