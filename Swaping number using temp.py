print('Swaping number using temp')
x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: '+ str(x))
print('The value of y after swapping: '+ str(y))

print('Swaping number without using temp')
x = input('Enter value of x: ')
y = input('Enter value of y: ')
x, y = y, x
print("x =", x)
print("y =", y)

print('Swaping number by addition and substration')
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x + y
y = x - y
x = x - y
print("x =",x)
print("y =", y)

print('Swaping number by multiplication and devision')
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x * y
y = x // y
x = x // y
print("x =",x)
print("y =", y)

print('Swaping number using XOR')
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
x = x ^ y
y = x ^ y
x = x ^ y
print("x =",x)
print("y =", y)