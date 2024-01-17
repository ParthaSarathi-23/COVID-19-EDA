import numpy as np 
import pandas as pd
import altair as alt 
import streamlit as st
import plotly.express as px
from datetime import date
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

#--------------------------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(layout="wide")

df = pd.read_csv("D:\Project\Covid19_EDA\Covid_19\day_wise.csv")

columns = df.columns

Date = []
Death = []
Active = []
Recovered = []
Confirmed = []
Active_Ratio = []

for i in range(0, len(df), 25):
  Date.append(df.iloc[i]['Date'])
  Confirmed.append(df.iloc[i]['Confirmed'])
  Death.append(df.iloc[i]['Deaths'])
  Recovered.append(df.iloc[i]['Recovered'])
  Active.append(df.iloc[i]['Active'])

for i in range(0, len(df)):
  Active_Ratio.append((df.iloc[i]['Active']/df.iloc[i]['Confirmed'])*100)

#----------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neat Decoration</title>
    <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .decorative-box {
            text-align: center;
            padding: 20px;
            border: 2px solid #3498db;
            border-radius: 10px;
            background-color: #ecf0f1;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #3498db;
        }
    </style>
</head>
<body>
    <div class="decorative-box">
        <h1>Date-Wise Analysis</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

death_ratio = list(df[columns[8]])
recovered_ratio = list(df[columns[9]])

max_death_ratio_date = df.iloc[death_ratio.index(max(death_ratio))][columns[0]]
max_death_ratio_value = max(death_ratio)

# Find the maximum Recovered Ratio and corresponding date
max_recovered_ratio_date = df.iloc[recovered_ratio.index(max(recovered_ratio))][columns[0]]
max_recovered_ratio_value = max(recovered_ratio)

# Calculate Active Ratio
active_ratio = [(df.iloc[i]['Active'] / df.iloc[i]['Confirmed']) * 100 for i in range(len(df))]

# Find the maximum Death Ratio (calculated from Active Ratio) and corresponding date
max_active_ratio_date = df.iloc[active_ratio.index(max(active_ratio))][columns[0]]
max_active_ratio_value = round(max(active_ratio), 2)

# Extract the Country column
countries = list(df[columns[-1]])

# Find the maximum number of countries and the corresponding date
max_countries_date = df.iloc[countries.index(max(countries))][columns[0]]
max_countries_value = max(countries)


# Create a centered table for all information
combined_table_html = f"""
    <table style="margin: auto;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Category</th>
            <th style="font-size: 24px; border: 2px solid white;">Date</th>
            <th style="font-size: 24px; border: 2px solid white;">Value</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Maximum Death Ratio </td>
            <td style="font-size: 20px; border: 2px solid white;">{max_death_ratio_date}</td>
            <td style="font-size: 20px; border: 2px solid white;">{max_death_ratio_value}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Maximum Recovered Ratio</td>
            <td style="font-size: 20px; border: 2px solid white;">{max_recovered_ratio_date}</td>
            <td style="font-size: 20px; border: 2px solid white;">{max_recovered_ratio_value}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Maximum Active Ratio</td>
            <td style="font-size: 20px; border: 2px solid white;">{max_active_ratio_date}</td>
            <td style="font-size: 20px; border: 2px solid white;">{max_active_ratio_value}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Maximum Number of Countries</td>
            <td style="font-size: 20px; border: 2px solid white;">{max_countries_date}</td>
            <td style="font-size: 20px; border: 2px solid white;">{max_countries_value}</td>
        </tr>
    </table>
"""

st.markdown(combined_table_html, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neat Decoration</title>
    <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .decorative-box {
            text-align: center;
            padding: 20px;
            border: 2px solid #3498db;
            border-radius: 10px;
            background-color: #ecf0f1;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #3498db;
        }
    </style>
</head>
<body>
    <div class="decorative-box">
        <h1>Analysis On Death Due to COVID19</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)



fig1 = go.Figure()
fig1.add_trace(go.Bar(x=Date, y=Confirmed, name='Confirmed'))
fig1.add_trace(go.Bar(x=Date, y=Death, name='Deaths'))

fig1.update_layout(
    xaxis=dict(title='Date'),
    yaxis=dict(title='Number of Cases'),
    title='Confirmed VS Deaths',
    barmode='group',
    width=600,
    height=500
)

fig2 = px.line(df, x='Date', y='Deaths / 100 Cases', title='Deaths / 100 Cases Over Time')
fig2.update_layout(xaxis_title='Date', yaxis_title='Deaths / 100 Cases', width=600, height=500)

# Display the figures in the same row
col1, col2 = st.columns(2)
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neat Decoration</title>
    <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .decorative-box {
            text-align: center;
            padding: 20px;
            border: 2px solid #3498db;
            border-radius: 10px;
            background-color: #ecf0f1;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #3498db;
        }
    </style>
</head>
<body>
    <div class="decorative-box">
        <h1>Analysis On Recovery From COVID19</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

fig3 = go.Figure()
fig3.add_trace(go.Bar(x=Date, y=Confirmed, name='Confirmed'))
fig3.add_trace(go.Bar(x=Date, y=Recovered, name='Recovered'))

fig3.update_layout(
    xaxis=dict(title='Date'),
    yaxis=dict(title='Number of Cases'),
    title='Confirmed VS Recovered',
    barmode='group',
    width=600,
    height=500
)

fig4 = px.line(df, x='Date', y='Recovered / 100 Cases', title='Recovered / 100 Cases Over Time')
fig4.update_layout(xaxis_title='Date', yaxis_title='Recovered / 100 Cases', width=600, height=500)

# Display the figures in the same row
col3, col4 = st.columns(2)
col3.plotly_chart(fig3)
col4.plotly_chart(fig4)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neat Decoration</title>
    <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .decorative-box {
            text-align: center;
            padding: 20px;
            border: 2px solid #3498db;
            border-radius: 10px;
            background-color: #ecf0f1;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #3498db;
        }
    </style>
</head>
<body>
    <div class="decorative-box">
        <h1>Analysis On Active Cases of COVID19</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

fig5 = go.Figure()
fig5.add_trace(go.Bar(x=Date, y=Confirmed, name='Confirmed'))
fig5.add_trace(go.Bar(x=Date, y=Active, name='Active'))

fig5.update_layout(
    xaxis=dict(title='Date'),
    yaxis=dict(title='Number of Cases'),
    title='Confirmed VS Avtive',
    barmode='group',
    width=600,
    height=500
)

fig6 = px.line(df, x='Date', y=Active_Ratio, title='Active / 100 Cases Over Time')
fig6.update_layout(xaxis_title='Date', yaxis_title='Active / 100 Cases', width=600, height=500)

# Display the figures in the same row
col5, col6 = st.columns(2)
col5.plotly_chart(fig5)
col6.plotly_chart(fig6)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neat Decoration</title>
    <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .decorative-box {
            text-align: center;
            padding: 20px;
            border: 2px solid #3498db;
            border-radius: 10px;
            background-color: #ecf0f1;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #3498db;
        }
    </style>
</head>
<body>
    <div class="decorative-box">
        <h1>COVID19 Case Veiwer</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

min_date = date(2020, 1, 22)
max_date = date(2020, 7, 27)

# Set a default date within the specified range
default_date = date(2020, 7, 1)

df['Date'] = pd.to_datetime(df['Date'])

# Extract only the date part
df['Date'] = df['Date'].dt.date

# Date selection
selected_date = st.date_input(" ", min_value=min_date, max_value=max_date, value=default_date)

# Filter data based on selected date
selected_data = df[df['Date'] == selected_date]

# Display active cases for the selected date
if not selected_data.empty:
    active_cases = selected_data['Active'].values[0]
    confirmed_cases = selected_data['Confirmed'].values[0]
    death_cases = selected_data['Deaths'].values[0]
    recovered_cases = selected_data['Recovered'].values[0]
    
    active_message = f"Active Cases   : {active_cases}"
    confirmed_message = f"Confirmed Cases  : {confirmed_cases}"
    death_message = f"Death Cases   : {death_cases}"
    recovered_message = f"Recovered Cases : {recovered_cases}"
    html_code = f"<div style='font-family: Arial; font-size: 24px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; text-align: center;'>{confirmed_message}</div><div style='font-family: Arial; font-size: 24px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; text-align: center;'>{active_message}</div><div style='font-family: Arial; font-size: 24px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; text-align: center;'>{recovered_message}</div><div style='font-family: Arial; font-size: 24px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; text-align: center;'>{death_message}</div>"

    st.markdown("<br>", unsafe_allow_html=True)
    # Print or use the generated HTML code
    st.markdown(html_code,unsafe_allow_html=True)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    chart_data = pd.DataFrame({
        'Cases': ['Active', 'Confirmed', 'Deaths', 'Recovered'],
        'Count': [active_cases, confirmed_cases, death_cases, recovered_cases]
    })

    chart = alt.Chart(chart_data).mark_bar().encode(
        x='Cases',
        y='Count',
        color=alt.Color('Cases', scale=alt.Scale(scheme='dark2'))
    ).properties(width=400, height=300)

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("No data available for the selected date. Please choose another date.")
    
#---------------------------------------------------------------------------------------------------------------------------------------------------
