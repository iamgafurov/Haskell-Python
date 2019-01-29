def area(lst):
    n=len(lst)
    s=0
    for i in range(0,n-1):
        s+=lst[i][0]*lst[i+1][1]
    #    print (lst[i][0] , lst[i+1][1])
    #print (s)
    s+=lst[0][1]*lst[n-1][0]
    #print (s)
    for i in range(0,n-1):
        s-=lst[i+1][0]*lst[i][1]
    s-=lst[n-1][1]*lst[0][0]
    return abs(s/2)
