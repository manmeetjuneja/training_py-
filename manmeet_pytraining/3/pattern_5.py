def print_P(n):
    for i in range(0,n+1):  
        for k in range (0,i+1): 
            print("*",end="") 
          
        print()
        
n= int(input("enter the no: "))
print_P(n)
