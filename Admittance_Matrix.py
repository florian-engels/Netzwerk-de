#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pypsa


# In[2]:


import matplotlib.pyplot as plt
plt.style.use("bmh")
#get_ipython().run_line_magic('matplotlib', 'inline')


# ## admittance Matrix

# In[192]:


def create_admittance(data):
    n = pypsa.Network(data)
    n.determine_network_topology()
    for sub in n.sub_networks.obj:
        pypsa.pf.calculate_Y(sub)
    
    return sub.Y


# In[193]:


##Erstelle Admittanzmatrix (noch mit Dateinamen hart gecodet)
create_admittance("elec_s_5_ec_lcopt_Co2L-24H.nc")


# In[194]:


np.array(n.buses.index)


# In[ ]:





# In[170]:





# In[172]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[103]:





# In[105]:





# In[106]:





# In[107]:





# In[108]:





# In[114]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




