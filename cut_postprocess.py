#!/usr/bin/env python
import matplotlib.pyplot as plt
from process_data import ReadComsol,PostProcData
import Plotting
import numpy as np
from scipy import constants as sp

#read in 1d data from comsol for plotting
bx = ReadComsol.ReadComsol('comsol_datafiles/Bx.csv')
by = ReadComsol.ReadComsol('comsol_datafiles/By.csv')
bn = ReadComsol.ReadComsol('comsol_datafiles/normB.csv')

xx,Bx = bx.read_1D_comsol_data()
xy,By = by.read_1D_comsol_data()
xn,Bn = bn.read_1D_comsol_data()

#centre axis about 0
xx = xx - max(xx)/2
xy = xy - max(xy)/2
xn = xn - max(xn)/2

#calcualte single spin couplinng coefficient
pp = PostProcData.PostProcData()
g = pp.cut_line_single_spin_coupling(Bx,By)

rho = pp.cut_line_spin_density(g)
rho = rho / sum(rho)


lambda_c = 6e-03 # Will work out properly, but just testing for now
epsilon_r = 11.9
n = np.sqrt(epsilon_r) / sp.c # Dielectric constant
Q = 20000 # Will get this data from CST
F = pp.purcell_factor(lambda_c,n,Q)
print(F)

plts = Plotting.Plotting()

xaxes = [xx,xy,xn]
yaxes = [Bx,By,Bn]

# plt1 = plts.subplot(xaxes,yaxes,2,1,colr=['r','g'],xlab='x ($\mu$m)',
# 	ylab='$B(T)$',
# 	filename='b_field.eps',show='yes',save='yes')

# # # plt.figure(figsize=(6,4))
# # fig, (ax1, ax2) = plt.subplots(1,2,sharex=True,figsize=(10,6))
# # ax1.plot(xx,Bx,LineWidth=4,color='r',label='$\delta B_{x}$')
# # ax1.plot(xy,By,LineWidth=4,color='g',label='$\delta B_{y}$')
# # ax1.set_ylabel('$B(T)$',fontsize=28)
# # ax1.legend(fontsize=16)
# # fig.text(0.54,0, '$x (\mu m)$', ha='center',fontsize='28')
# # #plt.xlabel('x')
# # ax2.plot(xn,Bn,LineWidth=4,color='b',label='$\delta B_{norm}$')
# # ax2.legend(fontsize=16)
# # fig.tight_layout()
# # plt.savefig(str(os.getcwd() + '/figs/b_field_subs.eps'))
# # #plt.show()


# plt2 = plts.plot(xx,g,colr='b',xlab='x ($\mu m$)',
# 	ylab='$\\frac{g}{2 \pi} (Hz)$',filename='g_single_spin.eps',
# 	show='yes',save='yes')

plt3 = plts.plot(g,rho,colr='b',xlab='$\\frac{g}{2 \pi} (Hz)$',
	ylab='$\\rho(g)$',filename='g_density.eps',
	show='yes',save='yes')

