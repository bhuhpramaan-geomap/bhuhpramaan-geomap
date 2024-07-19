import folium
import pandas as pd
import matplotlib.pyplot as plt

# Data for population density of Bangalore from 2000 to 2023
years = list(range(2000, 2024))
population_density = [
    11300, 11600, 11900, 12200, 12500, 12800, 13100, 13400, 13700, 14000,
    14300, 14600, 14900, 15200, 15500, 15800, 16100, 16400, 16700, 17000,
    17300, 17600, 17900, 18200
]

# Create a DataFrame
data = {'Year': years, 'PopulationDensity': population_density}
df = pd.DataFrame(data)

# Plot population density over the years
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['PopulationDensity'], marker='o')
plt.title('Population Density of Bangalore (2000-2023)')
plt.xlabel('Year')
plt.ylabel('Population Density (per km²)')
plt.grid(True)
plt.show()

# Create a map of Bangalore
bangalore_coordinates = [12.9716, 77.5946]
bangalore_map = folium.Map(location=bangalore_coordinates, zoom_start=12)

# Adding population density information as a popup
for year, density in zip(df['Year'], df['PopulationDensity']):
    folium.Marker(
        location=bangalore_coordinates,
        popup=f'Year: {year}, Population Density: {density} per km²'
    ).add_to(bangalore_map)

# Save map to HTML file
bangalore_map.save('bangalore_population_density_map.html')

print("Map and population density plot created successfully. Check the generated HTML file for the map.")
