file = open("f.txt","w")
#string = input("enter the detail to save:")
file.write("hello\n")
file.write("manmeet\n")
file.write("juneja\n")

file.close()

file = open("f.txt","r")
A = file.read()
print(A)
file.close()

file = open("f.txt","a")
string = input("enter the detail to save:")
file.write(string)
file.close()

#open for reading line wise
file2 = open("phill.txt","r")
line = file2.readline()
print(line)
#file2.close()

for line in file2:
    h=file.readline()
    print(h)
file2.close()
 
