# 2019 NASA SEES 'Weighing Water' Team Project
The programs here generate plots used to determine specific anomolies in climate model data that NASA's GRACE (Gravity Recovery and Climate 
Experiment) satellite was unable to detect. 
<br /><br />
Plots of climate data for 24 specified regions were created with the **Matplotlib** and **NumPy** libraries of Python. Then, the set of times 
that the GRACE satellite passed over each of the regions was determined, and the corresponding
times were plotted onto the climate graphs. 
<br /><br />
The 24 regions of interest are plotted on the map below. The map was created using the **Cartopy** package of Python in
`seescode/map_visualizer.py`<br />
<img src= /mapvisualizer.png width="600">
<br /><br /><br />
Two sets of climate models were plotted, the Atmosphere and Ocean De-Aliasing Model (AOD), which measures atmospheric 
variability, and the Global Land Data Assimilation System (GLDAS), which measures hydrological variability.
The code used to generate the graphs, such as the ones below, can be found in `seescode/model_data_wo_grace.py`.
<img src= /MapsWithoutGRACE/BalticSea02_AOD_noGRACE_plot.png width="600"><br />
In the AOD graph, higher values on the y-axis correspond to higher levels of water.
<br /><br />
<img src= /MapsWithoutGRACE/BalticSea02_GLDAS_noGRACE_plot.png width="600"><br />
On the contrary, in the GLDAS graph, higher values on the y-axis correspond to lower levels of water.
<br /><br /><br />
The times that the GRACE satellite passed through each region was determined in `seescode/grace_data_analysis`. 
These times were plotted on the original climate graphs in `seescode/model_data_w_grace`. The full list of graphs 
can be found in the `MapsWithGRACE` folder. <br />
<img src= /MapsWithGRACE/BalticSea02_GLDAS_plot.png width="600">
<br /><br />
**Note:** Most of the data used in this program, including the region names, locations, and climate data, can be accessed in the `data` folder.
The GRACE satellite ground track data used in `seescode/grace_data_analysis` is available [here](https://utexas.app.box.com/s/5mhzi68tnqixt8rauafecgq906i4w73m).
 



