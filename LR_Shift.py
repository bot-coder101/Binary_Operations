def toBinary(number):
	binary=''
	while number!=0:
		if number%2==0:
			binary+='0'
			number=number//2
		else:
			binary+='1'
			number=number//2
	return binary[::-1]

def toDecimal(bnum):
	decimal=0
	for i in range(len(bnum)):
		if bnum[i]=='1':
			decimal+=2**i
		else:
			continue
	return decimal

def shiftLeft(bnum,lsv):
	for i in range(lsv):
		bnum+='0'
	return bnum

def shiftRight(bnum,rsv):
	if len(bnum)<rsv:
		return '0'
	else:
		list=[]
		for i in range(len(bnum)):
			list.append(bnum[i])
		limit=len(list)
		for i in range(rsv):
			del list[limit-1-i]
		for i in range(rsv):
			list.insert(0,'0')
		shift=''
		for i in range(len(list)):
			shift+=list[i]
		return shift

if __name__=='__main__':
	dnum=int(input("Enter the number(Base 10) : "))
	bnum=toBinary(dnum)
	print("Number :",dnum,":: Binary Equivalent :",bnum)
	print()
	lsv=int(input("Enter Left Shift Value : "))
	if lsv < 0:
		print("Invalid value!")
	else:
		lnum=shiftLeft(bnum,lsv)
		print("Left shifted value :",lnum,":: Decimal Equivalent :",toDecimal(lnum[::-1]))
	print()
	rsv=int(input("Enter Right Shift Value : "))
	if rsv < 0:
		print("Invalid value!")
	else:
		rnum=shiftRight(bnum,rsv)
		print("Right shifted value :",rnum,":: Decimal Equivalent :",toDecimal(rnum[::-1]))
