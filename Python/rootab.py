def  sign(x):
    if x>0:
        return 1
    elif x == 0:
        return 0
    else: 
        return (-1)    

def root(f,a,b):
    fa = f(a)
    sa = sign(fa)
    if sa == 0:
        return (True, a)
    fb = f(b)
    sb = sign(fb)
    if sb == 0:
        return (True, b)
        
    if sa*sb>0:
        return (False, a)
    while b-a > 1e-12:
        c = (a + b)/2
        if c <= a or c >= b:
            return (True, c)
        fc = f(c)
        sc = sign(fc)
        
        if sc == 0:
           return (True, c)
        if sa*sc < 0:
            b = c
            sb = sc
        else:
            a = c
            sa = sc
    return (a+b)/2    