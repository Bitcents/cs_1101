from math import sqrt


def square_number(number):
    return number*number


def calc_hypotenuse(a, b):
    sum_of_squares = square_number(a) + square_number(b)
    hypotenuse = sqrt(sum_of_squares)
    return hypotenuse

print(calc_hypotenuse(3,4))
print(calc_hypotenuse(6,8))
print(calc_hypotenuse(5,12))
print(calc_hypotenuse(1,1))
