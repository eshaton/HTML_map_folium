import folium
import pandas

# sort txt file by columns
data = pandas.read_csv("Volcanoes.txt")

# create two separate lists with lat ans lon from data file created in the previous step
lat = data['LAT'].tolist()
lon = data['LON'].tolist()

# create list of tuples (join lat and lon from 2 lists)
lat_lon_list = list(zip(lat, lon))

# create folium map
map = folium.Map(location=[48.111, -121.111], zoom_start=10)
fg = folium.FeatureGroup(name="My Map")

# itterate through list to add every marker on the map
for coordinates in lat_lon_list:
    fg.add_child(folium.Marker(location=coordinates, popup="Moja kućica", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map1.html")

