# The code below almost works

name = raw_input("Enter your name")
print "Hello %s" % name

# Exercise 2.3

# This first line is provided for you

hrs = raw_input("Enter Hours:")

# This is a rate

rate = raw_input("Enter Rate:")

hrs = float(hrs)
rate = float(rate)

gross_pay = hrs * rate

print gross_pay