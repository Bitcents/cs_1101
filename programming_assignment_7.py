from typing import List, Dict

alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 


"""
+=================================+
| This section is concerns Part 1 |
| of the programming assignment   |
+=================================+
"""


# This function checks for duplicate characters
# In the provided string
# We will use Python typing
# To make things more clear
def __has_duplicates(input: str) -> bool:
    d = dict()
    for c in input:
        if c not in d:
            d[c] = 1
        else:
            return True
    return False


# The histogram and duplicates functions above
# Are very similar to one another
# Let us write another version of 
# has_duplicates, which uses 
# the histogram function 
def has_duplicates(input: str) -> bool:
    histogram_data: Dict[str, int]= histogram(input)
    # loop through each histogram entry
    # an entry value bigger than one
    # suggests there are multiple
    # instance of the same character
    for entry in histogram_data:
        if histogram_data[entry] > 1:
            return True
    # If no duplicates are detected
    # False is returned
    return False


"""
+=================================+
| This section is concerns Part 2 |
| of the programming assignment   |
+=================================+
"""
# This function prints letters
# that are in the alphabet, but
# missing in the string provided.
# We will again use 'histogram'
# to serve our purposes
def missing_letters(input: str) -> str:
    # We need to compare against the alphabets
    # Using the 'alphabet' global varaible
    # seems like the best choice.
    # We need to use the global modifier
    # in order to access the variable
    # from within a function
    global alphabet
    histogram_data = histogram(input)
    # string to store the array
    result = ''
    for letter in alphabet:
        # We will use an exception
        # to detect an entry that 
        # does not exist
        try:
            histogram_data[letter]
        # This is executed if the letter 
        # is missing in the string
        except KeyError:
            result += letter
        # This is not the usual way
        # but I thought it would be
        # fun to try out something new
    return result



"""
+=================================+
| This section performs the loops |
| of the programming assignment   |
+=================================+
"""
if __name__=='__main__':
    
    # loop checking for duplicates
    # in strings in 'test_dups'
    for string in test_dups:
        
        # if there are duplicates, then
        if has_duplicates(string):
            print(f'{string} has duplicates')
        
        # if there are no duplicates, then
        else:
            print(f'P{string} has no duplicates')

    
    # loop checking for missing letters
    # in strings in 'test_miss'
    for string in test_miss:
        missing = missing_letters(string)
        # if there are no missing letters
        if missing == '':
            print(f'{string} uses all the letters')
        # otherwise there must be missing letters
        # so we print the corresponding message
        else:
            print(f'{string} is missing letters {missing}')
    
    print([3,2,1].sort())