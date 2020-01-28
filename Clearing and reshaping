# importing libraries that I used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime 
!pip install researchpy
import researchpy as rp
import statsmodels.stats.api as sms
from scipy import stats
from datetime import date

#upload from .xlsl
an = pd.read_excel (r'C:\Users\ozguome\Desktop/Case Studies/Case Study ML/Keşifçi Veri Analizi/an_bc_karotsuz.xlsx') 

#variable and column name setting
an["soldtocustomer"]=an["soldtocustomer"].apply(str)
an["billno"]=an["billno"].apply(str)
an["channel"]=an["channel"].apply(str)
an["billday"]=pd.to_datetime(an["billday"],format='%d.%m.%Y')
an["materialno"]=an["materialno"].apply(str)
an.dtypes

#grouping customers by total value of sales annualy in descending order
an_satıs_sıralama=an.groupby(by=["soldtocustomer"], as_index=False)['try'].sum().sort_values(by=["try"],ascending=False)
an_satıs_sıralama=an_satıs_sıralama.reset_index(drop=True)
an_satıs_sıralama

#visualisation of sales volumes of customers
sns.kdeplot(an_satıs_sıralama["try"].head(54), shade=True, bw="silverman", color="red",gridsize=100)

#adding all customer invoice records to a descending order sales list by grouping for each customer invoices.
#each element of list includes a dataframe with [total_invoices x 16] matrix and list is in descending sales order
#highest sales customer's invoices=cust_rank[0]
cust_rank=list()
for i in an_satıs_sıralama["soldtocustomer"]: 
    cust_rank.append(an[an["soldtocustomer"]==i])
len(cust_rank)

## DETAILED SALES EXAMINATION
# Finding customers, which has the sales volume of above 50K TRY, and making a list(plusfifty_material_mean_unit_price) that holds every material's unit mean price as dataframe.
# Already know that first 55 customer's annual sales is bigger than 50k.

plusfifty_material_mean_unit_price=list()
for i in np.arange(0,55,1):
    plusfifty_material_mean_unit_price.append(cust_rank[i].groupby("materialno")["try"].sum()/cust_rank[i].groupby("materialno")["pc"].sum())
plusfifty_material_mean_unit_price[1]

