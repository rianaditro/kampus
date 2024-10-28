---
marp: true
author: Rian Adi
theme: gaia
backgroundColor: white
footer: Data Scraping | rianaditro
---
<!-- _backgroundColor: grey -->
<!-- _color: white -->
<!-- _paginate: skip -->
<br>
<br>
<br>
<br>

# Data Processing with Pandas
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Pandas
Pandas is a powerful and user-friendly Python library that is widely used for data manipulation and analysis. It helps you work with structured data (like spreadsheets or databases) efficiently and intuitively. For someone who isn’t a programmer, you can think of Pandas as a versatile tool for organizing and processing data—similar to using a digital spreadsheet (like Excel) but with the added capability of handling large datasets programmatically.

```python
import pandas as pd
```

---
## DataFrame
A DataFrame is a central feature of Pandas. You can think of it as a table or a spreadsheet that contains data organized in rows and columns. Each column can hold different types of data (like numbers, text, or dates), and each row represents a single observation or record.

```python
df = pd.DataFrame()
```
For better experience, use Jupyter Notebook or Google Collab.

---
**Creating a DataFrame from a List of Dictionaries**
```python
# Example scraped data in the form of a list of dictionaries
data = [
    {'name': 'Laptop', 'price': 999.99, 'rating': 4.5},
    {'name': 'Smartphone', 'price': 499.99, 'rating': 4.7},
    {'name': 'Tablet', 'price': 299.99, 'rating': 4.2},
]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
```
---
**Data Cleaning and Data Processing**
```python
# Assume we have a DataFrame with some missing values
df['rating'].fillna(df['rating'].mean(), inplace=True)  # Fill missing ratings with the mean rating

# Remove any duplicates
df.drop_duplicates(inplace=True)

# Display the cleaned DataFrame
print(df)
```
---
**Joining or Merging DataFrames**
```python
# Another DataFrame with more information
additional_data = [
    {'name': 'Laptop', 'brand': 'Brand A'},
    {'name': 'Smartphone', 'brand': 'Brand B'},
]

df_additional = pd.DataFrame(additional_data)

# Merge the two DataFrames on the 'name' column
merged_df = pd.merge(df, df_additional, on='name')

# Display the merged DataFrame
print(merged_df)
```
---
## Class Activity
Scrape https://books.toscrape.com/ and save it to an excel file!

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [Automate Table Extraction with BeautifulSoup, Pandas, and API Extraction](https://medium.com/@rianaditro/scraping-table-for-any-sites-with-bs4-pandas-and-api-extraction-ddd85e67f490)

---
## Homework Assignment
Use pandas to extract table from https://www.runnersworld.com/races-places/a20823734/these-are-the-worlds-fastest-marathoners-and-marathon-courses/ without using Requests!

---
<!-- _backgroundColor: grey -->
<!-- _color: white -->
<!-- _paginate: false -->
<br>
<br>
<br>
<br>

# Thank you
Any Question?
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

