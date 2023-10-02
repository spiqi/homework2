#!/usr/bin/env python
# coding: utf-8

# # Working with Data Lab 2
# 
# ## Introduction
# The lab is designed to be self-guided, providing solutions for each exercise to check your work and assist if you get stuck. However, it is important to first attempt to solve the problem on your own as this is the best way to learn. If you become stuck, don't give up and seek help from the instructor, peers, or even a search engine like Google. Be mindful that not all answers from a search engine may be correct, so use your judgement to determine the validity of the information. Remember, the best way to learn is to try solving the problem yourself first.
# 
# ### Learning Objectives
# This lab will introduce you to the basics of working with data in Python. You will learn:
# - how to secure your Database and API keys and secrets using environment variables
# - how to read data from a hosted SQL Database
# - how to read data from a an API
# - how to read data from a MongoDB database
# - how to perform web scraping to extract data from a website
# 
# ## Setup
# * 🚨 These may take a few minutes so get started with this as you settle in.
#   * Request an API Key from the Census Bureau.You can do this by going to the following link: https://api.census.gov/data/key_signup.html
#   * Create an account on RapidAPI. You can do this by going to the following link: https://rapidapi.com/
# * Install this lab's dependencies by running the following command in your terminal:
#   ```bash
#   pipenv install
#   ```
# * Make sure you switch to the correct environment by choosing the correct kernel in the top right corner of the notebook.
#   * Note: the name for this lab is very similar to the previous lab, so make sure you select the correct one.

# #### Package Imports
# We will keep coming back to this cell to add "import" statements, and configure libraries as we need

# In[ ]:


import os
from dotenv import load_dotenv


import pandas as pd
import numpy as np

from urllib.request import urlretrieve
from sqlalchemy import create_engine, text
from pymongo import MongoClient

import requests
from bs4 import BeautifulSoup

# Configure pandas to display 500 rows; otherwise it will truncate the output
pd.set_option('display.max_rows', 500)

# Load the project environment variables
load_dotenv(override=True)


# ## Part 1: Getting Data from a Hosted SQL Database (PostgreSQL)
# Get data from hosted PostgreSQL database using `psycopg2` driver and `pandas` library.
# 
# For that we need to install a driver for PostgreSQL that SQLAlchemy will use behind the scenes to interface with Postgres. We will use the `psycopg2` driver.
# and `psycopg2-binary` is a version of the driver that is already compiled and ready to use and has already been installed for you.
# 
# >🦉 **Note:** Each SQL dialect has its own driver, and we will be using the `psycopg2` driver for PostgreSQL.

# ### Exercise 1:  Connect to the database
# In the previous lab, you interacted with with a local SQLite database. 
# This time the database is hosted on a server and can be accessed using a URL.
# This time, you'll need to create the database connection yourself. (Refer to the previous lab for help.)
# 
# <details>
#   <summary>Connection information</summary>
# 
#   * Postgres database connections strings format: `postgres://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME`
#   * host: `it4063C.cech.uc.edu`
#   * port: `5432`
#   * database name: `demo`
#   * username: `student`
#   * and password: `student123`
# </details>

# In[ ]:


# create engine has already been imported above
# from sqlalchemy import create_engine


# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   connection_string = 'postgresql://student:student123@it4063c.cech.uc.edu:5432/demo'
#   engine = create_engine(connection_string)
# 
#   db_connection = engine.connect()
#   ```
# </details>
# 

# ### Exercise 2: Get Artist Data 
# using a similar query to the previous lab, get the artist data from the database.
# 
# <details>
#   <summary>Hints</summary>
# 
#   * The psycopg2 driver requires that your query be wrapped in sqlAlchemy's `text()` function.
#     * `query = text("SELECT * FROM my_table")`
# 
# </details>
# 
# <details>
#   <summary>🗺️ Database Diagram</summary>
# 
#   ![Chinook Database Diagram](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)
# </details>
# 

# In[ ]:


# Write your query here
sql = text("""
  
""")
# Pass your query to pandas


# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   sql = text('SELECT * FROM "Artist"')
#   artist_df = pd.read_sql_query(sql=sql, con=db_connection)
# 
#   artist_df
#   ```
# </details>

# ### Exercise 3: Genre with most tracks
# - Write a query showing how many tracks does each genre have.
# - Read the results into a pandas DataFrame called `genre_track_count_df`.
# 
# <details>
#   <summary>Hints</summary>
# 
#   * For some reason, the column names need to be wrapped in double quotes.
# </details>
# <details>
#   <summary>🗺️ Database Diagram</summary>
# 
#   ![Chinook Database Diagram](https://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)
# </details>
# 

# In[ ]:





# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   sql = text('SELECT * FROM "Artist"')
#   artist_df = pd.read_sql_query(sql=sql, con=db_connection)
# 
#   artist_df
#   ```
# </details>

# > 🚩 This is a good point to commit your code to your repository.

# ### 1 Extra Credit: 
# Sort the `genre_track_count_df` showing the genres with the most tracks first

# In[ ]:





# > 🚩 This is a good point to commit your code to your repository.

# ## Part 2: Protecting your Secrets
# In the previous exercise, you had to connect to the database using a connection string.
# This connection string contained the username and password for the database.
# This is a security risk, as anyone with access to the code can see the username and password.
# To protect your secrets, you can use environment variables.
# 
#  **(Not this again 😱)**
# 
# Environment variables are variables that are set in your operating system and are available to all programs running on your computer.
# You can set environment variables in your terminal using the `export` command.
# For example, to set the `MY_SECRET` environment variable to `12345`, you would run the following command in your terminal:
# ```bash
# export MY_SECRET=12345
# ```
# You can then access the value of the `MY_SECRET` environment variable in your code using the `os.environ` dictionary, or using the `os.getenv()` function.
# 
# ```python
# import os
# 
# the_secret = os.getenv('MY_SECRET')
# ```
# 
# But do we really want to modify our computer's environment variable with every project we work on?
# 
# No, that would be a pain.
# 
# Instead, we can use a `.env` file to store our environment variables. and we'll use a library called `python-dotenv` to load the environment variables from the `.env` file.
# 
# Because this file contains sensitive information, it should not be committed to your repository. (look at the `.gitignore` file in this repository to see how we are ignoring the `.env` file)
# 
# - Create a File called `.env` in the root of this repository.
# Copy the following snippet into the file, and change the values to your own username and password.
# 
# ```
# SQL_USERNAME=your_sql_user
# SQL_PASSWORD=your_sql_password
# ```

# In[ ]:


load_dotenv(override=True) # Ideally this should be done in the top cell

# Get the secrets from the environment variables
sql_host = os.getenv('SQL_HOST')
sql_username = os.getenv('SQL_USERNAME')
sql_password = os.getenv('SQL_PASSWORD')

connection_string = f'postgresql://{sql_username}:{sql_password}@{sql_host}:5432/demo'
print(connection_string)


# > 🦉 **Note:** The `.env` file is a special file that is not loaded by default. You need to use the `python-dotenv` library to load the environment variables from the `.env` file.
# 
# > 🔐: From this point forward, you should never have any sensitive information in your code. If you do, you will be fired.

# ## Part 3: Getting Data from a mongoDB Database
# MongoDB is a NoSQL database that stores data in JSON-like documents. It is a popular choice for storing data that is unstructured or semi-structured. It is also a popular choice for storing data that is not relational in nature.
# 
# Get data from hosted mongoDB database using `pymongo` driver and `pandas` library.
# 
# ### Exercise 1:
# Connect to the database and get the reviews data
# 1. Create a `MongoClient` object and connect to the database.
#    * You will need to install the `pymongo` package. (done)
#    * We'll be using the `MongoClient` class from the `pymongo` library to connect to the database.
# 2. Read the data from the `listingsAndReviews` collection in the `sample_airbnb` database. into a pandas DataFrame.
# 
# 
# <details>
#   <summary>Connection information</summary>
# 
#   * mongo_uri: `mongodb+srv://USERNAME:PASSWORD@HOST/?retryWrites=true&w=majority"`
#   * Use the following information to update the `.env` file
#     * host: `cluster0.9u8bdoy.mongodb.net`
#     * username: `<provided in class>`
#     * password: `<provided in class>`
# </details>

# In[ ]:


# import os
# from dotenv import load_dotenv
# from pymongo import MongoClient

load_dotenv(override=True) # Ideally this should be done in the top cell

mongo_host= 'cluster0.9u8bdoy.mongodb.net'
mongo_user = 
mongo_password = 

# The following database is hosted on MongoDB Atlas and the connection string was provided by the platform
mongo_connection_string=f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_host}/?retryWrites=true&w=majority"

mongo_client = 
mongo_db = 
mongo_collection = 

reviews_df = pd.DataFrame()

reviews_df.head()


# Notice that the data is not in a tabular format. It is in a JSON-like format. This is because MongoDB is a NoSQL database. It stores data in JSON-like documents.

# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   mongo_host= 'cluster0.9u8bdoy.mongodb.net'
#   mongo_user = os.getenv('MONGO_USERNAME')
#   mongo_password = os.getenv('MONGO_PASSWORD')
# 
#   # The following database is hosted on MongoDB Atlas and the connection string was provided by the platform
#   mongo_connection_string=f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_host}/?retryWrites=true&w=majority"
# 
#   mongo_client = MongoClient(mongo_connection_string)
#   mongo_db = mongo_client['sample_airbnb']
#   mongo_collection = mongo_db['listingsAndReviews']
# 
#   reviews_df = pd.DataFrame(mongo_collection.find())
# 
#   reviews_df.head()
#   ```
# </details>

# ### Exercise 2
# 
# Get the reviews for listings that has less than 3 bedrooms

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   query = {'bedrooms': {'$lt': 3}}
#   reviews_df = pd.DataFrame(mongo_collection.find(query))
#   ```
# </details>

# > 🚩 This is a good point to commit your code to your repository.

# ## Part 4: Getting Data using Web Scraping

# ### Exercise 1
# In this exercise, we'll be pulling the tabular data on this wikipedia page: https://en.wikipedia.org/wiki/Wealth_distribution_by_country
# 
# <details>
#   <summary>Hints</summary>
#   
#   * We'll use the `requests` library to get the HTML from the page.
#   * We'll use the `BeautifulSoup` library to parse the HTML and find the table we want.
#   * We'll use the `pandas` library (specifically the `read_html` function) to read the HTML table into a DataFrame.
#   * We'll use the `BeautifulSoup` library to find the table we want.
#   * You can use the [📜`read_table()` function](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html) to read a file into a DataFrame.
#   * There may be multiple tables on the page, so you'll need to find the one you want
#     * or get them all and merge them together
# </details>

# In[ ]:


from IPython.display import IFrame

IFrame("https://en.wikipedia.org/wiki/Wealth_distribution_by_country", width=800, height=400)


# #### Step 1: Get the HTML from the page and parse it using BeautifulSoup

# In[ ]:


# import requests
# from bs4 import BeautifulSoup


# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   url = 'https://en.wikipedia.org/wiki/Wealth_distribution_by_country'
#   page = requests.get(url)
# 
#   soup = BeautifulSoup(page.content,'html.parser')
#   ```
# </details>

# #### Step 2: Find the all the HTML elements that we want (i.e. table(s))

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   tables = soup.find_all('table')
# 
#   wealth_df = pd.read_html(str(tables[0]))[0]
#   wealth_df.head()
#   ```
# </details>

# #### Step 3: Filter out the rows/columns that we don't want 
# in this case the last 2 rows, 
# > make sure you save the new filtered DataFrame to the same variable name.

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   wealth_df = wealth_df[:-2]
#   wealth_df
#   ```
# </details>

# Remember: there are multiple tables on that webpage that contains the same information for the different continents. 
# 
# We want all the data from all the tables.
# 
# #### Step 4: get the data from all the tables and merge them together (programmatically)

# In[ ]:





# <details>
#   <summary>💡 Solution</summary>
# 
#   ```python
#   for i in range(1, len(tables)):
#     wealth_df = pd.concat([wealth_df, pd.read_html(str(tables[i]))[0]], ignore_index=True)
#     wealth_df = wealth_df[:-2]
# 
#   wealth_df.head()
#   ```
# </details>

# > 🚩 This is a good point to commit your code to your repository.

# ## Part 5: Getting Data from an API
# API stands for Application Programming Interface. It is a way for two applications to communicate with each other.
# Generally, those APIs will be protected by some sort of authentication.
# 
# We'll practice using APIs with 2 different APIs:
# - [Rapid API - COVID-19 Data](https://rapidapi.com/axisbits-axisbits-default/api/covid-19-statistics/)
# - [Census Bureau API](https://www.census.gov/data/developers.html)
# 
# <details>
#   <summary>Hopefully, you've already done this</summary>
# 
#   Both of these APIs require that you register with them and get an API key before you can use them.
#   - [Rapid API - COVID-19 Data](https://rapidapi.com/axisbits-axisbits-default/api/covid-19-statistics/)
#     - Sign up, create an app, and get an API key here: https://rapidapi.com/
#   - [Census Bureau API](https://www.census.gov/data/developers.html)
#     - Sign up for an API key here: https://api.census.gov/data/key_signup.html
# </details>

# ### Part 5.1: Covid-19 Data API
# #### Exercise 1: COVID-19 Data
# Using the COVID-19 Data API, get the data for the City of Cincinnati, OH. and store it in a Pandas DataFrame.
# Use the `/reports` endpoint.
# 
# * Add your `RAPID_API_KEY` to the `.env` file.
# 

# In[ ]:





# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   # import os
#   # from dotenv import load_dotenv
#   # import requests
#   load_dotenv(override=True) # Ideally this should be done in the top cell
# 
#   rapid_api_key = os.getenv("RAPID_API_KEY")
# 
#   url = "https://covid-19-statistics.p.rapidapi.com/reports"
#   request_params = {
#     "iso":"USA",
#     "region_name":"US",
#     "region_province":"Ohio",
#     "q":"US Ohio",
#     "date":"2020-04-16"
#   }
# 
#   headers = {
#     "X-RapidAPI-Key": rapid_api_key,
#     "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
#   }
# 
#   response = requests.request("GET", url, headers=headers, params=request_params)
#   # OR
#   # response = requests.get(url, headers=headers, params=request_params)
# 
#   # save json result into a pandas dataframe
#   covid_data = pd.DataFrame(response.json()["data"][0]["region"]["cities"])
#   covid_data.head()
#   ```
# </details>

# > 🚩 This is a good point to commit your code to your repository.

# ### Exercise 2: US Census Data
# From a technical perspective, this exercise is very similar to the previous one.
# The only differences are in how the API is structured and documented, and how the data is returned.
# 
# * Add your `CENSUS_API_KEY` to the `.env` file.
# * Query the "Small Area Income and Poverty Estimates: Small Area Income and Poverty Estimates: State and County" and get the state of Ohio's counties.
# * For each row, get the following columns:
#   * The County Name
#   * The Median Household Income Estimate
#   * The Count estimate for the number of people in poverty of all ages
#   * How many kids ages 0-17 live with families in poverty
# 
# 
# **Links:**
# * [All Census Data](https://api.census.gov/data.html)
# * [Our Dataset's Variables](https://api.census.gov/data/timeseries/poverty/saipe/variables.html)
# * [Examples for querying our dataset](https://api.census.gov/data/timeseries/poverty/saipe/examples.html)

# In[ ]:





# <details>
#   <summary>💡 Solution </summary>
#   
#   ```python
#   load_dotenv(override=True) # Ideally this should only be done in the top cell
# 
#   host='https://api.census.gov/data'
#   dataset='timeseries/poverty/saipe'
#   census_api_key = os.getenv("CENSUS_API_KEY")
# 
#   url=f"{host}/{dataset}"
# 
#   dataset_variables = ["NAME", "SAEMHI_PT", "SAEPOVALL_PT", "SAEPOV5_17R_PT"]
# 
#   request_params = {
#     "get": ",".join(dataset_variables),
#     "for": "county:*",
#     "in": "state:39",
#     "time": "2021",
#     "key": census_api_key
#   }
# 
#   response = requests.get(url, params=request_params)
# 
#   census_data = pd.DataFrame.from_records(response.json()[1:], columns=response.json()[0])
# 
#   census_data.head(5)
#   ```
# </details>
# 
# <details>
#   <summary>💡 How I got the state of Ohio's Code </summary>
#   
#   ```python
#   load_dotenv(override=True) # Ideally this should only be done in the top cell
# 
#   host='https://api.census.gov/data'
#   dataset='timeseries/poverty/saipe'
#   census_api_key = os.getenv("CENSUS_API_KEY")
# 
#   url=f"{host}/{dataset}"
# 
#   dataset_variables = ["NAME"]
# 
#   request_params = {
#     "get": ",".join(dataset_variables),
#     "for": "state:*",
#     "time": "2021",
#     "key": census_api_key
#   }
# 
#   response = requests.get(url, params=request_params)
# 
#   census_data = pd.DataFrame.from_records(response.json()[1:], columns=response.json()[0])
# 
#   census_data.head(5)
#   ```
# </details>

# ## 2 Extra Credit
# * Get the data for the county with the highest poverty count in Ohio
# * Get the data for the county with the highest median household income in Ohio
# 
# <details>
#   <summary>Hints </summary>
#   * You need to convert the values in the columns to integers before you can sort them
# </details>

# In[ ]:





# > 🚩 This is a good point to commit your code to your repository.

# ## Wrap up
# Remember to update the self reflection and self evaluations on the `README` file.

# Make sure you run the following cell; this converts this Jupyter notebook to a Python script. and will make the process of reviewing your code on GitHub easier

# In[ ]:


# 🦉: The following command converts this Jupyter notebook to a Python script.
get_ipython().system('jupyter nbconvert --to python notebook.ipynb')


# > 🚩 This is a good point to commit your code to your repository.
