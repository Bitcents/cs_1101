# Only the sqrt function from the math module
from math import sqrt

# Defining the custom square root function
def my_sqrt(a):
    # Initial value of x set to 1
    x = 1
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return x  

# This is the function that prints one result entry.
# The format is the one defined by the assignment.
# It is as follows:
# a = {input number} | my_sqrt(input number) | math.sqrt(a) | diff 
def print_result_entry(number, custom_root, math_root, difference):
    # This is quite a long assignment
    entry_str = f'a = {number} | my_sqrt(a) = {custom_root} | math.sqrt(a) = {math_root} | diff = {difference}'
    # Printing here is simpler than returning
    print(entry_str) 


# Looping function for printing result entries
def test_sqrt(upper_bound):
    # Enter loop. Entries are created for 1 <= a <= upper_bound
    # Python's range goes from "lower_bound" to "upper_bound - 1"
    # Hence the "+ 1" in the range
    for a in range(1, upper_bound + 1):
        # Square root returned from the custom function
        sqrt_1 = my_sqrt(a)
        # Square root from the math module function
        sqrt_2 = sqrt(a)
        # Calculate the absoulute difference of the square roots
        diff = abs(sqrt_1 - sqrt_2)
        # Print the result in the format
        print_result_entry(a, sqrt_1, sqrt_2, diff)

# Main function
if __name__=="__main__":
    print("enter upper bound: ")
    # Get user input...
    user_input = int(input())
    test_sqrt(user_input)
