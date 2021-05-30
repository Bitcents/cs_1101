import re
import os
import sys
from typing import List, Dict

""" 
The program assumes the following file format
- values are either numbers or strings only
- value/key pairs are defined on a new line
- value and key are separated by a single space
- input files need to have .dict extension
"""

# This function reads a file and
# returns the string representation 
# of the data contained in the file
def read_file(file_path: str) -> str:
    # make sure to open file in read-only mode
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("The provided file does not exist")
    except OSError:
        print("There was an error in reading the file")


# This function converts string
# read from a file
# into a list containing 
# key-value pairs
def get_key_value_pairs(file_data:str) -> List[str]:
    str_data = file_data.split('\n')
    key_value_array = []
    for line in str_data:
        key_value_array.append(line.split(" "))
    return key_value_array

# This function converts the
# list of key-value pairs
# to list of formatted strings 
# with the tokesn in reverse order
def reverse_order_of_pairs(pairs:List[str]) -> List[str]:
    inverted = []
    for pair in pairs:
        inverted.append(f"{pair[1]} {pair[0]}\n")
    return inverted

# This function will write the 
# inverted dict to a new file
def write_to_file(inverted_list, filepath) -> None:
    if os.path.exists(filepath):
        raise FileExistsError(f"There is already an inverted dict file. Aborting...")
    else:
        try:
            file = open(filepath, 'w')
            for reversed_pair in inverted_list:
                file.write(reversed_pair)
        except OSError:
            print("Could not write to file")

if __name__=="__main__":
    
    if len(sys.argv) != 2:
        raise ValueError("Please provide the filepath of the dictionary file")

    input_file_path = sys.argv[1]
    
    if input_file_path[-4:] != "dict":
        raise ValueError("Files must have .dict extension")
    
    output_file_path = input_file_path[:-4]+"_inverted.dict"

    # do the processing
    input_data_str = read_file(input_file_path)
    key_val_pairs = get_key_value_pairs(input_data_str)
    inverted = reverse_order_of_pairs(key_val_pairs)
    # write the inverted dict to file
    write_to_file(inverted, output_file_path)
    
# no other prints provided, 
# no output in Unix typically means
# everything is OK 
#########################################


    