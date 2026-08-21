import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('gurgaon_real_estate.csv')
# print(df.head())
# print(df.info())

#Data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')  # Remove leading/trailing whitespace from column names and replace spaces with underscores
# print(df.columns.tolist())
df = df.drop_duplicates()

#Numeric colomns cleaning
df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)  # Remove dollar sign and commas, convert to float
# print(df['price'].head())
df['area'] = df['area'].astype(str).str.replace(',', '').astype(int)  # Remove dollar sign and commas, convert to float
# print(df['area'].head())
df['rate_per_sqft'] = df['price'].astype(str).str.replace(',', '').astype(float) / df['area'].astype(float)  # Calculate rate per sqft
# print(df['rate_per_sqft'].head())

#Categorical colomn cleaning
df['status'] = df['status'].str.strip().str.lower().str.replace(' ', '_')  # Remove leading/trailing whitespace and standardize status values
# print(df['status'].head())
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})  
# print(df['rera_approval'].head())
df['flat_type'] = df['flat_type'].str.strip().str.lower()  # Remove leading/trailing whitespace from column names and replace spaces with 
df = df.drop_duplicates()

# print(df)
# print(df.info())

#Questions 1: Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
# print("Costliest flat details:")
# print(costliest_flat)
# print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK flat located in {costliest_flat['locality']} priced at {costliest_flat['price']/10000000} cores in {costliest_flat['socity']} socity.")

# Question 2:Which locality has the highest average price?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
# print(f"The locality with highest average price is {highest_avg_price_locality}.")
# print(df.groupby("locality")["price"].mean().sort_values(ascending=False))

#Question 3: Which locality has the highest rate per square foot?
highest_rate_per_square = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
# print(f"The locality with highest rate per square foot is {highest_rate_per_square}.")
# print(df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False))

#Question 4: Do ready-to-move properties cost more than under-construction properties?
ready_to_move = df[df['status'] == 'ready_to_move']['price'].mean()
under_construction = df[df['status'] == 'under_construction']['price'].mean()
# if ready_to_move > under_construction:
    # print("Ready -to-move properties cost more on average than under-construction properties.")
# else:
    # print("Under-construction properties cost more on average then ready-to-move properties.")
    
# print(df.groupby("status")["price"].median())

# Question 5: Do RERA-approved properties command a price premium?
rera_approved_avg_price = df.loc[df['rera_approval'] == True, 'price'].mean()
rera_not_approved_avg_price = df.loc[df['rera_approval'] == False, 'price'].mean()
# if rera_approved_avg_price > rera_not_approved_avg_price:
#     print("Rera-approved properties command a price premium.")
# else:
#     print("Rera-approved properties do not command a price premium.")

#Question 6:How does area (sqft) impact property price?
# sns.scatterplot(data=df, x='area', y='price')
#plt.show()

#Question 7: Which BHK configuration is the most expensive based on per sqft rate?
# df.groupby("bhk_count")["price"].mean()
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
# print(f"The most expensive BHk configuration on average is {most_expensive_bhk} BHK.")

#Question 8:Which property type (Apartment, Floor, Plot) is the costliest?
# df.groupby("flat_type")["price"].mean()
Costliest = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
# print(f"The most expensive properties type is {Costliest}.")

#Question 9:Do certain builders or companies consistently price higher?
# print(df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5))
#print name of top 5
print("The top 5 builders that price higher are:", end=" ")
top_5_builders = df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5)
# for builders in top_5_builders.index:
    # print(builders, end=", ")

#Question 10:Are larger homes always more expensive per square foot?
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()