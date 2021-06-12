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
	print("Program to print the one's and two's complement of a binary value -->")
	bin_value=input("Enter the binary number : ")
	print("One's complement value is :",ones_comp(bin_value))
	one='1'
	one=append_zeros(one,len(bin_value)-len(one))
	print("Two's complement value is :",twos_comp(bin_value,one))

main()
