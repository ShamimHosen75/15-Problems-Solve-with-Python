# find fectorial of any number

num = int(input('enter a number: '))

factorial = 1

for n in range(1,num+1):
    factorial = factorial*n

print('the factorial of ',num,' is = ',factorial)