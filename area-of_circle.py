#!/usr/bin/python3
import math
radius = float(input("Enter the radius of the circle: "))

area =  math.pi * pow(radius, 2)
result = float(round(area, 2))
print(f"The area of the circle is: {result} cm^2")