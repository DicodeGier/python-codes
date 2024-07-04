import pandas as pd
drinksDF = pd.read_csv("drinks.csv")


print(drinksDF.groupby('continent')['beer_servings'].mean())



print(drinksDF.groupby('continent')['wine_servings'].describe())


drinksDF.groupby('continent').mean()



drinksDF.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])



#################################################################################################### some things I tried to do fancier


# In[95]:


print(drinksDF['spirit_servings'].max())
print(drinksDF.loc[drinksDF['spirit_servings'] == drinksDF['spirit_servings'].max()])


# In[96]:


print(drinksDF['spirit_servings'].min())
print(drinksDF.loc[drinksDF['spirit_servings'] == drinksDF['spirit_servings'].min()])


# In[ ]:




