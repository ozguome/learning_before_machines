## Converting 9 sales volume and percentage lists for 9 business units
l_keeper = [list() for _ in range(8)]
s_keeper = [0] * 8 
lp_keeper = [list() for _ in range(8)]

detailed_cust=list()
detailed_cust=pd.DataFrame(detailed_cust,columns=["BU Anchor","BU Diamond","BU Direct Fastening","BU Fire Protection","BU Measuring Systems","BU Power Tools & Acc","BU Screw Fastening","BU Tool Services","Other"])
detailed_cust
l0=list()
l1=list()
l2=list()
l3=list()
l4=list()
l5=list()
l6=list()
l7=list()
l8=list()
s0=0
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
s7=0
s8=0
lp0=list()
lp1=list()
lp2=list()
lp3=list()
lp4=list()
lp5=list()
lp6=list()
lp7=list()
lp8=list()
for i in np.arange(0,len(piedata),1):
    for bu in np.arange(0,len(piedata[i]),1):
        
        if piedata[i].iloc[bu].butext==bulist[0]:
            l0.append(piedata[i].iloc[bu]["try"])
            lp0.append(piedata[i].iloc[bu]["percantage (%)"])
            s0=1
        elif piedata[i].iloc[bu].butext==bulist[1]:
            l1.append(piedata[i].iloc[bu]["try"])
            lp1.append(piedata[i].iloc[bu]["percantage (%)"])
            s1=1
        elif piedata[i].iloc[bu].butext==bulist[2]:
            l2.append(piedata[i].iloc[bu]["try"])
            lp2.append(piedata[i].iloc[bu]["percantage (%)"])
            s2=1
        elif piedata[i].iloc[bu].butext==bulist[3]:
            l3.append(piedata[i].iloc[bu]["try"])
            lp3.append(piedata[i].iloc[bu]["percantage (%)"])
            s3=1
        elif piedata[i].iloc[bu].butext==bulist[4]:
            l4.append(piedata[i].iloc[bu]["try"])
            lp4.append(piedata[i].iloc[bu]["percantage (%)"])
            s4=1
        elif piedata[i].iloc[bu].butext==bulist[5]:
            l5.append(piedata[i].iloc[bu]["try"])
            lp5.append(piedata[i].iloc[bu]["percantage (%)"])
            s5=1
        elif piedata[i].iloc[bu].butext==bulist[6]:
            l6.append(piedata[i].iloc[bu]["try"])
            lp6.append(piedata[i].iloc[bu]["percantage (%)"])
            s6=1
        elif piedata[i].iloc[bu].butext==bulist[7]:
            l7.append(piedata[i].iloc[bu]["try"])
            lp7.append(piedata[i].iloc[bu]["percantage (%)"])
            s7=1
        elif piedata[i].iloc[bu].butext==bulist[8]:
            l8.append(piedata[i].iloc[bu]["try"])
            lp8.append(piedata[i].iloc[bu]["percantage (%)"])
            s8=1
    if s0==0:
        l0.append(0)
        lp0.append(0)
    if s1==0:
        l1.append(0)
        lp1.append(0)
    if s2==0:
        l2.append(0)
        lp2.append(0)
    if s3==0:
        l3.append(0)
        lp3.append(0)
    if s4==0:
        l4.append(0)
        lp4.append(0)
    if s5==0:
        l5.append(0)
        lp5.append(0)
    if s6==0:
        l6.append(0)
        lp6.append(0)
    if s7==0:
        l7.append(0)
        lp7.append(0)
    if s8==0:
        l8.append(0)
        lp8.append(0)
    s0=0
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    s6=0
    s7=0
    s8=0
     
    ## list to dataframe
     
l0=pd.DataFrame(l0)
l1=pd.DataFrame(l1)
l2=pd.DataFrame(l2)
l3=pd.DataFrame(l3)
l4=pd.DataFrame(l4)
l5=pd.DataFrame(l5)
l6=pd.DataFrame(l6)
l7=pd.DataFrame(l7)
l8=pd.DataFrame(l8)
lp0=pd.DataFrame(lp0)
lp1=pd.DataFrame(lp1)
lp2=pd.DataFrame(lp2)
lp3=pd.DataFrame(lp3)
lp4=pd.DataFrame(lp4)
lp5=pd.DataFrame(lp5)
lp6=pd.DataFrame(lp6)
lp7=pd.DataFrame(lp7)
lp8=pd.DataFrame(lp8)

## Merging every customer sales volume with each other
bu_sales_per_customer=l0.merge(l1,left_index=True, right_index=True)
bu_sales_per_customer=bu_sales_per_customer.merge(l2,left_index=True, right_index=True)
bu_sales_per_customer=bu_sales_per_customer.merge(l3,left_index=True, right_index=True)
bu_sales_per_customer=bu_sales_per_customer.merge(l4,left_index=True, right_index=True)
bu_sales_per_customer=bu_sales_per_customer.merge(l5,left_index=True, right_index=True)
bu_sales_per_customer=bu_sales_per_customer.merge(l6,left_index=True, right_index=True)
bu_sales_per_customer=bu_sales_per_customer.merge(l7,left_index=True, right_index=True)
bu_sales_per_customer=bu_sales_per_customer.merge(l8,left_index=True, right_index=True)
## Setting new sales per customerdataframe's column names

bu_sales_per_customer.columns=["BU Anchor","BU Diamond","BU Direct Fastening","BU Fire Protection","BU Measuring Systems","BU Power Tools & Acc","BU Screw Fastening","BU Tool Services","Other"]

## Same for percentage too

bu_percentage_per_customer=lp0.merge(lp1,left_index=True, right_index=True)
bu_percentage_per_customer=bu_percentage_per_customer.merge(lp2,left_index=True, right_index=True)
bu_percentage_per_customer=bu_percentage_per_customer.merge(lp3,left_index=True, right_index=True)
bu_percentage_per_customer=bu_percentage_per_customer.merge(lp4,left_index=True, right_index=True)
bu_percentage_per_customer=bu_percentage_per_customer.merge(lp5,left_index=True, right_index=True)
bu_percentage_per_customer=bu_percentage_per_customer.merge(lp6,left_index=True, right_index=True)
bu_percentage_per_customer=bu_percentage_per_customer.merge(lp7,left_index=True, right_index=True)
bu_percentage_per_customer=bu_percentage_per_customer.merge(lp8,left_index=True, right_index=True)

## Setting new bu_percentage_per_customer dataframe's column names

bu_percentage_per_customer.columns=["BU Anchor","BU Diamond","BU Direct Fastening","BU Fire Protection","BU Measuring Systems","BU Power Tools & Acc","BU Screw Fastening","BU Tool Services","Other"]

## Calculating confidance intervals for Sales volume and Sales percentage for each customer

rp.summary_cont(bu_sales_per_customer[["BU Anchor","BU Diamond","BU Direct Fastening","BU Fire Protection","BU Measuring Systems","BU Power Tools & Acc","BU Screw Fastening","BU Tool Services","Other"]].head(8))
## Stats about sales per customer
bu_sales_per_customer_head_8.describe().T

bu_sales_per_customer[(bu_sales_per_customer["try"]>50000)&(bu_sales_per_customer["try"]<100000)].describe().T
