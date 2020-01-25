
'''for j in range(n):
    for i in range(n):
        print ("*", end=" ") 
    print("\n")
''' 
def print_P(n): 
    for i in range(1,n+1):  
        for k in range(i,n+1): 
            print("*",end="")   
        print() 
    for i in range(2,n+1):  
        for k in range (0,i+1): 
            print("*",end="") 
          
        print()
        
n= int(input("enter the no: "))
print_P(n)
