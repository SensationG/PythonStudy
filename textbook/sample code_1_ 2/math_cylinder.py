# -*- coding: utf-8 -*-

import math

PI = math.pi

# Convert input string to integer
r, h = eval(input("Enter radius and height: "))

c_pe = 2*PI*r
c_area = PI*(pow(r, 2))  # PI * (r**2)
volume =  c_area * h 
area = 2 * c_area + c_pe * h

print("Radius =  ", r)

# Print using %
print("\nPrint using %")

print("%s = %.2f" % ("Radius", r))

print("Volume = %.2f" % volume)

print("%6s = %.2f" % ("Area", area))

# print using format
print("\nPrint using format")

# {index:format}
print("{0:s} = {1:.2f}".format("Radius", r))

print("{0:s} = {1:.2f}".format("Volume", volume))

print("{0:>6} = {1:.2f} ".format("Area", area))
























