import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Arquivo
df = pd.read_csv('brazilian_cities_geo.csv')

# Mapa com localização baseada na latitude e longitude média
mapa = folium.Map(
    location=[df['city_latitude'].mean(), df['city_longitude'].mean()],
    zoom_start=5,
    tiles="Cartodb Positron",
    control_scale=True,
    zoom_control=True
)

# Marcadores ao mapa com MarkerCluster
marker_map = MarkerCluster().add_to(mapa)
for index, row in df.iterrows():
    # Estrutura do popup
    popup_content = f"""
    <div style="font-family: Arial, sans-serif; font-size: 14px; color: #333;">
        <strong style="font-size: 16px; color: #2a7ae2;">{row['city_name']}</strong><br>
        <span style="color: #555;">Estado:</span> {row['state_name']}<br>
        <span style="color: #555;">Região:</span> {row['region']}<br>
        <span style="color: #555;">IBGE:</span> {row['code_ibge']}<br>
        <span style="color: #555;">Latitude:</span> {row['city_latitude']}<br>
        <span style="color: #555;">Longitude:</span> {row['city_longitude']}<br>
    </div>
    """
    popup = folium.Popup(popup_content, max_width=300)
    
    # Marcadores no mapa
    folium.Marker(
        location=[row['city_latitude'], row['city_longitude']],
        popup=popup,
        tooltip=row['city_name'],
    ).add_to(marker_map)

# Arquivo HTML
mapa.save('mapa.html')