# -- coding: utf-8 --
#constant
c       =  3e8
micron  =  1e-6
lamada  =  10.6 * micron 
gridnumber = 2400
stop    =  5000
dt_snapshot= 9e-15
dt      =  dt_snapshot*1e15      #fs
x_max   =  80 * lamada   #60 * lamada #micron
x_min   =  0 * micron
x_end   =  x_max - x_min 
window_start_time =  (x_max - x_min) / c
delta_x =  x_end/gridnumber
t_end   =  stop * dt_snapshot
x_interval=10
t_total=1e15*x_end/c         #fs
t_size=t_total/(dt_snapshot*1e15)+1+1           #t_grid_number
######t_size=int(1e15*gridnumber*delta_x/c)+1

if t_end-window_start_time<0:
      xgrid   =  int(gridnumber)
else:
      xgrid   =  int(gridnumber + c*(t_end-window_start_time)/delta_x)
#####fft freqs
