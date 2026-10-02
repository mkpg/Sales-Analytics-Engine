import numpy as np
import pandas as pd

df = pd.read_csv('messy_sales_project1.csv')

# Identifying the missing values in the dataset

print(df.isna().sum())

print("ord_date \n")
print(df[df["Order_Date"].isna()])

print("\n cust_id \n")
print(df[df["Customer_ID"].isna()])

print("\n product \n")
print(df[df["Product"].isna()])

print("\n region \n")
print(df[df["Region"].isna()])

print("\n quantity \n")
print(df[df["Quantity"].isna()])

print("\n unit_price \n")
print(df[df["Unit_Price"].isna()])

print("\n discount \n")
print(df[df["Discount"].isna()])


# Cleaning Product

df['Product'] = df['Product'].str.lower()
df['Product'] = df['Product'].str.strip()
print(df['Product'].unique())


# Cleaning Region

df['Region'] = df['Region'].str.lower()
df['Region'] = df['Region'].str.strip()
df['Region'] = df['Region'].replace('bengaluru', 'bangalore')
print(df['Region'].unique())


# Cleaning Payment Method

df['Payment_Method'] = df['Payment_Method'].str.lower()
df['Payment_Method'] = df['Payment_Method'].str.strip()
print(df['Payment_Method'].unique())


# Checking numeric values

print(df.dtypes)
print(df['Quantity'].unique())
print(df['Unit_Price'].unique())
print(df['Discount'].unique())


# Cleaning Quantity

df['Quantity'] = pd.to_numeric(df['Quantity'], errors="coerce")
df.loc[df["Quantity"] <= 0, "Quantity"] = np.nan
print(df['Quantity'].unique())


# Cleaning Unit Price

df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors="coerce")
df.loc[df["Unit_Price"] <= 0, "Unit_Price"] = np.nan
print(df['Unit_Price'].unique())


# Cleaning Discount

df["Discount"] = df["Discount"].astype(str)

df.loc[df["Discount"].str.endswith("%"), "Discount"] = (
    df.loc[df["Discount"].str.endswith("%"), "Discount"]
    .str.replace("%", "", regex=False)
    .astype(float) / 100
)

df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")

df.loc[(df["Discount"] < 0) | (df["Discount"] > 1), "Discount"] = np.nan

print(df["Discount"].unique())


print("\n")

print(df.info())
print(df.isna().sum())
print(df.duplicated().sum())
print(df["Quantity"].min())      
print(df["Unit_Price"].min())      
print(df["Discount"].min())      
print(df["Discount"].max())      
print(df["Product"].unique())    
print(df["Region"].unique())    
print(df["Payment_Method"].unique())
print(df[df["Order_Date"].isna()])

df = df.drop_duplicates()
print(df.duplicated().sum())

df["Gross_sales"] = df['Quantity'] * df["Unit_Price"]
print(df["Gross_sales"].head())

df["Discount_amount"] = df["Gross_sales"] * df["Discount"]
print(df["Discount_amount"].head())

df["Net_sales"] = df["Gross_sales"] - df["Discount_amount"]
print(df["Net_sales"].head())
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print(df["Order_Date"].head())
df['Order_Date'] = pd.to_datetime(df['Order_Date'],errors = 'coerce')
df["ordered_Year"] = df["Order_Date"].dt.year
df["Ordered_month"] = df["Order_Date"].dt.month
df["Ordered_day"] = df["Order_Date"].dt.day

df["Quarter"] = df['Ordered_month'].apply(lambda x: 1 if x in [1,2,3] else (2 if x in [4,5,6] else (3 if x in [7,8,9] else 4)))

Gross_sum = df["Gross_sales"].sum()
Discount_sum = df["Discount_amount"].sum()
Net_sum = df["Net_sales"].sum()
tot_quantity = df["Quantity"].sum()
avg_net_sales = df["Net_sales"].mean()
 
net_sale_prod = df.groupby(df["Product"])["Net_sales"].sum()
quantity_prod = df.groupby(df["Product"])["Quantity"].sum()
no_of_ord = df.groupby(df["Product"])["Order_ID"].count()

reg_analysis_sales =  df.groupby(df["Region"]).Net_sales.sum()
reg_quantity_sold = df.groupby(df["Region"]).Quantity.sum()
reg_no_orders = df.groupby(df["Region"]).Order_ID.count()

net_sale_month = df.groupby(df['Ordered_month'])['Net_sales'].sum()
net_sale_quarter = df.groupby(df['Ordered_month'])['Net_sales'].sum()
quantity_sold_month = df.groupby(df['Ordered_month'])['Quantity'].sum()


netsale_payment_meth = df.groupby(df['Payment_Method'])['Net_sales'].sum()
no_ord_payment_meth = df.groupby(df['Payment_Method'])['Order_ID'].count()


avg_discount = df["Discount"].mean()
tot_discount = df["Discount"].sum()
net_sale_discount = df.groupby(df["Quarter"])["Net_sales"].sum()

# print("Total Gross Sales: ", Gross_sum)
# print("Total Discount: ", Discount_sum)
# print("Total Net Sales: ", Net_sum)
# print("Total Quantity: ", tot_quantity)
# print("Average Net Sales: ", avg_net_sales)
# print(net_sale_prod)
# print(quantity_prod)
# print(no_of_ord)    
# print(reg_analysis_sales)
# print(reg_quantity_sold)
# print(reg_no_orders)
# print(net_sale_month)
# print(net_sale_quarter)
# print(quantity_sold_month)
# print(netsale_payment_meth)
# print(no_ord_payment_meth)
# print(avg_discount)
# print(tot_discount)
# print(net_sale_discount)
d = {}
d["Total Gross Sales"] = Gross_sum
d["Total Discount"] = Discount_sum
d["Total Net Sales"] = Net_sum
d["Total Quantity"] = tot_quantity
d["Average Net Sales"] = avg_net_sales
d["net_sale_prod"] = net_sale_prod
d["quantity_prod"] = quantity_prod
d["no_of_ord"] = no_of_ord
d["reg_analysis_sales"] = reg_analysis_sales
d["reg_quantity_sold"] = reg_quantity_sold
d["reg_no_orders"] = reg_no_orders
d["net_sale_month"] = net_sale_month
d["net_sale_quarter"] = net_sale_quarter
d["quantity_sold_month"] = quantity_sold_month
d["netsale_payment_meth"] = netsale_payment_meth
d["no_ord_payment_meth"] = no_ord_payment_meth 
d["avg_discount"] = avg_discount
d["tot_discount"] = tot_discount
d["net_sale_discount"] = net_sale_discount
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
df.to_csv('cleaned_sales_data.csv', index=False) 