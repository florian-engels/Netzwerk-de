#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pypsa
import pandas as pd
import numpy as np


# In[ ]:





# In[19]:


n = pypsa.Network("elec_s_4.nc")


# In[20]:


n.import_from_csv_folder("Export_Import")


# In[21]:


#Kosten von Solar und Onwind auf 0 setzen
#Schleife hier schwer, da n.generators keine wiederkehrende Form hat
n.generators.loc['DE0 0 onwind','marginal_cost']=0
n.generators.loc['DE0 1 onwind','marginal_cost']=0
n.generators.loc['DE0 2 onwind','marginal_cost']=0
n.generators.loc['DE0 3 onwind','marginal_cost']=0
n.generators.loc['DE0 0 solar','marginal_cost']=0
n.generators.loc['DE0 1 solar','marginal_cost']=0
n.generators.loc['DE0 2 solar','marginal_cost']=0
n.generators.loc['DE0 3 solar','marginal_cost']=0
n.generators.loc['DE0 0 onwind','capital_cost']=0
n.generators.loc['DE0 1 onwind','capital_cost']=0
n.generators.loc['DE0 2 onwind','capital_cost']=0
n.generators.loc['DE0 3 onwind','capital_cost']=0
n.generators.loc['DE0 0 solar','capital_cost']=0
n.generators.loc['DE0 1 solar','capital_cost']=0
n.generators.loc['DE0 2 solar','capital_cost']=0
n.generators.loc['DE0 3 solar','capital_cost']=0


# In[22]:


#Da es beim Einlesen der CSV's nur Werte hinzugefügt werden und nicht entfernt werden können
#-->werfe hier die Offwind Spalten aus generators.p_max_pu raus
n.generators_t.p_max_pu = n.generators_t.p_max_pu[n.generators_t.p_max_pu.columns.drop(list(n.generators_t.p_max_pu.filter(regex='offwind')))]


# In[23]:


#Bringe nun die max_pu_Daten in ein Intervall zwischen 0 und 1 und belege p_nom entsprechend

#Erhalte die Maxima der einzelnen Onwind und Solar Daten
nodes=4 #Anzahl Knoten
max_pu_onwind = np.zeros((1,nodes),dtype=float) #Initialisierung
max_pu_solar = np.zeros((1,nodes),dtype=float) #Initialisierung
for i in range(0,nodes):
    max_pu_onwind[0,i] = max(n.generators_t.p_max_pu.iloc[:,2*i])
    max_pu_solar[0,i] = max(n.generators_t.p_max_pu.iloc[:,2*i+1])
    
#Dividiere jeden Wert durch das Maximum um im Intervall 0 und 1 zu landen
for i in range(0,nodes):
    n.generators_t.p_max_pu.iloc[:,i*2]=n.generators_t.p_max_pu.iloc[:,i*2] / max_pu_onwind[0,i]
    n.generators_t.p_max_pu.iloc[:,i*2+1]=n.generators_t.p_max_pu.iloc[:,i*2+1] / max_pu_solar[0,i]

    
#Setze die vorherigen Maxima nun auf p_nom, respektive der jeweiligen Generatoren
#(nicht mit Schleife lösbar, da Daten in Generators keine feste Form haben)
n.generators.loc["DE0 0 onwind","p_nom"] = max_pu_onwind[0,0]
n.generators.loc["DE0 1 onwind","p_nom"] = max_pu_onwind[0,1]
n.generators.loc["DE0 2 onwind","p_nom"] = max_pu_onwind[0,2]
n.generators.loc["DE0 3 onwind","p_nom"] = max_pu_onwind[0,3]
n.generators.loc["DE0 0 solar","p_nom"] = max_pu_solar[0,0]
n.generators.loc["DE0 1 solar","p_nom"] = max_pu_solar[0,1]
n.generators.loc["DE0 2 solar","p_nom"] = max_pu_solar[0,2]
n.generators.loc["DE0 3 solar","p_nom"] = max_pu_solar[0,3]

#belege p_nom_max mit den ausgerechneten p_nom Werten
n.generators.loc["DE0 0 onwind","p_nom_max"] = max_pu_onwind[0,0]
n.generators.loc["DE0 1 onwind","p_nom_max"] = max_pu_onwind[0,1]
n.generators.loc["DE0 2 onwind","p_nom_max"] = max_pu_onwind[0,2]
n.generators.loc["DE0 3 onwind","p_nom_max"] = max_pu_onwind[0,3]
n.generators.loc["DE0 0 solar","p_nom_max"] = max_pu_solar[0,0]
n.generators.loc["DE0 1 solar","p_nom_max"] = max_pu_solar[0,1]
n.generators.loc["DE0 2 solar","p_nom_max"] = max_pu_solar[0,2]
n.generators.loc["DE0 3 solar","p_nom_max"] = max_pu_solar[0,3]


# In[24]:


#p_nom jedes Generators soll extendable sein. Mit dem p_nom_max im vorherigen Schritt und
#den Kosten von 0 erreichen wir unser Ziel
n.generators.loc[:,"p_nom_extendable"]=True


# In[25]:


n.lopf()


# In[26]:


n.export_to_csv_folder('Solution')


# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:





# In[16]:





# In[131]:





# In[ ]:





# In[ ]:





# In[ ]:




