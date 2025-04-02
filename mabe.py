import plotly.express as px
import pandas as pd
import chart_studio.plotly as py

# Import data from USGS
data = pd.read_csv('query.csv')


# Drop rows with missing or invalid values in the 'mag' column
data = data.dropna(subset=['mag'])
data = data[data.mag >= 0]


# Create scatter map
fig = px.scatter_geo(data, lat='latitude', lon='longitude', color='mag',
                     hover_name='place', #size='mag',
                     title='Earthquakes Around the World')
fig.show()
