num = int(input('Enter the number whose table you want to find out:'))
print('the table of {0} is:'.format(num))
for i in range (1, 11, 1):
    print(num, 'x', i, '=', num*i)
    