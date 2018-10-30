#!/usr/bin/env python 
import numpy as np
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

    def purcell_rate(self,Q,*args,**kwargs):
        # Calculates the Purcell rate
        k = self.omega_0 / Q
        omega_s = kwargs.get('omega_s',omega_0)
        delta = omega_0 - omega_s
        
        purcell = k * ((self.g**2) / (k**2) / (4 + delta**2))
        return purcell

    def purcell_factor(self,lambda_c,n,Q):
        # Calculates the Purcell enhancement induced by the cavity
        F = ( 3 / (4*np.pi**2) ) * (lambda_c / n)**3 * ( Q / (self.w * self.t * self.l))
        return F 

    def cooperativity(self):
        return

    def finesse(self):
        return

    