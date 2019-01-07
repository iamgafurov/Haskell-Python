#def polindrom(s):
    s=input("Vvedite slovo");
    s1="";
    for i in range(0,len(s)):
        s1[i]=s[-i-1];
    if(s1==s):
        print("it's polindrom")
    else :
        print("it is't polindrom ")
