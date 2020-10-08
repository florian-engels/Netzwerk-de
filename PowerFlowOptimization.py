#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pypsa
import pandas as pd
import numpy as np


# In[4]:


n = pypsa.Network("elec_s_4.nc")


# In[5]:


n.import_from_csv_folder("Export_Import")


# In[6]:


n.lopf()


# In[7]:


n.export_to_csv_folder('Solution')


# In[ ]:




