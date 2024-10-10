# Python Data Scraping Materials

Welcome to the **Python Data Scraping Materials** repository! This repository is dedicated to providing structured Python examples and materials that will guide you through learning data scraping techniques. Whether you're a beginner or an experienced developer looking to expand your scraping skills, you'll find valuable content here.

## Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [How to Use](#how-to-use)
4. [Content Overview](#content-overview)
    - [Basic](#basic)
    - [Intermediate](#intermediate)
    - [Advanced](#advanced)
5. [Contribution Guidelines](#contribution-guidelines)
6. [License](#license)

## Overview
This repository contains various Python scripts aimed at teaching you different techniques for **web scraping**. The goal is to cover everything from basic HTML scraping to advanced methods, such as handling dynamic content, managing cookies, and bypassing scraping restrictions.

Web scraping is a technique for extracting data from websites by using scripts to automate the process. It is widely used for data collection in research, business analysis, and many other fields.

## Requirements
To run the Python scripts provided in this repository, you will need the following:
- Python 3.10 or later
- The list of python package in the requirements.txt
You can install these dependencies by running the following command:
```bash
pip install -r requirements.txt
```

## How to Use
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/data-scraping-materials.git
   ```
2. **Navigate to the Directory**:
   ```bash
   cd data-scraping-materials
   ```
3. **Run the Python Files**:
   Each Python file contains code for different scraping techniques. You can run any script directly:
   ```bash
   python filename.py
   ```
   Replace `filename.py` with the Python file you want to execute.

4. **Follow the Instructions**: Each Python script contains comments and instructions to help you understand the technique being demonstrated. 

## Content Overview
The repository is structured to cover various aspects of data scraping. Below is an overview of the content:

### Basic
- **Requests**: Send requests till get blocked.
  - Relevant File: [`beginner-intro-requests.py`](./basics/beginner-intro-requests.py)

### Intermediate
- **Speed Up Scraping**: Comparing Threading, Connection pooling, and asynchronous in time consumed.
  - Relevant File: [`speed-up-scraping-method.py`](./intermediate/speed-up-scraping-method.py)
  
- **Regex**: Regex daily tasks
  - Relevant File: [`intermediate-regex.py`](./intermediate/intermediate-regex.py)

### Advanced
- **FastAPI**: Simple fastapi for scraping.
  - Relevant File: [`advanced-fastapi.py`](./advanced/advanced-fastapi.py)

- **Asynchronous**: Deep understand on asyncio.
  - Relevant File: [`learn-asyncio.py`](./advanced/learn-asyncio.py)

## Contribution Guidelines
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
- Add your content in the folder base on its level (basic, intermediate, advanced)
- Update the file reference on the README.md file and add description.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Create a Pull Request.

## License
This project is licensed under the MIT License. Feel free to use and modify the materials as needed.
