#!/usr/bin/env python
from scipy import constants as sp
import os
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
from process_data import ReadComsol,PostProcData
import Plotting

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

post = PostProcData.PostProcData()

# hist, edges = post.spin_density(bx_x,bx_y,g)

# Calculate Purcell enhancement at each grid point
Q = 10000 # Q factor - for now typed in, but will be found from CST calcs ultimately
purcell = post.purcell_rate(g,Q)
plt.plot(g,purcell)
plt.show()

pdens, pedge = post.purcell_density(bx_x,bx_y,purcell)

plt.bar(pdens,height=pedge,alpha=0.15)
plt.plot(pedge,pdens)
plt.show()

# plt.plot(pdens,hist)
# plt.show()
# fig, ax = plt.subplots(figsize=(6,4))
# ax1 = plt.subplot(1,2,1)
# ax1.bar(edges,height=hist,alpha=0.15)
# ax1.plot(edges,hist)
# ax1.set_xlabel('$\\frac{g}{2 \pi} (Hz)$',fontsize='24')
# ax1.set_ylabel('$\\rho(g)$',fontsize='24')
# plt.tight_layout()

# ax2 = plt.subplot(1,2,2)
# #ax.bar(pedge,height=pdens,alpha=0.15)
# ax2.plot(pedge,pdens)
# ax2.set_xlabel('$\Gamma_{p}$',fontsize='24')
# ax2.set_ylabel('$\\rho(g)$',fontsize='24')
# plt.tight_layout()
# plt.show()

# plt.savefig(str(os.getcwd() + '/figs/' + filename))

# plts = Plotting.Plotting()

# plt1 = plts.barplot(edges,hist,colr='b',xlab='$\\frac{g}{2 \pi} (Hz)$',
# 	ylab='$\\rho(g)$',filename='g_density.eps',
# 	show='yes',save='no')

# # n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
# # 	alpha=0.7, rwidth=0.85)