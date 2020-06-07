def search1():
    fi=open(r"C:\Users\Aishu\Desktop\FS\index3.csv","r")
    line=fi.readline()
    a=line.split(",")
    l=[]

    while line:
        line=fi.readline()
        a=line.split(",")
        l.append(a[0])
    l1= l[: len(l) - 2]
    test_list1= list(map(float, l1))
    l2= list(map(int, test_list1))
       

    def binary_search(l2, low, high, x): 
        if high >= low: 
            mid=(high + low) // 2		
            if l2[mid] == x:
                return mid
            elif l2[mid] >x:
                return binary_search(l2, low, mid - 1, x)
            else:
                return binary_search(l2, mid + 1, high, x)
        else:
            return -1
    x = int(input("enter key "))
    result = binary_search(l2, 0, len(l2)-1, x) 
    if (result==-1):
        print("not found")
    else:
        print("found")
        fi=open(r"C:\Users\Aishu\Desktop\FS\index3.csv","r")
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
        
    
    fi=open(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv","r")
    fi.seek(a)
    b=fi.readline()
    c=b.split(",")
    print(b)
    print("ID: " +c[0])
    print("Case number: "+c[1])
    print("Description: " +c[2])
    print("District: "+c[3])
    print("Ward: "+c[4])
    print("FBI code: "+c[5])
    print("Year: "+c[6])
#search1()