from geopy.geocoders import Nominatim
import folium
import webbrowser

location = input("Enter location: ")
nom = Nominatim(user_agent="map")
map_form = folium.Map(location=[nom.geocode(location).latitude, nom.geocode(
    location).longitude], zoom_start=12, tiles='Stamen Terrain')
folium.Marker(location=[nom.geocode(location).latitude, nom.geocode(location).longitude], popup=nom.geocode(
    location).address, icon=folium.Icon(color='red')).add_to(map_form)
folium.GeoJson(
    data=(open('world.json', 'r', encoding='utf-8-sig').read())).add_to(map_form)
map_form.save("Map.html")
webbrowser.open_new_tab("Map.html")
