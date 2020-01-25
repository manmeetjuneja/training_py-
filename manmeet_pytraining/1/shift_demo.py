number = int(input("enter a no for left shift:"))
shift = number <<1
print(shift)
if(shift == 2*number):
    print("left shift is twice")
    
numberN = int(input("enter a no for right shift:"))
right_shift = numberN >>1
print(right_shift)

if(right_shift == number/2):
    print("right shift is half")

    

    


