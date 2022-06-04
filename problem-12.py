# letter grade function

number = int(input('enter the number: '))

if(number > 100 or number < 1):
    print('you enter a wrong number')
elif(number >= 80):
    print('you got A+')
elif(number >= 70):
    print('you got A')
elif(number >= 60):
    print('you got A-')
elif(number >= 50):
    print('you got B')
elif(number >= 40):
    print('you got C')
elif(number >= 33):
    print('you got D')
else:
    print('you are fail')