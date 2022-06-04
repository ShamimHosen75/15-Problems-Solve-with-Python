# read number form keyboard and find the larged number in three number 

num1 = input('enter the first number: ')
num2 = input('enter the second number: ')
num3 = input('enter the third number: ')

if(num1 > num2 and num1 > num3 ):
    print('Larged number is', num1)
elif( num2 > num1 and num2 > num3):
    print('Larged number is ', num2)
else:
    print('larged number is', num3)


# read number form keyboard and find the smallest number in three number 

if(num1 < num2 and num1 < num3 ):
    print('smallest number is', num1)
elif( num2 < num1 and num2 < num3):
    print('smallest number is ', num2)
else:
    print('smallest number is', num3)