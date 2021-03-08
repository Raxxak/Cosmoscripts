#Calculates Velocity distribution directly from Snapshot
#Rakshak Adhikari, 10/29/2020
from pygadgetreader import *

from scipy import*
import numpy as np
from pylab import*
from scipy.spatial import distance
import matplotlib.pyplot as plt
from io import StringIO
import matplotlib.ticker





dir=r'C:\Users\rakshak\OneDrive\Documents\L5N128_2CDM_sigma01'



snapnumber=0
for snapnumber in range(0,20):
    num=str(snapnumber)
    num1='00'+num
    num2=num1[-3:]
    name='snap_'+num2
    snap1 = '%s/snap_'+num2
    snap= snap1 % (dir)


    print(snap)
    

    DMvel=readsnap(snap,'vel','dm',units=0)
    Vx = DMvel[:,0]
    Vy = DMvel[:,1]
    Vz = DMvel[:,2]

    print(Vx)
    





    # we shall take the absolute value of the velocities
  
    V_abs=[]
    a=0
    i=0
    for i in range(0, len(DMvel)):
        a=sqrt(Vx[i]*Vx[i]+Vy[i]*Vy[i]+Vz[i]*Vz[i])
        V_abs.append(a)   




    print('The maximum and minimum velocities are')
    print(max(V_abs), min(V_abs))

    # make a bin for the velocities

                   
    Vinitial=min(V_abs)-0.5*min(V_abs)
    Vfinal=max(V_abs)
    Bin=[]
    v=0
    i=0
    while v<Vfinal:
        v=np.power(1.05,i)*Vinitial
        i=i+1
        #print(v)
        Bin.append(v)        
    print('This is your velocity bin',Bin)
    
    print('this is the lenght of the bin',Bin)

    #    Here we do the magic
    Vdistribution=[]        #This the the thing that we shall plot along the bin
    Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
    i=0
    for i in range(0, len(Bin)):
        j=0
        Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
        for j in range(0,len(V_abs)):
            if V_abs[j]>Bin[i]:
                if V_abs[j]<Bin[i+1]:
                    Temp.append(V_abs[j])
                    #print('Secondary iteration, j=',j)
                       
                       
        Vdistribution.append(len(Temp))
        #print('primary iteration i=',i)           
                      
    #Bin.pop(0)
            
    print(Bin)
    print(Vdistribution)

         
    fig,ax=plt.subplots()
    ax.plot(Bin, Vdistribution)
    #ax.plot(MaxVel_cdmBin, N_halo_cdm, label='cdm')

    #ax.plot(MaxVel_2cdmBin, N_halo_2cdm,label='2cdm')

    plt.yscale("log")
    plt.xscale("log")

    plt.grid(True, which="both", ls="-")

    '''ax.set_xticks([10,20,30,40,50])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())'''


    plt.title("Particle Distribution L5N128 2CDM sigma 0.1 snap"+num2)
    plt.xlabel("Velocity (km/sec)")
    plt.ylabel("Halo Number")
    plt.legend()
    #plt.show()
    output_filename = 'Particle_distribution_L5N128_2cdm_sigma01'+num2 + '.png'

    print(output_filename)
    plt.savefig(output_filename)
    #plt.show()








                


                   
                   
       
