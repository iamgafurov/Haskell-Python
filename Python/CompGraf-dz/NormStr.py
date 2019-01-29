import sys
def NormalizeStr(x):
	f = open("input.txt")
	lines = f.readlines()
	n=len(lines)
	k=0
	for i in lines :
		for j in range(0,len(i)):
			if j>x:
				break
			sys.stdout.write(i[j])
			
		print("\n")
	
	

