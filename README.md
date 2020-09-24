# 2019 NASA SEES 'Weighing Water' Team Project
In this project, we used real data from climate models to investigate the gravitational anomalies of 24 specified regions around the world that the GRACE (Gravity Recovery and Climate Experiment) satellite was unable to capture. 
<br />
## Background
The GRACE satellite creates a map of Earth's gravitational field every 30 days. As mass affects gravity and water has mass, the GRACE satellite can effectively measure water variations on Earth. More specifically, GRACE measures variations in the gravitational field due to runoff, groundwater, water storage, and fluctuating ocean levels. 

Gravitational anomalies are caused by unusual concentrations of mass in an area. Gravitational anomalies such as mountains or trenches will consistently be captured by GRACE, but since the orbital geometry of the GRACE satellites means that it makes a global map only every 30 days, there are major short-term gravitational anomalies, such as floods, that occur without being detected by GRACE.

In this project, we investigated the gravitational anomalies of 24 specified regions around the world. The regions can be found in the `data/regions.txt` folder. They are also shown in the map below, which was created using the **Cartopy** package of Python in `seescode/map_visualizer.py`<br />
<img src= /mapvisualizer.png width="600"><br />

## Methodology
**Phase 1**: Plot data from climate models for specific regions <br /> <br />
Two sets of climate models were plotted, the Atmosphere and Ocean De-Aliasing Model (AOD), which measures atmospheric 
variability, and the Global Land Data Assimilation System (GLDAS), which measures hydrological variability. These two models are used as a reference to detect the short-term variations that the GRACE satellite missed in the subsequent phases of the project. <br />
The code used to generate the graphs, such as the ones below, can be found in `seescode/model_data_wo_grace.py`.

Plots of climate data for 24 specified regions were created with the **Matplotlib** and **NumPy** libraries of Python. 
<br /><br />
<img src= /MapsWithoutGRACE/BalticSea02_AOD_noGRACE_plot.png width="600"><br />
In the AOD graph, higher values on the y-axis correspond to higher levels of water.
<br /><br />
<img src= /MapsWithoutGRACE/BalticSea02_GLDAS_noGRACE_plot.png width="600"><br />
On the contrary, in the GLDAS graph, higher values on the y-axis correspond to lower levels of water.
<br /><br /><br />

**Phase: 2**: Determine when GRACE visited each region and plot times on climate graphs <br /> <br />
By using the GRACE satellite's ground track data (available [here](https://utexas.app.box.com/s/5mhzi68tnqixt8rauafecgq906i4w73m)), the set of times 
that the GRACE satellite passed over each of the regions was determined, and the corresponding times were plotted onto the climate graphs. <br/>
These times were plotted on the original climate graphs in `seescode/model_data_w_grace.py`. The full list of graphs can be found in the `MapsWithGRACE` folder. <br />
<img src= /MapsWithGRACE/BalticSea02_GLDAS_plot.png width="600"><br />
In the graph above, each red dot represents when the GRACE satellite passed over each region and was able to capture changes in hydrological variability. There are many sections of the line with no red dot on it, and these gaps represent time periods where GRACE was unable to capture any data. 
<br /><br /><br />
**Phase: 3**: Investigate anomalies in climate data that GRACE was unable to capture <br /> <br />
To provide a more specific example of a short-term variation GRACE was unable to capture, we can analyze the atmospheric variability of the Baltic Sea. In the graph below, there are many steep drops and spikes that are not captured by GRACE, as evidenced by the lack of red crosses on those parts. In the circled part around January 2008, there was a sharp drop in atmospheric variability that GRACE was not present to detect. From conducting research on the region, we found that the short-term drop in atmospheric variability in the Baltic Sea reflects the seasonal coastal flooding that the region experiences during the early months of the year. However, GRACE was unable to provide real-time updates on the impact of the flooding in the region.<br />
<img src= /images/BalticSeaExample.png width="550"><br />
<br />
## Future Improvements
Due to the relative low frequency of passes over regions, the GRACE satellite can miss short-term variations in hydrological variability or atmospheric variability. In order to improve the ability of future GRACE missions to detect these variations, our team proposed a satellite constellation consisting of three GRACE satellites. This will effectively increase the frequency of passes of GRACE over regions of the world. By being able to capture more short-term geographic phenomena, GRACE can also become a better resource to reference when deciding on emergency response measures to geographical disasters, such as flash flooding, and provide a more informative assessment of the impact of these disasters. <br />
<img src= /images/graceconstellations.gif width="500"><br />

**Note:** Most of the data used in this program, including the region names, locations, and climate data, can be accessed in the `data` folder.
The GRACE satellite ground track data used in `seescode/grace_data_analysis` is available [here](https://utexas.app.box.com/s/5mhzi68tnqixt8rauafecgq906i4w73m).
 



