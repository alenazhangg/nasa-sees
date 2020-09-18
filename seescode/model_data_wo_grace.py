""" Creates plots of the climate data (atmospheric variability versus time
and hydrological variability versus time) for each of the 24 regions.
"""
import matplotlib.pyplot as plt
import numpy as np
import os

directory = '/Users/AlenaZ/NASA-SEES/Model_Data_for_Grace_Sampling_Exercise'

for filename in os.listdir(directory):
	# Creates a plot with a specified size
	fig= plt.figure(figsize=(14,9))

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

		plt.xlabel("Hours past midnight, January 1st, 2008", fontsize = 25)
		plt.xticks(fontsize=20)
		plt.yticks(fontsize=20)

		# Saves each plot generated for the 24 regions in a specified folder
		plt.savefig("/Users/AlenaZ/NASA-SEES/MapsWithoutGRACE/" + filename[:filename.index('2008')] + 'noGRACE_plot.png', dpi=fig.dpi)
		plt.clf()
		
		