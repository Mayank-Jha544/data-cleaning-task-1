import pandas as pd

df = pd.read_csv("netflix_titles.csv")

# Fill missing values
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Not Rated")

# Drop missing important rows
df = df.dropna(subset=['date_added'])

# Remove duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert date
df['date_added'] = pd.to_datetime(df['date_added'])

# Clean text
df['country'] = df['country'].str.strip()

# Save cleaned file
df.to_csv("cleaned_netflix_data.csv", index=False)