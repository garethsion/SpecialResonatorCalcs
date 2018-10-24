#!/usr/bin/env python
import numpy as np
import csv
from scipy import constants as sp

class CPW:
    def __init__(self,x,l,w,t,pen,Z,omega):
        self.x = x
        self.l = l
        self.w = w
        self.t = t
        self.pen = pen
        self.Z = Z
        self.omega = omega
        self.V = 1
    
    def J(self):
        ans = []
        for i in self.x:
            if abs(i) > self.w/2.:
                ans.append(0)
            elif abs(i) == self.w/2.:
                ans.append(1.165/self.pen*(self.w*self.t)**.5)
            elif abs(i) < self.w/2. and abs(i) > self.w/2. - self.pen**2/(2*self.t):
                ans.append(1.165/self.pen*(self.w*self.t)**.5*np.exp(-(self.w/2. - abs(i))*self.t/self.pen**2))
            else:
                ans.append((1 - (2*abs(i)/self.w)**2)**-.5)
        return np.asarray(ans)
    
    def normalize_J(self):
        #normalise 
        Js = self.J()
        dI = self.omega*(sp.hbar/(2*self.Z))**.5
        dx = self.x[1] - self.x[0]
        Jnorm = dI*Js/(self.t*dx*np.sum(Js))
        return Jnorm
    
    def current(self,*args,**kwargs):
        norm = kwargs.get('norm','yes')

        if norm=='yes':
            I = self.l * self.normalize_J()
        else:
            I = self.l * self.J()
        return I
    
    def resistance(self):
        R = self.V / self.current()
        return R
    
    def resistivity(self):
        A = self. w * self.t # Cross-sectional area of cpw
        rho = self.resistance() * (A / self.l)
        return rho
        
    def conductivity(self):
        G = 1/self.resistivity()
        return G
    
    def E(self):
        E = self.normalize_J() * self.conductivity()
        return E

    # def single_spin_coupling(self,Bx,By):
    #     ang = np.cos(0)
    #     ue = sp.physical_constants["Bohr magneton"][0]
    #     g = 0.47 * ue * np.sqrt(By**2 + (ang**2) * Bx**2)
    #     return g/sp.h

    # def spin_density(self,g):
    #     volume = g * self.t * self.l
    #     rho =  sp.m_e / volume
    #     return rho
#     if __name__ == '__main__':
#         main()
