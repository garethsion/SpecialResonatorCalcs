#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import csv
from vacuum_flucs import CPW
from process_data import SetParams
import Plotting
import os

#define the superconductor
setp = SetParams.SetParams()
params = setp.set_params()
w = params["w"]
t = params["t"]
l = params["l"]
pen = params["pen"]

#define the resonator - from CST or experiment
omega = params["omega"]
Z = params["Z"]

#define the 'mesh'
x = np.linspace(-w, w, int(1e04))

#instantiate Special CPW object
cpw = CPW.CPW(x,l,w,t,pen,Z,omega)

#solve for currents - not normalised
Js = cpw.J()

#normalise 
Jnorm = cpw.normalize_J()

I = cpw.current(norm='no')

#calculate electric field
E = cpw.E()

#calculate conductivity
sigma = cpw.conductivity()

paramlist = setp.param_list(x,I,Jnorm)

n = [abs(i) for i in x]
idx = n.index(min(n))

# I0 = I[idx]
# J0 = I0/(2*(w+t)*pen)
# pen_perp = pen**2 / (2*t)
# C = (0.506*np.sqrt(w/(2*pen_perp)))**0.75
# l1 = pen*np.sqrt(2*pen/pen_perp)
# l2 = 0.774*pen**2/pen_perp + 0.5152*pen_perp
# J2overJ1 = (1.008/np.cosh(t/pen)*np.sqrt(w/pen_perp/
# 	(4*pen_perp/pen - 0.08301*pen/pen_perp)))

J1 = Jnorm[idx]
print(J1)

#save data to csv file
currentDensityFile = str(os.getcwd() + "/data_preprocess/current_density.csv")
np.savetxt(currentDensityFile, np.column_stack((x,Jnorm)), delimiter=",")

eFile = str(os.getcwd() + "/data_preprocess/electric_field.csv")
np.savetxt(eFile, np.column_stack((x,E)), delimiter=",")

condFile = str(os.getcwd() + "/data_preprocess/conductivity.csv")
np.savetxt(condFile, np.column_stack((x,sigma)), delimiter=",")

plts = Plotting.Plotting

plt0 = plts.plot(x*1e6,I,colr = 'b',xlab='x ($\mu$m)',
	ylab='$Current (A/m)$',filename='current.eps',
	show='yes',save='no')

plt1 = plts.plot(x*1e6,Jnorm*1e6,colr='r',xlab='x ($\mu$m)',
	ylab='Current density\n (MAm$^{-2}$)',
	filename='current_density.eps',show='yes',save='yes')

plt2 = plts.plot(x*1e6,sigma,colr='g',xlab='x ($\mu$m)',
	ylab='Conductivity\n ($S/m}$)',
	filename='conductivity.eps',show='no',save='yes')

plt3 = plts.plot(x*1e6,E,colr='b',xlab='x ($\mu$m)',
	ylab='Electric Field\n ($V/m$)',
	filename='e_files.eps',show='no',save='yes')
