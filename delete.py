import pandas as pd
import secindex
def dell():
    data =pd.read_csv(r"C:\Users\Aishu\Desktop\FS\NewCSV.csv",index_col="ID")
    del_ID = int(input('Enter the ID to delete: \n'))
    data.drop([del_ID],inplace=True) 
    a=pd.DataFrame(data)
    print("DELETED SUCCESSFULLY")
    b=a.to_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv")
    secindex.ind() 
 
