import math
def tcos(x, eps = 1e-14):
	i=0
	p=1
	z=1
	l=1
	x=abs(x);
	if(x>2*math.pi):
		while(x>2*math.pi):
			x-=2*math.pi
	while(l>eps):
		i+=2;
		z*=-1
		l=pow(x,i)/(math.factorial(i))
		p+=z*l
		
	return p;
