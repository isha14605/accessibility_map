import folium
import pandas as pd

# initialize Map
my_map = folium.Map(location=[43.66430664668449, -79.39241763253044],
                    zoom_start=15)

# read banks.csv and convert it into a Dataframe
df = pd.read_csv('banks.csv')

# convert the Dataframe into a dictionary of dictionaries, with keys being the
# row number/index of the Dataframe and values being dictionaries (keys are
# column labels, such as Name, Address, Latitude, etc., and values are the
# corresponding value)
banks_dict = df.to_dict('index')

# loop through banks_dict
for i in range(df.shape[0]):
    # if the bank has a branch and an ATM at the current location, then color it blue (default)
    if banks_dict[i]['Branch'] == 'Y' and banks_dict[i]['ATM'] == 'Y':
        html = """
           <h4> {} - {} </h4>
           <span><i> Branch Facilities: </i></span>
           <ul>
                <li> Wheelchair Accessible: {} </li>
                <li> Barrier-Free Safe Deposit Boxes: {} </li>
                <li> Tablets for ASL: {} </li>
           </ul>
           <span><i> ATM Facilities: </i></span>
           <ul>
                <li> Wheelchair Accessible: {} </li>
                <li> Voice-Enabled: {} </li>
                <li> Braille: {} </li>
           </ul>
           """.format(banks_dict[i]['Name'],
                      banks_dict[i]['Address'],
                      banks_dict[i]['Wheelchair Accessible'],
                      banks_dict[i]['Barrier-free safe deposit boxes'],
                      banks_dict[i]['Tablets for ASL'],
                      banks_dict[i]['Wheelchair Accessible.1'],
                      banks_dict[i]['Voice-enabled'],
                      banks_dict[i]['Braille'])
        folium.Marker(location=[banks_dict[i]['Latitude'],
                                banks_dict[i]['Longitude']],
                      popup=folium.Popup(html=html,
                                         max_width=250),
                      icon=folium.Icon(icon="university", prefix="fa"),).add_to(my_map)

    # if the bank only has an ATM at the current location, then color it purple
    elif banks_dict[i]['Branch'] == 'N' and banks_dict[i]['ATM'] == 'Y':
        html = """
           <h4> {} - {} </h4>
           <span><i> ATM Facilities: </i></span>
           <ul>
                <li> Wheelchair Accessible: {} </li>
                <li> Voice-Enabled: {} </li>
                <li> Braille: {} </li>
           </ul>
           """.format(banks_dict[i]['Name'],
                      banks_dict[i]['Address'],
                      banks_dict[i]['Wheelchair Accessible.1'],
                      banks_dict[i]['Voice-enabled'],
                      banks_dict[i]['Braille'])
        folium.Marker(location=[banks_dict[i]['Latitude'],
                                banks_dict[i]['Longitude']],
                      popup=folium.Popup(html=html,
                                         max_width=250),
                      icon=folium.Icon(color="purple", icon="university", prefix="fa"),).add_to(my_map)

    # if the bank only has a branch at the current location, then color it orange
    else:
        html = """
           <h4> {} - {} </h4>
           <span><i> Branch Facilities: </i></span>
           <ul>
                <li> Wheelchair Accessible: {} </li>
                <li> Barrier-Free Safe Deposit Boxes: {} </li>
                <li> Tablets for ASL: {} </li>
           </ul>
           """.format(banks_dict[i]['Name'],
                      banks_dict[i]['Address'],
                      banks_dict[i]['Wheelchair Accessible'],
                      banks_dict[i]['Barrier-free safe deposit boxes'],
                      banks_dict[i]['Tablets for ASL'])
        folium.Marker(location=[banks_dict[i]['Latitude'],
                                banks_dict[i]['Longitude']],
                      popup=folium.Popup(html=html,
                                         max_width=250),
                      icon=folium.Icon(color="orange", icon="university", prefix="fa"),).add_to(my_map)

# renders Map
my_map.save("index.html")
