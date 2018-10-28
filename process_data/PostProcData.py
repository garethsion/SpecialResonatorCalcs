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
            	
    def single_spin_coupling(self,Bx,By,*args,**kwargs):
        theta = kwargs.get('theta',0)
        ang = np.cos(theta)
        ue = sp.physical_constants["Bohr magneton"][0]
        g = 0.47 * ue * np.sqrt(By**2 + (ang**2) * Bx**2)
        return g/sp.h

    def spin_density(self,g):
        volume = g * self.t * self.l
        rho =  sp.m_e / volume
        return rho

    def cooperativity(self):
        return

    def finesse(self):
        return

    