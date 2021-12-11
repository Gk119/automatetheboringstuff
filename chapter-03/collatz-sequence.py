import sys

def collatz(number):
	if(number%2 == 0):
		n = number//2
		print(n)
		return n
	else:
		n = 3*number + 1
		print(n)
		return n

try:	
	num = int(input("Enter number:\n"))
except:
	print("Enter a number!")
	sys.exit()
while num != 1:
	num = collatz(num)
		
