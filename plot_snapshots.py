#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:42:14 2021

@author: rakshakadhikari
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:11:59 2021

@author: rakshakadhikari
"""
import numpy as np
from scipy import *
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.spatial import distance
import h5py


snap = h5py.File('/Users/rakshakadhikari/Desktop/L05N512_cdm_2cdm_alllight_delm0_cosntcross100/L05N512_060221_2CDM_const100_delm0_all_light/snap_060221_2CDM_000.hdf5', 'r')
#snap = h5py.File('/Users/rakshakadhikari/Desktop/L05N512_cdm_2cdm_alllight_delm0_cosntcross100/L01N512_060221_CDM/snap_060221_CDM_000.hdf5', 'r')



Boxsize=int((snap['Header'].attrs['BoxSize']))
Redshift="{:.2e}".format(snap['Header'].attrs['Redshift'])





 

 
 

DM1=snap.get('PartType1')
Gas1=snap.get('PartType0')
Stars1=snap.get('PartType4')

DMpos=np.array(DM1['Coordinates'])
Gaspos=np.array(Gas1['Coordinates'])
Starpos=np.array(Stars1['Coordinates'])


         
DMpos=np.array(DMpos)
Gaspos=np.array(Gaspos)
Starpos=np.array(Starpos)

x1 = DMpos[:,0]
y1 = DMpos[:,1]
z1 = DMpos[:,2]

if len(Gaspos)!=0:
    x0 = Gaspos[:,0]
    y0 = Gaspos[:,1]
    z0 = Gaspos[:,2]

if len(Starpos)!=0:
    x4= Starpos[:,0]
    y4 = Starpos[:,1]
    z4= Starpos[:,2]


fig = plt.figure(figsize=(12,12))
ax = plt.axes(projection='3d')
fig.set_facecolor('black')
ax.set_facecolor('black') 
ax.grid(False) 
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False
title_obj=plt.title('2cdm snapshot with Redshift= ' +str(round(float(Redshift),2)))
#plt.getp(title_obj)
plt.setp(title_obj,color='w', fontsize=18)

ax.plot3D(x1,y1,z1,'o', color='cyan',markersize=0.4 ,alpha=0.5)
ax.plot3D(x0,y0,z0,'o', color='fuchsia',markersize=0.2 ,alpha=0.3)
ax.plot3D(x4,y4,z4,'o', color='green',markersize=0.7 ,alpha=0.9)

#newfig=fig[10:30,10:30]
fig.tight_layout()
output_filename='2cdmsnapshot''L'+str(Boxsize/1000)+'snap'+str(Redshift)+'.png'
plt.savefig('/Users/rakshakadhikari/Desktop/L05N512_cdm_2cdm_alllight_delm0_cosntcross100/plots_L05N512/'+ output_filename,dpi=150)

plt.show()