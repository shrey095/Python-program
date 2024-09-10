#  Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]} 
# No,we cannot include mutable types like lists or dictionaries inside a set in Python. 
# because sets require their elements to be hashable and immutable, which lists and dictionaries are not.