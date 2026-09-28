import pandas as pd

# ==========================================
# STEP 1: LOAD DATA
# ==========================================

file_path = rfile_path = r"C:\Users\Ketan\OneDrive\Desktop\Logistics_Analytics_AI\EXCEL\Business_Operations_Analytics.xlsx"

df = pd.read_excel(file_path)

print("Data loaded successfully!")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())


# ==========================================
# STEP 2: DATA INSPECTION
# ==========================================

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe())


# ==========================================
# STEP 3: DATA VALIDATION
# ==========================================

print("\n--- DATA VALIDATION ---")

# Check duplicate Order IDs
print("\nDuplicate Order IDs:")
print(df["order_id"].duplicated().sum())


# Check sales calculation
df["Calculated_sales"] = df["quantity"] * df["unit_price"]

print("\nSales Calculation Check:")
print(
    (df["total_sale"].round(2) == df["Calculated_sales"].round(2)).value_counts()
)


# Check invalid quantities
print("\nInvalid Quantity Records:")
print(df[df["quantity"] <= 0])


# Check invalid unit prices
print("\nInvalid Unit Price Records:")
print(df[df["unit_price"] <= 0])


# Check duplicate orders
print("\nDuplicate Orders:")
print(df[df["order_id"].duplicated(keep=False)])