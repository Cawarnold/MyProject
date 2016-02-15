#!/usr/bin/env Env3_Python276_Django171_djangoextensions



def computepay(h,r):
    if h > 40:
    	overtime = h - 40
    	return (40 * r) + (overtime * r * 1.5)
    else:
    	return (h * r)

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")

h = float(hrs)
r = float(rate)

p = computepay(h,r)
print "Pay",p