exten = input("enter full path of a file: ")
A = exten.split(".")
print(A)
S = repr(A[-1].replace("pof","pdf"))

#S = S.replace(S,"pdf")
#A[2] = "pdf"
#print(A)




#output   python.pdf
