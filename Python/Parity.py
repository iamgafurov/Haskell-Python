def parity(lst):
    n=len(lst)
    k=0
    for i in range(0,n):
        for j in range(0,n):
            if lst[i]<lst[j]:
                temp=lst[i]
                lst[i]=lst[j]
                lst [j]=temp
                k+=1
    if k%2 == 0:
        return 0
    else :
        return 1
