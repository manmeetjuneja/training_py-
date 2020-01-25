def Sum(n1,n2,list1,list2,X):
    for a in range(n1):
        for b in range(n2):
            if(list1[a]+list2[b]==X):
                print(list1[a],list2[b])
            else:
                pass
    
list1 = [2,3,4,5]
list2 = [3,4,5,6]

n1 = len(list1)
n2 = len(list2)

X = int(input("enter the value of X: "))
Sum(n1,n2,list1,list2,X)

