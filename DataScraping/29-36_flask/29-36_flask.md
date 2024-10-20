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

# Flask - A Lightweight Web Framework
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
Now it’s time to take your skills to the next level. While we’re moving beyond just data scraping, these advanced skills are crucial for your growth as a data scraper. 

Web development is a key complementary skill—it enables you to **present your data in an interactive and engaging way**. After all, you don’t want to deliver your data in plain CSV files forever, right? With web development, you can turn your scraped data into something your audience can truly engage with.

---
## Advanced Python Web Development Framework
1. FastAPI: Building fast and efficient APIs
2. Streamlit: Creating data-driven web apps for data science
3. Django: Building full-featured, scalable web applications
4. Flask: Creating lightweight web applications with flexibility

---
## What is Flask?
Flask is a lightweight web framework for Python that allows you to create web applications easily. It’s called "lightweight" because it gives you only the essential tools to start building a web app, allowing you to decide what additional components you need as your app grows.

You can think of Flask as a basic toolbox. It doesn't come with every tool you might need, but it gives you the most important ones to start building things fast.

---
## A Minimal Application
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
<!-- If the Flask app is defined in app.py, then __name__ will be set to "app". -->
run it by:
`flask --app your_file_name run`
As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app.

---
## Task
1. Add a new route of your own!
2. What happens when you have same function name for different route?
3. What happens when you have same route? Which one is executed?
4. What happens when you return a plain string or a number? Explore with another data types too!
5. Can you run your flask web app in debug mode?
6. Can you run your flask web app from another file?

---
## Routing
**Dynamic Routing**
```python

@app.route("/user/<username>")  # <username> is a dynamic part of the URL
def show_user_profile(username):
    return f"User: {username}"

```

---
When returning HTML (the default response type in Flask), any user-provided values rendered in the output must be escaped to protect from **injection attacks.**
```python
from markupsafe import escape

@app.route("/user/<username>")  # <username> is a dynamic part of the URL
def show_user_profile(username):
    return f"User: {escape(username)}"
```
If a user managed to submit the name `<script>alert("bad")</script>`, escaping causes it to be rendered as text, rather than running the script in the user’s browser.

---
**Using url_for() to Build URLs**
```python
from flask import url_for

@app.route("/profile/<username>")
def profile(username):
    return f"Profile page of {username}"

@app.route("/")
def index():
    # Generate a URL to the 'profile' view function dynamically
    return f'<a href="{url_for("profile", username="Hafizan")}">Go to Hafizan\'s Profile</a>'

```

---
**Query String Parameters**
```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get('query')  # Get 'query' parameter from the URL
    return f"Search results for: {query}"
```
Try http://127.0.0.1:5000/search?query= + your keyword

---
## Task
**Build a simple product catalog web app.**
Create a homepage that displays product names as clickable links. When clicked, it should display the product details in JSON / dictonary. Add search url to search by its category. 

**Challenge**
Set the parameter to accept ID as an integer not string. Add a redirect url if the product is out of list.

---
## Rendering Templates
Flask’s template rendering feature allows you to separate your HTML structure from your Python logic, making your code cleaner and easier to maintain.

Now, lets re-use your dummy data to render them into our HTML file.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", products=products)
```

---
Our index.html will be:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product List</title>
</head>
<body>
    <h1>Products</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

---
## Task
"You've successfully displayed your product list using an `<ul>` in HTML. Now, try converting it into a table! Add some basic CSS to enhance its appearance!"

---
## Learn More
Jinja2 template engine
https://jinja.palletsprojects.com/en/3.1.x/templates/#html-escaping

---
## Static Files
Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from.

Now, let's separate the CSS into `static/style.css` then in the HTML file add reference to it
```HTML
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---
## Rendering (extended) Templates
 Extending layouts is a powerful feature in Flask using Jinja2's template inheritance. This allows you to create a base layout (like a common structure for your website) and extend it in other templates. It helps in keeping your HTML code DRY (Don't Repeat Yourself) by reusing common elements like headers, footers, and navigation across multiple pages.

---
The base HTML
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Web App{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="/">Home</a> | 
        <a href="/products">Products</a> | 
        <a href="/about">About</a>
    </nav>

    <div class="content">
        {% block content %}{% endblock %}
    </div>

    <footer>
        <p>&copy; 2024 My Web App</p>
    </footer>
</body>
</html>
```

---
The child HTML
```HTML
{% extends "base.html" %}

{% block title %}Product List{% endblock %}

{% block content %}
    <h1>Product List</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Price ($)</th>
            </tr>
        </thead>
        <tbody>
            {% for product in products %}
                <tr>
                    <td>{{ product.id }}</td>
                    <td>{{ product.name }}</td>
                    <td>{{ product.price }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

---
Another child HTML
```HTML
{% extends "base.html" %}

{% block title %}About Us{% endblock %}

{% block content %}
    <h1>About Us</h1>
    <p>Welcome to My Web App! We sell a variety of products ranging from electronics to clothing.</p>
{% endblock %}
```

This child still haven't connected to any route. Let's add one.

```python
@app.route("/about")
def about():
    return render_template("about.html")
```

---
## Task
Let's create a product page using extended template. You can improve your last task using this method to return a real HTML page instead of JSON data.

---
## Task

---
## Task

---
## Task

---
## Task

---
## Task
Check your code using flake8, how many improvement suggestion you have?

---
## Learn More
PEP 8 – Style Guide for Python Code
https://peps.python.org/pep-0008/

Automate Code Testing
https://medium.com/python-in-plain-english/efficient-django-testing-implementing-github-actions-for-automation-on-youngfounder-id-530833756336

---
## Discover Advanced Topic
Publishing Python Program to PyPI using Poetry
https://medium.com/@rianaditro/publishing-python-program-to-pypi-using-poetry-eb4685a73044

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

