import numpy as np
import matplotlib.pyplot as plt
import sdf
import imageio
import os
plt.switch_backend('agg')
###
start=1
stop =22967
step =1000
####
sdfdir="../Data/density2.0/"
filenumber=5
savedir ="./gif/"
if (os.path.isdir(savedir) == False):
    os.mkdir(savedir)
image_list=[]
for i in range(start,stop,step):
  x=i
  savefigdir="./gif/png/"+str(x)
  data=sdf.read(sdfdir+str(x).zfill(filenumber)+".sdf",dict=True)
  Bz=data['Magnetic Field/Bz']
  time=data['Header']['time']
  bz=Bz.data
  #density=data['Derived/Number_Density/electron'].data
  bz=bz.T
  #dengsity=density.T
  fig,ax=plt.subplots()
  im=ax.pcolormesh(bz,cmap=plt.get_cmap('gray'))
  ax.set_title(time,fontsize=12,color='r')
  fig.savefig(savefigdir+"bz.png",dpi=200)

  image_list.append(str(savefigdir+"bz.png"))
  plt.cla()
  plt.clf()
  plt.close('all')
###
def create_gif(image_list, gif_name, duration = 1.0):
    '''
    ''' 
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main():
    #image_list = ['1.jpg', '2.jpg', '3.jpg']
    gif_name = './gif/new.gif'
    duration = 1
    create_gif(image_list, gif_name, duration)

#if __name__ == '__main__':
main()
