def nrootofx (a,n):
    x0=a+1;
    x1=(x0+a/x0)/n;
    while abs(x1-x0)>1e-15:
        x0=x1;
        x1=((n-1)*x0+a/(x0**(n-1)))/n;
    return x1;
