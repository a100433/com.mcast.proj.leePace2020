import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

#https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db
#https://marinecadastre.gov/ais/
'''
#COMBINE DATASETS INTO ONE
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv1.csv", index=False, encoding='utf-8-sig')

'''
df = pd.read_csv("combined_csv.csv")

#print(df.head())

#Box dimension for map
BBox = (df.LON.min(), df.LON.max(), 30.00, 44.00)

#print(BBox)

ruh_m = plt.imread("map.png")

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.LON, df.LAT, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting Spatial Data on America')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
plt.show()