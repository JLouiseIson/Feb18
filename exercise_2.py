num = input("place a number:")
sum=num
for i in range (1, num):
	sum = sum * (num-i)
	print 'factorial of',num, 'is',sum
	
