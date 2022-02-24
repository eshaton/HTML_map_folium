import folium
import pandas

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

# create list of tuples (join lat and lon from 2 lists)
complete_list = list(zip(lat, lon, elev))

# create folium map
map = folium.Map(location=[48.111, -121.111], zoom_start=10)
fg = folium.FeatureGroup(name="My Map")

# itterate through list to add every marker on the map
for lat, lon, el in complete_list:
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lat, lon], color= 'grey', radius=7, fill=True,
                                     popup=folium.Popup(iframe), fill_color=marker_color(el),
                                     fill_opacity=0.7))
    # fg.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe), icon=folium.Icon(color=marker_color(el))))

# creating country borders layer
# TODO napraviti boje prema populaciji iz datoteke world.json
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'yellow'}))

map.add_child(fg)
map.save("Map1.html")

