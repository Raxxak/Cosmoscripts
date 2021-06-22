#Rakshak Adhikari
#with edits by Ryan Low
#Creates Density profile for DM halos using twice the halfmass radius
import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
​
​
def calculate_mass_in_bin(CM_pos, part_pos_arr, mass_arr, bin_lower, bin_upper):
    '''
    Given the center-of-mass position, the array of particle positions,
    the array of particle masses, and the bin boundaries,
    calculates the total mass within that bin.
    '''
    distances = np.sqrt(np.square(part_pos_arr - CM_pos).sum(axis=1))
    
    mass_in = mass_arr[ (distances > bin_lower) & (distances <= bin_upper) ].sum()
    
    return mass_in
​
​
fof = h5py.File('/home/ryan/Downloads/run_CDM_L3N256/fof_subhalo_tab_003.hdf5','r')
snap = h5py.File('/home/ryan/Downloads/run_CDM_L3N256/snap_003.hdf5','r')
​
​
​
#Get Redshift, boxsize, n_particle
Redshift="{:.2e}".format(fof['Header'].attrs['Redshift'])
Boxsize=int((fof['Header'].attrs['BoxSize']))
DMmass_array=snap['Header'].attrs['MassTable']
​
Subhalo=fof.get('Subhalo')
​
Subhalo_CM=np.array(Subhalo['SubhaloCM'])
Subhalo_Mass=np.array(Subhalo['SubhaloMass'])
Subhalo_Radius=2*np.array(Subhalo['SubhaloHalfmassRad'])
Number_particles=np.array(Subhalo['SubhaloLenType'])
​
DM=snap.get('PartType1')
DMpos=np.array(DM['Coordinates'])
DMmass= DMmass_array[1] * np.ones(len(DMpos))
​
Gas=snap.get('PartType0')
Gaspos=np.array(Gas['Coordinates'])
Gasmass=np.array(Gas['Masses'])
​
Star=snap.get('PartType4')
Starpos=np.array(Star['Coordinates'])
Starmass=np.array(Star['Masses'])
​
halo_no=(-Subhalo_Mass).argsort()[:7] #gets the index of the 5 largest halos
print('halono ', halo_no)
halo=0
for halo in halo_no:
    r_part=Subhalo_Radius[halo]*0.02 #This is the smallest value of the radial distance from where the calculations begin
​
    #Making the Bins here
    n=[0]
    DM_Density,Gas_Density,Star_Density=[],[],[]
    Total_Density=[]
    a=r_part
    j=1
    while a < Subhalo_Radius[halo]: #creates the bin
            n.append(a)
            a=np.power(1.2,j)*r_part
            j=j+1
   
    print(n)
    print('bins created sucessfully')
    
    ### The Dark Matter Density
    m=0
    for m in range(0,len(n)-1):
        mass=calculate_mass_in_bin(Subhalo_CM[halo], DMpos, DMmass, n[m], n[m+1])
        
        #print("number of particles in this bin number ",n[m],"is ",mass/DMmass)            
        
        DM_rho=mass*3/4/np.pi/(np.power(n[m+1],3)-np.power(n[m],3))
        DM_Density.append(DM_rho)
    DM_Density = np.array(DM_Density) 
      
    #GasDensity
    m=0
    for m in range(0,len(n)-1):
        mass=calculate_mass_in_bin(Subhalo_CM[halo], Gaspos, Gasmass, n[m], n[m+1])
        
        #print("number of particles in this bin number ",n[m],"is ",mass/DMmass)            
        
        Gas_rho=mass*3/4/np.pi/(np.power(n[m+1],3)-np.power(n[m],3))
        Gas_Density.append(Gas_rho)
    
    Gas_Density = np.array(Gas_Density)   
    
    ###Star Density     
    m=0
    for m in range(0,len(n)-1):
        mass=calculate_mass_in_bin(Subhalo_CM[halo], Starpos, Starmass, n[m], n[m+1])
        
        #print("number of particles in this bin number ",n[m],"is ",mass/DMmass)            
        
        Star_rho=mass*3/4/np.pi/(np.power(n[m+1],3)-np.power(n[m],3))
        Star_Density.append(Star_rho)
    Star_Density = np.array(Star_Density)
​
    Total_Density=DM_Density + Gas_Density + Star_Density
    #slope = np.diff(np.log(Density))/np.diff(np.log(n))
    #print (slope) 
    print('density= ',DM_Density[3],Total_Density[3])
      
    n.pop(0) 
    plt.plot(n, DM_Density,'r-', alpha=0.7,color='red',label="DM")
    
    if len(Gaspos)>100:
        plt.plot(n, Gas_Density,color='green',label="Gas")
        
    plt.plot(n, Total_Density,'r-', alpha=0.7,linestyle='dotted', color='blue',label="Total(Gas+DM+Star)")
​
​
   
    
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
​
    plt.suptitle("Radial Density Distribution for L"+str(Boxsize)+" halo "+str(halo)+" of radius "+str(round(Subhalo_Radius[halo],3)), fontsize=12)
    plt.title('CDM '+"halo Mass= "+str(round(Subhalo_Mass[halo],2))+" \n #gas & DM "+str(Number_particles[halo][0])+' '+str(Number_particles[halo][1])+" com= "+str(np.around(Subhalo_CM[halo],2)), fontsize=10)
    plt.xlabel(" Radial Distance (Kpc)")
    plt.ylabel(" Density($M_\odot$ /Kpc^3)")
    output_filename="new_CDM_Radial_Density_Distribution_for_L"+str(Boxsize)+"halo_no_"+str(halo)+".png"
    plt.savefig('/home/ryan/Downloads/plots_L3N256/'+ output_filename,dpi=150)
    plt.show()
