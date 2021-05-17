# Today we will try out some things with lists.
# let us first create a long string though:

star_wars_planets = 'Coruscant Tatooine Naboo Dathomir Kashyyyk Mustafar Hoth Bespin Dagobah Kamino Yavin Geonosis Mandalore'

# Not let us turn the above string into a list of words

list_of_planets = star_wars_planets.split(' ') 

# Let us print the list just to be sure

print(list_of_planets) # output: ['Coruscant', 'Tatooine', 'Naboo', 'Dathomir', 'Kashyyyk', 'Mustafar', 'Hoth', 'Bespin', 'Dagobah', 'Kamino', 'Yavin', 'Geonosis', 'Mandalore']

# Once we are satisfied with our output, let us delete three words from the list
# Let us try using a different method to remove the words

# These will modify the list

# First is the pop method, which returns a single element from the list
# If we provide an index, the element at the index will be removed
# If no index is provided, the last element will be returned
# The element will also removed from the list
# Let us remove the last element from the list
list_of_planets.pop() # output: Mandalore
# If we print the list now, we will see that Mandalore is removed from the list

# The second way to remove an element is to use the 'remove' method
# This time, we specify the element to be removed using the value of the element
# For example, if we wanted to remove 'Dagobah' from the list we would do the following:
list_of_planets.remove('Dagobah') # Output: None  | the remove method returns nothing
# Printing the list this time will show that Dagobah has been removed 

# The third way to remove an item is to use the 'del' method
# This method takes a slice index to remove from the list
# To delete the 3rd, 4th and 5th elements for example, we would use "del list_to_be_deleted[2:6]". 
# The 2nd index refers to the third element hence the 2 in '2:5'. 
# Let us delete the 3rd through 5th elements in our planets list
del list_of_planets[2:5]
# Finally let us print our list of planets once more to check that 5 planets have been removed from the original
print(list_of_planets) # Output: ['Coruscant', 'Tatooine', 'Mustafar', 'Hoth', 'Bespin', 'Kamino', 'Yavin', 'Geonosis']
# We seem to have been successful in our endeavors


# Let us now sort the list in alphabetical order
list_of_planets.sort()
print(list_of_planets) # Output: ['Bespin', 'Coruscant', 'Geonosis', 'Hoth', 'Kamino', 'Mustafar', 'Tatooine', 'Yavin']


# Let us now add some new planets to our list
# Again we will use three different ways to accomplish this

# First we wil use the 'append' method of Python lists
# The append method takes in one argument: the element to be added 
# Append will add the given element to the end of the list
# Let us add the planet Alderaan to the list
list_of_planets.append('Alderaan')


# If, however, we wanted to insert an element before a particular index, we use the insert method
# The insert method takes two arguments: the index at which to insert to, the item to be inserted
# So if we wanted to add the planet Corellia before Coruscant we would do the following:
list_of_planets.insert(1, 'Corellia')
# Note that 'Coruscant' has an index of 1
# We esesntially move Coruscant one position to the right and insert 'Corellia' in its place

# The third method to add to a list is to use the extend method
# This takes a second list as the argument 
# It then attaches the second list to the first
# Let us add back the planets we deleted before
deleted_planets = ['Mandalore', 'Dagobah', 'Naboo', 'Dathomir', 'Kashyyyk']
list_of_planets.extend(deleted_planets)
# We can then print the list of planets for our satisfaction
print(list_of_planets) # Output: ['Bespin', 'Corellia', 'Coruscant', 'Geonosis', 'Hoth', 'Kamino', 'Mustafar', 'Tatooine', 'Yavin', 'Alderaan', 'Mandalore', 'Dagobah', 'Naboo', 'Dathomir', 'Kashyyyk']

# Let us sort this list:
list_of_planets.sort()
# Just for fun, let us turn the list back into a space separated string using the 'join' method:
planets_string = ' '.join(list_of_planets)
# Finally let us print this string
print(planets_string) # Output: Alderaan Bespin Corellia Coruscant Dagobah Dathomir Geonosis Hoth Kamino Kashyyyk Mandalore Mustafar Naboo Tatooine Yavin