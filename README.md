# COVID-19-EDA

## Overview

This project focuses on the Exploratory Data Analysis (EDA) of COVID-19 datasets, providing insights into the global impact of the pandemic. Three datasets have been utilized for in-depth analysis:

1. **Day-wise Analysis (Dataset 1):**
   - Analyzing COVID-19 statistics on a daily basis from January 22, 2022, to July 27, 2022.
   - Metrics include the number of active cases, recovered cases, death cases, confirmed cases, and the count of countries affected each day.

2. **Country-wise Analysis (Dataset 2):**
   - Country-specific data for confirmed cases, active cases, recovered cases, and death cases.
   - This dataset allows for a detailed examination of the COVID-19 situation in individual countries.

3. **Worldwide Analysis (Dataset 3):**
   - Aggregated data for all countries affected by COVID-19, including total population, confirmed cases, active cases, recovered cases, death cases, and total tests conducted.


## Code Structure

The project code is organized into one Jupyter notebooks for each dataset, providing a clear and modular structure for analysis.

- `Covid_Analysis.ipynb`

## Dependencies
-Python 3.x
-Jupyter Notebook
-Pandas
-NumPy
-Matplotlib
-Plotly
-Streamlit

## Interactive Dashboard

I have developed an interactive dashboard using Streamlit where all the visualizations from the analysis are accessible in one place. The dashboard enhances the user experience and allows for dynamic exploration of the COVID-19 data.

To run the Streamlit dashboard, execute the following command:

```bash
streamlit run dashboard.py
