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

if hrs <= 40:
    gross_pay = hrs * rate
else:
    gross_pay = (hrs * rate) + ((hrs - 40) * (rate * 0.5))

print gross_pay