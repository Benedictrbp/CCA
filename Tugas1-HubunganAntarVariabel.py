#!/usr/bin/env python
# coding: utf-8

# <h1>1. Apa itu Covariance dan cara menghitungnya</h1>

# <p>Covariance bisa dibilang ukuran dari seberapa banyak dua buah variabel acak berubah bersama. Dengan kata lain covariance merupakan ukuran kekuatan korelasi dua buah variabel acak.</p>

# <p>Cara menghitungnya : </p>
# <p>E (Xi - mean X) (Yi - mean Y) / n-1</p>

# <h1>2. Buat tabel perbedaan covariance dan correlation<h1>

# <table style="width:100%">
#     <tr>
#         <th style="text-align:center;color:blue">Covariance</th>
#         <th style="text-align:center;color:blue">Correlation</th>
#     </tr>
#     <tr>
#         <td style="text-align:left">Ada 3 jenis : 
#             <ul>Covariance positif : p > 0 </ul>
#             <ul>Covariance negatif : p < 0 </ul>
#             <ul>Zero Covariance : p = 0 </ul>
#         </td>
#         <td style="text-align:left">Nilainya ada diantara : -1 <= p <= 1</td>
#     </tr>
#     <tr>
#         <td style="text-align:left">Ukuran kekuatan korelasi</td>
#         <td style="text-align:left">Ukuran kekuatan linearitas</td>
#     </tr>
# </table>

# <h1>3. Scatterplot and Correlation Mileage vs Price</h1>

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


dataset_mobil = pd.read_csv("Dataset Penjualan Mobil.csv")
dataset_mobil


# <h2>DATA CLEANING</h2>

# In[4]:


dataset_mobil.info()


# In[5]:


df1 = dataset_mobil
df1.info()


# In[6]:


df1.isnull().sum()


# In[7]:


df1['Price'].mean()


# In[8]:


df1['EngineVolume'].mean()


# In[9]:


price = df1['Price'].dropna()
sns.distplot(price)


# In[10]:


enginevolume = df1['EngineVolume'].dropna()
sns.distplot(enginevolume)


# <p>Karena ternyata data enginevolume dan price exponensial jadinya ga boleh diisi data yang hilang dengan nilai mean harus median</p>

# In[12]:


me1 = df1['Price'].median()
me2 = df1['EngineVolume'].median()


# In[14]:


me1


# In[15]:


me2


# In[16]:


df_final = dataset_mobil


# In[17]:


dict_in = {'Price':me1 , 'EngineVolume':me2}
df_final = df_final.fillna(dict_in)
df_final.info()


# In[18]:


x = df_final['Mileage']
y = df_final['Price']


# In[19]:


plt.scatter(x,y)
plt.show()


# In[20]:


df2 = df_final[['Price','Mileage']]
df2.info()


# In[21]:


df2.corr()


# <h1>4. Covariation Mileage vs Price</h1>

# In[22]:


df3 = df_final[['Price','Mileage']]
df3.info()


# In[23]:


df3.cov()


# <h1>5. Contoh Hubungan CCA pada dataset mobil ini</h1>

# In[24]:


df_final.info()


# <p> info diatas menunjukkan tipe2 variabel yang ada<p>

# <p> Kemungkinan hubungan CCA yang ada adalah : </p> 
# <ul> Dependent variabel : Price dan EngineVolume (yang mau dicari)</ul>
# <ul> Independent variabel : Mileage dan Year </ul>
