
import numpy as np

Reaction=0
Sigma_naught=0.1


#Dont Change these
#################################################
Cross_Vbins=1000000
Vmax=1.0e5
Vmin=1.0e-2

Dvlog= np.log(Vmax/Vmin)/Cross_Vbins

LightSpeed=299972.0
Conversion_factor=100
##################################################
print('This will create a crosssection table for sigma of ', Sigma_naught)
wait=input('Does thine person understand that?')



###---------------Zero
Velocity_array=[]
Crosssection_array=[]
velocity=0
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_0.txt",data,delimiter="\t")

################################################################



####--------------One


#############################################################
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_1.txt",data,delimiter="\t")
###---------------Two
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_2.txt",data,delimiter="\t")
###---------------Three
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_3.txt",data,delimiter="\t")

###---------------Four
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_4.txt",data,delimiter="\t")
###---------------Five
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_5.txt",data,delimiter="\t")



###---------------Six
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_6.txt",data,delimiter="\t")
###---------------Seven
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_7.txt",data,delimiter="\t")
###---------------Eight
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_8.txt",data,delimiter="\t")
###---------------Nine
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_9.txt",data,delimiter="\t")
###---------------Ten
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=0.5*(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_10.txt",data,delimiter="\t")
###---------------Eleven
velocity=0
Velocity_array=[]
Crosssection_array=[]
for i in range(0,Cross_Vbins):
        velocity = np.exp(Dvlog*(i+0.5)+np.log(Vmin)) #km/sec
        
        newvel=velocity*100000 #cm/sec
        newvel_normalized=newvel/10000000
        Crosssec=(newvel_normalized)**-2*Sigma_naught
        Velocity_array.append(velocity)
        Crosssection_array.append(Crosssec)

        #print(newvel,Crosssec)
        








data=np.vstack((Velocity_array,Crosssection_array)).T
np.savetxt("sidm_cross_reaction_11.txt",data,delimiter="\t")

