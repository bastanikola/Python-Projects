---------------------------------
### PROJECT: WEB MAP - FOLIUM ###
---------------------------------
import folium
import pandas

#importing data from volcanoes.csv using pandas library
data = pandas.read_csv("volcanoes.csv")

#extracting data and creating 3 lists
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#creating a function for coloring the elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#creating a map and start location
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

#creating a Volcanoes group and applying loop for creating markers as well as coloring them
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 15, popup="Elev: " + str(el)+" mil",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.9))

#creating a Population group and applying lambda function for coloring them
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'blue'}))

#creating LayerControls visible on the UI
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

#saving the map in html format
map.save("Map1.html")
