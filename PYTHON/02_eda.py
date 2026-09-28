import pandas as pd

# ==========================================
# STEP 1: LOAD DATA
# ==========================================

file_path = rfile_path = r"C:\Users\Ketan\OneDrive\Desktop\Logistics_Analytics_AI\EXCEL\Business_Operations_Analytics.xlsx"

df = pd.read_excel(file_path)

print("Data loaded successfully!")


# ==========================================
# STEP 2: CREATE CALCULATED SALES
# ==========================================

df["Calculated_sales"] = df["quantity"] * df["unit_price"]


# ==========================================
# STEP 3: BUSINESS KPIs
# ==========================================

total_orders = df["order_id"].count()
total_sales = df["total_sale"].sum()
average_order_value = df["total_sale"].mean()
total_quantity = df["quantity"].sum()

print("\n--- BUSINESS KPIs ---")

print("Total Orders:", total_orders)
print("Total Sales:", round(total_sales, 2))
print("Average Order Value:", round(average_order_value, 2))
print("Total Quantity Sold:", total_quantity)


# ==========================================
# STEP 4: SALES BY REGION
# ==========================================

sales_by_region = (
    df.groupby("region")["total_sale"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- SALES BY REGION ---")
print(sales_by_region)


# ==========================================
# STEP 5: SALES BY CATEGORY
# ==========================================

sales_by_category = (
    df.groupby("category")["total_sale"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- SALES BY CATEGORY ---")
print(sales_by_category)


# ==========================================
# STEP 6: SALES BY SALES REPRESENTATIVE
# ==========================================

sales_by_rep = (
    df.groupby("sales_rep")["total_sale"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- SALES BY SALES REPRESENTATIVE ---")
print(sales_by_rep)


# ==========================================
# STEP 7: ORDER STATUS
# ==========================================

order_status = df["status"].value_counts()

print("\n--- ORDER STATUS ---")
print(order_status)