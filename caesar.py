"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of the Caesar cipher.

The user is first asked to enter a number that determines
how much the alphabet should be shifted to form a cipher
table. After that, any input string will be encrypted
using the generated cipher.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    n=int(input('Secret number:')) #4
    ciphered=input('Ciphered String:')#輸入要解密的英文
    shifted_alpha=create_shifted(n)#平移後新的字串W~V
    print(shifted_alpha)
    decipher(ciphered,shifted_alpha)#(輸入要解密的英文,新的字串)因為要將ciphered,shifted_alpha傳到下的 def decipher(c,s)
    print(decipher(ciphered,shifted_alpha))


def decipher(c,s):
    ans=""
    for ch in c: #WLLHA 將WLLHA一個一個帶入進去CH W L L H A
        i=s.find(ch) #將每個單字的位置(數字找出來)
        ans += ALPHABET[i]#i為子母位置的數字 後對照ALPHABET的字串比對後 所對應的子母

    return ans


def create_shifted(n):
    first=ALPHABET[len(ALPHABET)-n:]#ALPHAVET(26)-N(4)=22 -->[22:] 因為數字在冒號前面的話由第22開始算到26所以(WXYZ)保留
    second=ALPHABET[:len(ALPHABET)-n]#ALPHAVET(26)-N(4)=22-->[:22] 因為數字在冒號後面所以由0開始到22 保留
    return first+second#所以first(WXYZ)+second(A~V)新的字串由W~V

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
