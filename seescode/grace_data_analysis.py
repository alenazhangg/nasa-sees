""" Iterates through the ground tracks of the GRACE satellites
and adds the time that it passed through each location in 
regions.txt to a new .txt file.

A new .txt file will be created for each region containing the set 
of seconds after 2000 that the GRACE satellite passed through it.
"""
import numpy as np
import glob

def square_bounds(lat, lon):
	""" Returns the upper and lower longitude and latitude
	bounds that create a 3 degree x 3 degree square around the 
	specified location.
	"""

	points = []
	points.append(lat-1.5)
	points.append(lat+1.5)
	points.append(lon-1.5)
	points.append(lon+1.5)
	return points


# Storing path to relevant directories.
ground_path = '/Users/AlenaZ/NASA-SEES/grace_groundtrack_data/'
model_path = '/Users/AlenaZ/NASA-SEES/Model_Data_Grace_Sampling_Exercise/'
regions = '/Users/AlenaZ/NASA-SEES/regions.txt'
region_names = '/Users/AlenaZ/NASA-SEES/regionNames.txt'

# Only need to access ground tracks of 2008.
ground_tracks = glob.glob(groundPath + '2008*.latlon')
aod = glob.glob(modelPath + '*_AOD_*')
gldas = glob.glob(modelPath + '*GLDAS*')

rdata = np.loadtxt(regions, delimiter= ' ')
rnames = np.genfromtxt(regionNames, dtype = 'str')

for path in ground_tracks:
	tracks = np.loadtxt(path)

	for p in range(0, np.size(tracks, 0)):
		lat = tracks[p,1] # Second column contains latitude of GRACE.
		lon = tracks[p,2] # Third column contains latitude of GRACE.
		name = ""

		for region in range(0, rNames.size):
			name = rnames[region]
			rlat = rdata[region, 0] # Latitude of region.
			rlon = rdata[region, 1] # Longitude of region.

			bounds = square_bounds(rlat, rlon)

			if(bounds[0] <= dlat <= bounds[1] and bounds[2] <= dlon <= bounds[3]):
				# Writes a .txt file if GRACE passed through region
				# or creates new file if no .txt file exists.
				new_file = open('/Users/AlenaZ/NASA-SEES/timesgracepassed/' + name + '.txt', 'a' )
				new_file.write(str(tracks[p,0])+ " ")