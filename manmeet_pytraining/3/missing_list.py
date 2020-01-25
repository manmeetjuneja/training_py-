#list1 = [1,2,3,4,5]
#list2 = [1,3,4,5]
#A = sum(list1) - sum(list2)
#print(A)

input_string1 = input("Enter a first list numbers or elements separated by space: ")
userList = input_string1.split()
print("user list is ", userList)

sum = 0
for num in userList:
    sum += int(num)
    sum1 = sum

input_string2 = input("Enter a second list numbers or elements separated by space: ")
userList1 = input_string2.split()
print("user list is ", userList1)

sum = 0
for num in userList1:
    sum += int(num)
    sum2 = sum

missing = sum1 - sum2
print("Missing no:"+str(missing))
