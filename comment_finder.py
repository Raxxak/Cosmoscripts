import numpy as np
import matplotlib.ticker
import matplotlib.pyplot as plt
import re
import pandas

name='Config.sh-7'
j=0
stringToMatch = '#' 
matchedLine = '' 
#get line
f= open("comparing_"+name+".txt","w+")

with open(name, 'r') as file:
    print('These here things are turned on in the file '+name)
    for i, line in enumerate(file):
                if line[0]!=stringToMatch:
                    f.write(line)
                        


f.close()
with open("comparing_"+name+".txt") as f:
    print "".join(line for line in f if not line.isspace())



#################



        










