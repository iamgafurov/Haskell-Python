def RPN(s):
    lst1=s.split(' ')
    lst2 = []
    res=int(lst1[0])
    for i in lst1:
        if i.isnumeric():
            lst2.append(i)
        elif(i=='+'):
            res+=int(lst2[1])
            lst2[1]=res;
            del lst2[0]
        elif(i=='-'):
            res-=int(lst2[1])
            lst2[1]=res;
            del lst2[0]
        elif(i=='*'):
            res*=int(lst2[1])
            lst2[1]=res;
            del lst2[0]
        elif(i=='/'):
            res/=int(lst2[1])
            lst2[1]=res;
            del lst2[0]


    return res
