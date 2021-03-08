
#********** EVAPORATING_DM **************
#Keita Todoroki
#Aug 30, 2018
#Sep 8, 2018

from pygadgetreader import *
from numpy import *
from scipy import *
from pylab import *
import math
import matplotlib.pyplot as plt

import matplotlib.colors as colors
import matplotlib.cm as cmx

from matplotlib.colors import LogNorm


### input

#########


dir=r'C:\Users\rakshak\OneDrive\Documents\Arepo_November _simulations\L5N128_110920_2CDM_power00_sigma1'
snap   = '%s/snap_110920_2CDM_000' % (dir) 




DMtype=readsnap(snap,'SIDM_STATE','dm')
# thsi is Mark's Arepo imprementation


nH = nL = 0


for i in range(len(DMtype)):
    if DMtype[i] == 0:
        nH = nH + 1
    if DMtype[i] == 1:
        nL = nL + 1


print ('H = ', nH)
print ('L = ', nL)
