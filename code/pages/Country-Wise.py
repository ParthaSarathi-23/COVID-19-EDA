import pandas as pd
import streamlit as st
import plotly.graph_objects as go

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(layout="wide")

df = pd.read_csv("D:\Project\Covid19_EDA\Covid_19\country_wise_latest.csv")

country = list(df['Country/Region'])

#---------------------------------------------------------------------------------------------------------------------------------------------------

def create_map_plot(df, coordinates, highlight_country):
    
    
    
    latitudes = pd.DataFrame.from_dict(coordinates, orient='index', columns=['latitude'])
    longitudes = pd.DataFrame.from_dict(coordinates, orient='index', columns=['longitude'])

    # Reorder data to have the highlighted country first
    latitudes = latitudes.loc[[highlight_country] + [country for country in latitudes.index if country != highlight_country]]
    longitudes = longitudes.loc[[highlight_country] + [country for country in longitudes.index if country != highlight_country]]

    # Create a scatter plot with latitude and longitude as markers
    fig = go.Figure()

    df['hover_text'] = (
        '<br>Location: ' + df['Country/Region'] +
        '<br>Confirmed: ' + df['Confirmed'].astype(str) +
        '<br>Active : ' + df['Active'].astype(str) +
        '<br>Recovered : ' + df['Recovered'].astype(str) +
        '<br>Death : ' + df['Deaths'].astype(str)
    )

    # Add scatter plot with lat and long as markers
    fig.add_trace(go.Scattergeo(
        lon=longitudes['longitude'],
        lat=latitudes['latitude'],
        mode='markers',
        marker=dict(
            size=8,  # Adjust the marker size as needed
            color=['red' if country == highlight_country else 'blue' for country in latitudes.index],
        ),
        text=df['hover_text'],  # Location text to display on hover
    ))

    # Set an initial rotation angle
    initial_rotation = dict(lon=longitudes.iloc[0]['longitude'], lat=latitudes.iloc[0]['latitude'])

    # Update layout settings to set the initial rotation
    fig.update_geos(projection_type='orthographic', 
                    landcolor='darkgreen', 
                    oceancolor='darkblue',
                    showcoastlines=True,
                    showland=True,
                    showocean=True,
                    showframe=False,
                    coastlinewidth=2
                    )
    fig.update_geos(showland=True)
    fig.update_layout(
        legend_title_text='Categories',
        geo=dict(
            projection_rotation=initial_rotation
        ),
        height=600,  # Adjust the height as needed
        width=1200
    )

    return fig

#---------------------------------------------------------------------------------------------------------------------------------------------------

def Top_5(top_5, label):
    top = {
    top_5.iloc[0]['Country/Region']: top_5_confirmed.iloc[0][label],
    top_5.iloc[1]['Country/Region']: top_5_confirmed.iloc[1][label],
    top_5.iloc[2]['Country/Region']: top_5_confirmed.iloc[2][label],
    top_5.iloc[3]['Country/Region']: top_5_confirmed.iloc[3][label],
    top_5.iloc[4]['Country/Region']: top_5_confirmed.iloc[4][label],
    
    }


    fig = go.Figure(data=[go.Bar(x=list(top.keys()), y=list(top.values()), marker_color='skyblue')])

    fig.update_layout(
        title='Top 5 Confirmed Cases Country',
        xaxis=dict(title='Country'),
        yaxis=dict(title='No. of Cases'),
        width=1000,
        height=400
    )
    
    return fig

#---------------------------------------------------------------------------------------------------------------------------------------------------

coordinates ={
    'Afghanistan': {'latitude': 33.9391, 'longitude': 67.7100},
    'Albania': {'latitude': 41.1533, 'longitude': 20.1683},
    'Algeria': {'latitude': 28.0339, 'longitude': 1.6596},
    'Andorra': {'latitude': 42.5063, 'longitude': 1.5218},
    'Angola': {'latitude': -11.2027, 'longitude': 17.8739},
    'Antigua and Barbuda': {'latitude': 17.0608, 'longitude': -61.7964},
    'Argentina': {'latitude': -38.4192, 'longitude': -63.5980},
    'Armenia': {'latitude': 40.0691, 'longitude': 45.0382},
    'Australia': {'latitude': -25.2744, 'longitude': 133.7751},
    'Austria': {'latitude': 47.5162, 'longitude': 14.5501},
    'Azerbaijan': {'latitude': 40.1431, 'longitude': 47.5769},
    'Bahamas': {'latitude': 25.0343, 'longitude': -77.3963},
    'Bahrain': {'latitude': 26.0667, 'longitude': 50.5577},
    'Bangladesh': {'latitude': 23.6850, 'longitude': 90.3563},
    'Barbados': {'latitude': 13.1939, 'longitude': -59.5432},
    'Belarus': {'latitude': 53.7098, 'longitude': 27.9534},
    'Belgium': {'latitude': 50.8503, 'longitude': 4.3517},
    'Belize': {'latitude': 17.1899, 'longitude': -88.4976},
    'Benin': {'latitude': 9.3077, 'longitude': 2.3158},
    'Bhutan': {'latitude': 27.5142, 'longitude': 90.4336},
    'Bolivia': {'latitude': -16.2902, 'longitude': -63.5887},
    'Bosnia and Herzegovina': {'latitude': 43.9159, 'longitude': 17.6791},
    'Botswana': {'latitude': -22.3285, 'longitude': 24.6849},
    'Brazil': {'latitude': -14.2350, 'longitude': -51.9253},
    'Brunei': {'latitude': 4.5353, 'longitude': 114.7277},
    'Bulgaria': {'latitude': 42.7339, 'longitude': 25.4858},
    'Burkina Faso': {'latitude': 12.2383, 'longitude': -1.5616},
    'Burma': {'latitude': 21.9162, 'longitude': 95.9560},
    'Burundi': {'latitude': -3.3731, 'longitude': 29.9189},
    'Cabo Verde': {'latitude': 16.5388, 'longitude': -23.0418},
    'Cambodia': {'latitude': 12.5657, 'longitude': 104.9910},
    'Cameroon': {'latitude': 7.3697, 'longitude': 12.3547},
    'Canada': {'latitude': 56.1304, 'longitude': -106.3468},
    'Central African Republic': {'latitude': 6.6111, 'longitude': 20.9394},
    'Chad': {'latitude': 15.4542, 'longitude': 18.7322},
    'Chile': {'latitude': -35.6751, 'longitude': -71.5430},
    'China': {'latitude': 35.8617, 'longitude': 104.1954},
    'Colombia': {'latitude': 4.5709, 'longitude': -74.2973},
    'Comoros': {'latitude': -11.6455, 'longitude': 43.3334},
    'Congo (Brazzaville)': {'latitude': -0.2280, 'longitude': 15.8277},
    'Congo (Kinshasa)': {'latitude': -4.0383, 'longitude': 21.7587},
    'Costa Rica': {'latitude': 9.7489, 'longitude': -83.7534},
    "Cote d'Ivoire": {'latitude': 7.5390, 'longitude': -5.5471},
    'Croatia': {'latitude': 45.1000, 'longitude': 15.2000},
    'Cuba': {'latitude': 21.5218, 'longitude': -77.7812},
    'Cyprus': {'latitude': 35.1264, 'longitude': 33.4299},
    'Czechia': {'latitude': 49.8175, 'longitude': 15.4730},
    'Denmark': {'latitude': 56.2639, 'longitude': 9.5018},
    'Djibouti': {'latitude': 11.8251, 'longitude': 42.5903},
    'Dominica': {'latitude': 15.4150, 'longitude': -61.3710},
    'Dominican Republic': {'latitude': 18.7357, 'longitude': -70.1627},
    'Ecuador': {'latitude': -1.8312, 'longitude': -78.1834},
    'Egypt': {'latitude': 26.8206, 'longitude': 30.8025},
    'El Salvador': {'latitude': 13.7942, 'longitude': -88.8965},
    'Equatorial Guinea': {'latitude': 1.6508, 'longitude': 10.2679},
    'Eritrea': {'latitude': 15.1794, 'longitude': 39.7823},
    'Estonia': {'latitude': 58.5953, 'longitude': 25.0136},
    'Eswatini': {'latitude': -26.5225, 'longitude': 31.4659},
    'Ethiopia': {'latitude': 9.1450, 'longitude': 40.4897},
    'Fiji': {'latitude': -17.7134, 'longitude': 178.0650},
    'Finland': {'latitude': 61.9241, 'longitude': 25.7482},
    'France': {'latitude': 46.6035, 'longitude': 1.8883},
    'Gabon': {'latitude': -0.8037, 'longitude': 11.6094},
    'Gambia': {'latitude': 13.4432, 'longitude': -15.3101},
    'Georgia': {'latitude': 42.3154, 'longitude': 43.3569},
    'Germany': {'latitude': 51.1657, 'longitude': 10.4515},
    'Ghana': {'latitude': 7.5400, 'longitude': -1.5477},
    'Greece': {'latitude': 39.0742, 'longitude': 21.8243},
    'Greenland': {'latitude': 71.7069, 'longitude': -42.6043},
    'Grenada': {'latitude': 12.1165, 'longitude': -61.6790},
    'Guatemala': {'latitude': 15.7835, 'longitude': -90.2308},
    'Guinea': {'latitude': 9.9456, 'longitude': -9.6966},
    'Guinea-Bissau': {'latitude': 11.8037, 'longitude': -15.1804},
    'Guyana': {'latitude': 4.8604, 'longitude': -58.9302},
    'Haiti': {'latitude': 18.9712, 'longitude': -72.2852},
    'Holy See': {'latitude': 41.9029, 'longitude': 12.4534},
    'Honduras': {'latitude': 15.1998, 'longitude': -86.2419},
    'Hungary': {'latitude': 47.1625, 'longitude': 19.5033},
    'Iceland': {'latitude': 64.9631, 'longitude': -19.0208},
    'India': {'latitude': 20.5937, 'longitude': 78.9629},
    'Indonesia': {'latitude': -0.7893, 'longitude': 113.9213},
    'Iran': {'latitude': 32.4279, 'longitude': 53.6880},
    'Iraq': {'latitude': 33.3152, 'longitude': 44.3661},
    'Ireland': {'latitude': 53.1424, 'longitude': -7.6921},
    'Israel': {'latitude': 31.0461, 'longitude': 34.8516},
    'Italy': {'latitude': 41.8719, 'longitude': 12.5674},
    'Jamaica': {'latitude': 18.1096, 'longitude': -77.2975},
    'Japan': {'latitude': 36.2048, 'longitude': 138.2529},
    'Jordan': {'latitude': 30.5852, 'longitude': 36.2384},
    'Kazakhstan': {'latitude': 48.0196, 'longitude': 66.9237},
    'Kenya': {'latitude': -1.2921, 'longitude': 36.8219},
    'Kosovo': {'latitude': 42.6026, 'longitude': 20.9029},
    'Kuwait': {'latitude': 29.3759, 'longitude': 47.9774},
    'Kyrgyzstan': {'latitude': 41.2044, 'longitude': 74.7661},
    'Laos': {'latitude': 19.8563, 'longitude': 102.4955},
    'Latvia': {'latitude': 56.8796, 'longitude': 24.6032},
    'Lebanon': {'latitude': 33.8547, 'longitude': 35.8623},
    'Lesotho': {'latitude': -29.6099, 'longitude': 28.2336},
    'Liberia': {'latitude': 6.4281, 'longitude': -9.4295},
    'Libya': {'latitude': 26.3351, 'longitude': 17.2283},
    'Liechtenstein': {'latitude': 47.1660, 'longitude': 9.5554},
    'Lithuania': {'latitude': 55.1694, 'longitude': 23.8813},
    'Luxembourg': {'latitude': 49.8153, 'longitude': 6.1296},
    'Madagascar': {'latitude': -18.8792, 'longitude': 46.8691},
    'Malawi': {'latitude': -13.2543, 'longitude': 34.3015},
    'Malaysia': {'latitude': 4.2105, 'longitude': 101.9758},
    'Maldives': {'latitude': 3.2028, 'longitude': 73.2207},
    'Mali': {'latitude': 17.5707, 'longitude': -3.9962},
    'Malta': {'latitude': 35.9375, 'longitude': 14.3754},
    'Mauritania': {'latitude': 21.0079, 'longitude': -10.9408},
    'Mauritius': {'latitude': -20.348404, 'longitude': 57.552152},
    'Mexico': {'latitude': 23.6345, 'longitude': -102.5528},
    'Moldova': {'latitude': 47.4116, 'longitude': 28.3699},
    'Monaco': {'latitude': 43.7384, 'longitude': 7.4246},
    'Mongolia': {'latitude': 46.8625, 'longitude': 103.8467},
    'Montenegro': {'latitude': 42.7087, 'longitude': 19.3744},
    'Morocco': {'latitude': 31.7917, 'longitude': -7.0926},
    'Mozambique': {'latitude': -18.6657, 'longitude': 35.5296},
    'Namibia': {'latitude': -22.9576, 'longitude': 18.4904},
    'Nepal': {'latitude': 28.3949, 'longitude': 84.1240},
    'Netherlands': {'latitude': 52.1326, 'longitude': 5.2913},
    'New Zealand': {'latitude': -40.9006, 'longitude': 174.8860},
    'Nicaragua': {'latitude': 12.8654, 'longitude': -85.2072},
    'Niger': {'latitude': 17.6078, 'longitude': 8.0817},
    'Nigeria': {'latitude': 9.0820, 'longitude': 8.6753},
    'North Macedonia': {'latitude': 41.6086, 'longitude': 21.7453},
    'Norway': {'latitude': 60.4720, 'longitude': 8.4689},
    'Oman': {'latitude': 21.4735, 'longitude': 55.9754},
    'Pakistan': {'latitude': 30.3753, 'longitude': 69.3451},
    'Panama': {'latitude': 8.5380, 'longitude': -80.782},
    'Papua New Guinea': {'latitude': -6.314993, 'longitude': 143.955550},
    'Paraguay': {'latitude': -23.442503, 'longitude': -58.443832},
    'Peru': {'latitude': -9.190000, 'longitude': -75.015152},
    'Philippines': {'latitude': 12.879721, 'longitude': 121.774017},
    'Poland': {'latitude': 51.9194, 'longitude': 19.1451},
    'Portugal': {'latitude': 39.3999, 'longitude': -8.2245},
    'Qatar': {'latitude': 25.276987, 'longitude': 51.520008},
    'Romania': {'latitude': 45.9432, 'longitude': 24.9668},
    'Russia': {'latitude': 61.5240, 'longitude': 105.3188},
    'Rwanda': {'latitude': -1.9403, 'longitude': 29.8739},
    'Saint Kitts and Nevis': {'latitude': 17.357822, 'longitude': -62.782998},
    'Saint Lucia': {'latitude': 13.9094, 'longitude': -60.9789},
    'Saint Vincent and the Grenadines': {'latitude': 12.9843, 'longitude': -61.2872},
    'San Marino': {'latitude': 43.9424, 'longitude': 12.4578},
    'Sao Tome and Principe': {'latitude': 0.1864, 'longitude': 6.6131},
    'Saudi Arabia': {'latitude': 23.8859, 'longitude': 45.0792},
    'Senegal': {'latitude': 14.4974, 'longitude': -14.4524},
    'Serbia': {'latitude': 44.0165, 'longitude': 21.0059},
    'Seychelles': {'latitude': -4.6796, 'longitude': 55.4920},
    'Sierra Leone': {'latitude': 8.4606, 'longitude': -11.7799},
    'Singapore': {'latitude': 1.3521, 'longitude': 103.8198},
    'Slovakia': {'latitude': 48.6690, 'longitude': 19.6990},
    'Slovenia': {'latitude': 46.1512, 'longitude': 14.9955},
    'Somalia': {'latitude': 5.1521, 'longitude': 46.1996},
    'South Africa': {'latitude': -30.5595, 'longitude': 22.9375},
    'South Korea': {'latitude': 35.9078, 'longitude': 127.7669},
    'South Sudan': {'latitude': 6.8770, 'longitude': 31.3070},
    'Spain': {'latitude': 40.4637, 'longitude': -3.7492},
    'Sri Lanka': {'latitude': 7.8731, 'longitude': 80.7718},
    'Sudan': {'latitude': 12.8628, 'longitude': 30.2176},
    'Suriname': {'latitude': 3.9193, 'longitude': -56.0278},
    'Sweden': {'latitude': 60.1282, 'longitude': 18.6435},
    'Switzerland': {'latitude': 46.8182, 'longitude': 8.2275},
    'Syria': {'latitude': 34.8021, 'longitude': 38.9968},
    'Taiwan*': {'latitude': 23.6978, 'longitude': 120.9605},
    'Tajikistan': {'latitude': 38.8610, 'longitude': 71.2761},
    'Tanzania': {'latitude': -6.369028, 'longitude': 34.888822},
    'Thailand': {'latitude': 15.8700, 'longitude': 100.9925},
    'Timor-Leste': {'latitude': -8.8742, 'longitude': 125.7275},
    'Togo': {'latitude': 8.6195, 'longitude': 0.8248},
    'Trinidad and Tobago': {'latitude': 10.6918, 'longitude': -61.2225},
    'Tunisia': {'latitude': 33.8869, 'longitude': 9.5375},
    'Turkey': {'latitude': 38.9637, 'longitude': 35.2433},
    'US': {'latitude': 37.0902, 'longitude': -95.7129},
    'Uganda': {'latitude': 1.3733, 'longitude': 32.2903},
    'Ukraine': {'latitude': 48.3794, 'longitude': 31.1656},
    'United Arab Emirates': {'latitude': 23.4241, 'longitude': 53.8478},
    'United Kingdom': {'latitude': 55.3781, 'longitude': -3.4360},
    'Uruguay': {'latitude': -32.5228, 'longitude': -55.7658},
    'Uzbekistan': {'latitude': 41.3775, 'longitude': 64.5853},
    'Venezuela': {'latitude': 6.4238, 'longitude': -66.5897},
    'Vietnam': {'latitude': 14.0583, 'longitude': 108.2772},
    'West Bank and Gaza': {'latitude': 31.9522, 'longitude': 35.2332},
    'Western Sahara': {'latitude': 24.2155, 'longitude': -12.8858},
    'Yemen': {'latitude': 15.5524, 'longitude': 48.5164},
    'Zambia': {'latitude': -13.1339, 'longitude': 27.8493},
    'Zimbabwe': {'latitude': -19.0154, 'longitude': 29.1549},
}

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
        <h1>Top 5 Confirmed Cases Country</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

top_5_confirmed = df.nlargest(5, ['Confirmed']) 
top_5_confirmed = top_5_confirmed.reset_index(drop=True)

combined_table_html = f"""
    <table style="margin: auto;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Confirmed Cases</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[0]['Confirmed']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[1]['Confirmed']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[2]['Confirmed']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[3]['Confirmed']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[4]['Confirmed']}</td>
        </tr>
    </table>
"""

st.markdown(combined_table_html, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

fig = Top_5(top_5_confirmed, 'Confirmed')
# Display the bar plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

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
        <h1>Top 5 Active Cases Country</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

top_5_confirmed = df.nlargest(5, ['Active']) 
top_5_confirmed = top_5_confirmed.reset_index(drop=True)

combined_table_html = f"""
    <table style="margin: auto;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Active Cases</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[0]['Active']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[1]['Active']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[2]['Active']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[3]['Active']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[4]['Active']}</td>
        </tr>
    </table>
"""

st.markdown(combined_table_html, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

fig = Top_5(top_5_confirmed, 'Active')
# Display the bar plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

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
        <h1>Top 5 Recovered Cases Country</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

top_5_confirmed = df.nlargest(5, ['Recovered']) 
top_5_confirmed = top_5_confirmed.reset_index(drop=True)

combined_table_html = f"""
    <table style="margin: auto;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Recovered Cases</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[0]['Recovered']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[1]['Recovered']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[2]['Recovered']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[3]['Recovered']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[4]['Recovered']}</td>
        </tr>
    </table>
"""

st.markdown(combined_table_html, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

fig = Top_5(top_5_confirmed, 'Recovered')
# Display the bar plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

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
        <h1>Top 5 Death Cases Country</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

top_5_confirmed = df.nlargest(5, ['Deaths']) 
top_5_confirmed = top_5_confirmed.reset_index(drop=True)

combined_table_html = f"""
    <table style="margin: auto;">
        <tr>
            <th style="font-size: 24px; border: 2px solid white;">Country</th>
            <th style="font-size: 24px; border: 2px solid white;">Active Cases</th>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[0]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[0]['Deaths']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[1]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[1]['Deaths']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[2]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[2]['Deaths']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[3]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[3]['Deaths']}</td>
        </tr>
        <tr>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[4]['Country/Region']}</td>
            <td style="font-size: 20px; border: 2px solid white;">{top_5_confirmed.iloc[4]['Deaths']}</td>
        </tr>
    </table>
"""

st.markdown(combined_table_html, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

fig = Top_5(top_5_confirmed, 'Deaths')
# Display the bar plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

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
        <h1>Country-Wise Analysis</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

selected_country = st.selectbox(" ", df['Country/Region'].unique())


fig = create_map_plot(df, coordinates, selected_country)

# Show the plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

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
        <h1>No of Cases of Country</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

selected_country_number = st.selectbox("  ", df['Country/Region'].unique())

y = country.index(selected_country_number)

# Extract data for the selected country
selected_country_data = {
    'Confirmed': df.iloc[y]['Confirmed'],
    'Active': df.iloc[y]['Active'],
    'Recovered': df.iloc[y]['Recovered'],
    'Death': df.iloc[y]['Deaths'],
    'LastWeek': df.iloc[y]['Confirmed last week'],
    'Increased In Last Week': df.iloc[y]['1 week change']
}

# Create a bar plot using Plotly
fig = go.Figure(data=[go.Bar(x=list(selected_country_data.keys()), y=list(selected_country_data.values()), marker_color=['red', 'green', 'grey', 'blue', 'purple', 'orange'])])

fig.update_layout(
    title=df.iloc[y]['Country/Region'],
    xaxis=dict(title='Cases'),
    yaxis=dict(title='No. of Cases'),
    width=1000,
    height=400
)

# Display the bar plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

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
        <h1>Ratio of Country</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

selected_country_rate = st.selectbox("   ", df['Country/Region'].unique())

y = country.index(selected_country_number)

Active_Ratio = []

for i in range(0, len(df)):
  Active_Ratio.append((df.iloc[i]['Active']/df.iloc[i]['Confirmed'])*100)

data = { 'Active Ratio':Active_Ratio[y], 
        'Recovered Ratio':df.iloc[y]['Recovered / 100 Cases'], 
        'Death Ratio':df.iloc[y]['Deaths / 100 Cases'],
        'Increased In Last Week Ratio' : df.iloc[y]['1 week % increase']}

courses = list(data.keys())
values = list(data.values())

# Create a bar plot using Plotly
fig = go.Figure(data=[go.Bar(x=courses, y=values, marker_color=['orange', 'red', 'blue', 'green'])])

fig.update_layout(
    title=df.iloc[y]['Country/Region'],
    xaxis=dict(title='Rate'),
    yaxis=dict(title='Ratio'),
    width=1000,
    height=400
)

st.plotly_chart(fig, use_container_width=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------
