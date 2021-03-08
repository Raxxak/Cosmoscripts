#Crosssection generator for (0,0)
import numpy as np

Reaction=0
Sigma_naught=1
ps=-2 #power for scattering
pc=-2 #power for conversion, we will actually use pc-1, -1 comes from momentum ratios


#Dont Change these
#################################################
Cross_Vbins=1000000
Vmax=1.0e5
Vmin=1.0e-2

Dvlog= np.log(Vmax/Vmin)/Cross_Vbins

LightSpeed=299972.0
Conversion_factor=100
##################################################
print('This will create a crosssection table for sigma of ', Sigma_naught,'and power laws of,(',ps,',',pc,'-1)')
wait=input('Does thine person understand that?Press enter if thy doth!')



###---------------For the Elastic Scattering
Velocity_array=[]
Crosssection_array=[]
velocity=0
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=(newvel_normalized)**(ps)*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data1=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_0.txt",data1,delimiter="\t")
np.savetxt("sidm_cross_reaction_4.txt",data1,delimiter="\t")
np.savetxt("sidm_cross_reaction_7.txt",data1,delimiter="\t")
np.savetxt("sidm_cross_reaction_11.txt",data1,delimiter="\t")




################################################################



####--------------For Inelastic Scattering/Conversion


#############################################################
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**(pc-1)*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data2=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_1.txt",data2,delimiter="\t")
np.savetxt("sidm_cross_reaction_2.txt",data2,delimiter="\t")
np.savetxt("sidm_cross_reaction_3.txt",data2,delimiter="\t")
np.savetxt("sidm_cross_reaction_5.txt",data2,delimiter="\t")
np.savetxt("sidm_cross_reaction_6.txt",data2,delimiter="\t")
np.savetxt("sidm_cross_reaction_8.txt",data2,delimiter="\t")
np.savetxt("sidm_cross_reaction_9.txt",data2,delimiter="\t")
np.savetxt("sidm_cross_reaction_10.txt",data2,delimiter="\t")










print('It is done My Liege')

