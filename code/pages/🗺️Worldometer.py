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

df = pd.read_csv("D:\Project\Covid19_EDA\Covid_19\worldometer_data.csv")

#--------------------------------------------------------------------------------------------------------------------------------------------------

df['TotalDeaths'] = df['TotalDeaths'].fillna(0)
df['TotalRecovered'] = df['TotalRecovered'].fillna(0)
df['ActiveCases'] = df['ActiveCases'].fillna(0)
df['Serious,Critical'] = df['Serious,Critical'].fillna(0)
df['Deaths/1M pop'] = df['Deaths/1M pop'].fillna(0)
df['TotalTests'] = df['TotalTests'].fillna(0)
df['Tests/1M pop'] = df['Tests/1M pop'].fillna(0)

df.drop('NewCases', inplace=True, axis=1)
df.drop('NewDeaths', inplace=True, axis=1)
df.drop('NewRecovered', inplace=True, axis=1)
df.drop(156, inplace=True, axis=0)

df = df.reset_index(drop = True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

def table(d, selected_value):
    
    key = list(d.keys())
    value = list(d.values())
    
    combined_table_html = f"""
    <table style="margin: auto; width: 80%; border-collapse: collapse; border: 2px solid black;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Continent</th>
            <th style="font-size: 24px; border: 2px solid white;">{selected_value} Count</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{key[0]}</td>
            <td style="font-size: 20px; border: 2px solid white;">{value[0]}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{key[1]}</td>
            <td style="font-size: 20px; border: 2px solid white;">{value[1]}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{key[2]}</td>
            <td style="font-size: 20px; border: 2px solid white;">{value[2]}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{key[3]}</td>
            <td style="font-size: 20px; border: 2px solid white;">{value[3]}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{key[4]}</td>
            <td style="font-size: 20px; border: 2px solid white;">{value[4]}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{key[5]}</td>
            <td style="font-size: 20px; border: 2px solid white;">{value[5]}</td>
        </tr>
    </table>
    """

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(combined_table_html, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

def top_5(continent, dataframe):
    
    Case = dataframe.nlargest(5, ['TotalCases'])
    Case = Case.reset_index(drop=True)
    
    combined_table_html = f"""
    <table style="margin: auto; width: 80%; border-collapse: collapse; border: 2px solid black;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Total Case Count</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['TotalCases']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['TotalCases']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['TotalCases']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['TotalCases']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['TotalCases']}</td>
        </tr>
    </table>
    """
    
    title = "Total Case Count of "+ continent
    st.title(title)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(combined_table_html, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------
    
    Case = dataframe.nlargest(5, ['TotalDeaths'])
    Case = Case.reset_index(drop=True)
    
    combined_table_html = f"""
    <table style="margin: auto; width: 80%; border-collapse: collapse; border: 2px solid black;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Total Death Case Count</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['TotalDeaths']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['TotalDeaths']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['TotalDeaths']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['TotalDeaths']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['TotalDeaths']}</td>
        </tr>
    </table>
    """

    title = "Death Case Count of "+ continent
    st.title(title)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(combined_table_html, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

    Case = dataframe.nlargest(5, ['TotalRecovered'])
    Case = Case.reset_index(drop=True)
    
    combined_table_html = f"""
    <table style="margin: auto; width: 80%; border-collapse: collapse; border: 2px solid black;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Total Recovered Case Count</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['TotalRecovered']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['TotalRecovered']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['TotalRecovered']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['TotalRecovered']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['TotalRecovered']}</td>
        </tr>
    </table>
    """

    title = "Recovered Case Count of "+ continent
    st.title(title)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(combined_table_html, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

    Case = dataframe.nlargest(5, ['ActiveCases'])
    Case = Case.reset_index(drop=True)
    
    combined_table_html = f"""
    <table style="margin: auto; width: 80%; border-collapse: collapse; border: 2px solid black;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Total Active Case Count</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['ActiveCases']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['ActiveCases']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['ActiveCases']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['ActiveCases']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['ActiveCases']}</td>
        </tr>
    </table>
    """

    title = "Active Case Count of "+ continent
    st.title(title)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(combined_table_html, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

    Case = dataframe.nlargest(5, ['Serious,Critical'])
    Case = Case.reset_index(drop=True)
    
    combined_table_html = f"""
    <table style="margin: auto; width: 80%; border-collapse: collapse; border: 2px solid black;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Total Critical Case Count</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['Serious,Critical']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['Serious,Critical']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['Serious,Critical']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['Serious,Critical']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['Serious,Critical']}</td>
        </tr>
    </table>
    """

    title = "Critical Case Count of "+ continent
    st.title(title)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(combined_table_html, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

    Case = dataframe.nlargest(5, ['TotalTests'])
    Case = Case.reset_index(drop=True)
    
    combined_table_html = f"""
    <table style="margin: auto; width: 80%; border-collapse: collapse; border: 2px solid black;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Total Test Count</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[0]['TotalTests']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[1]['TotalTests']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[2]['TotalTests']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[3]['TotalTests']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{Case.iloc[4]['TotalTests']}</td>
        </tr>
    </table>
    """

    title = "Test Count of "+ continent
    st.title(title)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(combined_table_html, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

def dictionary(selected_value):
    continent = {}
    
    for i in range(len(df)):
        if(df.iloc[i]['Continent'] in continent ):
            continent[df.iloc[i]['Continent']] += df.iloc[i][selected_value]
        else:
            continent[df.iloc[i]['Continent']] = df.iloc[i][selected_value]

    return continent

#--------------------------------------------------------------------------------------------------------------------------------------------------

def List():
    TotalCase = []
    TotalActive = []
    TotalRecovered = []
    TotalDeath = []
    TotalTest = []
    Critical = []
    
    select_lst = ['TotalCases', 'ActiveCases', 'TotalRecovered', 'TotalDeaths', 'Serious,Critical', 'TotalTests']
    continent_lst = list(df['Continent'].unique())
    
    dic = dictionary(select_lst[0])
    TotalCase = list(dic.values())
    
    dic = dictionary(select_lst[1])
    TotalActive = list(dic.values())
    
    dic = dictionary(select_lst[2])
    TotalRecovered = list(dic.values())
    
    dic = dictionary(select_lst[3])
    TotalDeath = list(dic.values())
    
    dic = dictionary(select_lst[4])
    Critical = list(dic.values())
    
    dic = dictionary(select_lst[5])
    TotalTest = list(dic.values())
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=continent_lst, y=TotalCase, name='Total Case'))
    fig.add_trace(go.Bar(x=continent_lst, y=TotalActive, name='Total Active Case'))
    fig.add_trace(go.Bar(x=continent_lst, y=TotalRecovered, name='Total Recovered Case'))
    fig.add_trace(go.Bar(x=continent_lst, y=TotalDeath, name='Total Death Case'))
    fig.add_trace(go.Bar(x=continent_lst, y=TotalTest, name='Total Test'))
    fig.add_trace(go.Bar(x=continent_lst, y=Critical, name='Critical Case'))

    fig.update_layout(
        xaxis=dict(title='Continent'),
        yaxis=dict(title='Number of Cases'),
        barmode='group',
        width=1400,
        height=750
    )
    
    st.plotly_chart(fig)

#--------------------------------------------------------------------------------------------------------------------------------------------------
       
def pie_chart(selected_value):
    
    continent = dictionary(selected_value)
    
    
    fig = px.pie(
    names=list(continent.keys()),
    values=list(continent.values()),
    title='Distribution of Test by Continent',
    labels={'names': 'Continent', 'values': 'Test'}
    )
    
    fig.update_layout(
    width=800,  # Set the width of the plot
    height=600  # Set the height of the plot
    )

    # Show the plot
    st.plotly_chart(fig, use_container_width=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

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
        <h1>Case Count in the World</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


combined_table_html = f"""
    <table style="margin: auto; width: 80%; border-collapse: collapse; border: 2px solid black;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Category</th>
            <th style="font-size: 24px; border: 2px solid white;">Case Count</th>
        </tr> 
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Total Cases</td>
            <td style="font-size: 20px; border: 2px solid white;">{df['TotalCases'].sum()}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Total Active Cases</td>
            <td style="font-size: 20px; border: 2px solid white;">{df['ActiveCases'].sum()}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Total Recovered Cases</td>
            <td style="font-size: 20px; border: 2px solid white;">{df['TotalRecovered'].sum()}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Total Death Cases</td>
            <td style="font-size: 20px; border: 2px solid white;">{df['TotalDeaths'].sum()}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Critical Cases</td>
            <td style="font-size: 20px; border: 2px solid white;">{df['Serious,Critical'].sum()}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">Total Test Taken</td>
            <td style="font-size: 20px; border: 2px solid white;">{df['TotalTests'].sum()}</td>
        </tr>
    </table>
    """

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(combined_table_html, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

data = {'Total Cases': df['TotalCases'].sum(), 
            'Total Active Cases': df['ActiveCases'].sum(), 
            'Total Recovered Cases': df['TotalRecovered'].sum(),
            'Total Death Cases': df['TotalDeaths'].sum(), 
            'Critical Cases': df['Serious,Critical'].sum(), 
            'Total Test Taken': df['TotalTests'].sum()}

key = list(data.keys())
values = list(data.values())

# Create a bar plot using Plotly
fig = go.Figure(data=[go.Bar(x=key, y=values, marker_color=['orange', 'red', 'blue', 'green', 'purple', 'grey'])])

fig.update_layout(
    xaxis=dict(title='Case'),
    yaxis=dict(title='Count'),
    width=1000,
    height=400
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

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
        <h1>Top 5 in World</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


top_5('World', df)

#--------------------------------------------------------------------------------------------------------------------------------------------------

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
        <h1>Case Count in each Continent</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

map_dict = {'Total Cases': 'TotalCases', 
            'Total Active Cases': 'ActiveCases', 
            'Total Recovered Cases': 'TotalRecovered',
            'Total Death Cases': 'TotalDeaths', 
            'Critical Cases': 'Serious,Critical', 
            'Total Test Taken': 'TotalTests'}

selected_value = st.selectbox(" ", ['Total Cases', 'Total Active Cases', 'Total Recovered Cases', 'Total Death Cases', 'Critical Cases', 'Total Test Taken'])


continent = dictionary(map_dict[selected_value])
table(continent, selected_value)

#--------------------------------------------------------------------------------------------------------------------------------------------------

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
        <h1>Top 5</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

selected_continent_value = st.selectbox("  ", df['Continent'].unique())

top_5(selected_continent_value, df[df['Continent'] == selected_continent_value])

#--------------------------------------------------------------------------------------------------------------------------------------------------

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
        <h1>Bar Plot for Cases in each Continent</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

List()

#--------------------------------------------------------------------------------------------------------------------------------------------------

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
        <h1>Pie Chart</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

selected_value_piechart = st.selectbox("   ", ['Total Cases', 'Total Active Cases', 'Total Recovered Cases', 'Total Death Cases', 'Critical Cases', 'Total Test Taken'])

pie_chart(map_dict[selected_value_piechart])

#--------------------------------------------------------------------------------------------------------------------------------------------------

NorthAmerica = df[df['Continent'] == 'North America']
SouthAmerica = df[df['Continent'] == 'South America']
Asia = df[df['Continent'] == 'Asia']
Europe = df[df['Continent'] == 'Europe']
Africa = df[df['Continent'] == 'Africa']
Australia = df[df['Continent'] == 'Australia/Oceania']

NorthAmerica = NorthAmerica.reset_index(drop=True)
SouthAmerica = SouthAmerica.reset_index(drop=True)
Asia = Asia.reset_index(drop=True)
Europe = Europe.reset_index(drop=True)
Africa = Africa.reset_index(drop=True)
Australia = Australia.reset_index(drop=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

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
        <h1>Case Count/100 population</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

percentage = {'NorthAmerica': [round((NorthAmerica[map_dict[i]].sum()/NorthAmerica['Population'].sum())*100, 2) for i in map_dict],
              'SouthAmerica': [round((SouthAmerica[map_dict[i]].sum()/SouthAmerica['Population'].sum())*100, 2) for i in map_dict],
              'Asia': [round((Asia[map_dict[i]].sum()/Asia['Population'].sum())*100, 2) for i in map_dict],
              'Europe': [round((Europe[map_dict[i]].sum()/Europe['Population'].sum())*100, 2) for i in map_dict],
              'Africa': [round((Africa[map_dict[i]].sum()/Africa['Population'].sum())*100, 2) for i in map_dict],
              'Australia': [round((Australia[map_dict[i]].sum()/Australia['Population'].sum())*100, 2) for i in map_dict]}

key = list(percentage.keys())
values = list(percentage.values())

fig = go.Figure()
fig.add_trace(go.Bar(x=key, y=[values[0][0], values[1][0], values[2][0], values[3][0], values[4][0], values[5][0]], name='Total Case'))
fig.add_trace(go.Bar(x=key, y=[values[0][1], values[1][1], values[2][1], values[3][1], values[4][1], values[5][1]], name='Total Active Case'))
fig.add_trace(go.Bar(x=key, y=[values[0][2], values[1][2], values[2][2], values[3][2], values[4][2], values[5][2]], name='Total Recovered Case'))
fig.add_trace(go.Bar(x=key, y=[values[0][3], values[1][3], values[2][3], values[3][3], values[4][3], values[5][3]], name='Total Death Case'))
fig.add_trace(go.Bar(x=key, y=[values[0][5], values[1][5], values[2][5], values[3][5], values[4][5], values[5][5]], name='Total Test'))


fig.update_layout(
        xaxis=dict(title='Continent'),
        yaxis=dict(title='Number of Cases'),
        barmode='group',
        width=1400,
        height=750
)
    
st.plotly_chart(fig)

st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------

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
        <h1>Each Countries Case Count/100 population</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

selected_value_percentage = st.selectbox("    ", list(df['Country/Region'].unique()))

extracted = df[df['Country/Region'] == selected_value_percentage]

different_case = ['Total Cases', 'Total Active Cases', 'Total Recovered Cases', 'Total Death Cases', 'Total Test Taken']
in_percentage = [round(extracted.iloc[0]['TotalCases']/extracted.iloc[0]['Population'],5),
                 round(extracted.iloc[0]['ActiveCases']/extracted.iloc[0]['Population'],5),
                 round(extracted.iloc[0]['TotalRecovered']/extracted.iloc[0]['Population'],5),
                 round(extracted.iloc[0]['TotalDeaths']/extracted.iloc[0]['Population'],5),
                 round(extracted.iloc[0]['TotalTests']/extracted.iloc[0]['Population'],5)]


fig = go.Figure(data=[go.Bar(x=different_case, y=in_percentage, marker_color=['orange', 'red', 'blue', 'green', 'purple', 'grey'])])

fig.update_layout(
    xaxis=dict(title='Case'),
    yaxis=dict(title='Count'),
    width=1000,
    height=400
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------------------------
