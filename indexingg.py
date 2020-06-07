import pandas as pd
import csv
from itertools import zip_longest
import matplotlib.pyplot as plt

def indi():
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
        l1.append(a[0])

    l2=[l1,l]

    export_data=zip_longest(*l2)
    with open(r'C:\Users\Aishu\Desktop\FS\indexfile.csv','w', newline='') as myfile:
        wr=csv.writer(myfile)
        wr.writerow(("PrimaryKey","Index Value"))
        wr.writerows(export_data)
    a=pd.read_csv("indexfile.csv",index_col=0)
    b=a.sort_values(["PrimaryKey"], axis=0,ascending=True)
    d=pd.DataFrame(b)
    d.to_csv("indexfile.csv")
    
    myfile.close()
    fi.close()
indi()