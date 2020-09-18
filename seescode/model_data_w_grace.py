""" Creates plots of the climate data (atmospheric variability versus time
and hydrological variability versus time) with additional points plotted that 
correspond to when the GRACE satellite visited each region.
"""
import matplotlib.pyplot as plt
import numpy as np
import os, sys
import timeconversions

directory = '/Users/AlenaZ/NASA-SEES/Model_Data_for_Grace_Sampling_Exercise/'

for filename in os.listdir(directory):
	# Creates a plot with a specified size
	fig = plt.figure(figsize=(14,9))

	if filename.endswith(".txt"):
		holder = "/Users/AlenaZ/NASA-SEES/Model_Data_for_Grace_Sampling_Exercise/%s" % filename
		file = open(holder, "r")
		content = file.readlines()
		time = []
		cm = []

		# Adds all times and climate data taken from the region
		# to lists.
		for i in content:
			time.append(float(i.split()[1])) 
			cm.append(float(i.split()[3]))

		# Plots the relationship between time (x) and the climate data (y)
		plt.plot(time, cm)

		plt.title(filename[:len(filename)-4], fontsize =30)

		if "AOD" in filename:
			plt.ylabel("Atmospheric variability (cm)", fontsize = 25)
		else:
			plt.ylabel("Hydrological variability (cm)", fontsize = 25)

		plt.xlabel("2008", fontsize = 25)
		
		# Sets the x-axis labels to be months instead of hours.
		plt.xticks(timeconversions.monthstohours(), timeconversions.hourstomonths(), fontsize=20)
		
		plt.yticks(fontsize=20)

		# Stores path to the file containing the set of times GRACE passed through each region.
		path= '/Users/AlenaZ/NASA-SEES/timesgracepassed/'+ filename[:filename.index('_')]+'.txt'
		
		t_file=np.loadtxt(path)

		for xval in t_file:
			# Since xval is the number of seconds after 2000, it is converted to 
			# number of hours after 2008. 
			#
			# The y value of the corresponding time is then found.
			yval = np.interp((xval/3600)-70080,time,cm)

			# Plots the point on the graph.
			plt.plot((xval/3600)-70080,yval,'r+')

		# Saves each plot generated for the 24 regions in a specified folder
		plt.savefig('/Users/AlenaZ/NASA-SEES/MapsWithGrace/'+filename[:filename.index('2008')]+'plot.png', dpi=fig.dpi)
		plt.clf()