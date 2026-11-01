"""
File: weather_master.py
Name:
-----------------------
This program implements a console-based application that
asks the user to enter weather data and computes summary
statistics based on the inputs.

The program calculates the average, highest, and lowest
temperatures, as well as the number of cold days. The
output format should match the sample run shown in the
Assignment 2 handout.
"""
move=-100


def main():
	total = 0    #重0開始帶入
	step = 0     #重0開始帶入
	print("stanScod\"Weather Master 4.0\"!")#標題
	user=int(input('Nest Temperature:'+('(or -100 to quit)?')))#使用者輸入
	if user!=-100: #為了讓最大與最小值被輸入-100使帶入
		highest = user
		lowest = user
	while move!=user:#開始進入迴圈
			step = step +1 #從第一次使用者輸入時 0+1=1
			total=total+user#從第一次使用者輸入數值時 0+使用者數值

			user = int(input('Nest Temperature:' + ('(or -100 to quit)?')))#再次輸入 數值(第二次輸入)
			if user!=-100:#先判斷使用者輸入是否為-100 避免帶入判斷最高與最低
				if user>highest:
					highest=user
			if user!=-100:
				if lowest>user:
					lowest=user

	else:
		if step == 0:
			print('No temperatures were entered')
		else:
			average = total / step
			print('Average',average)
			print('highest',highest)
			print('lowest',lowest)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
