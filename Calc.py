from math import factorial
from math import sqrt
from math import pi
import sys

def isPrimeNumber(num1):
    isPrime = True
    if num1<2:
        print(num1, 'is not prime nor composite.')
    elif num1 == 2:
        isPrime = True  
    else:
        for a in range(2, num1):
            if num1%a == 0:
                isPrime = False                
                break
            else:
                continue
        return isPrime;

def is_int(num):
    try:
        x = int(num)
        return True
    except ValueError:
        return False

print('This is a calculator')
print('Enter username')
tryagain_valid = ['yes', 'ok', 'sure', 'y', 'okay', 'yeah', 'yea', 'ya', 'yah', 'mhm','mmhm', 'k', 'kk', 'yea man', 'go']
tryagain = 'yes'
v = input()
if v == 'Suyash' or v == 'Suvansh' or v == 'Sanjeev' or v == 'Reema':
    print('You are a legend. You don\'t need a password because of your immensely high level of savageness.\n')
else:
    print(v, 'enter password to access calculator')
    password = input()
    if password != 'lightningboy2003':
        print('Password incorrect')
        sys.exit()
    else:
        pass
print('Welcome to Suyash\'s Calculator.')
while True:
    invalid_input = False
    print('+ is add\n'
        + '- is subtract\n'
        + '* is multiply\n'
        + '/ is divide\n'
        + '// is divide and knock off everything after the decimal\n'
        + '% is remainder\n'
        + '! is factorial\n'
        + '%% is percent of something\n'
        + '^ is to the power of\n'
        + 'sqrt is square root\n'
        + 'hyp is finding the hypotenuse if x and y are legs of a right triangle\n'
        + '#% is division in the form of something remainder something\n'
        + 'OA is area of a circle\n'
        + 'OC is circumference of a circle\n'
        + 'OD is diameter of a circle\n'
        + 'ave is the average of x and y\n'
        + 'pri checks if a number is prime or not\n'
        + 'expr lets you input an expression and solves that expression. CAUTION use spaces between numbers and operators in the expression.\nCAUTION for operations \'pri\', \'OA\', \'OC\', and \'OD\' write x pri/OA/OC/OD y even though the program will disregard the number y.\nCAUTION for OA, OC, OD num1 is the radius.\n')
        
    print('What is your expression?')
    x = input()
    splits = x.split()
    if len(splits) == 3:
        num1 = int(splits[0])
        num2 = int(splits[2])
        operation = splits[1]
    elif len(splits) == 2:
        if is_int(splits[0]):
            num1 = int(splits[0])
            operation = splits[1]
        elif is_int(splits[1]):
            num1 = int(splits[1])
            operation = splits[0]
        else:
            print("Invalid syntax: must enter a number")
    elif splits[0] == "quit":
        break
    else:
        print("Invalid syntax: must enter expression in format \"<number> <operand> <number>\", \"<number> <operand>\", or \"<operand> <number>\"")
    if operation == '+':
        y = num1 + num2
    elif operation == '-':
        y = num1 - num2
    elif operation == '*':
        y = num1 * num2
    elif operation == '/':
        y = num1/num2
    elif operation == '//':
        y = num1//num2
    elif operation == '%':
        y = num1%num2
    elif operation == '%%':
        y = (num1/100)*num2
    elif operation == 'hyp':
        y = sqrt(num1**2 + num2**2)
    elif operation == '()%':
        y = num1//num2, 'R', num1%num2
    elif operation == 'ave':
        y = (num1+num2)/2
    elif operation == '^':
        y = num1**num2
    elif operation == 'sqrt':
        y = sqrt(num1)    
    elif operation == 'pri':
        y = ''
        if isPrimeNumber(num1):
            print(num1, 'is prime.')
        else:
            print(num1, 'is not prime.')
    elif operation == 'OA':
        y = (num1**2)* pi
    elif operation == 'OC':
        y = (2*num1)* pi
    elif operation == 'OD':
        y = num1*2
    else:
        invalid_input = True
        print('Invalid syntax: operation invalid')
    if not invalid_input:
        print(y, '\n')
