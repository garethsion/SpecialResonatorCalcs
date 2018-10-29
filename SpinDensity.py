#!/usr/bin/env python
from scipy import constants as sp
import os
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
from process_data import ReadComsol

# Read data from downloads
file_dbx = os.getcwd() + '/data_postprocess/downloads/comsol_datafiles/Bx_fullData.csv'
file_dby = os.getcwd() + '/data_postprocess/downloads/comsol_datafiles/By_fullData.csv'

rdx = ReadComsol.ReadComsol(file_dbx)
rdy = ReadComsol.ReadComsol(file_dby)

# Read csv file, and get x,y annd dbx/dby data for each
# blocked point in space
bx_x,bx_y,bx_z = rdx.read_full_data()
by_x,by_y,by_z = rdy.read_full_data()
#xax = np.linspace(float(bx_x[0]),float(bx_x[len(bx_x)-1]),len(bx_x))
dbx = np.asarray(bx_z).astype(np.float)
dby = np.asarray(by_z).astype(np.float)

# Calculate the single spin coupling for each site each grid point
theta = 0 # Angle the static magnetic field is applied on
ang = np.cos(theta)
ue = sp.physical_constants["Bohr magneton"][0]
g = [*map(lambda x,y: 0.47 * ue * np.sqrt(y**2 + x**2),dbx,dby)]
g = np.asarray([x / sp.h for x in g])

# Reshape g so we can append multiple values for each box section
g=g.reshape(len(g),1)
np.shape(g)

# Calculate the size of the boxes
bucket = bx_x.count(bx_x[0]) # number of samples for each point in space
x_box = abs(float(bx_x[bucket-1]) - float(bx_x[bucket]))
y_box = abs(float(bx_y[0]) - float(bx_y[1]))
z_box = x_box
volume = x_box * y_box * z_box

# Calculate number of spins in each cell
no_spins_in_box = 1e7
Ncell = round(no_spins_in_box * volume)

g = np.matlib.repmat(g, 1, Ncell)

# Calculate histogram
hist, edges = np.histogram(g, bins=500) # single spin
hist = hist * Ncell # with 3d box
hist = hist / sum(hist) # normalize
edges = edges[0:len(hist)] # shift bin edges to get the same length as data


fig = plt.figure(figsize=(10,8))
# plt.stem(edges,hist)
plt.bar(edges,height=hist)
plt.xlabel('$\\frac{g}{2\pi} (Hz)$',fontsize=24)
plt.ylabel('$\\rho(g)$',fontsize=24)
plt.show()

# # n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
# # 	alpha=0.7, rwidth=0.85)