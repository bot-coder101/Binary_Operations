def binary(number):
	bin_value=''
	while(number>0):
		bin_value+=str(number%2)
		number=number//2
		if number==1:
			bin_value+='1'
			break
	return bin_value[::-1]

def append_zeros(number,count):
	new_num=''.join(('0'*count,number))
	return new_num

def list_output(lis):
	for i in range(len(lis)):
		print(lis[i],end='')

def menu(choice,num1,num2):
	print("Binary number 1 : ",num1," :: ","Binary number 2 : ",num2)
	if choice not in ['1','2','3']:
		print("Invalid option selected!")
	if choice=='1':
		and_value=[]
		for i in range(len(str(num2))):
			if (num1[i]=='1' and num2[i]=='1'):
				and_value.append(1)
			else:
				and_value.append(0)
		print("AND value of the two is : ",end='')
		list_output(and_value)
	if choice=='2':
		or_value=[]
		for i in range(len(str(num1))):
			if(num1[i]=='1' or num2[i]=='1'):
				or_value.append(1)
			else:
				or_value.append(0)
		print("OR value of the two is : ",end='')
		list_output(or_value)

	if choice=='3':
		xor_value=[]
		for i in range(len(str(num1))):
			if (( int(num1[i]) + int(num2[i]) )%2==1):
				xor_value.append(1)
			else:
				xor_value.append(0)
		print("XOR Value of the two is : ",end='')
		list_output(xor_value)

def main():
	print("PROGRAM TO PERFORM BOOLEAN OPERATIONS ON THE BINARY VALUE OF TWO INTEGERS -->")
	num_1=int(input("Enter the first number : "))
	num_2=int(input("Enter the second number : "))
	bin_num1=binary(num_1)
	bin_num2=binary(num_2)
	print("The binary values are",bin_num1,bin_num2,"respectively.")
	if (len(bin_num1) < len(bin_num2)):
		bin_num1=append_zeros(bin_num1,len(bin_num2)-len(bin_num1))
	if (len(bin_num2) < len(bin_num1)):
		bin_num2=append_zeros(bin_num2,len(bin_num1)-len(bin_num2))

	while(True):
		print()
		print("What action do you want to perform between the binary values -->")
		print("1) AND")
		print("2) OR")
		print("3) Exclusive OR")
		print("4) Exit the program")
		choice=input()
		if choice=='4':
			break
		else:
			menu(choice,bin_num1,bin_num2)
		print()
	print("Thank you :)")
	print()

main()

