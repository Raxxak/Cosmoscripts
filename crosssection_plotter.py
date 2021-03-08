#this here thingamabob plots the crosssectionfiles to see if they be alright
# Rakshak Shivovitch Adhikari
#01/16/2021
import os
import sys
import matplotlib.pyplot as plt
from io import StringIO
from pylab import*
import numpy as np


a=(log(18)-log(8))/(log(3)-log(2))
print(a)
print(type(a))

file0=os.path.join(sys.path[0], 'sidm_cross_reaction_0.txt')

file1=os.path.join(sys.path[0], 'sidm_cross_reaction_1.txt')
file2=os.path.join(sys.path[0], 'sidm_cross_reaction_2.txt')
file3=os.path.join(sys.path[0], 'sidm_cross_reaction_3.txt')
file4=os.path.join(sys.path[0], 'sidm_cross_reaction_4.txt')
file5=os.path.join(sys.path[0], 'sidm_cross_reaction_5.txt')
file6=os.path.join(sys.path[0], 'sidm_cross_reaction_6.txt')
file7=os.path.join(sys.path[0], 'sidm_cross_reaction_7.txt')
file8=os.path.join(sys.path[0], 'sidm_cross_reaction_8.txt')
file9=os.path.join(sys.path[0], 'sidm_cross_reaction_9.txt')
file10=os.path.join(sys.path[0], 'sidm_cross_reaction_10.txt')
file11=os.path.join(sys.path[0], 'sidm_cross_reaction_11.txt')



cross0=genfromtxt(file0,usecols=(1),unpack=True)

cross1=genfromtxt(file1,usecols=(1),unpack=True)
print('cross',type(cross1[3]))
cross2=genfromtxt(file2,usecols=(1),unpack=True)
cross3=genfromtxt(file3,usecols=(1),unpack=True)
cross4=genfromtxt(file4,usecols=(1),unpack=True)
cross5=genfromtxt(file5,usecols=(1),unpack=True)
cross6=genfromtxt(file6,usecols=(1),unpack=True)
cross7=genfromtxt(file7,usecols=(1),unpack=True)
cross8=genfromtxt(file8,usecols=(1),unpack=True)
cross9=genfromtxt(file9,usecols=(1),unpack=True)
cross10=genfromtxt(file10,usecols=(1),unpack=True)
cross11=genfromtxt(file11,usecols=(1),unpack=True)

print("Reading Crosssection in progress. Please have some patience")

velocity0=genfromtxt(file0,usecols=(0),unpack=True)
velocity1=genfromtxt(file1,usecols=(0),unpack=True)
velocity2=genfromtxt(file2,usecols=(0),unpack=True)
velocity3=genfromtxt(file3,usecols=(0),unpack=True)
velocity4=genfromtxt(file4,usecols=(0),unpack=True)
velocity5=genfromtxt(file5,usecols=(0),unpack=True)
velocity6=genfromtxt(file6,usecols=(0),unpack=True)
velocity7=genfromtxt(file7,usecols=(0),unpack=True)
velocity8=genfromtxt(file8,usecols=(0),unpack=True)
velocity9=genfromtxt(file9,usecols=(0),unpack=True)
velocity10=genfromtxt(file10,usecols=(0),unpack=True)
velocity11=genfromtxt(file11,usecols=(0),unpack=True)





n0=(log(cross0[2])-log(cross0[1]))/(log(velocity0[2])-log(velocity0[1]))
n1=(log(cross1[2])-log(cross1[1]))/(log(velocity1[2])-log(velocity1[1]))
n2=(log(cross2[2])-log(cross2[1]))/(log(velocity2[2])-log(velocity2[1]))
n3=(log(cross3[2])-log(cross3[1]))/(log(velocity3[2])-log(velocity3[1]))
n4=(log(cross4[2])-log(cross4[1]))/(log(velocity4[2])-log(velocity4[1]))
n5=(log(cross5[2])-log(cross5[1]))/(log(velocity5[2])-log(velocity5[1]))
n6=(log(cross6[2])-log(cross6[1]))/(log(velocity6[2])-log(velocity6[1]))
n7=(log(cross7[2])-log(cross7[1]))/(log(velocity7[2])-log(velocity7[1]))
n8=(log(cross8[2])-log(cross8[1]))/(log(velocity8[2])-log(velocity8[1]))
n9=(log(cross9[2])-log(cross9[1]))/(log(velocity9[2])-log(velocity9[1]))
n10=(log(cross10[2])-log(cross10[1]))/(log(velocity10[2])-log(velocity10[1]))
n11=(log(cross11[2])-log(cross11[1]))/(log(velocity11[2])-log(velocity11[1]))


print("Work in progress. Please have some patience")
fig,ax=plt.subplots()

plt.yscale("log")
plt.xscale("log")


ax.plot(cross0[:100], velocity0[:100], label='table-0,power= '+str(n0), linestyle='dashed')

ax.plot(cross1[:100], velocity1[:100], label='table-1,power= '+str(n1) )
ax.plot(cross2[:100], velocity2[:100], label='table-2,power= '+str(n2))
ax.plot(cross3[:100], velocity3[:100], label='table-3,power= '+str(n3))
ax.plot(cross4[:100], velocity4[:100], label='table-4,power= '+str(n4))
ax.plot(cross5[:100], velocity5[:100], label='table-5,power= '+str(n5))
ax.plot(cross6[:100], velocity6[:100], label='table-6,power= '+str(n6))
ax.plot(cross7[:100], velocity7[:100], label='table-7,power= '+str(n7))
ax.plot(cross8[:100], velocity8[:100], label='table-8,power= '+str(n8))
ax.plot(cross9[:100], velocity9[:100], label='table-9,power= '+str(n9))
ax.plot(cross11[:100], velocity11[:100], label='table-11,power= '+str(n11))

sigma=cross1[2]/(velocity1[2]**n1)




plt.title("Cross-section velocity graph")#+ "sigma_naught="+str(sigma))
plt.xlabel("Cross-section")
plt.ylabel("Velocity")
plt.legend()
#plt.legend(loc=3,bbox_to_anchor=(1,0))
#ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())


plt.show()
output_filename = 'crosssection_plot.png'
 
plt.savefig(output_filename)
#plt.show()


