###solution to exercise 81 from ben stephenson's "the python workbook".

import math

def hypotenuse(x,y):
  return math.sqrt(x ** 2 + y ** 2)

x, y = input('Enter the two shorter sides:').split(',')

x = int(x)
y = int(y)

print(f'The hypotenuse is {hypotenuse(x,y):.2f}.')
