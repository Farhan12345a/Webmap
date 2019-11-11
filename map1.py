import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location = [38.50, -99.05], zoom_start = 6)

fg = folium.FeatureGroup(name = "My Map")


for lat, long, ele in zip(lat,long, elev):
    fg.add_child(folium.CircleMarker(location = [lat,long], radius = 6, popup = str(ele) + " meters", fill_color = color_producer(ele), color = 'grey', fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig',
style_funnction =  lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
 else 'orange' if 1000000 <= x['properties']['POP2005'] < 10000000 else 'red'})))



map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("Map1.html")
