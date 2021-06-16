from PIL import Image
import h5py
import glob
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import imageio
import os
from natsort import natsorted


frames_num=0
num_slices=0
#num_slices=50
for num_slices in [30,60,80,100]:
    for frames_num in [3,5,7,8]:

        snap = h5py.File('snap_030821_2CDM_005.hdf5', 'r')
        Boxsize=int((snap['Header'].attrs['BoxSize']))


        z_bins=np.linspace(0, Boxsize, num=num_slices, endpoint=True, retstep=False, dtype=None, axis=0)

        DM1=snap.get('PartType1')
        Gas=snap.get('PartType0')
        DMpos1=np.array(DM1['Coordinates'])
        Gaspos=np.array(Gas['Coordinates'])

        x1 = DMpos1[:,0]
        y1 = DMpos1[:,1]
        z1 = DMpos1[:,2]

        x0 = Gaspos[:,0]
        y0 = Gaspos[:,1]
        z0 = Gaspos[:,2]



        z_value=0

        i=0
        for i in range(0,len(z_bins)-1):
            x_dm,y_dm,z_dm=[],[],[]
            x_gas,y_gas,z_gas=[],[],[]
            z_pos=0
            j=0
            for j in range(0,len(z0)):
                if z0[j]>= z_bins[i]:
                    if z0[j]<= z_bins[i+1]:
                        x_gas.append(x0[j])
                        y_gas.append(y0[j])
                        z_gas.append(z0[j])
            j=0            
            for j in range(0,len(z1)):
                if z1[j]>= z_bins[i]:
                    if z1[j]<= z_bins[i+1]:
                        x_dm.append(x1[j])
                        y_dm.append(y1[j])
                        z_dm.append(z1[j])



            x_dm=np.array(x_dm)
            y_dm=np.array(y_dm)
            z_dm=np.array(z_dm)
            x_gas=np.array(x_gas)
            y_gas=np.array(y_gas)
            z_gas=np.array(z_gas)

           
                        
            fig = plt.figure(figsize=(12,12))
            ax = plt.axes()


            fig.set_facecolor('black')
            ax.set_facecolor('black')
            ax.set_facecolor("black")
            '''plt.style.use('dark_background')'''
            #ax.grid(False)
            #ax.w_xaxis.pane.fill = False
            #ax.w_yaxis.pane.fill = False
            #ax.w_zaxis.pane.fill = False


            #ax.set_xlabel(r'$x$',fontsize=20)
            #ax.set_ylabel(r'$y$',fontsize=23)

            ax.plot(x_dm,y_dm,'o', color='mediumturquoise',markersize=0.7 ,alpha=0.7)
            ax.plot(x_gas,y_gas,'o', color='white',markersize=0.7 ,alpha=0.5)
            ax.plot([],[],'o', label='z= {:.2f}'.format(z_bins[i]/2+z_bins[i+1]/2))

           

            


            output_filename = 'fig_' +str(i)+ '.png'
            plt.legend(loc=2)
            plt.savefig(output_filename)
            
            
            

            
           
            plt.close(fig)


        folder = 'pics' 
        files = glob.glob("*.png")
        files=natsorted(files)


        images = [imageio.imread(file) for file in files]
        imageio.mimwrite('movie_frame_'+str(frames_num)+'_slices_'+str(num_slices)+'.gif', images, fps=frames_num)

        mydir=os.getcwd()
        filelist = glob.glob(os.path.join(mydir, "*.png"))
        for f in filelist:
            os.remove(f)                
                
