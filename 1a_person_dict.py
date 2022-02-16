# start with empty dictionary and are adding key/value pairs
# joe and fonebone are string
# age is an integer, keys do not have to all be same elements
# dictionary can have a list in it, there is no limit, children list
# pets is a dictionary because it has key/value pairs
# with a dictionary you need a KEY, with a list you need INDEX VALUE
person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# print(person)

# print(type(person["children"]))

# this is how you get it from the list. put the index location
print(person["children"][2])

# the first key brings us to key, but we use cat again because its a key
# and this will print out the name of the cat
print(person["pets"]["cat"])

# i would be the iterator for every thing in the list
for i in person["children"]:
    print(i)

for i, j in person["pets"].items():
    print(i)
