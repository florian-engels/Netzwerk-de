#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pypsa
import os


# In[2]:


LoadData = pd.read_csv('LoadDataTest.csv', sep=",",decimal=".")


# In[3]:


SolarData = pd.read_csv('SolarTest.csv', sep=",",decimal=".")


# In[4]:


WindData = pd.read_csv('WindTest.csv', sep=",",decimal=".")


# In[5]:


n = pypsa.Network("elec_s_4.nc")


# In[6]:


n.export_to_csv_folder('Export_Import')


# In[7]:


generators = pd.read_csv('Export_Import/generators-p_max_pu.csv', sep=",",decimal=".")

#Offwind Spalten rausschmeißen
generators = generators[generators.columns.drop(list(generators.filter(regex='offwind')))]

#Länge der Input Daten anpassen
SolarData = SolarData[0:744]
WindData = WindData[0:744]

#Generator Daten mit Input Daten überschreiben
generators["DE0 0 onwind"] = WindData["DE0 0"]
generators["DE0 0 solar"] = SolarData["DE0 0"]

generators["DE0 1 onwind"] = WindData["DE0 1"]
generators["DE0 1 solar"] = SolarData["DE0 1"]

generators["DE0 2 onwind"] = WindData["DE0 2"]
generators["DE0 2 solar"] = SolarData["DE0 2"]

generators["DE0 3 onwind"] = WindData["DE0 3"]
generators["DE0 3 solar"] = SolarData["DE0 3"]


# In[8]:


loads = pd.read_csv('Export_Import/loads-p_set.csv', sep=",",decimal=".")

#Länge der Input Daten anpassen
LoadData = LoadData[0:744]

#Load Daten mit Input Daten überschreiben
loads["DE0 0"] = LoadData["DE0 0"]
loads["DE0 1"] = LoadData["DE0 1"]
loads["DE0 2"] = LoadData["DE0 2"]
loads["DE0 3"] = LoadData["DE0 3"]


# In[ ]:





# In[9]:


dir = os.getcwd()
output_fileG = dir + '/Export_Import/generators-p_max_pu.csv'
output_fileL = dir + '/Export_Import/loads-p_set.csv'

generators.to_csv(output_fileG, index = False)
loads.to_csv(output_fileL, index = False)


# In[ ]:





# In[32]:





# In[33]:





# In[ ]:





# In[ ]:





# In[ ]:




