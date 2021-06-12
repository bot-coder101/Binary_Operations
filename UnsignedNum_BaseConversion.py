def val(character):
	if character >= '0' and character <= '9':
		return ord(character) - ord('0')
	else:
		return ord(character) - ord('A') + 10;

def todecimal(str,base):
	limit = len(str)
	power = 1
	num = 0
	for i in range(limit - 1, -1, -1):
		if val(str[i]) >= base:
			print('Invalid Number')
			return -1
		num += val(str[i]) * power
		power = power * base
	return num

def conversion(number,base):
    result=[]
    while (number>0):
        result.append(number%base)
        number=number//base
        if number==1:
            result.append(1)
            break
    for i in range(len(result)):
        if result[i] in range(10,36):
            for j in range(26):
                if (result[i]==j+10):
                    result[i]=chr(ord('A') + j)
    return result[::-1]

def list_output(lis):
    for i in range(len(lis)):
        print(lis[i],end='')

def main():
    import sys
    print("Welcome to the base converter!")
    print("===  X (<=36) --> Y (<=36)  ===")
    strr=input("Enter the number to be converted : ")
    base=int(input("Enter the base of the number entered : "))
    if (base>36):
        print("Invalid base entered!")
        sys.exit()
    target_base = int(input("Enter the target base : "))
    if (target_base>36):
        print("Invalid base entered!")
        sys.exit()
    dec_string=todecimal(strr, base)
    converted_string=conversion(dec_string,target_base)
    print(strr,"in base",target_base,"is : ",end='')
    list_output(converted_string)
    print()
main()
