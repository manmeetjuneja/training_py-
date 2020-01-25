A= int(input("enter a 5 digit no:"))
addition = 0

while(A>0):
    B = A % 10
    addition = addition + B
    A = A //10

print("sum of digits are:"+str(addition))
    
