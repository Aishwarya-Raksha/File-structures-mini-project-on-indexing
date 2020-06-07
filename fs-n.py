import pandas as pd
import add
import search 
import delete
import indexingg
import time
import secindex
import secsearch
import secdelete


def modify():
    fi=open(r"C:\Users\Aishu\Desktop\FS\indexfile.csv","r")
    line=fi.readline()
    a=line.split(",")
    l=[]

    while line:
        line=fi.readline()
        a=line.split(",")
        l.append(a[0])
    l1= l[: len(l) - 2]
    #print(l1)
    test_list1= list(map(float, l1))
    l2= list(map(int, test_list1))
       

    def binary_search(l2, low, high, x): 
        if high >= low: 
            mID=(high + low) // 2		
            if l2[mID] == x:
                return mID
            elif l2[mID] >x:
                return binary_search(l2, low, mID - 1, x)
            else:
                return binary_search(l2, mID + 1, high, x)
        else:
            return -1
    x = int(input("Enter key: "))
    result = binary_search(l2, 0, len(l2)-1, x) 
    if (result==-1):
        print("NOT FOUND")
    else:
        print("FOUND")
        fi=open(r"C:\Users\Aishu\Desktop\FS\indexfile.csv","r")
        line=fi.readline()
        a=line.split(",")
        l=[]
        while line:
            line=fi.readline()
            a=line.split(",")
            l.append(a[-1])
    
            res = l[: len(l) - 1]
            l2= list(map(int, res))
            for index, value in enumerate(l2): 
                if(result==index):
                    a=value
        #fi.close()

    f1=open(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv","a+")
    f1.seek(a)
    b=f1.readline()
    c=b.split(",")
    d1=c[0]
    a1=c[1]
    b1=c[2]
    c1=c[3]
    print("ID: " +c[0])
    print("Case Number: "+c[1])
    print("Description: " +c[2])
    print("District: "+c[3])
    print("Ward: "+c[4])
    print("FBI Code: "+c[5])
    print("Year: "+c[6])
    ch=0
    while ch!=5:
        print("Enter 1 to modify Description")
        print("Enter 2 to modify District")
        print("Enter 3 to modify Ward number")
        print("Enter 4 to modify FBI code")
        print("Enter 5 to go back to main menu")
        ch=int(input("PLEASE ENTER YOUR OPTION: "))
        if(ch==1):
            name1=input("Enter the new crime description: ")
            a1=name1
            str=d1+","+a1+","+b1+","+c1
            f1=open(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv","a+")
            f1.seek(a)
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv",index_col="ID")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv")
            f1.close()
            indexingg.indi()
        elif (ch==2):
            name1=input("Enter the new district: ")
            b1=name1
            str=d1+","+a1+","+b1+","+c1            
            print(str)
            f1=open(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv","a+")
            f1.seek(a)
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv",index_col="ID")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv")
            f1.close()
            indexingg.indi()
        elif (ch==3):
            name1=input("Enter the new ward number: ")
            c1=name1
            str=d1+","+a1+","+b1+","+c1            
            print(str)
            f1=open(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv","a+")
            f1.seek(a) 
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv",index_col="ID")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv")
            f1.close()
            indexingg.indi()
        elif (ch==4):
            name1=input("Enter the new FBI code: ")
            c1=name1
            str=d1+","+a1+","+b1+","+c1            
            print(str)
            f1=open(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv","a+")
            f1.seek(a) 
            f1.write(str)
            data =pd.read_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv",index_col="ID")
            data.drop([int(d1)],inplace=True) 
            data1=pd.DataFrame(data)
            data2=data1.to_csv(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv")
            f1.close()
            indexingg.indi()
        else:
            main2()
    
    
    fi.close()
#modify()       
def main2(): 
    print("------WELCOME TO CHICAGO CRIMES DATASET------")
    ch=0
    while(ch!=7):
        print("PRESS 1 TO ADD A RECORD")
        print("PRESS 2 TO DELETE A  RECORD USING PRIMARY KEY ")
        print("PRESS 3 TO SEARCH FOR A RECORD USING PRIMARY KEY ")
        print("PRESS 4 TO SEARCH FOR A RECORD USING SECONDARY KEY ")
        print("PRESS 5 to MODIFY A RECORD")
        print("PRESS 6 TO DELETE A  RECORD USING SECONDARY KEY ")
        ch=int(input("PLEASE ENTER YOUR OPTION: "))
        if(ch==1):
            start=time.time()
            indexingg.indi()
            add.add1()
            indexingg.indi()
            stop=time.time()
            t=int(stop-start)
            print("Time taken to insert a record in ms is : ", t )
        elif (ch==2):
            start=time.time()
            delete.dell()
            indexingg.indi()
            stop=time.time()
            t=int(stop-start)
            print("Time taken to delete a record in ms is : ", t )
        elif (ch==3):
            start=time.time()
            search.search1()
            indexingg.indi()
            stop=time.time()
            t=int(stop-start)
            print("Time taken to search a record in ms is : ", t )
        elif(ch==4):
            start=time.time()
            secsearch.search1()
            secindex.ind()
            stop=time.time()
            t=int(stop-start)
            print("Time taken to search a record in ms is : ", t )
        elif (ch==5):
            start=time.time()
            modify()
            indexingg.indi()
            stop=time.time()
            t=int(stop-start)
            print("Time taken to modify a record in ms is : ", t )
        elif (ch==6):
            start=time.time()
            secdelete.dell()
            secindex.ind()
            stop=time.time()
            t=int(stop-start)
            print("Time taken to delete a record in ms is : ", t )    
        else:
           print("InvalID choice!!!!") 
main2()