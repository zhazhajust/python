mport numpy as np
import matplotlib.pyplot as plt
import sdf
import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator, FuncFormatter
plt.switch_backend('agg')
locate="../Data/delaylaser/0700.sdf"
data=sdf.read(locate,dict=True)

data[""]

