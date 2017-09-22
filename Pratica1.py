#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:37:36 2017

@author: labsim
"""

import numpy as np
import matplotlib.pyplot as plt 

i1,i2=0.8,0.3

theta= np.linspace(-3,3,1000)

L11=(3+np.cos(2*theta))*(10e-3)
L22=0.3*np.cos(theta)
L12=(30+10*np.cos(2*theta))

W=0.5*L11*i1**2 + L12*i1*i2 + 0.5*L22*i2**2 

T_total=np.diff(W)

W_relutancia=0.5*L11*i1**2+0.5*L22*i2**2
W_mutuo=L12*i1*i2

T_relutancia=np.diff(W_relutancia)
T_mutuo=np.diff(W_mutuo)

plt.figure(1)

plt.subplot(311)
plt.plot(theta[0:len(theta)-1],T_total,'r') # Cria o plot 
plt.title("Torque Total")
plt.ylabel("Torque [N.m]")
plt.xlabel("$\Theta$ [radianos]")
plt.grid()

plt.subplot(312)
plt.plot(theta[0:len(theta)-1],T_relutancia,'g')
plt.title("Torque de Relutancia")
plt.ylabel("Torque [N.m]")
plt.xlabel("$\Theta$ [radianos]")
plt.grid()

plt.subplot(313)
plt.plot(theta[0:len(theta)-1],T_mutuo,'b')
plt.title("Torque Mutuo")
plt.ylabel("Torque [N.m]")
plt.xlabel("$\Theta$ [radianos]")
plt.grid()

plt.tight_layout()
plt.show() #Mostra o Plot 
