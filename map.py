import folium

# initialize Map and save it for viewing in index.html
m = folium.Map(location=[43.66430664668449, -79.39241763253044])
m.save("index.html")
