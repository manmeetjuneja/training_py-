from collections import Counter
list =[]

n = int(input("enter no of integers in list:"))
for i in range(0,n):
    a  = int(input())
    list.append(a)
print(list)
print(list.sort())

print ("initial list", str(list))  
result = [item for items, c in Counter(list).most_common() 
                                      for item in [items] * c] 
print("final list", str(result))
