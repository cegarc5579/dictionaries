import csv

# this opens the file and creates a file object
# creates a 'customer" file object
# import csv to read it
# creates a csv object when you read it

customers = open("customers.csv", "r")

# delimiter tells you how the columns are seperated
# so the comma is set as the delimiter that seperates columns
customer_file = csv.reader(customers, delimiter=",")

# to skip a line if the file contains a header record
next(customer_file)

# "for record in customer_file" means it will go through
# each line one at a time
for record in customer_file:
    print(record)
    print("first name:", record[1])
    print("last name:", record[2])
    print("City:", record[3])
    print("Country:", record[4])
    print("Phone:", record[5])

    # input () is a break unless you hit something on your keyboard
    input()
