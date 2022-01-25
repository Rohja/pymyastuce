#!/usr/bin/env python3

# Import all required classes
from pymyastuce import *

# Find your station
s = Station.getStationByName("europe")
print("My station:", s)

# Find your line
l = Line.getLineByName("Métro")
print("My line:", l)

# Chose a direction (either 1 or 2)
print("Direction 1 is:", l.getTerminus(1))
print("Direction 2 is:", l.getTerminus(2))

# Do a request to know in how many minute is the next ride to do to direction 1
r = Request().getNext(l, s, 1)
print(r)