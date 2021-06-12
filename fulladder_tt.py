def main():
	print("Program to print the full-adder truth table of 3 variables -->")
	x=[0,0,0,0,1,1,1,1]
	y=[0,0,1,1,0,0,1,1]
	z=[0,1,0,1,0,1,0,1]
	print("X Y Z | C S")
	for i in range(8):
		if i==0:
			print("______|____")
			print(x[i],y[i],z[i],"|",(x[i] & y[i]) | ((x[i] ^ y[i])&z[i]),x[i]^y[i]^z[i])
		else:
			print(x[i],y[i],z[i],"|",(x[i] & y[i]) | ((x[i] ^ y[i])&z[i]),x[i]^y[i]^z[i])

main()
