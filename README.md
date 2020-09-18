# 2019 NASA SEES 'Weighing Water' Team Project
With the **Matplotlib** and **NumPy** libraries of Python, created plots of climate data for 24 
specified regions. Determined when the GRACE satellite passed over each of the regions and plotted the corresponding
times onto the climate graphs. 
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
can be found in the `MapsWithGRACE` folder. 
<img src= /MapsWithGRACE/BalticSea02_GLDAS_plot.png width="600">
<br /><br />
The plots generated were analyzed to determine specific anomolies in the climate model data that GRACE was unable
to detect. 



