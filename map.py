import folium
import pandas as pd
from branca.element import Template, MacroElement

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
                      icon=folium.Icon(color="darkpurple", icon="university", prefix="fa"),).add_to(my_map)

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

store_df = pd.read_csv('stores.csv')
for index in store_df.index:
    if store_df['Name'][index] == "Canadian Tire":
        icon_color = 'black'
    elif store_df['Name'][index] == "Loblaws":
        icon_color = 'lightgray'
    elif store_df['Name'][index] == "Longo's":
        icon_color = 'beige'
    else:
        icon_color = 'darkblue'
    text = """
           <h4> {} - {} </h4>
           <span><i> Wheelchair Facilities: </i></span>
           <ul>
                <li> Entrance: {} </li>
                <li> Elevator: {} </li>
                <li> Parking: {} </li>
           </ul>
           """.format(store_df['Name'][index],
                      store_df['Address'][index],
                      store_df['Entrance'][index],
                      store_df['Elevator'][index],
                      store_df['Parking'][index])
    folium.Marker(location=[store_df['Latitude'][index],
                            store_df['Longitude'][index]],
                  icon=folium.Icon(icon="shopping-cart", prefix="fa", color=icon_color),
                  popup=folium.Popup(html=text, max_width=250)).add_to(my_map)

template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
<div class='legend-title'>Legend</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:#49a6d8;opacity:0.9;'></span>Bank Branch and ATM</li>
    <li><span style='background:#5a3869;opacity:0.9;'></span>ATM only</li>
    <li><span style='background:#f09440;opacity:0.9;'></span>Branch only</li>
    <li><span style='background:black;opacity:0.9;'></span>Canadian Tire</li>
    <li><span style='background:#a3a3a3;opacity:0.9;'></span>Loblaws</li>
    <li><span style='background:#f7ca91;opacity:0.9;'></span>Longo's</li>
    <li><span style='background:#2766a0;opacity:0.9;'></span>Shoppers</li>
  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)

my_map.get_root().add_child(macro)


# renders Map
my_map.save("index.html")
