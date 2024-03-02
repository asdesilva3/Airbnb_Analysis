# Airbnb Analysis Project

## Table of Contents
- [Overview](#overview)
- [Domain](#domain)
- [Objectives](#objectives)
- [Data](#data)
- [Workflow](#workflow)
- [Approach](#approach)
- [Technologies Used](#technologies-used)

## Overview
This project aims to analyze Airbnb data from MongoDB Atlas, perform Exploratory Data Analysis (EDA), develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.

## Domain
Travel industry, property management, and tourism.

## Objectives
1. **Establish a MongoDB connection**, retrieve the Airbnb dataset, and ensure efficient data retrieval for analysis.
2. **Clean and prepare** the dataset, addressing missing values, duplicates, and data type conversions for accurate analysis.
3. **Develop a Streamlit web application** with interactive maps showcasing the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.
4. **Conduct price analysis and visualization**, exploring variations based on location, property type, and seasons using dynamic plots and charts.
5. **Analyze availability patterns** across seasons, visualizing occupancy rates and demand fluctuations using suitable visualizations.
6. **Investigate location-based insights** by extracting and visualizing data for specific regions or neighborhoods.
7. **Create interactive visualizations** that enable users to filter and drill down into the data.

## Data
- MongoDB Atlas is used as the database environment.
- [Sample data](https://www.mongodb.com/docs/atlas/sample-data/sample-airbnb/) includes collections for listings, reviews, and users.

## Workflow

![Airbnb - Workflow](https://github.com/asdesilva3/Airbnb_Analysis/assets/148002331/8d76208d-8980-447c-b4ae-3de2b5b20ccb)


## Approach

1. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Exploratory Data Analysis (EDA)**:
    - Explore data distributions, summary statistics, and data quality issues.
    - Identify correlations between variables.
    - Visualize data using histograms, scatter plots, correlation matrices, etc.
    - Detect outliers and anomalies.

    **i) Data Collection**

    MongoDB Connection and Data Retrieval: Establish a connection to the MongoDB Atlas database and retrieve the Airbnb dataset.

    ```python
    import pymongo
    
    # Add your MongoDB connection string
    client = pymongo.MongoClient("your_connection_string_here")
    
    # Access the database and collection
    db = client["sample_airbnb"]
    data = db["listingsAndReviews"]
    ```

    **ii) Data Cleaning**

    Clean the dataset by handling missing values, removing duplicates, and transforming data types.

    **iii) Statistics Summary**

    The information gives a quick and simple description of the data

    **iv) Categorical Analysis**

    When both the variables contain categorical data, we perform categorical analysis.

3. **Interactive Visualizations**:

    Develop a Streamlit web application with interactive maps showcasing the distribution of listings.

    - **Price Analysis and Visualization**: Analyze and visualize price variations across different locations, property types, and seasons.
    - **Location-Based Insights**: Investigate how prices vary across different locations.
    - **Interactive Visualizations**: Develop dynamic and interactive visualizations for user exploration.

## Technologies Used
- Python
- MongoDB Atlas
- PyMongo
- Pandas
- Streamlit
- Matplotlib
- Seaborn
- Plotly
