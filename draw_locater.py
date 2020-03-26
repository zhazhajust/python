import numpy as np
import matplotlib.pyplot as plt
import sdf
data=sdf.read("../Data/delaylaser/0700.sdf",dict=True)
data
Bz=data['Magnetic Field/Bz']
bz=Bz.data
density=data['Derived/Number_Density/electron1'].data
fig,ax=plt.subplots()
plt.switch_backend('agg')
fig,ax=plt.subplots()

im=ax.pcolormesh(bz,cmap=plt.get_cmap('rainbow'))
im2=ax.pcolormesh(density,cmap=plt.get_cmap('gray'))
fig.savefig("./fig/0700.png",dpi=200)
