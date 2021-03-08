#Calculates the velocity distribution inside a halo

from pygadgetreader import *

from scipy import*
import numpy as np
from pylab import*
from scipy.spatial import distance
import matplotlib.pyplot as plt
from io import StringIO
import matplotlib.ticker


##################input######################

dir=r'C:\Users\rakshak\OneDrive\Documents\JAN2021 simulations\L01N256\L01N256_011821_2CDM_power00_sigma1'
ahf= '%s/ahf_011821_2CDM_005.0000.00000.AHF_halos' % (dir)

snap = '%s/snap_011821_2CDM_005' % (dir)

row_number=0
for row_number in range(0,15):
    #The halo you want to use from AHF , stored as each row in AHF halo output

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
    '''
    COM_x=1.9369*1000
    COM_y=2.2085*1000
    COM_z=2.0315*1000
    Radius=129.92
    '''


    print(COM_x,COM_y,COM_z,Radius)

    DMpos=readsnap(snap,'pos','dm',units=0)

    DMvel=readsnap(snap,'vel','dm',units=0)

    vx = DMvel[:,0]
    vy = DMvel[:,1]
    vz = DMvel[:,2]


    x = DMpos[:,0]
    y = DMpos[:,1]
    z = DMpos[:,2]

    ##test
    print('the centre of mass coordinates are', COM_x ,COM_y ,COM_z )
    print('The Radius is',Radius)

    print('this is the max pos ',max(x))
    print('this is the max velocity_x ',max(vx))


    ##test

    #make an array of velocities of particles in the halo

    i=0
    distance=0
    Velocity=[]  #This Will be the list of all the (absolute) velocity values
    Absolutevelocity=0
    print('lenght of dmpos',len(DMpos))

    for i in range(0,len(DMpos)):
        distance=((COM_x-x[i])**2+(COM_y-y[i])**2+(COM_z-z[i])**2)**0.5
        #print('i=',i,'distance=',distance,'radius=',Radius)
        if distance<Radius:
            Absolutevelocity=(vx[i]**2+vy[i]**2+vz[i]**2)**0.5
            #print('absvel=',Absolutevelocity)
            Velocity.append(Absolutevelocity)


    print('This is the number of particles inside the halo =',len(Velocity))

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


    Vdistribution1=[]        #This the the thing that we shall plot along the bin
    i=0
    for i in range(0, len(Bin1)):
        j=0
        Temp=[] #This is the temporary array the length of which will give us the number of particles with velocities in the range
        for j in range(0,len(Velocity)):
            if Velocity[j]>Bin1[i]:
                if Velocity[j]<Bin1[i+1]:
                    Temp.append(Velocity[j])
                    #print(Velocity[j], 'is greater than',Bin1[i],'and less than',Bin1[i+1])
                    #print('Secondary iteration, j=',j)
                           
                           
        Vdistribution1.append(len(Temp))
        


    #print(Vdistribution1)
          
    fig,ax=plt.subplots()
    ax.plot(Bin1, Vdistribution1)

    fig.suptitle('Distribution inside Halo L5N128 2CDM ', fontsize=14, fontweight='bold')



    plt.yscale("log")
    plt.xscale("log")

    plt.grid(True, which="both", ls="-")

    #ax.set_xticks([10,20,30,40,50])
    #ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())


    plt.title("Radius ="+str(Radius)+"#particles="+str(numberofparticles)+'COMx= '+str(COM_x))
    plt.xlabel("Velocity (km/sec)")
    plt.ylabel("Halo Number")
    plt.legend()
    #plt.show()
    output_filename = 'Particle_distribution_inside_halo_L5N128_2cdm'+str(numberofparticles) + '.png'

    print(output_filename)
    plt.savefig(output_filename)
    #plt.show()



