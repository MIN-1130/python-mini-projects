"""
File: hailstone.py
Name:
-----------------------
This program implements a console-based simulation of the
Hailstone sequence, as defined by Douglas Hofstadter.

Starting from a user-provided number, the program repeatedly
applies the Hailstone rules and prints each step. The output
format should match the sample run shown in the Assignment 2 handout.
"""

def main():
    print('This program computes Hailstone sequences')
    n=int(input('Please enter a nuber:'))
    steps = 0
    if n==0:
        print('It took'+str(steps)+'steps to reach 1')
    else:
        while n!=1:
            if n % 2 == 1:
                new_n=3*n+1
                print(str(n)+' is odd, so I make 3n+1: '+str(new_n))
                #odd
            else:
                new_n=n//2
                print(str(n) + ' is even, so I take half: ' + str(new_n))
                #even
            n=new_n
            steps = steps+1
        print('It took'+str(steps)+'steps to reach 1')










if __name__ == "__main__":
    main()