name = 'John'
print("Hello, %s!" % name)

name = 'John'
age = 23
print("%s is %d years old." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

#exercise
# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
