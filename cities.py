import folium
import pandas

# dump world_cities.json file into dict
data_cities = pandas.read_csv('worldcities.csv')
cities_lat = data_cities['lat'].tolist()
cities_lon = data_cities['lng'].tolist()
cities_names = data_cities['city_ascii'].tolist()
cities_country = data_cities['country'].tolist()

# sort txt file by columns
data = pandas.read_csv("Volcanoes.txt")
# create two separate lists with lat ans lon from data file created in the previous step
lat = data['LAT'].tolist()
lon = data['LON'].tolist()
elev = data['ELEV'].tolist()

# setting marker color depending of eleveation value
def marker_color(elevation):

    if elevation < 1500:
        return 'green'
    elif elevation >= 1500 and el < 2500:
        return 'orange'
    else:
        return 'red'

html = """<h4>Volcano information:</h4>
            Height: %s m
        """
# joined lists of country, names, lat and lon of cities
complete_list_name_lat_lon_cities = list(zip(cities_country, cities_names, cities_lat, cities_lon))

# create list of tuples (join lat, lon, elev from 3 lists)
complete_list_volcanoes = list(zip(lat, lon, elev))

# create folium map and zoom to lacation
map = folium.Map(location=[48.111, -121.111], zoom_start=5)

# creating feature group for volcanoes markers
fg_volcanoes = folium.FeatureGroup(name="Volcanoes")

# creating feature group for population poligons layer
fg_population = folium.FeatureGroup(name="Population")

# creating feature group for cities
fg_cities = folium.FeatureGroup(name="Cities")

# itterate through list to add every volcano marker on the map
for lat, lon, el in complete_list_volcanoes:
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg_volcanoes.add_child(folium.CircleMarker(location=[lat, lon], color= 'grey', radius=7, fill=True,
                                     popup=folium.Popup(iframe), fill_color=marker_color(el),
                                     fill_opacity=0.7))
    # fg.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe), icon=folium.Icon(color=marker_color(el))))

# creating country borders layer
# country is colored by population number
fg_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green'
                                                      if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000
                                                      else 'red'}))

# creating cities markers
for country, name, lat, lon in complete_list_name_lat_lon_cities:
    if country == 'Croatia':
        fg_cities.add_child(folium.CircleMarker(location=[lat, lon], color= 'grey', radius=2, fill=True, popup=name))

map.add_child(fg_volcanoes)
map.add_child(fg_population)
map.add_child(fg_cities)

# adding layer control feature
map.add_child(folium.LayerControl())

map.save("Map1.html")