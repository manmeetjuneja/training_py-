def plus(n):
    for i in range(1,(n*2 - 1)):
        if(i==n):
            for j in range(1,(n*2 - 1)):
                print("+ ",end=" ")
        else:
            for i in range(n-1,1):
                if(i==4):
                    print("+")
            print("+")
        print()

'''for i in range(0,8):
    for j in range(0,8):
        if(j==4):
            print("+",end=" ")
        else:
            print(" ",end=" ")
    print()
    for i in range(0,8):
        if (i==4):
            print("+",end=" ")
'''    
n = int(input("enter a number:"))
plus(n)

'''for i in range(0,):
    for j in range(0,9):
        if(i==4):
            print("#",end=" ")
        else:
            print(" ")
    print()
'''
