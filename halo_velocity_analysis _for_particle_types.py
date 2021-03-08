#Calculates the velocity distribution inside a halo
#12/19/2020
#DMtype=readsnap(snap,'SIDM_State',1) # thsi is Mark's Arepo imprementation


from pygadgetreader import *

from scipy import*
import numpy as np
from pylab import*
from scipy.spatial import distance
import matplotlib.pyplot as plt
from io import StringIO
import matplotlib.ticker


##################input######################

dir=r'C:\Users\rakshak\OneDrive\Documents\JAN2021 simulations\sigma10\L100N256_011721_2cdm_power00_sigma10_hdf5'
ahf= '%s/ahf_011721_2CDM_005.0000.00000.AHF_halos' % (dir)

snap = '%s/snap_011721_2CDM_005' % (dir)
name=ahf[64:72]

row_number=0
for row_number in range(0,100):
    #The halo you want to use from AHF , stored as rows in AHF halo output

    ###############################################


    numberofparticles_array=genfromtxt(ahf,usecols=(0),unpack=True)
    COM_x_array=genfromtxt(ahf,usecols=(2),unpack=True)
    COM_y_array=genfromtxt(ahf,usecols=(3),unpack=True)
    COM_z_array=genfromtxt(ahf,usecols=(4),unpack=True)

    Radius_array=genfromtxt(ahf,usecols=(9),unpack=True)




    #Position
    COM_x=COM_x_array[row_number]*1000
    COM_y=COM_y_array[row_number]*1000
    COM_z=COM_z_array[row_number]*1000
    Radius=Radius_array[row_number]
    numberofparticles=numberofparticles_array[row_number]
    

    


    print("Centre of mass coordinates and radius",COM_x,COM_y,COM_z,Radius)


    DMpos=readsnap(snap,'pos','dm',units=0)

    DMvel=readsnap(snap,'vel','dm',units=0)
    DMtype=readsnap(snap,'SIDM_State','dm') 


    vx = DMvel[:,0]
    vy = DMvel[:,1]
    vz = DMvel[:,2]


    x = DMpos[:,0]
    y = DMpos[:,1]
    z = DMpos[:,2]

    Velocity=[]
    i=0
    for i in range(0,len(vx)):
        distance=((COM_x-x[i])**2+(COM_y-y[i])**2+(COM_z-z[i])**2)**0.5
        if distance<=Radius:
            Velocity.append((vx[i]**2+vy[i]**2+vz[i]**2)**0.5)
        



    #make an array of velocities of particles in the halo

    i=0
    distance=0
    Velocity0=[]  #This Will be the list of all the (absolute) velocity values (for type 0, light)
    Absolutevelocity0=0

    for i in range(0,len(DMpos)):
        if DMtype[i]==0:
            distance=((COM_x-x[i])**2+(COM_y-y[i])**2+(COM_z-z[i])**2)**0.5
            #print('i=',i,'distance=',distance,'radius=',Radius)
            if distance<=Radius:
                Absolutevelocity0=(vx[i]**2+vy[i]**2+vz[i]**2)**0.5
                #print('absvel=',Absolutevelocity)
                Velocity0.append(Absolutevelocity0)
            
    i=0
    distance=0
    Velocity1=[]  #This Will be the list of all the (absolute) velocity values (for type 0, light)
    Absolutevelocity1=0

    for i in range(0,len(DMpos)):
        if DMtype[i]==1:
            distance=((COM_x-x[i])**2+(COM_y-y[i])**2+(COM_z-z[i])**2)**0.5
            #print('i=',i,'distance=',distance,'radius=',Radius)
            if distance<Radius:
                Absolutevelocity1=(vx[i]**2+vy[i]**2+vz[i]**2)**0.5
                #print('absvel=',Absolutevelocity)
                Velocity1.append(Absolutevelocity1)




    #make a bin for the velocity
    v_min=0.5*min(Velocity)
    v_max=max(Velocity)
    Bin1=[]
    v=0
    i=0
    while v<v_max:
        v=np.power(1.08,i)*v_min
        i=i+1
        #print(v)
        Bin1.append(v)


    #print('Bin',Bin1)



    #############Here we calculate the velocity distribution
    Vdistribution0=[]        #This the the thing that we shall plot along the bin
    i=0
    for i in range(0, len(Bin1)):
        j=0
        Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
        for j in range(0,len(Velocity0)):
            if Velocity0[j]>Bin1[i]:
                if Velocity0[j]<Bin1[i+1]:
                    Temp.append(Velocity0[j])
                    #print(Velocity[j], 'is greater than',Bin1[i],'and less than',Bin1[i+1])
                    #print('Secondary iteration, j=',j)
                           
                           
        Vdistribution0.append(len(Temp))


    Vdistribution1=[]        #This the the thing that we shall plot along the bin
    i=0
    for i in range(0, len(Bin1)):
        j=0
        Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
        for j in range(0,len(Velocity1)):
            if Velocity1[j]>Bin1[i]:
                if Velocity1[j]<Bin1[i+1]:
                    Temp.append(Velocity1[j])
                    #print(Velocity[j], 'is greater than',Bin1[i],'and less than',Bin1[i+1])
                    #print('Secondary iteration, j=',j)
                           
                           
        Vdistribution1.append(len(Temp))
        


    #print(Vdistribution1)
          
    fig,ax=plt.subplots()
    ax.plot(Bin1, Vdistribution1,label='heavy')
    ax.plot(Bin1, Vdistribution0, label='light')


    fig.suptitle('Distribution inside Halo L5N128 2CDM ', fontsize=14, fontweight='bold')



    plt.yscale("log")
    plt.xscale("log")

    plt.grid(True, which="both", ls="-")

    #ax.set_xticks([10,20,30,40,50])
    #ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())


    plt.title("Radius ="+str(Radius)+"#particles="+str(numberofparticles))
    plt.xlabel("Velocity (km/sec)")
    plt.ylabel("Halo Number")
    plt.legend()
    output_filename = 'Particle_distribution_type_inside_halo_'+str(name)+str(numberofparticles) + '.png'

    #print(output_filename)
    plt.savefig(output_filename)
    #plt.show()


