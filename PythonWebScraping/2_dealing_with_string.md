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

# Dealing with Strings
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
When working on data scraping tasks, string manipulation is crucial for cleaning and processing the extracted data.

```python
print("We are learning Python string!")
```

---
## Common String Operations
**1. f-strings**
```python
product = "Laptop"
price = 999.99
text = f"Product: {product}, Price: ${"${price}"}"
print(text)  # Output: "Product: Laptop, Price: $999.99"
```
**2. lower() / upper()**
```python
text = "Product Name"
normalized_text = text.lower()  # Convert to lowercase
print(normalized_text)  # Output: "product name"
```
---
**3. strip()**
```python
text = "  Product Name  "
cleaned_text = text.strip()  # Removes leading and trailing spaces
print(cleaned_text)  # Output: "Product Name"
```
**4. join()**
```python
words = ["Product", "Name"]
full_text = " ".join(words)  # Join with space
print(full_text)  # Output: "Product Name"
```
---
**5. split()**
```python
text = "Price: $20.99"
parts = text.split(": ")  # Split by ": "
print(parts[1])  # Output: "$20.99"
```
**6. replace()**
```python
text = "$20.99"
cleaned_text = text.replace("$", "")  # Remove dollar sign
print(cleaned_text)  # Output: "20.99"
```
---
## Class Activity
```python
message = "   Hello, world! How, are you today? "
print(message)
```
Manipulate the current message to get the output `hello-world!-how;-are-you-today?`

`Additional` Finish this [String Exercise](https://www.w3schools.com/python/exercise.asp?x=xrcise_strings_modify1)!

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [Strings and Character Data in Python](https://realpython.com/python-strings)
- [Python - String Methods](https://www.w3schools.com/python/python_strings_methods.asp)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [Learn Regex: A Beginner’s Guide](https://www.sitepoint.com/learn-regex/)

---
## Homework Assignment
```python
"""
    John Doe can be contacted via 
    email at john.doe@example.com or 
    call him at 8000-1234-4567
"""
```
From this text, extract name, email, phone number in the dictionary.

`Optional` Try to solve one or more [Strings Challenges](https://www.hackerrank.com/domains/python/py-strings/difficulty/2).

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

