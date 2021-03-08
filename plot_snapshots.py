
import os

from pygadgetreader import *
from numpy import *
from scipy import *

from pylab import *
#import math
import matplotlib.pyplot as plt

#import matplotlib.colors as colors
#import matplotlib.cm as cmx

from matplotlib.colors import LogNorm

fig = plt.figure()

#ax = fig.add_subplot(1,1,1)
ax = plt.axes(projection='3d')


fig.patch.set_facecolor('white')

ax.set_xlabel(r'$x$',fontsize=20)
ax.set_ylabel(r'$y$',fontsize=23)

dir=r'G:\Cluster Backup\L5N64_2cdm_sigma1\L5N64_2cdm_sigma1_snaps'



snapnumber=0
for snapnumber in range(0,19):
    num=str(snapnumber)
    num1='00'+num
    num2=num1[-3:]
    name='snap_'+num2
    
    
    print(name)
    snap1 = '%s/snap_'+num2
    snap= snap1 % (dir)
    print("this is snap name:"+snap)
    DMpos=readsnap(snap,'pos','dm',units=0)
    DMmass = readsnap(snap,'mass','dm')

    #print(DMmass, len(DMmass))

    x = DMpos[:,0]
    y = DMpos[:,1]
    z = DMpos[:,2]


    print(x)



    #ax.plot(x, y,'o', color='k')
    #ax.hist2d(x,y,bins=150,norm=LogNorm())

    ax.plot3D(x, y, z,'o', color='crimson',markersize=0.0018 ,alpha=0.5)

    print(dir)
    print(snap)

    namie = snap[-8:]


    output_filename = namie + '.png'

    print(output_filename)
    plt.savefig(output_filename)







    



