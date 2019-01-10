
def gcd(n,m):
    while n!=0:
        r=m%n
        m=n;n=r
    if(m>0):
        return m;
    else:
        return -m;
class Rational(object):
    '''Rational numbers'''
    #Number is defined by numerator n and denminator m
    #n/m  , where gcd(n,m)==1
    def __init__(self,num=0 ,denom = 1):
        if type(num) == Rational:
            self.n = num.n;
            self.m = num.m;

        elif type(num)== str:
            #3/7
            frac=num.find('/')
            if frac> 0 :
                self.n = int (num [:frac])
                self.m = int (num [frac+1])
            elif frac ==0:
                raise ValueError()
            else :
                self.n= int(num)
                self.m= 1
        else:
            self.n = int(num)
            self.m = int(denom)
        d=gcd(self.n , self.m)
        if d!=1:
            self.n //=d
            self.m//=d
        elif self.m == 0:
            raise ValueError("Zro denominator")

    def __str__ (self):
        if self.m == 1:
            return str(self.n)
        else :
            return str (self.n) + "/"+ str(self.m)
    def __repr__ (self):
        return str(self)
    def __add__ (self,b):
        return Rational(
            self.n * b.m  + self.m * b.n,
            self.m*b.m
        )
    def __sub__ (self,b):
        return Rational(
            self.n * b.m  - self.m * b.n,
            self.m*b.m
        )
    def __mul__ (self,b):
        return Rational(
            self.n * b.n,
            self.m*b.m
        )
    def __truediv__ (self,b):
        return Rational(
            self.n * b.m,
            self.m* b.n
        )
    def __gt__(self, other):
        if(self.n /self.m > other.n/other.m):
            return True
        else:
            return False

    '''def rootofR(self, epsl):
        p=(self.n/self.m)
        x0 = p
        x1 = (x0 + p/x0) *0.5
        while abs(x1 - x0) > epsl:
            x0 = x1
            x1 = (x0 + self / x0) / 2
        return x1'''
    def __abs__(self):
        return Rational(abs (self.n),abs(self.m))
    def RtoF(self):
            return float(self.n/self.m)



def main():

    a=Rational(input('Please input a: '))
    b=Rational(input('Please input b: '))
    #a=Rational(a)
    #a=Rational(a)
    #print(a-Rational(1,1))
    print(a + b)
    print(a * b)
    print (a/b)
    #print rootofR(a,1e-15)
    #def __iad__(self,b): #a+=b
    #             n1 = self.n*b.m + self.m*b.n;
    #            m1 = self.m*b.m
    #           d=gcd(n1,m1)'''
def rootofR(self):
    #epsl = Rational(epsl,1)
    x0 =self +  Rational(1)
    x1 = (x0 + self/ x0) * Rational(1/2)
    while abs(x1 - x0) > Rational(1/100000000):
        x0 = x1
        x1 = (x0 + (self/ x0)) / Rational(2)
    return x1
if __name__ == "__main__":
    main()
