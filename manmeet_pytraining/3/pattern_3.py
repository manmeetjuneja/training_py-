def pyramid(n):
    for i in range(1, (n+1)//2 + 1): 
        for j in range((n+1)//2 - i):
            print(" ", end = "")
        for k in range((i*2)-1):
            print("*", end = "")
        print()

    for a in range((n+1)//2 + 1, n + 1): 
        for b in range(a - (n+1)//2):
            print(" ", end = "")
        for c in range((n+1 - a)*2 - 1):
            print("*", end = "")
        print()
    
n = int(input("Enter a odd no:"))
pyramid(n)
