A = input("Enter the name:")
list = []
list.append(A)
for a in range(5):
    k = int(input("enter"+str(a)+"theory marks:"))
    list.append(k)

for n in range(3):
    k = int(input("enter"+str(n)+"ptatical marks:"))
    list.append(k)
print(list)
S = list[1:6]
y = sum(S)
#print(Sum)
F = list[6:9]
w =sum(F)
percent = (sum(S+F)/500)*100

print(str(A)+" obtained "+str(y)+" marks out of 500 in theory and "+str(sum(S+F))+" marks out of 40 in praticals and successfully passed the exam with "+str(percent)+"in aggrgate ,Many congratulation to"+str(a))
