A = [0 , 0 , 1 , 1 ]
B = [0 , 1 , 0 , 1 ]


def OR (X,Y, theta) :
	print("OR :")
	for i,j in zip(A,B):
		if (X*i + Y*j) >= theta:
			print(" 1 ")
		else:	
			print(" 0 ")

def AND (X,Y, theta) :
	print("AND :")
	for i,j in zip(A,B):
		if i == j == 1 :
			if (X*i + Y*j) >= theta:
	 			print(" 1 ")
		else:	
			print(" 0 ")

def NAND (X,Y, theta) :
	print("NAND :")
	for i,j in zip(A,B):
		if (X*i) - (Y*j) >= theta:
	 		print(" 1 ")
		else:	
			print(" 0 ")


def NOR (X,Y, theta) :
	print("NOR :")
	for i,j in zip(A,B):
		if i == j == 0 :
			if (X*i + Y*j) >= theta:
	 			print(" 1 ")
			else:
				print(" 0 ")
		else:	
			print(" 0 ")

def XOR (X,Y, theta) :
	print("XOR :")
	for i,j in zip(A,B):
		if i == j :
			print(" 0 ")
		elif (X*i + Y*j) >= theta:
			print(" 1 ")
		else:
			print(" 0 ")



X = input('enter X :')
Y = input('enter Y :')
theta = input('enter threshold value :')
OR(int(X),int(Y),int(theta))
AND(int(X),int(Y),int(theta))
NAND(int(X),int(Y),int(theta))
NOR(int(X),int(Y),int(theta))
XOR(int(X),int(Y),int(theta))