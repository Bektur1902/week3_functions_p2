import math

a = int(input('Enter number: '))

def chislo(a):

	if a < 2:
	    print("Число должно быть больше 1")
	    quit()
	elif a == 2:
	    print("Это простое число")
	    quit()
	 
	i = 2 
	 
	limit = int(math.sqrt(a))
	 
	while i <= limit:
	    if a % i == 0:
	        print("Это сложное число")
	        quit() 
	    i += 1 
	 
	print("Это простое число")

chislo(a)