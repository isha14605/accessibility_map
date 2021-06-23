import folium
import pandas as pd

# initialize Map
my_map = folium.Map(location=[43.66430664668449, -79.39241763253044],
                    zoom_start=15)

# sample Marker for Map
# folium.Marker(location=[43.64668848, -79.3800808],
#               popup=folium.Popup('<b>RBC Branch and ATM: 200 Bay Street<b>',
#                                  max_width=100),
#               icon=folium.Icon(icon="cloud"),).add_to(my_map)

df = pd.read_csv('banks.csv')

banks_dict = df.to_dict('index')

for i in range(df.shape[0]):
    folium.Marker(location=[banks_dict[i]['Latitude'],
                            banks_dict[i]['Longitude']],
                  popup=folium.Popup('<b>{} - {}<b>'.format(banks_dict[i]['Name'],
                                                            banks_dict[i]['Address']),
                                     max_width=100),
                  icon=folium.Icon(icon="cloud"),).add_to(my_map)

# renders Map
my_map.save("index.html")
