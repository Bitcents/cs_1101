""" 
+=====================================+
|  Part 1 of discussion assignment    |
+=====================================+
 """



""" Difference between objects and values:
An object can be thought of as an entity ( or thing ). A value is a property of an object. Two objects might have the same properties. 
For example, two cars of the same model might have the same color, engine power, wheel size and number of doors.
If all their properties are the same, they are equivalent to one another. However since they are two separate cars they are not identical. 
Consider also the possibility that you had a clone. You and your clone would be equivalent to one another. 
However, you are not your clone and your clone is not you. Hence the two of you are not identical.
In Python, we can demonstrate the same thing with lists. The Python interpreter creates a new list object every time a list is instantiated.
Consider the following example:
 """
list_a = ['rock', 'paper', 'scissor']
list_b = ['rock', 'paper', 'scissor']
# The two lists contain the same values, they are equivalent:

print(list_a == list_b)
# OUTPUT: True

# However they are not the same object as we can easily show using the 'is' operator:

print(a is b)
# OUTPUT: False



""" Objects. references, aliasing:

In most programming languages, an object has an actual presence in memory. 
We need a way to access that object, and a variable acts as the conduit. A variable knows where the object is in memory. 
In other words it has a reference to it. The same object can be referenced by different names. These names (or variables) share references to the same object.
In other words, they are identical to one another. In real life a person maybe known by names other than his given name: we call those names his aliases. 
Objects in Python might also have several names and this is called aliasing.

Again, we can use Python lists to illustrate this: """

# We first create a list. The variable has a reference to the list.
a = ['this', 'is', 'a', 'list']

# We set the variable b to a
b = a

# This means that b now has the same reference to the list
# In other words they are not equivalent
print(a is b)

# OUTPUT: True
# The list now has two names 'a' and 'b.' 'a' and 'b' are aliases of the list


""" 
+=====================================+
|  Part 2 of discussion assignment    |
+=====================================+
 """


todo_list = []

# Add to-do entry
def add_todo(list, item):
    # check if item already in list
    if item in list:
        print('item already in list')
    # add item if not in list
    else:
        list.append(item)

# Edit to-do entry
def edit_todo(list, item_num, edited_item):
    # if item exists, edit item
    if not list[item_num - 1] == None:
        list[item_num - 1] = edited_item
    else:
        print("entry does not exist")


# Delete to-do entry
def delete_todo(list, item_num):
    if not list[item_num-1] ==  None:
        list.remove(list[item_num-1])
    else:
        print("item does not exist")


# Print to do list in nice format
def print_todo(list):
    print('No.' + ' '*8 + 'Entry')
    for i in range(len(list)):
        print(f"{i+1}          {list[i]}")


if __name__=='__main__':
    
    # add some todo stuff
    add_todo(todo_list, 'buy fried chicken')
    add_todo(todo_list, 'eat fried chicken')
    add_todo(todo_list, 'sh** out undigested fried chicken')
    
    print_todo(todo_list)
    print('\n'+ '-' * 30 + '\n')
    # edit one entry 
    edit_todo(todo_list, 3, 'eat more fried chicken')

    print_todo(todo_list)
    print('\n'+ '-' * 30 + '\n')
    # delete first entry
    delete_todo(todo_list, 1)

    print_todo(todo_list)