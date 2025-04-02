import plotly.express as px
import pandas as pd


# Import data 
data = pd.read_csv("Burn_data.csv")
data = data.dropna(subset=["savannas"])
data = data[data.savannas >=0]

# Create map with parameters
fig = px.choropleth(data, locations="gid_0", color="savannas", hover_name="country",
                    projection="natural earth", animation_frame="year",
                    title="Burning Fires")
fig.show()            
