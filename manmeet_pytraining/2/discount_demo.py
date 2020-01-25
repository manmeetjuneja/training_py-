qua = int(input("enter the number of packages to purchase:"))
pack = 99
if qua in range(10):
    cost  = 99*qua
    dis = 0
    cost = cost - dis
    print("discount:"+str(dis))
    print("amount:"+str(cost))
    
elif qua in range(10,19):
    cost  = 99*qua
    dis = (10/100)*cost
    cost = cost - dis
    print("discount:"+str(dis))
    print("amount:"+str(cost))

elif qua in range(20,49):
    cost  = 99*qua
    dis = (20/100)*cost
    cost = cost - dis
    print("discount:"+str(dis))
    print("amount:"+str(cost))
    
elif qua in range(50,99):
    cost  = 99*qua
    dis = (30/100)*cost
    cost = cost - dis
    print("discount:"+str(dis))
    print("amount:"+str(cost))

else:
    cost  = 99*qua
    dis = (40/100)*cost
    cost = cost - dis
    print("discount:"+str(dis))
    print("amount:"+str(cost))
    
