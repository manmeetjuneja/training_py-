def print_P(n): 
    for i in range(1,n+1):  
        for k in range(i,n+1): 
            print("*",end="")   
        print() 
n= int(input("enter the no: "))
print_P(n)
