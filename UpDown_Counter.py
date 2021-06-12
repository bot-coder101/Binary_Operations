import sys

def subtract(num_1,num_2):
	#Two's complement of number 2
	num2_tc=twos_comp(num_2,one)
	#Addition of tc and num_1
	diff=bin_addition(num_1[::-1],num2_tc[::-1])
	omit_carry=''
	for i in range(1,len(diff)):
		omit_carry+=diff[i]
	return omit_carry

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

if __name__=='__main__':
	print("-- 5-bit Up/Down counter --")
	number=input("Enter the initial binary number : ")
	for i in range(len(number)):
		if number[i] not in ['0','1']:
			print("Invalid number entered!")
			sys.exit(1)
	if len(number)>5:
		print("Overflow!")
		sys.exit(1)
	else:
		number=append_zeros(number,5-len(number))
	choice='Y'
	one='00001'
	while choice != 'N':
		print()
		print("Number :",number)
		print("1) UP")
		print("2) DOWN")
		print("3) EXIT")
		option=int(input(":"))
		if option not in [1,2,3]:
			print("ERROR : Invalid Option!!!")
		else:
			if option == 1:
				if number == '11111':
					print("Overflow!")
					number='11111'
				else:
					number=bin_addition(number[::-1],one[::-1])
			elif option == 2:
				if number == '00000':
					print("Underflow!")
					number = '00000'
				else:
					number=subtract(number,one)
			else:
				choice='N'
