import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")

outfile = open("customer_country.csv", "w")


for record in customer_file:
    # "\n is a line break "
    # the line break makes sure it goes to the next line
    outfile.write(record[1] + "," + record[2] + "," + record[4] + "\n")


outfile.close()
