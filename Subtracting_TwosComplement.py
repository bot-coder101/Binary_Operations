def subtract(dnum_1,dnum_2,num_1,num_2):
	one='1'
	one=append_zeros(one,len(num_2)-len(one))

	#Two's complement of number 2
	num2_tc=twos_comp(num_2,one)
	#Addition of tc and num_1
	diff=bin_addition(num_1[::-1],num2_tc[::-1])
	print("Difference -->")
	#Carry case
	if dnum_1>dnum_2:
		omit_carry=''
		for i in range(1,len(diff)):
			omit_carry+=diff[i]
		print("Number :",decimal(omit_carry[::-1]),":: Binary Equivalent :",omit_carry)
	#Negative case
	else:
		one='1'
		one=append_zeros(one,len(diff))
		diff_neg=twos_comp(diff,one)
		print("Number : -",decimal(diff_neg[::-1])," :: Binary Equivalent : -",diff_neg,sep='')

def equateLength(num_1,num_2):
	if (len(num_1) < len(num_2)):
		num_1=append_zeros(num_1,len(num_2)-len(num_1))
	if (len(num_2) < len(num_1)):
		num_2=append_zeros(num_2,len(num_1)-len(num_2))
	return num_1,num_2

def binary(number):
	bin_value=''
	while(number>0):
		bin_value+=str(number%2)
		number=number//2
		if number==1:
			bin_value+='1'
			break
	return bin_value[::-1]

def decimal(bin_value):
	result=0
	for i in range(len(bin_value)):
		if bin_value[i]=='1':
			result+=2**i
	return result

def ones_comp(bin_value):
	new_num=''
	for i in range(len(bin_value)):
		if bin_value[i]=='0':
			new_num+='1'
		else:
			new_num+='0'
	return new_num[::1]

def twos_comp(bin_value,one):
	first_stage=ones_comp(bin_value)
	second_stage=bin_addition(first_stage[::-1],one[::-1])
	return second_stage

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

def append_zeros(number,count):
	new_num=''.join(('0'*count,number))
	return new_num

def main():
	print("Program to perform binary subtraction between two numbers-->")
	dnum_1=int(input("Enter number 1 : "))
	dnum_2=int(input("Enter number 2 : "))
	num_1=binary(dnum_1)
	num_2=binary(dnum_2)
	num_1,num_2=equateLength(num_1,num_2)
	print("Number :",dnum_1,":: Binary Equivalent :",num_1)
	print("Number :",dnum_2,":: Binary Equivalent :",num_2)
	subtract(dnum_1,dnum_2,num_1,num_2)
main()
