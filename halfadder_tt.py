def main():
	print("Program to print the truth table of half adder -->")
	X=[0,0,1,1]
	Y=[0,1,0,1]
	print("X Y | C S")
	for i in range(4):
		if X[i]==0 and Y[i]==0:
			print("____|____")
			print(X[i],Y[i],"|",X[i] & Y[i],X[i] ^ Y[i])
		else:
			print(X[i],Y[i],"|",X[i] & Y[i],X[i] ^ Y[i])

main()
