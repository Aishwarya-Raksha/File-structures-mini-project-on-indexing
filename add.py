import indexingg

def add1():
    ID1=input("Enter ID: \n")
    with open(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv", 'r') as myfile:
        if ID1 in myfile.read():
            print("Primary key already present!!")
        else:
            #name1=input("Enter ID: \n")
            age1=input("Enter Casenumber: \n")
            weight1=input("Enter Description: \n")
            district1=input("Enter District: \n")
            ward1=input("Enter Ward: \n")
            fbiCode1=input("Enter FBI code: \n")
            year1=input("Enter Year: \n")
            with open(r"C:\Users\Aishu\Desktop\FS\NewCSv.csv", 'a') as file:
                str=ID1+","+age1+","+weight1+","+district1+","+ward1+","+fbiCode1+","+year1
                file.write(str)
                file.write("\n")
                indexingg.indi()
    
#add1()
