import sys

def equateLength(num_1,num_2):
	if (len(num_1) < len(num_2)):
		num_1=append_zeros(num_1,len(num_2)-len(num_1))
	if (len(num_2) < len(num_1)):
		num_2=append_zeros(num_2,len(num_1)-len(num_2))
	return num_1,num_2

def append_zeros(number,count):
	new_num=''.join(('0'*count,number))
	return new_num

def selectiveSet(bin1,bin2):
	temp=[]
	for i in range(len(bin1)):
		temp.append(bin1[i])
	for i in range(len(bin1)):
		if bin2[i]=='1':
			temp[i]='1'
	updatedBin=''
	for i in range(len(bin1)):
		updatedBin+=temp[i]
	print("A :",bin1,'(BEFORE)')
	print("B :",bin2)
	print("A :",updatedBin,"(AFTER)")

if __name__=='__main__':
	print("-- Program to implement Selective Set logical operation --")
	A=input("Enter binary number A : ")
	B=input("Enter binary number B : ")
	for i in range(len(A)):
		if A[i] not in ['0','1']:
			print("Invalid number!")
			sys.exit(1)
	for i in range(len(B)):
		if B[i] not in ['0','1']:
			print("Invalid number!")
			sys.exit(1)
	A,B=equateLength(A,B)
	selectiveSet(A,B)
