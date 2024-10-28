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

# Scraping Hidden APIs
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

```python
isinstance(".../api...", HiddenAPI)
```

---
## Identify Hidden APIs
**Step 1: Monitor Network Activity**
1. Open your browser (Chrome/Firefox).
2. Right-click on the page and select **Inspect**.
3. Navigate to the **Network** tab.
4. Perform an action on the page (e.g., search for an item or load a list).
5. Look at the requests made under the **Network** tab.
---
**Step 2: Reconstruct the API Call**
1. Examine the URLs listed in the **Name** section of the Network tab.
2. Look for patterns like `/api/`, `.json`, `.xml`, or query parameters that suggest the request is fetching data.
3. Click on the request to inspect the **Response** and **Headers** tabs to see the data returned by the API.
4. Right-click on the network request and select **Copy as cURL**. This gives you the command to replicate the request using `cURL`.
5. Convert this request into Python using the `requests` library.
---
## Class Activity
Find the hidden API on https://dtm.com/en/standings and parse it!

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [Always Check for the Hidden API when Web Scraping](https://www.youtube.com/watch?v=DqtlR0y0suo)
- [I Don't Waste Time Parsing HTML (So I do THIS)](https://www.youtube.com/watch?v=FPSyjJdudHU)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [How to use Postman in your API projects.](https://learning.postman.com/docs/introduction/overview/)
- [Leveraging GraphQL API Over Web Scraping: A Backend Approach](https://dev.to/ranggakd/leveraging-graphql-api-over-web-scraping-a-backend-approach-14km)

---
## Homework Assignment
Identify how https://www.beerwulf.com/en-gb/c/sub-kegs send data and parse it!
`Optional` Identify how https://faskes.bpjs-kesehatan.go.id/ send data and parse it!

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

