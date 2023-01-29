#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = [["Felipe", 24, "Masculino", 4.5], ["Andrea", 21, "Femenino", 7.0], 
       ["Tomas", 22, "Masculino", 6.1], ["Roberto", 20, "Masculino", 5.5]]
df = pd.DataFrame(data, columns=["NOMBRE", "EDAD", "GENERO", "CALIFICACIONES"])
print(df)


# In[ ]:




