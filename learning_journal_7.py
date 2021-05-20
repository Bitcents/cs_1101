from typing import List, Dict, Tuple
# Let us create a new dictionary
# For this assignment, we will store contact info
# The name of the person will be the key
# The value will include various information
contacts: Dict[str, List[str]] = dict()
# Let us add some entries
contacts['dad'] = ['239-273-2938', 'dademail@domain.com']
contacts['mom'] = ['717-832-5571', 'momemail@domain.com']
contacts['bro'] = ['314-309-4826', 'broemail@domain.com']
contacts['sis'] = ['925-419-1934', 'sisemail@domain.com']


# From Section 11.5 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def invert_dict(d):
     inverse = dict()
     for key in d:
          val = d[key]
          if val not in inverse:
               inverse[val] = [key]
          else:
               inverse[val].append(key)
     return inverse 


# Python lists are not hashable
# This means that they cannot be 
# used as keys in dictionaries
# We must therefore convert our list
# into a hashable data type
# A tuple will be perfect for this purpose
def invert_dict_2(d: Dict[str, List[str]]) -> Dict[Tuple, str]:
    inverse = dict()
    for key in d:
        # converts the list into a tuple
        t = tuple(d[key])
        if t not in inverse:
            inverse[t] = [key]
        else:
            inverse[t].append(key)
    return inverse

if __name__=='__main__':
    print(f'original dictionary: {contacts}')
    reversed: Dict = invert_dict_2(contacts)
    print(f'reversed dictionary: {reversed}')