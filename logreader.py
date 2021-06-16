import numpy as np
import matplotlib.ticker
import matplotlib.pyplot as plt
import re
import pandas

name='/Users/rakshakadhikari/Desktop/compare_L1N1024_cdm_2cdm_delm0_const100_all_light/L1N1024_042421_sigmacons100_delm0/LOG_L1N11024_mod_042421_sigma_cons_100_delm0_from0.10z'

stringToMatch = 'percent of particles' 
matchedLine = '' 
percent_light_particle=[]
percent_heavy_particle=[]
number_light_particle=[]
number_heavy_particle=[]
#get line 
with open(name, 'r') as file:
        for i, line in enumerate(file):
        #for line in file:
        #while (line != null):
                if stringToMatch in line:
                        if 'state 00' in line: 

                                matchedLine = line
                                strtemp00=matchedLine[:10]
                                percent00=float(strtemp00[-4:])
                                percent_light_particle.append(percent00)
                                number_light_particle.append(int(matchedLine[39:50]))
                                
                                
                        if 'state 01' in line: 

                                matchedLine = line
                                strtemp01=matchedLine[:10]
                                percent01=float(strtemp01[-4:])
                                percent_heavy_particle.append(percent01)
                                numeric_string = re.sub("[^0-9]", "", matchedLine[39:51])

                                number_heavy_particle.append(int(numeric_string))
                        


                                
                         



#################
                        
i=0
x_axis=[]
for i in range(0,len(percent_heavy_particle)):
        x_axis.append(i)

##############


x=len(percent_heavy_particle)
snap=[0,2,50,100,int(x/4),int(x/3),int(x/2),x-1]
print(snap)
i=0
heavy=[]
light=[]
total=[]
for i in snap:
        heavy.append(number_heavy_particle[i])
        light.append(number_light_particle[i])
        total_value=(number_heavy_particle[i]+number_light_particle[i])
        total.append(total_value)


print('l',light)
        
##########plotting to plot the data#################
fig,ax=plt.subplots(figsize=(7.2,8.4))



ax.plot(x_axis, number_light_particle, label='Light')

ax.plot(x_axis, number_heavy_particle,label='Heavy')

plt.yscale("log")
plt.xscale("log")

plt.grid(True, which="both", ls="-")



#plotting table
data=np.transpose([heavy,light,total])

columns = ('#heavy','#light', '#total')
rows = ['step'+'# %d' % p for p in snap]


plt.table(cellText=data,rowLabels=rows, colLabels=columns, bbox=[0.07,-0.55,0.8,0.4])

plt.subplots_adjust(bottom=0.4)

#############################



plt.title("Evolution of Light and Heavy Species"+name[4:12])
plt.xlabel("Time-Step")
plt.ylabel("Number of particles")
plt.legend()


output_filename = 'Species_number'+'L1N1024'+ '.png'
print(output_filename)
plt.savefig(output_filename,dpi=150)
plt.show()











        










