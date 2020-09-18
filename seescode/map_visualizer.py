""" Creates a map with all 24 regions plotted with 
the Cartopy package.
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

regions = open("/Users/AlenaZ/NASA-SEES/regions.txt", "r")
region_names = open("/Users/AlenaZ/NASA-SEES/regionNames.txt", "r")

coordinates = regions.readlines()
names = region_names.readlines()

for i in range(0, len(names):
	lat = float(coordinates[i].split()[0])

	if float(coordinates[i].split()[1]) < 180:
		lon = float(coordinates[i].split()[1])
	else:
		# Longitude in file ranges from 0 to 360 degrees but longitude
		# must range from -180 to 180 degrees to be compatible with map.
		lon = float(coordinates[i].split()[1]) - 360

	plt.plot([lon], [lat], marker='o', markersize=3, color="blue")

	if(i % 2 == 0):
		namelon = lon - 3
		alignment = 'right'
	else:
		namelon = lon + 3
		alignment = 'left'

	# Creates a label next to the plotted point.
	plt.text(namelon, lat-6, names[i], fontsize=13, horizontalalignment = alignment)

plt.show()
