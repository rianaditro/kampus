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

## Dynamic Web Scraping: Implementing Arguments
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
 Enhance your web scraping projects by utilizing arguments to make your scripts more dynamic and flexible. By allowing users to input various parameters at runtime, we can create more robust scrapers that adapt to different websites and data requirements, saving both time and effort.

```python
import argparse
```

---
## Introduction to argparse
The argparse module provides a simple and effective way to parse command-line arguments. This module allows developers to define expected arguments, provide help messages, and validate user inputs seamlessly.

---
**Simple argparse**
```python
import argparse

# Initialize the argument parser
parser = argparse.ArgumentParser(description="A simple argument parser example.")
parser.add_argument('-n', '--name', required=True, help='Your name')
parser.add_argument('-a', '--age', type=int, help='Your age', required=True)
parser.add_argument('-g', '--greeting', default='Hello', help='default: Hello')

args = parser.parse_args() # Parse the arguments

# Access the arguments
name = args.name
age = args.age
greeting = args.greeting

# Simple output using the provided arguments
print(f"{greeting}, {name}! You are {age} years old.")
```
---
**Execute**
`python greet.py -n "John Doe" -a 30 -g "Hi"`

---
## Web Scraping using argparse
**scraper function**
```python
def scrape(url, output_file):
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title of the page
        title = soup.title.string if soup.title else 'No title found'

        # Write the title to the output file
        with open(output_file, 'w') as file:
            file.write(title)
        
        print(f"Scraped title: '{title}' has been saved to '{output_file}'")
```
---
**argparse Implementation**
```python
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="A simple web scraper.")
    parser.add_argument("url", type=str, help="The URL of the web page to scrape")
    parser.add_argument("output_file", type=str, help="The file to save the scraped title")

    # Parse the arguments
    args = parser.parse_args()

    # Call the scrape function with the provided arguments
    scrape(args.url, args.output_file)

if __name__ == "__main__":
    main()
```
---
## Class Activity
Improve this code based on your customization!

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [url title](url)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [url title](url)

---
## Homework Assignment
any
`Optional` 

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

