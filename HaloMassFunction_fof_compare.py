import h5py
import numpy as np
import matplotlib.pyplot as plt

#cdm file
file1=h5py.File('/Users/rakshakadhikari/Desktop/L05N512_cdm_2cdm_alllight_delm0_cosntcross100/L01N512_060221_CDM/fof_subhalo_tab_005.hdf5','r')

#2cdm file
file2=h5py.File('/Users/rakshakadhikari/Desktop/L05N512_cdm_2cdm_alllight_delm0_cosntcross100/L05N512_060221_2CDM_const100_delm0_all_light/fof_subhalo_tab_005.hdf5','r')

#print((file.keys()))

Subhalo1=file1.get('Subhalo')
SubhaloMass1=np.array(Subhalo1['SubhaloMass'])
SubhaloMass1=10**10*SubhaloMass1 #converting to solar masses


Subhalo2=file2.get('Subhalo')
SubhaloMass2=np.array(Subhalo2['SubhaloMass'])
SubhaloMass2=10**10*SubhaloMass2 #converting to solar masses

#Get Redshift, boxsize, n_particle
Redshift="{:.2e}".format(file1['Header'].attrs['Redshift'])
Boxsize=int((file1['Header'].attrs['BoxSize']))





a=min(min(SubhaloMass1),min(SubhaloMass2))/2
Mass_Bins=[]
i=1
while a<max(max(SubhaloMass1),max(SubhaloMass2)):
    Mass_Bins.append(a)
    a=np.power(2,i/2)*min(min(SubhaloMass1),min(SubhaloMass2))/2
    i=i+1

print('MassBins Created Sucesfully')
print(Mass_Bins)


i=0
j=0
N_halo_cdm=[]
for i in range(0,len(Mass_Bins)):
    array=[]
    for j in range(0,len(SubhaloMass1)):
            if SubhaloMass1[j]>Mass_Bins[i]:
                array.append(SubhaloMass1[j])
    N_halo_cdm.append(len(array))
    
    #MassBins.pop(0)


i=0
j=0
N_halo_2cdm=[]
for i in range(0,len(Mass_Bins)):
    array=[]
    for j in range(0,len(SubhaloMass2)):
            if SubhaloMass2[j]>Mass_Bins[i]:
                array.append(SubhaloMass2[j])
    N_halo_2cdm.append(len(array))



    #fig,ax=plt.subplots()
plt.rcParams["figure.figsize"] = (6,6)
plt.plot(Mass_Bins, N_halo_cdm,label='cdm')
plt.plot(Mass_Bins, N_halo_2cdm,label='2cdm')


plt.plot([],[],label='L '+str(Boxsize)+' kpc')


plt.yscale("log")
plt.xscale("log")
plt.legend();


plt.grid(True, which="both", ls="-")




plt.title('Halo Mass Distribution L'+str(Boxsize)+', z= '+Redshift)
plt.xlabel("HaloMass ($M_{\odot}$)")
plt.ylabel("Halo Number")


output_filename=('Halo_Mass_Distribution_L'+str(Boxsize)+'_z_'+Redshift+'.png')
plt.savefig('/Users/rakshakadhikari/Desktop/L05N512_cdm_2cdm_alllight_delm0_cosntcross100/plots_L05N512/'+ output_filename,dpi=150)
plt.show()
file1.close()

















