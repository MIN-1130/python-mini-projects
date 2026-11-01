"""
File: prime_checker.py
Name:
-----------------------
This program asks the user to enter a number and checks whether
the number is a prime number.

When the program starts, it first prints a welcome message to
the console. It then repeatedly prompts the user to enter an
integer greater than 1 and determines whether the number is prime.

The program will stop running when the user enters the EXIT value.
"""
move=-100

def main():
	print("Welcome to the prime checker")
	n=int(input('n:'))

	while n!=-100:#使用者可以一直輸入直到 輸入-100
		i = 2
		count = 0
		while i<n:#當i<n時進入迴圈
			if n%i==0:#判斷
				count=count+1
			i = i + 1#被除的要一直累加除 直到i==n停止迴圈

		if count==0:
			print(n,"is a prime number")
		else:
			print(n,"is not a prime number")
		n = int(input('n:'))
	else:
		print('Have a good one!')





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
