import numpy as np

Order  =int(input("enter the order of matrix(0-3):"))
lo_shu_magic = np.zeros((Order,Order), dtype=int)
print(lo_shu_magic)
n = 1
i, j = 0, Order//2

while n <= Order**2:
    lo_shu_magic[i, j] = n
    n += 1
    Ai, Aj = (i-1) % Order, (j+1)% Order
    if lo_shu_magic[Ai, Aj]:
        i += 1
    else:
        i, j = Ai, Aj
print("your desired"+str(Order)+"matrix is:")

print(np.transpose(lo_shu_magic))
