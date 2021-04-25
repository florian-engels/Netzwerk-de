#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pypsa
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json


# In[13]:


def admittance_to_json(admittance_matrix):
    # admittance to JSON
    # first calculate imaginary and real parts of nodes
    nodes_real = []
    nodes_imag = []
    nodes_names = []
    for i in range(0,len(admittance_matrix)):
        nodes_real = nodes_real + [admittance_matrix.iloc[i,i].real]
        nodes_imag = nodes_imag + [admittance_matrix.iloc[i,i].imag]
        nodes_names = nodes_names + [admittance_matrix.columns[i]]
    
    nodes = [0]*len(admittance_matrix)
    for i in range(0,len(admittance_matrix)):
        nodes[i] = {'B':nodes_imag[i].astype(str), 'G':nodes_real[i].astype(str), 'id':nodes_names[i]}

    # calculate real and imaginary parts of transmissionlines
    transmission_line_real = []
    transmission_line_imag = []
    transmission_line_from = []
    transmission_line_to = []
    transmission_line_id = []
    for i in range(0, len(admittance_matrix)):
        for j in range(0, len(admittance_matrix)):
            if not i == j:
                transmission_line_real = transmission_line_real + [np.float64(admittance_matrix.iloc[i,j].real)]
                transmission_line_imag = transmission_line_imag + [np.float64(admittance_matrix.iloc[i,j].imag)]
                transmission_line_from = transmission_line_from + [admittance_matrix.index[i]]
                transmission_line_to = transmission_line_to + [admittance_matrix.columns[j]]
                transmission_line_id = transmission_line_id + [admittance_matrix.index[i]+"_"+admittance_matrix.columns[j]]

    transmission_lines = [0]*(pow(len(admittance_matrix),2)-len(admittance_matrix))
    for i in range(0,pow(len(admittance_matrix),2)-len(admittance_matrix)):
        transmission_lines[i] = {'B':transmission_line_imag[i].astype(str), 
                                 'G':transmission_line_real[i].astype(str), 
                                 'from':transmission_line_from[i],
                                 'id':transmission_line_id[i],
                                 'to':transmission_line_to[i]}
    
    # store results in JSON Format    
    admittance_in_json = {'nodes': {'PVnode':nodes}, 'connections': {'Transmissionline':transmission_lines}}
    admittance_in_json = json.dumps(admittance_in_json)
    return admittance_in_json


# In[ ]:





# In[ ]:





# In[ ]:




