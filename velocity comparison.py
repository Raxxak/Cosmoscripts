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





dir=r'C:\Users\rakshak\OneDrive\Documents\particle distribution comparison'



snapnumber=0

###########################CDM#####################################
for snapnumber in range(19,20):
    num=str(snapnumber)
    num1='00'+num
    num2=num1[-3:]
    name='snap_'+num2
    snapp1 = '%s/snap_L5N128_cdm_'+num2
    snap1= snapp1 % (dir)
    print(snap1)

    

    DMvel1=readsnap(snap1,'vel','dm',units=0)
    Vx1 = DMvel1[:,0]
    Vy1 = DMvel1[:,1]
    Vz1 = DMvel1[:,2]

    





    # we shall take the absolute value of the velocities
  
    V_abs1=[]
    a=0
    i=0
    for i in range(0, len(DMvel1)):
        a=sqrt(Vx1[i]*Vx1[i]+Vy1[i]*Vy1[i]+Vz1[i]*Vz1[i])
        V_abs1.append(a)   


    # make a bin for the velocities

                   
    Vinitial1=min(V_abs1)-0.5*min(V_abs1)
    Vfinal1=max(V_abs1)
    Bin1=[]
    v=0
    i=0
    while v<Vfinal1:
        v=np.power(1.08,i)*Vinitial1
        i=i+1
        #print(v)
        Bin1.append(v)        
    

    #    Here we do the magic
    Vdistribution1=[]        #This the the thing that we shall plot along the bin
    i=0
    for i in range(0, len(Bin1)):
        j=0
        Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
        for j in range(0,len(V_abs1)):
            if V_abs1[j]>Bin1[i]:
                if V_abs1[j]<Bin1[i+1]:
                    Temp.append(V_abs1[j])
                    #print('Secondary iteration, j=',j)
                       
                       
        Vdistribution1.append(len(Temp))
                   
                      
    #########################################  2CDM sigma 0.1 ##################
    name='snap_'+num2
    snapp2 = '%s/snap_L5N128_2cdm_sigma01_'+num2
    snap2= snapp2 % (dir)

    DMvel2=readsnap(snap2,'vel','dm',units=0)
    Vx2 = DMvel2[:,0]
    Vy2 = DMvel2[:,1]
    Vz2 = DMvel2[:,2]

    
    # we shall take the absolute value of the velocities
  
    V_abs2=[]
    a=0
    i=0
    for i in range(0, len(DMvel2)):
        a=sqrt(Vx2[i]*Vx2[i]+Vy2[i]*Vy2[i]+Vz2[i]*Vz2[i])
        V_abs2.append(a)   

    # make a bin for the velocities

                   
    Vinitial2=min(V_abs2)-0.5*min(V_abs2)
    Vfinal2=max(V_abs2)
    Bin2=[]
    v=0
    i=0
    while v<Vfinal2:
        v=np.power(1.08,i)*Vinitial2
        i=i+1
        #print(v)
        Bin2.append(v)        
    

    #    Here we do the magic
    Vdistribution2=[]        #This the the thing that we shall plot along the bin
    Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
    i=0
    for i in range(0, len(Bin2)):
        j=0
        Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
        for j in range(0,len(V_abs2)):
            if V_abs2[j]>Bin2[i]:
                if V_abs2[j]<Bin2[i+1]:
                    Temp.append(V_abs2[j])
                    #print('Secondary iteration, j=',j)
                       
                       
        Vdistribution2.append(len(Temp))
                   
                    


    ############################## 2CDM constant crosssection 100##############################

    name='snap_'+num2
    snapp3 = '%s/snap_constantcrosssection1_newmass_'+num2
    snap3= snapp3 % (dir)

    DMvel3=readsnap(snap3,'vel','dm',units=0)
    Vx3 = DMvel3[:,0]
    Vy3 = DMvel3[:,1]
    Vz3 = DMvel3[:,2]

    
    # we shall take the absolute value of the velocities
  
    V_abs3=[]
    a=0
    i=0
    for i in range(0, len(DMvel3)):
        a=sqrt(Vx3[i]*Vx3[i]+Vy3[i]*Vy3[i]+Vz3[i]*Vz3[i])
        V_abs3.append(a)   

    # make a bin for the velocities

                   
    Vinitial3=min(V_abs3)-0.5*min(V_abs3)
    Vfinal3=max(V_abs3)
    Bin3=[]
    v=0
    i=0
    while v<Vfinal3:
        v=np.power(1.08,i)*Vinitial3
        i=i+1
        #print(v)
        Bin3.append(v)        
    

    #    Here we do the magic
    Vdistribution3=[]        #This the the thing that we shall plot along the bin
    Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
    i=0
    for i in range(0, len(Bin3)):
        j=0
        Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
        for j in range(0,len(V_abs3)):
            if V_abs3[j]>Bin3[i]:
                if V_abs3[j]<Bin3[i+1]:
                    Temp.append(V_abs3[j])
                    #print('Secondary iteration, j=',j)
                       
                       
        Vdistribution3.append(len(Temp))


    ###########PLOT##############        




         
    fig,ax=plt.subplots()
    ax.plot(Bin1, Vdistribution1,label='CDM')
    ax.plot(Bin2, Vdistribution2,label='2CDM sigma=0.1')
    ax.plot(Bin3, Vdistribution3,label='2CDM constant sigma = 1 new mass')




    #plt.yscale("log")
    #plt.xscale("log")

    plt.grid(True, which="both", ls="-")

    '''ax.set_xticks([10,20,30,40,50])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())'''


    plt.title("Particle Distribution L5N128 2CDM sigma 0.1 snap"+num2)
    plt.xlabel("Velocity (km/sec)")
    plt.ylabel("Halo Number")
    plt.legend()
    #plt.show()
    output_filename = 'Particle_distribution_comparison_L5N128_nolog'+num2 + '.png'

    print(output_filename)
    plt.savefig(output_filename)
    #plt.show()








                


                   
                   
       
