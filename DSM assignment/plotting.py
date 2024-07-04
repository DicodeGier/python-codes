import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

data_set = pd.read_excel("data_set.xlsx")
years = np.arange(np.min(data_set["Year"]),np.max(data_set["Year"]) + 1)
countries = ["Australia","Austria","Belgium","Bulgaria","China","Czechia",
               "Denmark", "Estonia", "Finland","France", "Germany", "Hungary",
               "India", "Indonesia","Italy","Latvia","Lithuania","Netherlands",
               "Poland", "Portugal","Romania", "Russia", "Slovakia", "Spain",
               "Sweden", "Switzerland", "Ukraine", "United Kingdom", "United States"]

# b
plt.figure()
for i in countries:
    subset = data_set[data_set["Entity"] == i]
    data_to_plot = subset["AnnualCOEmissionsperCapita"]
    plt.plot(years, data_to_plot, linewidth = 0.8, label = i)

plt.grid()
plt.xlabel("Year")
plt.ylabel("Co2 emission per capita in tonnes")
plt.title("Co2 emission per capita per year per country")  
legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol = 2)
for line in legend.get_lines():
    line.set_linewidth(2.0)

#plt.savefig('QuestionB.eps',bbox_inches='tight')
#print("figure b saved") 

plt.show()
 

# c
country_to_drop = data_set[data_set["AnnualCOEmissionsperCapita"] == np.max(data_set["AnnualCOEmissionsperCapita"])]["Entity"]
country_to_drop = list(filter(None, country_to_drop.to_string().split(" ")))[1]
countries2 = countries.copy()
countries2.remove(country_to_drop) 

plt.figure()
for i in countries2:
    subset = data_set[data_set["Entity"] == i]
    data_to_plot = subset["AnnualCOEmissionsperCapita"]
    plt.plot(years, data_to_plot, linewidth = 0.8, label = i)

plt.grid()
plt.xlabel("Year")
plt.ylabel("Co2 emission per capita in tonnes")
plt.title("Co2 emission per capita per year per country")  
legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol = 2)
for line in legend.get_lines():
    line.set_linewidth(2.0)

#plt.savefig('QuestionC.eps',bbox_inches='tight')
#print("figure c saved") 
plt.show()
 
