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

# Python Collections
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Lists vs Dictionaries
When working on data scraping tasks, it's essential to be familiar with core Python data structures like **lists**, and **dictionaries**, as they are key to processing and organizing the scraped data efficiently.

```python
an_empty_list = []
an_empty_dictionary = dict()
```

---
## Common List Operations
**1. append()**
```python
data = []
data.append("Product A")
data.append("Product B")
print(data)  # Output: ['Product A', 'Product B']
```
**2. extend()**
```python
data1 = ["Product A", "Product B"]
data2 = ["Product C", "Product D"]
data1.extend(data2)
print(data1)  # Output: ['Product A', 'Product B', 'Product C', 'Product D']
```

---
## Common Dictionary Operations
**1. get()**
```python
data = {"name": "Laptop", "price": 999.99}
product_name = data.get("name", "Unknown")
product_rating = data.get("rating", "No rating")  # Key not present, returns default
print(product_name)  # Output: Laptop
print(product_rating)  # Output: No rating
```
**2. keys()**
```python
data = {"name": "Laptop", "price": 999.99}
keys = data.keys()
print(keys)  # Output: dict_keys(['name', 'price'])
```
---
**3. values()**
```python
data = {"name": "Laptop", "price": 999.99}
values = data.values()
print(values)  # Output: dict_values(['Laptop', 999.99])
```
**4. items()**
```python
data = {"name": "Laptop", "price": 999.99}
for key, value in data.items():
    print(f"{key}: {value}")
# Output:
# name: Laptop
# price: 999.99
```
---
## Class Activity
Complete these [List Exercise](https://www.w3schools.com/python/exercise.asp?x=xrcise_lists_comprehension1) and [Dictionary Exercise](https://www.w3schools.com/python/exercise.asp?x=xrcise_dictionaries_nested1)!

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [Common Python Data Structures (Guide)](https://realpython.com/python-data-structures/)
- [Python Stacks, Queues, and Priority Queues in Practice](https://realpython.com/queue-in-python/)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [Python Stacks, Queues, and Priority Queues in Practice](https://realpython.com/queue-in-python/)

---
## Homework Assignment
Complete this [Data Structure Challenges](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-basic-data-types) to enhance your understanding.

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

