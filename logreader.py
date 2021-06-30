import numpy as np
import matplotlib.ticker
import matplotlib.pyplot as plt
import re
import pandas

from PIL import Image, ImageDraw, ImageFont
import os

name='LOG_L01N256_mod_042321_sigma_cons_100_delm0'
'''
stringToMatch = 'percent of particles' 
matchedLine = '' 
percent_light_particle=[]
percent_heavy_particle=[]
number_light_particle=[]
number_heavy_particle=[]
Redshift=[]
#get line 
with open(name, 'r') as file:
        
        for i, line in enumerate(file):
                

                
                if stringToMatch in line:
                        if 'state 00' in line: 

                                matchedLine = line
                                strtemp00=matchedLine[:10]
                                percent00=float(strtemp00[-4:])
                                percent_light_particle.append(percent00)
                                numeric_string = re.sub("[^0-9]", "", matchedLine[39:51])
                                number_light_particle.append(int(numeric_string))
                             
                                
                                
                        if 'state 01' in line: 

                                matchedLine = line
                                strtemp01=matchedLine[:10]
                                percent01=float(strtemp01[-4:])
                                percent_heavy_particle.append(percent01)
                                numeric_string = re.sub("[^0-9]", "", matchedLine[39:51])

                                number_heavy_particle.append(int(numeric_string))
                        


                                
 
                                      

                if "Redshift:" in line:
                        string1=line.rpartition(', Systems')[0]
                        string2=string1.rpartition('Redshift:')[2]
                        redshift=float(string2)
                        Redshift.append(redshift)

for i in (0,10,100,1000,10000,50000,90000):
        print(Redshift[i])
print(Redshift[-10:])
#################
                        
i=0
x_axis=[]
for i in range(0,len(percent_heavy_particle)):
        x_axis.append(i)

##############


x=len(percent_heavy_particle)
snap=[0,2,50,100,int(x/4),int(x/3),int(x/2),x-1]
i=0
heavy=[]
light=[]
total=[]
for i in snap:
        heavy.append(number_heavy_particle[i])
        light.append(number_light_particle[i])
        total_value=(number_heavy_particle[i]+number_light_particle[i])
        total.append(total_value)




        
##########plotting to plot the data#################

########Remove two extra values, not sure where the extra 2 values come from
number_heavy_particle.pop(0)
number_heavy_particle.pop(len(number_heavy_particle)-1)
number_light_particle.pop(0)
number_light_particle.pop(len(number_light_particle)-1)        
fig,ax=plt.subplots(figsize=(6,7))



ax.plot(Redshift, number_light_particle, label='Light')

ax.plot(Redshift, number_heavy_particle,label='Heavy')

plt.yscale("log")
plt.xscale("log")

plt.grid(True, which="both", ls="-")
#plt.invert_xaxis()


#plotting table
data=np.transpose([heavy,light,total])

columns = ('#heavy','#light', '#total')
rows = ['step'+'# %d' % p for p in snap]


plt.table(cellText=data,rowLabels=rows, colLabels=columns, bbox=[0.07,-0.55,0.8,0.4])

plt.subplots_adjust(bottom=0.4)

#############################


plt.title("Evolution of Light and Heavy Species"+name[4:12])
plt.xlabel("Redshift")
plt.ylabel("Number of particles")
plt.legend()


output_filename = 'Species_number'+name[4:12] + '.png'
print(output_filename)
plt.savefig(output_filename)
plt.show()

'''
######################Second plot################

with open(name, 'r') as file:
        for i, line in enumerate(file):
                
                if 'BoxSize' in line:
                        size=line
                        print(size)
                if 'SofteningComovingType0' in line:
                        Sof_length= line
                        print(line)
                if 'InitCondFile' in line:
                       IC = line
                       print(line)
                if 'OutputDir' in line:
                       Output = line

with open(name, 'r') as file:
        for j, line in enumerate(file): 
                if "SIDM: Scatter State: state=1:" in line:
                        print(line)
                        SIDM1= 'This is a SIDM Simulation. '+
                        Delm=line
                        SIDM=SIDM1+str(line)
                        print(SIDM)

                      
fig = plt.figure(figsize=(9,6))
plt.title("Details of the simulation")
ax = fig.add_subplot()

ax.annotate("Boxsize= "+size[-8:],xy=(0.01,0.8),size=10)

ax.annotate("softening length type 0 = "+ Sof_length[-10:],xy=(0.01,0.7),size=10)
ax.annotate(SIDM,xy=(0.01,0.6),size=10)
ax.annotate("IC: "+IC[-50:],xy=(0.01,0.3), size=10)
ax.annotate("Outputfile: "+Output[-80:],xy=(0.01,0.2),size=10)
ax.annotate("Logfile: "+name,xy=(0.01,0.1),size=10)




Imagename='Details_'+Output_filename

plt.savefig(Imagename)

plt.show()
                               

 

 
 















        










