a = int(input('Enter the number'))
for i in range (2,a):
    if a%i == 0:
        print('Not prime')
        break
else:
    print('prime')
