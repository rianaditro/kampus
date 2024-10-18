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

# Hidden API
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
Data scraping involves extracting information from websites or web applications. While some websites provide public APIs for easy data access, others may not. However, many web applications still rely on APIs behind the scenes to fetch data dynamically.

---
## What is a Hidden API?
A hidden API is a backend service that a website uses to fetch data dynamically. Unlike publicly documented APIs, these are not directly advertised or designed for third-party use. However, with the right tools, we can intercept and use these APIs to scrape data in a structured format, such as JSON or XML, rather than scraping the raw HTML from the website.


---
## Identify Hidden APIs
**Step 1: Monitor Network Activity**
1. Open your browser (Chrome/Firefox).
2. Right-click on the page and select **Inspect**.
3. Navigate to the **Network** tab.
4. Perform an action on the page (e.g., search for an item or load a list).
5. Look at the requests made under the **Network** tab.

---
## Identify Hidden APIs
**Step 2: Identify the API Calls**
1. Examine the URLs listed in the **Name** section of the Network tab.
2. Look for patterns like `/api/`, `.json`, `.xml`, or query parameters that suggest the request is fetching data.
3. Click on the request to inspect the **Response** and **Headers** tabs to see the data returned by the API.

---
## Identify Hidden APIs
**Step 3: Reconstruct the API Call**
1. Right-click on the network request and select **Copy as cURL**. This gives you the command to replicate the request using `cURL`.
2. Convert this request into Python using the `requests` library.

---
## Task
https://www.sunglasshut.com/us/mens-sunglasses
https://www.beerwulf.com/en-gb/c/sub-kegs
https://faskes.bpjs-kesehatan.go.id/

**Challenge**

---
## Learn More
Always Check for the Hidden API when Web Scraping
https://www.youtube.com/watch?v=DqtlR0y0suo

I Don't Waste Time Parsing HTML (So I do THIS)
https://www.youtube.com/watch?v=FPSyjJdudHU

Automate Table Extraction with BeautifulSoup, Pandas, and API Extraction
https://medium.com/@rianaditro/scraping-table-for-any-sites-with-bs4-pandas-and-api-extraction-ddd85e67f490

---
## Discover Advanced Topic
How to use Postman in your API projects.
https://learning.postman.com/docs/introduction/overview/

Leveraging GraphQL API Over Web Scraping: A Backend Approach
https://dev.to/ranggakd/leveraging-graphql-api-over-web-scraping-a-backend-approach-14km

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

