"""
File: rocket.py
Name:
-----------------------
This program implements a console-based application that
draws an ASCII art rocket.

The size of the rocket is determined by a constant named
SIZE, which is defined at the top of the file. The output
format should match the sample run shown in the Assignment 3 handout.
"""

# This constant determines rocket size.
SIZE = 3

def main():
    head()
    belt()
    upper()
    lower()
    belt()
    head()

def head():
    for i in range(SIZE):#SIZE(3)所以給i為012(3次)從0開始到2 3不算 0.1.2
        for j in range(SIZE-i):#1迴圈 size(3)-i(0)=3  2迴圈 size(3)-i(1)=2  3迴圈size(3)-i(2)=1
            print(" ",end="")#1迴圈所以會有三個空格  2......
        for j in range(i+1):#1迴圈 i(0)+1=1  2迴圈i(1)+1=2  3迴圈i(2)+1=3
            print('/',end="")#1迴圈 因為前面有三個空格後接著i(0)+1()=1 所以接一個/  2....
        for j in range(i+1):#1迴圈 i(0)+1=1 2迴圈i(1)+1=2  3迴圈i(2)+1=3
            print('\\',end="")#1迴圈(0)+1()=1  因為前面有三個空格接一個/ 現在會在接一個\   2....
        print("")#結束後 面空白
def belt():
    for i in range(1):
        print("+",end="")#第一個固定一個+
        for j in range(SIZE*2):#size(3)*2=6
            print("=",end="")#會有6各=
        print("+")#6各=後再接一個+
def upper():
    for i in range(SIZE):
        print("|",end="")
        for j in range(SIZE - i-1):
            print(".", end="")
        for j in range(i + 1):
             print('/', end="")
             print('\\',end="")
        for j in range(SIZE - i-1):
            print(".", end="")
        print("|")

def lower():
    for i in range(SIZE):
        print("|",end="")
        for j in range(i):
            print(".",end="")
        for j in range(SIZE-i):
            print('\\', end="")
            print('/', end="")
        for j in range(i):
            print(".", end="")
        print("|")







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
