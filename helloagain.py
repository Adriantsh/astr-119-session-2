def main():
	i = 0  #initializing variable
	x = 119.0

	for i in range(120): #loops over i between 0 and 120

		if((i%2) == 0): #if i is even
			x += 3.0 #add three to x
		else:
			x -= 5.0  #subtract 5 from x

	s = "%3.2f" % x #sets s to x and converts x to a floating point variable
	
	print(s) #print final value

if __name__ == "__main__":
	main()