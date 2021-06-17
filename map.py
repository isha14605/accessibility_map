import folium

# initialize Map
my_map = folium.Map(location=[43.66430664668449, -79.39241763253044],
                    zoom_start=15)

# sample Marker for Map
folium.Marker(location=[43.64668848, -79.3800808],
              popup=folium.Popup('<b>RBC Branch and ATM: 200 Bay Street<b>',
                                 max_width=100),
              icon=folium.Icon(icon="cloud"),).add_to(my_map)

# renders Map
my_map.save("index.html")
