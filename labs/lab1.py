import math

print('введите x, y, z')
x = float(input())
y = float(input())
z = float(input())

a = ((pow((abs(x - 1)),1/5) + math.exp(-y)) / (math.sin(x) + math.log10(1 + y)))
b = (math.sin(pow((abs(z + 71)),5)) + math.cos(pow(abs(y),3)) + pow(x,3) + pow(y,4))

print('a: ',a)
print('b: ',b)
