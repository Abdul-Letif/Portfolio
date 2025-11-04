import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define parameters
start_date = "2022-01-01"
end_date = "2024-12-31"
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

regions = ["North America", "Europe", "Asia-Pacific", "Latin America", "Middle East & Africa"]
product_categories = ["Laptops", "Smartphones", "Cloud Services", "Software Licenses", "Accessories"]
sales_reps = [fake.name() for _ in range(20)]
customer_segments = ["Enterprise", "Small Business", "Individual"]

# Generate dataset
records = []
for date in date_range:
    for _ in range(np.random.randint(3, 8)):  # 3 to 7 transactions per day
        category = random.choice(product_categories)
        subcategory = f"{category} - Model {random.randint(100, 999)}"
        region = random.choice(regions)
        rep = random.choice(sales_reps)
        segment = random.choice(customer_segments)
        units_sold = np.random.randint(1, 10)
        unit_price = round(np.random.uniform(100, 2000), 2)
        cost_per_unit = round(unit_price * np.random.uniform(0.6, 0.9), 2)
        sales_amount = round(units_sold * unit_price, 2)
        cost = round(units_sold * cost_per_unit, 2)
        profit = round(sales_amount - cost, 2)
        profit_margin = round(profit / sales_amount, 4)

        records.append({
            "Date": date,
            "Region": region,
            "Sales Rep": rep,
            "Product Category": category,
            "Product Sub-Category": subcategory,
            "Customer Segment": segment,
            "Units Sold": units_sold,
            "Unit Price": unit_price,
            "Sales Amount": sales_amount,
            "Cost": cost,
            "Profit": profit,
            "Profit Margin": profit_margin
        })

# Create DataFrame
df_sales = pd.DataFrame(records)

# Save to Excel
file_path = "D:/Data Analysis/Portfolio/Sales Dashboard/sale_data.xlsx"
df_sales.to_excel(file_path, index=False)

file_path
