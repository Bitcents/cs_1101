def dec_to_binary(number):
    number = int(number)                   # sanitizing the input to take only integers
    result =  ''
    while (number != 0):
        result += str(number%2)
        number = int(number/2)
    

    return result[::-1]                    # the binary form is in reverse order 
                                           # so we just reverse it once again


print(dec_to_binary(8))
# Let us call dec_to_binary with values, variables and expressions
# call with value
print(dec_to_binary(50))

# call with variable                       
input = 50
print(dec_to_binary(input))

# call with expression
print(dec_to_binary(48+2))

# all of these should print the same value

def say_hello(name):
    string = "hello, " + name
    print(string)

string = "John"
print(string)