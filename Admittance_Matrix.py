#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pypsa


# In[2]:


import matplotlib.pyplot as plt
plt.style.use("bmh")
# get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


n = pypsa.Network("elec_s_317_ec_lcopt_Co2L-24H.nc")
n.plot();


# ## admittance Matrix

# In[4]:


n.determine_network_topology()


# In[6]:


for sub in n.sub_networks.obj:
    pypsa.pf.calculate_Y(sub)


# In[8]:


print(sub.Y)


# In[ ]:





# In[ ]:




