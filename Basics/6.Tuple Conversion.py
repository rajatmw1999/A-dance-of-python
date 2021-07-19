
# To some extent, lists are similar to arrays in C. 
# One difference between them is that all the items belonging to a list can be of different data type.

# -----------------------------------

#  The main differences between lists and tuples are: 
# Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, 
# while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
# Tuples can be thought of as read-only lists.


def tuple_to_list(tup):
    print("Converting tuple to list")
    mylist = list(tup)
    print(mylist)

def tuple_to_dict(tup):
    print("Converting tuple to dictionary")
    mylist = dict(tup)
    print(mylist)

tuple_to_list(  (1,2,3,4,5,6) )
tuple_to_dict(  (("Age",2),("Class",4),("Marks",6)) )