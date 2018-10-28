#!/usr/bin/env python
from scipy import constants as sp
import os
import numpy as np
import matplotlib.pyplot as plt
from process_data import ReadComsol

file_dbx = os.getcwd() + '/data_postprocess/downloads/comsol_datafiles/Bx_fullData.csv'
file_dby = os.getcwd() + '/data_postprocess/downloads/comsol_datafiles/By_fullData.csv'

rdx = ReadComsol.ReadComsol(file_dbx)
rdy = ReadComsol.ReadComsol(file_dby)

# Seperate the datafile into blocks for each point in space
bx_x,bx_y,bx_z = rdx.read_full_data()
by_x,by_y,by_z = rdy.read_full_data()
xax = np.linspace(float(bx_x[0]),float(bx_x[len(bx_x)-1]),len(bx_x))

theta = 0
ang = np.cos(theta)
ue = sp.physical_constants["Bohr magneton"][0]

dbx = np.asarray(bx_z).astype(np.float)
dby = np.asarray(by_z).astype(np.float)

# Single spin coupling for each grid point
g = [*map(lambda x,y: 0.47 * ue * np.sqrt(y**2 + x**2),dbx,dby)]
g = np.asarray([x / sp.h for x in g])

fig = plt.figure(figsize=(6,4))
plt.plot(xax,g)
plt.show()
