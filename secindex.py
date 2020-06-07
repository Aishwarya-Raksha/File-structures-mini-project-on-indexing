import pandas as pd
import csv
from itertools import zip_longest
def ind():
    fi=open(r"C:\Users\Aishu\Desktop\FS\NewCSV.csv","r")
    pos=fi.tell()
    line=fi.readline()
    a=line.split(",")
    l=[]
    l1=[]
    while line:
        pos=fi.tell()
        line=fi.readline()
        a=line.split(",")
        l.append(pos)
        l1.append(a[-1])
        
        

    l2=[l1,l]

    export_data=zip_longest(*l2)
    with open(r'C:\Users\Aishu\Desktop\FS\index3.csv','w', newline='') as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("secondarykey","Index Value"))
        wr.writerows(export_data)
    a=pd.read_csv("index3.csv",index_col=0)
    b=a.sort_values(["secondarykey"], axis=0,ascending=True)
    d=pd.DataFrame(b)
    d.to_csv("index3.csv")

    myfile.close()
    fi.close()
#ind()