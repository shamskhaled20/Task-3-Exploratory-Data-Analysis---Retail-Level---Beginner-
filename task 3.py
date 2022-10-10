#!/usr/bin/env python
# coding: utf-8

# In[7]:


#importing required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


#Loading data into dataframe

df = pd.read_csv('Downloads\SampleSuperstore.csv')
df.head(5)


# In[11]:


df.info()


# In[12]:


# describtion of dataset

df.describe()


# In[16]:


#Shape of dataframe

df.shape


# In[17]:


#Listing the features of the dataset

df.columns


# In[18]:


#checking for null value

df.isna().sum()


# In[19]:


#unique value in dataset

df.nunique()  


# In[21]:


#checking for outlier

col=["Postal Code","Sales","Quantity","Discount","Profit"]
new_data=df
for i in col:
    new_data=new_data.sort_values(by=[i])
    q1=new_data[i].quantile(0.25)
    q3=new_data[i].quantile(0.75)
    iqr=q3-q1
    lwo=q1-1.5*iqr
    upo=q3+1.5*iqr
    new_data=new_data[(new_data[i]<upo) & (new_data[i]>lwo)]
    new_data=new_data.sort_index().reset_index(drop=True)

if(new_data.size<df.size):
    print("There exist outlier in dataset.")


# Visualizing the data:

# In[23]:


#correlation among dataset

df.corr().abs()


# In[24]:


#Correlation heatmap

plt.figure(figsize=(7,5))
sns.heatmap(df.corr(), annot=True)
plt.show()


# In[27]:


#plotting count plot for various feature

fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(10,10));
sns.countplot(x='Segment',data=data,ax=axs[0][0])
sns.countplot(x='Category',data=data,ax=axs[0][1])
sns.countplot(x='Region',data=data,ax=axs[1][0])
sns.countplot(x='Ship Mode',data=data,ax=axs[1][1])
sns.countplot(x='Quantity',data=data,ax=axs[2][0])
sns.countplot(x='Discount',data=data,ax=axs[2][1])


axs[0][0].set_title('Segment',fontsize=15)
axs[0][1].set_title('Category',fontsize=15)
axs[1][0].set_title('Region',fontsize=15)
axs[1][1].set_title('Ship Mode',fontsize=15)
axs[2][0].set_title('Quantity',fontsize=15)
axs[2][1].set_title('Discount',fontsize=15)

plt.tight_layout()


# In[22]:


#histogram for Visualizing

df.hist(bins = 50,figsize = (15,11));


# In[28]:


plt.figure(figsize=(18,5))
sns.countplot(x='State',data=data)
plt.xticks(rotation=90)
plt.title('State',fontsize=20)
plt.show()


# In[29]:


plt.figure(figsize=(18,5))
sns.countplot(x='Sub-Category',data=data)
plt.title('Sub-Category',fontsize=20)
plt.show()


#  Data Analysis:

#  Statewise analysis:

# In[36]:


dt1 = df['State'].value_counts()
dt1


# In[37]:


dt1.plot(kind='bar', figsize=(20, 10))
plt.xlabel('States')
plt.ylabel('Number of Deals')
plt.title('Deals  per State')
plt.show()


# In[38]:


print("The average number of deals per state is {}".format(round(dt1.mean())))


# In[39]:


data_state = df.groupby(['State'])[['Sales','Discount','Profit']].mean()
data_state


# In[40]:


data_state.describe()


# In[41]:


dt_s1 = data_state.sort_values('Profit')
dt_s1[['Profit']].plot(kind='bar',figsize=(15,5))
plt.title('Statewise analysis of Profit');


# In[42]:


dt_s1 = data_state.sort_values('Discount')
dt_s1[['Discount']].plot(kind='bar',figsize=(15,5),color="lightgreen")
plt.title('Statewise analysis of Discount');


# In[43]:


dt_s1 = data_state.sort_values('Sales')
dt_s1[['Sales']].plot(kind='bar',figsize=(15,5),color="red")
plt.title('Statewise analysis of Sales');


# Citywise analysis:

# In[44]:


dt2 = data['City'].value_counts()
dt2.head(30)


# In[45]:


dt2.head(30).plot(kind='bar',figsize=(20,5))
plt.xlabel('Cities')
plt.ylabel('Count')
plt.show()


# In[46]:


print("The average number of deals per City is {}".format(round(dt2.mean())))


# In[47]:


data_city = df.groupby(['City'])[['Sales','Discount','Profit']].mean()
data_city = data_city.sort_values('Profit')
data_city


# In[48]:


data_city.describe()


# In[49]:


data_city['Profit'].head(50).plot(kind='bar',figsize=(15,5),color='lightgreen')
plt.title('Citywise analysis of Profit');


# In[50]:


data_city['Profit'].tail(50).plot(kind='bar',figsize=(15,5),color='lightgreen')
plt.title('Citywise analysis of Profit');


# In[51]:


dt_s1 = data_city.head(50).sort_values('Discount')
dt_s1[['Discount']].plot(kind='bar',figsize=(15,5))
plt.title('Citywise analysis of Discount');


# In[52]:


dt_s1 = data_city.head(50).sort_values('Sales')
dt_s1[['Sales']].plot(kind='bar',figsize=(15,5),color='grey')
plt.title('Statewise analysis of Sales');


# 4.3. Quantitywise analysis :

# In[53]:


dt3 = df['Quantity'].value_counts().sort_index()
dt3


# In[54]:


dt3.plot.pie(subplots=True,autopct='%1.1f%%',figsize=(10,10),startangle=90)
plt.show()


# In[56]:


data_qnt = df.groupby(['Quantity'])[['Sales','Discount','Profit']].mean()
data_qnt


# In[57]:


data_qnt.describe()


# In[58]:


data_qnt.plot.pie(subplots=True,autopct='%1.1f%%',figsize=(20,20),startangle=90)
plt.show()


# 4.4. Regionwise analysis:

# In[59]:


dt4 = df['Region'].value_counts().sort_index()
dt4


# In[60]:


dt4.plot.pie(subplots=True,autopct='%1.1f%%',figsize=(7,7),startangle=90)
plt.show()


# In[61]:


data_reg = df.groupby(['Region'])[['Sales','Discount','Profit']].mean()
data_reg


# In[62]:


data_reg.describe()


# In[63]:


data_reg.plot.pie(subplots=True,autopct='%1.1f%%',figsize=(15,20),startangle=90)
plt.show()


# shipmentmodewise analysis:
# 

# In[64]:


dt5 = df['Ship Mode'].value_counts().sort_index()
dt5


# In[65]:


dt5.plot.pie(subplots=True,autopct='%1.1f%%',figsize=(7,7),startangle=90)
plt.show()


# In[66]:


data_ship = df.groupby(['Ship Mode'])[['Sales','Discount','Profit']].mean()
data_ship


# In[67]:


data_ship.describe()


# In[68]:


data_ship.plot.pie(subplots=True,figsize=(15,20), autopct='%1.1f%%',startangle=90)
plt.show()


# Categorywise analysis:
# 

# In[69]:


dt6 = df['Category'].value_counts().sort_values()
dt6


# In[70]:


dt6.plot.pie(subplots=True,autopct='%1.1f%%',figsize=(7,7),startangle=90)
plt.show()


# In[71]:


data_cat = df.groupby(['Category'])[['Sales','Discount','Profit']].mean()
data_cat


# In[72]:


data_cat.describe()


# In[73]:


data_cat.plot.pie(subplots=True,figsize=(15,20), autopct='%1.1f%%')
plt.show()


# subcategorywise analysis:
# 

# In[74]:


dt7 = df['Sub-Category'].value_counts().sort_values()
dt7


# In[75]:


dt7.plot.pie(subplots=True,autopct='%1.1f%%',figsize=(7,7),startangle=90)
plt.title("Pie Chart for Sub-Category")
plt.show()


# In[76]:


data_subcat = df.groupby(['Sub-Category'])[['Sales','Discount','Profit']].mean()
data_subcat


# In[77]:


data_subcat.describe()


# In[78]:


dt_s1 = data_subcat.sort_values('Profit')
dt_s1['Profit'].plot(kind='bar',figsize=(15,5),color='orange')
plt.title('Citywise analysis of Profit');


# In[79]:


dt_s1 = data_subcat.sort_values('Sales')
dt_s1['Sales'].plot(kind='bar',figsize=(15,5),color='red')
plt.title('Citywise analysis of Profit');


# In[80]:


dt_s1 = data_subcat.sort_values('Discount')
dt_s1['Discount'].plot(kind='bar',figsize=(15,5),color='grey')
plt.title('Citywise analysis of Profit');


# In[ ]:




