#! /usr/bin/python3

__author__      = "Batang Hamog"
__copyright__   = "Copyright 2019, Planet Earth"

import os

class color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

print (color.BOLD + color.YELLOW +"""

MATHINICS:

Description:

This is a Simple MDAS Calculator written in Python3
and the logic behind this program uses Classes Functions 
Here's the list of operators that you can use for this program

For Addition type plus sign: + 
For Subtraction type minus sign: - 
For Multiplication type asteris: *
For Division type forward slash:  /

Enjoy and Happy Computing! :D

""")



class Mathindi(object):

    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        return Mathindi(self.val + other.val)

    def __sub__(self, other):
        return Mathindi(self.val - other.val)

    def __mul__(self, other):
        return Mathindi(self.val * other.val)
    
    def __truediv__(self, other):
        return Mathindi(self.val / other.val)



 
def main():
  

    try:
        
        ch_ops = input('Press Enter Key to Start... ')


        while (ch_ops != '+') and (ch_ops != '-') and (ch_ops != '*') and (ch_ops != '/'):

                ch_ops = input('Enter What Operation you want to use: ')

                if(ch_ops == '+') or (ch_ops == '-') or (ch_ops == '*') or (ch_ops == '/'):

                    op_num1 = int(input('Enter First Number: '))
                    op_num2 = int(input('Enter Second Number: '))
            
                    num1 = Mathindi(op_num1)
                    num2 = Mathindi(op_num2)
    
                    if(ch_ops == '+'):
                        result = num1 + num2
                        print('Total: ',result.val)
            
                    elif (ch_ops == '-'):
                        result = num1 - num2
                        print('Total: ',result.val)

                    elif (ch_ops == '*'):
                        result = num1 * num2
                        print('Total: ',result.val)

                    elif (ch_ops == '/'):
                        result = num1 / num2
                        print('Total: ',result.val)
                    
                    else:
                         print('Invalid Input! \n Wag kang Hacker. ')
                    
                elif(ch_ops == 'help'):

                    print('''
                    ######### AVAILABLE #########
                              OPERATORS
                              WAG MANG HULA 

                    For Addition type plus sign: + 
                    For Subtraction type minus sign: - 
                    For Multiplication type asteris: *
                    For Division type forward slash:  /

                    Type: 
                     exit or quit or Ctrl + C 
                     To exit to the program 

                    ################################
                    ''')

                elif(ch_ops == 'exit') or (ch_ops == 'quit') :

                    print('''
                          ################################
                           Thank You For Using This Program!
                          #################################
                          ''')
                    cmd = exit()
                    os.system(cmd)

                else:
                    print('''

                       Ivalid Operator Wag Kang Hacker uy!..
                        type; help to see the operator list

                       ''')
        

    except ValueError as e:
        print('Check your Inputs', e)

    


if __name__=='__main__':
    main()
 
