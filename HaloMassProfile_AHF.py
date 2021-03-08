#Calculates HaloMAss profile from AHF output
#Rakshak Adhikari, 10/1/2020

from scipy import*
import numpy as np
from pylab import*
from scipy.spatial import distance
import matplotlib.pyplot as plt
from io import StringIO





dir=r'C:\Users\rakshak\OneDrive\Desktop\CDM-2CDM compare'

snapnumber=0
for snapnumber in range(2,19):
    num=str(snapnumber)
    num1='00'+num
    num2=num1[-3:]
    print('the number of this snapshot is'+num1)
    name_cdm='%s/snapoutput'+num2+'.0000.00000.AHF_halos'
    name_2cdm='%s/snapoutput_2cdm_'+num2+'.0000.00000.AHF_halos'

    
    
    print(name_cdm)
    
    print(name_2cdm)
    file_cdm = '%s/name_cdm'
    file_2cdm = '%s/name_2cdm'
    print(file_2cdm)
    print(file_cdm)
    AHFoutput_cdm= name_cdm % (dir)
    AHFoutput_2cdm= name_2cdm % (dir)



    Mass_cdm=genfromtxt(AHFoutput_cdm,usecols=(8),unpack=True)
    Mass_2cdm=genfromtxt(AHFoutput_2cdm,usecols=(8),unpack=True)



    #Creates Mass Bins

    ###################For CDM#####################

    a=min(Mass_cdm)/2
    Mass_cdmBins=[]
    i=1
    while a<max(Mass_cdm):
        Mass_cdmBins.append(a)
        a=np.power(2,i/2)*min(Mass_cdm)
        i=i+1

    print('MassBins Created Sucesfully')
    print(Mass_cdmBins)


    i=0
    j=0
    N_halo_cdm=[]
    for i in range(0,len(Mass_cdmBins)):
                   array=[]
                   for j in range(0,len(Mass_cdm)):
                           if Mass_cdm[j]>Mass_cdmBins[i]:
                               array.append(Mass_cdm[j])
                   N_halo_cdm.append(len(array))        
    #MassBins.pop(0)


    print('Here is the Number-of-halo Array:')
    print(N_halo_cdm)




    #####################For 2CDM ###############################

    b=min(Mass_2cdm)/2
    Mass_2cdmBins=[]
    i=1
    while b<max(Mass_2cdm):
        Mass_2cdmBins.append(b)
        b=np.power(2,i/2)*min(Mass_2cdm)
        i=i+1

    print('Mass_2cdmBins Created Sucesfully')
    print(Mass_2cdmBins)


    i=0
    j=0
    N_halo_2cdm=[]
    for i in range(0,len(Mass_2cdmBins)):
                   array=[]
                   for j in range(0,len(Mass_2cdm)):
                           if Mass_2cdm[j]>Mass_2cdmBins[i]:
                               array.append(Mass_2cdm[j])
                   N_halo_2cdm.append(len(array))        
    #MassBins.pop(0)


    print('Here is the Number-of-halo Array:')
    print(N_halo_2cdm)
    #Plot Halo Mass distribution




    #fig,ax=plt.subplots()
    plt.rcParams["figure.figsize"] = (6,6)
    plt.plot(Mass_cdmBins, N_halo_cdm, label='cdm')
    plt.plot(Mass_2cdmBins, N_halo_2cdm,label='2cdm')




    plt.yscale("log")
    plt.xscale("log")
    plt.legend();


    plt.grid(True, which="both", ls="-")




    plt.title('Halo Mass Distribution(L5N64,snap'+num2+')')
    plt.xlabel("HaloMass ($M_{\odot}$)")
    plt.ylabel("Halo Number")

    output_filename = 'Halo_mass proflie_cdm2cd_L5N64_snap'+num2 + '.png'

    print(output_filename)
    plt.savefig(output_filename)
    plt.show()






