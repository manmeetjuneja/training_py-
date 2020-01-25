def printPairs(arr, arr_size, sum): 
    s = set() 
      
    for i in range(0, arr_size): 
        temp = sum - arr[i] 
        if (temp in s): 
            print("Pair with sum"+ str(Sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
        s.add(arr[i])
arr = [2,4,5,7,10,15,18]
print(arr)
Sum = int(input("enter a random sum:"))

printPairs(arr,len(arr),Sum)

