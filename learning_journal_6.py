""" This is the first part of the week 6 learning journal """

# Today we will try out some things with lists.
# let us first create a long string though:

star_wars_planets = 'Coruscant Tatooine Naboo Dathomir Kashyyyk Mustafar Hoth Bespin Dagobah Kamino Yavin Geonosis Mandalore'

# Not let us turn the above string into a list of words

list_of_planets = star_wars_planets.split(' ') 

# Let us print the list just to be sure

print(list_of_planets) # output: ['Coruscant', 'Tatooine', 'Naboo', 'Dathomir', 'Kashyyyk', 'Mustafar', 'Hoth', 'Bespin', 'Dagobah', 'Kamino', 'Yavin', 'Geonosis', 'Mandalore']

""" Once we are satisfied with our output, let us delete three words from the list
Let us try using a different method to remove the words

These will modify the list

First is the pop method, which returns a single element from the list
If we provide an index, the element at the index will be removed
If no index is provided, the last element will be returned
The element will also removed from the list
Let us remove the last element from the list """

list_of_planets.pop() # output: Mandalore

# If we print the list now, we will see that Mandalore is removed from the list

""" The second way to remove an element is to use the 'remove' method
This time, we specify the element to be removed using the value of the element
For example, if we wanted to remove 'Dagobah' from the list we would do the following: """

list_of_planets.remove('Dagobah') 
# Output: None  | the remove method returns nothing

# Printing the list this time will show that Dagobah has been removed 


""" The third way to remove an item is to use the 'del' method
This method takes a slice index to remove from the list
To delete the 3rd, 4th and 5th elements for example, we would use "del list_to_be_deleted[2:6]". 
The 2nd index refers to the third element hence the 2 in '2:5'. 
Let us delete the 3rd through 5th elements in our planets list """
del list_of_planets[2:5]
# Finally let us print our list of planets once more to check that 5 planets have been removed from the original
print(list_of_planets) 
# Output: ['Coruscant', 'Tatooine', 'Mustafar', 'Hoth', 'Bespin', 'Kamino', 'Yavin', 'Geonosis']
# We seem to have been successful in our endeavors


# Let us now sort the list in alphabetical order
list_of_planets.sort()
print(list_of_planets) 
# Output: ['Bespin', 'Coruscant', 'Geonosis', 'Hoth', 'Kamino', 'Mustafar', 'Tatooine', 'Yavin']


""" Let us now add some new planets to our list
Again we will use three different ways to accomplish this


First we wil use the 'append' method of Python lists
The append method takes in one argument: the element to be added 
Append will add the given element to the end of the list
Let us add the planet Alderaan to the list """

list_of_planets.append('Alderaan')


""" If, however, we wanted to insert an element before a particular index, we use the insert method
The insert method takes two arguments: the index at which to insert to, the item to be inserted
So if we wanted to add the planet Corellia before Coruscant we would do the following:
Note that 'Coruscant' has an index of 1 """

list_of_planets.insert(1, 'Corellia')

# We esesntially move Coruscant one position to the right and insert 'Corellia' in its place

""" The third method to add to a list is to use the extend method
This takes a second list as the argument 
It then attaches the second list to the first
Let us add back the planets we deleted before """

deleted_planets = ['Mandalore', 'Dagobah', 'Naboo', 'Dathomir', 'Kashyyyk']
list_of_planets.extend(deleted_planets)

# We can then print the list of planets for our satisfaction
print(list_of_planets) 
# Output: ['Bespin', 'Corellia', 'Coruscant', 'Geonosis', 'Hoth', 'Kamino', 'Mustafar', 'Tatooine', 'Yavin', 'Alderaan', 'Mandalore', 'Dagobah', 'Naboo', 'Dathomir', 'Kashyyyk']

# Let us sort this list:
list_of_planets.sort()
# Just for fun, let us turn the list back into a space separated string using the 'join' method:
planets_string = ' '.join(list_of_planets)
# Finally let us print this string
print(planets_string) # Output: Alderaan Bespin Corellia Coruscant Dagobah Dathomir Geonosis Hoth Kamino Kashyyyk Mandalore Mustafar Naboo Tatooine Yavin




""" 
-------------------------------------------------------+
This is the second part of the week 6 learning journal |
-------------------------------------------------------+
"""

""" Nested Lists
In other words, lists within lists """
nested_list = [['pasta', 'spagehtti', 'pizza', 'meatballs'], ['sushi', 'onigiri', 'yakisoba', 'takoyaki'], ['chow mein', 'maabo doofu', 'beijing kaoya'], 'foods' ]
print(nested_list)

# Output: [['pasta', 'spagehtti', 'pizza', 'meatballs'], ['sushi', 'onigiri', 'yakisoba', 'takoyaki'], ['chow mein', 'maabo doofu', 'beijing kaoya'], 'foods']

""" Use of * operator"""
# Let us create a list of our bank balances 
bank_balances = ['USDT 1000', 'JPY 10000', 'EUR 23000', 'BTC 5.22111002']
new_balances = bank_balances*5
print(new_balances)

# Output: ['USDT 1000', 'JPY 10000', 'EUR 23000', 'BTC 5.22111002', 'USDT 1000', 'JPY 10000', 'EUR 23000', 'BTC 5.22111002', 'USDT 1000', 'JPY 10000', 'EUR 23000', 'BTC 5.22111002', 'USDT 1000', 'JPY 10000', 'EUR 23000', 'BTC 5.22111002', 'USDT 1000', 'JPY 10000', 'EUR 23000', 'BTC 5.22111002']


""" List Slices """
# We have apple pie for dessert
apple_pie_slices = [1,2,3,4,5,6,7,8,9,10]
# I take four slices from 6 through 9
slices_for_me = apple_pie_slices[5:9]
print(slices_for_me)

# Output: [6, 7, 8, 9]


""" The += operator """
groceries_list = ['eggs', 'chicken', 'lettuce', 'cabbage']
things_the_wife_added = ['milk', 'youghurt', 'more milk']
# update groceries list
groceries_list += things_the_wife_added
# print the updated list
print(groceries_list)

# Output: ['eggs', 'chicken', 'lettuce', 'cabbage', 'milk', 'youghurt', 'more milk']


""" List filter"""
# list to be used
ages = [11,15,21,45,31,18,19,55,27]
# We could use a funtion that takes a list as an argument
def allow_over_18(ages_list):
    # create an empty list for storing matches
    res = [] 
    # Iterate over the elements in the provided list
    for age in ages_list: 
        # only add to results if over 18
        if age >= 18:
            res.append(age)
    # Finally return the results
    return res

filtered_ages = allow_over_18(ages)
print(filtered_ages)

# Output: [21, 45, 31, 18, 19, 55, 27]

# We could also use the filter method
second_filtered_age = filter(lambda age: age >= 18, ages)
print(list(second_filtered_age))

# Output: [21, 45, 31, 18, 19, 55, 27]



""" Unexpected results """
# Let us define a new list
a = ['1', '2', '3', '112', '122']

# Then sort this list
a.sort()

# We would expect nothing to change 
# However since strings do not work the same way as numbers,
# We get unexpected results
print(a)

# Output: ['1', '112', '122', '2', '3']
