#Q1

Unlimited, i.e, 0 or more

#Q2

False False True False

#Q3

Hello world
Is it over yet?

#Q4

n = 123
print (n - n % 10)/ 10
print ((n - n % 10) % 100) / 10
print (n % 100 - n % 10) / 10

#Q5

10

#Q6

import math

def f(x):
  return (-5 * math.pow(x, 5)) + (69 * math.pow(x, 2)) - 47

print f(0)
print f(1)
print f(2)
print f(3)

print max(f(0), f(1), f(2), f(3))

#Q7

import math
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * math.pow(1 + rate_per_period, periods)
print "$500 at 4% compounded daily for 10 years yields $", future_value(500, .04, 10, 10) 
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

#Q8

import math

def polygon_area(sides, length):
    a = math.tan(math.pi / sides)
    b = (sides) * math.pow(length, 2)
    c = b / a
    return c / 4

print polygon_area(5, 7)
print polygon_area(7, 3)

#Q9

Incorrect indentation

#Q10

import math
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)
