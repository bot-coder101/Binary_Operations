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

def decimal(bin_value):
	result=0
	for i in range(len(bin_value)):
		if bin_value[i]=='1':
			result+=2**i
	print(bin_value[::-1],"decimal equivalent is :",result)

def one_zero(num_1,num_2,carry):
	if carry=='0':
		if num_1=='0' and num_2=='0':
			return '0','0'
		if num_1=='0' and num_2=='1':
			return '1','0'
		if num_1=='1' and num_2=='0':
			return '1','0'
		if num_1=='1' and num_2=='1':
			return '0','1'
	else:
		if num_1=='0' and num_2=='0':
			return '1','0'
		if num_1=='0' and num_2=='1':
			return '0','1'
		if num_1=='1' and num_2=='0':
			return '0','1'
		if num_1=='1' and num_2=='1':
			return '1','1'

def bin_addition(num_1,num_2):
	new_num=''
	carry='0'
	for i in range(len(num_1)):
		if i==(len(num_1)-1):
			temp,carry=one_zero(num_1[i],num_2[i],carry)
			new_num+=temp
			if carry=='1':
				new_num+=carry
		else:
			temp,carry=one_zero(num_1[i],num_2[i],carry)
			new_num+=temp
	return new_num[::-1]

def main():
	print("Program to perform binary addition of two numbers -->")
	num_1=int(input("Enter number 1 : "))
	num_2=int(input("Enter number 2 : "))
	bin_num1=binary(num_1)
	bin_num2=binary(num_2)
	if (len(bin_num1) < len(bin_num2)):
		bin_num1=append_zeros(bin_num1,len(bin_num2)-len(bin_num1))
	if (len(bin_num2) < len(bin_num1)):
		bin_num2=append_zeros(bin_num2,len(bin_num1)-len(bin_num2))
	print("The binary values are",bin_num1,bin_num2,"resepctively.")
	added=bin_addition(bin_num1[::-1],bin_num2[::-1])
	print("The binary addition of the two is :",added)
	decimal(added[::-1])
main()
