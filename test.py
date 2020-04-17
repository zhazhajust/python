import numpy as np
import matplotlib.pyplot as plt
import sdf
import os
import scipy.signal as signal
import constant as const
plt.switch_backend('agg')
###
start=1
stop =5000
step =200
####
sdfdir="../Data/density2e-2/"
filenumber=4
savedir ="./gif/"
density_name="density2e-2.gif"
E_name="e_density2e-2.gif"
if (os.path.isdir(savedir) == False):
    os.mkdir(savedir)
x=4000
savefigdir="./gif/test/"+str(x)
data=sdf.read(sdfdir+str(x).zfill(filenumber)+".sdf",dict=True)
Bz=data['Magnetic Field/Bz']
time=data['Header']['time']
bz=Bz.data
density=data['Derived/Number_Density/electron1'].data
bz=bz.T
bz_y0=bz[1000]
f,x,zxx=signal.stft(bz_y0,fs=const.c/const.delta_x,nperseg=50)
density=density.T
fig,axs=plt.subplots(3,1)
im=axs[0].pcolormesh(bz,cmap=plt.get_cmap('bwr'))
im2=axs[1].pcolormesh(density,cmap=plt.get_cmap('gray'))
im3=axs[2].pcolormesh(x,f,np.abs(zxx),cmap=plt.get_cmap('jet'))
axs[0].set_title(time,fontsize=12,color='r')
fig.savefig("./gif/test/gif.png",dpi=200)
  
