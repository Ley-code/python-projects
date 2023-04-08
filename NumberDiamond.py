for i in range(19):
    for j in range(10 - i):
        print(str(j),end= " ")
    
    for j in range(i):
        if i < 10:
            print("@",end=" ")

    for l in range(i-1):
        if i <10:
            print("@",end=" ")


    for k in range(9-i,-1,-1):
        if i == 0:
            if k!= 0:
                print(k-1,end=" ")
                continue
            if k==0:
                continue
        if i < 10:
            print(k,end=" ")
    
    if i >9:
        for m in range(i-8):
            print(m,end=" ")
        for n in range(18-i,0,-1):
            print("@",end=" ")
        for o in range(17-i,0,-1):
            print("@",end=" ")
        
        for p in range(i-9,-1,-1):
            if i == 18:
                print("8 7 6 5 4 3 2 1 0",end=" ")
                break
            print(p,end=" ")
    
    print()

