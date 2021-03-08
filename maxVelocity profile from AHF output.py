#Calculates Maximum Velocity profile using amiga max velocity
#Rakshak Adhikari, 7/27/2020

from scipy import*
import numpy as np
from pylab import*
from scipy.spatial import distance
import matplotlib.pyplot as plt
from io import StringIO
import matplotlib.ticker





dir=r'C:\Users\rakshak\OneDrive\Documents\JAN2021 simulations\AHFcompare'


snapnumber=0
for snapnumber in range(2,20):
    num=str(snapnumber)
    num1='00'+num
    num2=num1[-3:]
    print('the number of this snapshot is'+num1)
    name_cdm='%s/snapoutput'+num2+'.0000.00000.AHF_halos'
    name_2cdm='%s/snapoutput_2cdm_'+num2+'.0000.00000.AHF_halos'

    
    
    
    AHFoutput_cdm= name_cdm % (dir)
    AHFoutput_2cdm= name_2cdm % (dir)

    #AHFoutput_cdm = '%s/snapoutput_cdm_005.AHF_halos' % (dir)
    #AHFoutput_2cdm = '%s/snapoutput_2cdm_005.AHF_halos' % (dir)


    MaxVel_cdm1=genfromtxt(AHFoutput_cdm,usecols=(10),unpack=True)
    MaxVel_2cdm1=genfromtxt(AHFoutput_2cdm,usecols=(10),unpack=True)



    #MaxVel1 has neg value too so we gotta take the absolute value


    ##################For CDM##################################

    MaxVel_cdm=[]
    for i in range(0,len(MaxVel_cdm1)):
        AbsVel_cdm=np.absolute(MaxVel_cdm1[i])
        MaxVel_cdm.append(AbsVel_cdm)


    print(min(MaxVel_cdm),max(MaxVel_cdm))



    #Gotta Create a maximum velocity bin

    a=min(MaxVel_cdm)-5
    MaxVel_cdmBin=[]
    while a<max(MaxVel_cdm):
        MaxVel_cdmBin.append(a)
        a=np.power(a,1.01)

    print('Maximum Velocity_cdm bin created sucessfully')
    print(MaxVel_cdmBin)
    print('Its length is')
    print(len(MaxVel_cdmBin))

    #Doing the magic here

    N_halo_cdm=[]
    i=0
    k=0
    for i in range(0,len(MaxVel_cdmBin)):
        TempArray=[]
        for k in range(0,len(MaxVel_cdm)):
                if MaxVel_cdm[k]> MaxVel_cdmBin[i]:
                    TempArray.append(MaxVel_cdm)

        N_halo_cdm.append(len(TempArray))
            
                    
                       
    #############MAx Vel for  2cdm###################

        MaxVel_2cdm=[]
    for i in range(0,len(MaxVel_2cdm1)):
        AbsVel_2cdm=np.absolute(MaxVel_2cdm1[i])
        MaxVel_2cdm.append(AbsVel_2cdm)


    print(min(MaxVel_2cdm),max(MaxVel_2cdm))



    #Gotta Create a maximum velocity bin

    b=min(MaxVel_2cdm)-5
    MaxVel_2cdmBin=[]
    while b<max(MaxVel_2cdm):
        MaxVel_2cdmBin.append(b)
        b=np.power(b,1.01)

    print('Maximum Velocity_2cdm bin created sucessfully')
    print(MaxVel_2cdmBin)
    print('Its length is')
    print(len(MaxVel_2cdmBin))

    #Doing the magic here

    N_halo_2cdm=[]
    i=0
    k=0
    for i in range(0,len(MaxVel_2cdmBin)):
        TempArray=[]
        for k in range(0,len(MaxVel_2cdm)):
                if MaxVel_2cdm[k]> MaxVel_2cdmBin[i]:
                    TempArray.append(MaxVel_2cdm)

        N_halo_2cdm.append(len(TempArray))

    #Plot Maximum Velocity Profile
        
    fig,ax=plt.subplots()
    ax.plot(MaxVel_cdmBin, N_halo_cdm, label='cdm')

    ax.plot(MaxVel_2cdmBin, N_halo_2cdm,label='2cdm')

    plt.yscale("log")
    plt.xscale("log")

    plt.grid(True, which="both", ls="-")

    '''ax.set_xticks([10,20,30,40,50])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())'''


    plt.title("Max Velocity Distribution L5N64 sigma0.1 cdm vs 2cdm for snap"+num2)
    plt.xlabel("Maximum Velocity (Km/s)")
    plt.ylabel("Halo Number")
    plt.legend()
    #plt.show()
    output_filename = 'cdm2cdm_comparison_L5N64_snap'+num2 + '.png'

    print(output_filename)
    plt.savefig(output_filename)
    #plt.show()










        

