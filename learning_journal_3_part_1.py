
def countdown(n):                    # this function is from the textbook
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

def countup(n):                      # countup takes a negative integer and counts up from there 
    if n >= 0:                       # the counting up is done recursively
        print('Blastoff!')           # the function will terminate once it reaches a number larger than or equal to zero
    else:
        print(n)
        countup(n+1)

def launch_sequence():               # this function will prompt the user to enter a integer
                                     # a print statement to prompt the user is always a nice touch
    print("Please enter time before launch.")
    try:
        p = int(input())             # we first try to sanitize the user input
                                     # anything other than a number will cause an exception
    except ValueError:               
        print("Try again with a valid number.")
        
    print("Initiating launch sequence:")
    if(p >= 0):                      # countdown is called for p >= 0
        countdown(p)
    else:                            # otherwise countup is called; essentially for all p < 0
        countup(p)


launch_sequence()                    # main program, where we actually call the function