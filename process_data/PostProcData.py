#!/usr/bin/env python 
import numpy as np
import numpy.matlib
from scipy import constants as sp
from process_data import SetParams

class PostProcData:
    def __init__(self):
        setp = SetParams.SetParams()
        params = setp.set_params()
        self.w = params["w"]
        self.t = params["t"]
        self.l = params["l"]
        self.pen = params["pen"]

        #define the resonator - from CST or experiment
        self.omega = params["omega"]
        self.Z = params["Z"]
        self.g = None

        self.volume_cell = None
            	
    def cut_line_single_spin_coupling(self,Bx,By,*args,**kwargs):
        # Calculates the single spin coupling for a given grid area
        theta = kwargs.get('theta',0)
        ang = np.cos(theta)
        ue = sp.physical_constants["Bohr magneton"][0]
        self.g = 0.47 * ue * np.sqrt(By**2 + (ang**2) * Bx**2)
        return self.g/sp.h

    def cut_line_spin_density(self,g):
        self.volume_cell = g * self.t * self.l
        rho =  sp.m_e / self.volume_cell
        return rho

    def spin_density(self,x,y,g):
        Ncell = self.ncell(x,y,g)

        g = np.matlib.repmat(g, 1, Ncell)

        # Calculate histogram
        hist, edges = np.histogram(g, bins=500) # single spin
        hist = hist * Ncell # with 3d box
        hist = hist / sum(hist) # normalize
        edges = edges[0:len(hist)] # shift bin edges to get the same length as data

        return hist, edges

    def purcell_density(self,x,y,gamma):
        Ncell = self.ncell(x,y,gamma)

        gamma = np.matlib.repmat(gamma, 1, Ncell)

        # Calculate histogram
        hist, edges = np.histogram(gamma, bins=500) # single spin
        hist = hist * Ncell # with 3d box
        hist = hist / sum(hist) # normalize
        edges = edges[0:len(hist)] # shift bin edges to get the same length as data

        return hist, edges

    def ncell(self,x,y,param):
        # Reshape g so we can append multiple values for each box section
        param=param.reshape(len(param),1)

        # Calculate the size of the boxes
        bucket = x.count(x[0]) # number of samples for each point in space
        x_box = abs(float(x[bucket-1]) - float(x[bucket]))
        y_box = abs(float(y[0]) - float(y[1]))
        z_box = x_box
        volume = x_box * y_box * z_box

        # Calculate number of spins in each cell
        no_spins_in_box = 1e7
        Ncell = round(no_spins_in_box * volume)
        return Ncell

    def purcell_rate(self,g,Q,*args,**kwargs):
        # Calculates the Purcell rate
        k = self.omega / Q
        omega_s = kwargs.get('omega_s',self.omega)
        delta = self.omega - omega_s
        
        purcell = k * ((g**2) / (k**2) / (4 + delta**2))
        # purcell = (4*(g**2)) / k
        return purcell

    def purcell_factor(self,lambda_c,n,Q):
        # Calculates the Purcell enhancement induced by the cavity
        F = ( 3 / (4*np.pi**2) ) * (lambda_c / n)**3 * ( Q / (self.w * self.t * self.l))
        return F 

    def cooperativity(self):
        return

    def finesse(self):
        return

    