#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pypsa
import pandas as pd
import numpy as np


# In[2]:


import matplotlib.pyplot as plt
plt.style.use("bmh")
# get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


#Erstelle Admittanz-Matrix
def create_admittance(data):
    
    n = pypsa.Network(data)
    n.determine_network_topology()
    for sub in n.sub_networks.obj:
        pypsa.pf.calculate_Y(sub)
        
    return sub.Y


# In[2]:


#Erstelle DataFrame mit Bus-Namen und Bus-Art
def create_info_df(data):
    
    n = pypsa.Network(data)
    d = {'buses': np.array(n.buses.index), 'control': np.array(n.buses.control)}
    df = pd.DataFrame(data=d)
    
    return df


# In[ ]:


import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid Numbers of Arguments. Script will be terminated.')
    else:
        adm = create_admittance(sys.argv[1])
        save_csv = "{}/admittance".format(os.getcwd())
        pd.DataFrame(adm).to_csv(save_csv)
        
        buses = create_info_df(sys.argv[1])
        save_csv = "{}/buses".format(os.getcwd())
        pd.DataFrame(buses).to_csv(save_csv)

