# Sales volume percentage of Business Units for each customer in "piedata" list
buperc=list()
custno=1
busales=pd.DataFrame(cust_rank[custno].groupby("butext")["try"].sum().sort_values(ascending=False))
busales.reset_index(level=0, inplace=True)
for i in np.arange(0,len(cust_rank[custno].groupby("butext")["try"].sum().sort_values(ascending=False)),1):
    buperc.append((cust_rank[custno].groupby("butext")["try"].sum().sort_values(ascending=False)[i])/(cust_rank[custno]["try"].sum())*100)
perc=pd.DataFrame(buperc,columns=["percantage (%)"])
piedata=busales.merge(perc,left_index=True, right_index=True)

# Pie Chart Visualisation of percantages of every customer,
explode = (0.1, 0.1, 0, 0)
plt.pie(piedata["try"],labels=piedata["butext"],
autopct='%1.1f%%', shadow=True, startangle=0,labeldistance=1,radius=100,frame=False,rotatelabels=False)
plt.legend( piedata["butext"], loc="best")
plt.axis('equal')

plt.tight_layout()
fig = plt.gcf()
fig.set_size_inches(8,7)
plt.show()

# Boxplot visualisation of BU sales for each customer
plt.figure(figsize=(30,5))
sns.boxplot(
    data=musteri[2],
    x='butext',
    y='pc',
    color='red')
   
# Visualisation of single item's sales per month

from matplotlib.pyplot import figure
figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
order_per_month = re500500.groupby('purch_month', as_index=False)["try"].sum()
plt.plot(order_per_month["purch_month"], order_per_month["try"])
plt.show()
