# first define a boolean function
# that checks whether an integer 
# is divisible by another
# function checks if a is divisble by b
def is_divisible(a: int, b: int) -> bool:
    return (a%b == 0)


# we then define the is_power function
# this function also takes two integer arguments
# and returns a boolean valuee
# function checks if a is a power of b
def is_power(a: int, b: int) -> bool:
    # we first define the base case
    # a number is always a power of itself
    # therefore if a and b are equal
    # the function returns true
    if (a == b):
        return True
    
    # 1 is a power of any integer
    # this is because any integer to the power 0 is 1
    # the above condition a == b 
    # is a special case of a == 1
    # we could remove the a == b condition 
    # and the program would still work
    if (a == 1):
        return True

    # on the other hand there is only integer
    # that is a power of 1
    # and that is 1 itself
    # trying to check whether some other positive integer
    # is a power of 1 will cause the program to raise 
    # a maximum recursion depth error
    # therefore if the base is 1 
    # the function returns false
    # since we check a first, if a is 1
    # we will get true even if b is 1 
    if (b == 1):
        return False
    
    # this is the recursion condition
    # we first check if a is divisible by b
    # if it is, we take out a factor of b out of a
    # and perform the check again
    if is_divisible(a,b):
        a = a/b
        return is_power(a, b)
    
    # if a is not divisible by b 
    # even at some point of the recursion
    # the function will return false
    else:
        return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))