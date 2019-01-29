import sys
def NormalizeStr(x):
	f = open("input.txt")
	lines = f.readlines()
	n=len(lines)
	k=0
	for i in lines :
		for j in range(0,len(lines)):
			k+=1
			sys.stdout.write(lst[i][j])
			if k>x:
				k=0
				break
	
	

