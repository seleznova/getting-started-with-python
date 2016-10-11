
# Exercise


# This first line is provided for you

hrs = raw_input("Enter Hours:")

# This is a rate

rate = raw_input("Enter Rate:")

try:
    hrs = float(hrs)
    rate = float(rate)
    gross_pay = hrs * rate
    print gross_pay

except:
    print "Error, please enter numeric input"

