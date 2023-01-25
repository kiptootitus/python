# python math functions
# example 1 math.ceil(x) returns the smallest integer greater than or equal to x

import math

x = 4.2
rounded_up = math.ceil(x)
print(rounded_up) # Output: 5

x = -3.14
rounded_up = math.ceil(x)
print(rounded_up) # Output: -3


y = 67.901456
rounded_up = math.ceil(y)
print(rounded_up) # Output: 68


# example 2 math.floor(x) returns the largest integer less than or equal to x
import math
e = 2.718281828459045
floor_up = math.floor(e)
print(floor_up) # Output: 2



# example 3 math.fabs(x) returns the absolute value of x
# The absolute value of a number is its value without regard to whether it is positive or negative.
import math
x = -10
fab_up = math.fabs(x)
print(fab_up) 

g =12.45
fab_up= math.fabs(g)
print(fab_up)
 

# example 4 math.factorial(x) returns the factorial of x

d= 8
factor_up = math.factorial(d)
print(factor_up)
# example 5 math.fmod(x,y) returns the remainder when x is divided by y
import math
r = 1900; y = 2000;
f_up = math.fmod(r,y)
print (f_up)

print(10%9)
# example 6 math.frexp(x) returns the mantissa and exponent of x as the pair (m,e)
# example 7 math.ldexp(x,y) returns x * (2**y)
