# -*- coding: utf-8 -*-
import sys
import os
currentPath = os.path.dirname(os.path.realpath(__file__))
april_path = os.path.join(os.path.dirname(currentPath), "pyapril")
sys.path.insert(0, april_path)

import numpy as np
from matplotlib import pyplot as plt    
import metricExtract as me

#
#  Clutter filter parameter scan
#  Test: Wiener-SMI-MRE dimension

# Load target track file
#track = np.load("VEGAM20190729FOXC0S0FM_SurvP5_track.npy")[:,0:2].astype(dtype=int)
track = np.load("VEGAM20180313C1S0FM_track_tr0.npy")


win=[5,5,3,3]
win_pos=[50,-45]

#filename_temp = "_raw_iq/VEGAM20190729FOXC0S0_"
filename_temp = "_raw_iq/VEGAM20180313HR2C1S0FM/VEGAM20180313HR2U0C1S0FM_"
scan_res = me.scan_time_domain_dimension(statistic='avg',
                                      dim_list=np.arange(2,64,1).tolist(),                                      
                                      iq_fname_temp=filename_temp,
                                      start_ind=77, 
                                      stop_ind=87,
                                      filter_method="SMI-MRE",
                                      target_rds=track, 
                                      win=win,
                                      win_pos=win_pos,
                                      rd_size=[128, 300],
                                      rd_windowing="Hann",
                                      max_clutter_delay=128)

#plt.plot(scan_res[0,:], scan_res[1,:])  # CA 
#plt.plot(scan_res[0,:], scan_res[2,:])  # Rnf
#plt.plot(scan_res[0,:], scan_res[3,:])  # Mu_imp
#plt.plot(scan_res[0,:], scan_res[4,:])  # Delta_imp
#plt.plot(scan_res[0,:], scan_res[5,:])  # Alpha_imp
#plt.plot(scan_res[0,:], scan_res[6,:])  # L
#plt.plot(scan_res[0,:], scan_res[7,:])  # R_dpi
#plt.plot(scan_res[0,:], scan_res[8,:])  # R_zdc
#plt.plot(scan_res[0,:], scan_res[9,:])  # P
#plt.plot(scan_res[0,:], scan_res[10,:]) # D

for i in np.arange(1, scan_res.shape[0],1):
    plt.plot(scan_res[0,:], scan_res[i,:],linestyle="-")
plt.legend(['CA','R_nf','Mu imp','Delta imp','Alpha imp','L','Rdpi','Rzdc','P','D'])
#plt.legend(['R_nf','Delta imp','Rzdc','P'])
#plt.legend(['CA','R_nf','Rdpi','Rzdc','P','D']) # Metrics without target coord knowledge
    
"""
# To compare the statistics
i = 10
plt.plot(scan_res[0,:], scan_res_avg[i,:])
plt.plot(scan_res[0,:], scan_res_med[i,:])
plt.plot(scan_res[0,:], scan_res_max[i,:])
plt.legend(['Average','Median','Max'])

plt.grid(True)
plt.ylabel('Normalized Amplitude [dB]')
plt.xlabel('Filter dimension')
#plt.title("Filter dimension sweep - Wiener-SMI-MRE")
plt.title("Filter dimension sweep - Wiener-SMI-MRE - D")
"""