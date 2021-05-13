# This is a simple script to create some empty python files
# This was made for the CS 1101 course at UOPeople
# We have to write programs for the following:
#   1. discussion forum
#   2. learning journal
#   3. programming assignment
# This script creates the respective files if they do not exist already
# In the current working directory
# I plan on extending the script to include more options

# MODULES:
import sys
import os
from enum import Enum


# GLOBAL VARIABLES:
class FileNames(Enum):
    DISCUSSION = './discussion_'
    JOURNAL = './learning_journal_'
    ASSIGNMENT = './programming_assignment_'

# I planned on using a list at some time
# But I went with an enum class at the end
# The list would have had the following structure:
# FILE_NAME_PREFIXES = ['./discussion_', './learning_jNeournal_', './programming_assignment_']

# Grab the command line arguments
args = sys.argv

# Check the arguments for compatability with the script
# Only integers are accepted
# However there is no reason why as string could not be used 
# This was a design choice 

try:
    assert len(args) == 2
    assert isinstance(int(args[1]), int)

except AssertionError as e:
    print("check arguments: usage: [lesson_number: int]")
    exit()

lesson_number = sys.argv[1]

# FUNCTIONS:

# This is function that creates the files
# It runs through every enum entry 
# And creates the respective files
# If the files already exists, then no additional files are created
# The exisiting files are also not overwritten
# Again this was a design choice
def create_files(lesson_number):
    for enum in FileNames:
        file_path = f'{enum.value}{lesson_number}.py'
        # check if the file exists
        if os.path.exists(file_path):
            print(f'the file: {file_path} already exists')
        else:
            # opening with the 'a' option is important
            # this allows us to create a file
            # if one does not already exist
            # the default 'r' option would raise an exception
            with open(f'{enum.value}{lesson_number}.py', 'a') as f:
                f.write("")
                f.close()
    print("done creating files")


# MAIN:
if __name__ == "__main__":
    create_files(lesson_number)