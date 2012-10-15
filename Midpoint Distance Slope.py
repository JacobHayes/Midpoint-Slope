#Jacob Hayes
#Distance and Midpoint Formula Calculator

import math

print "\nIf the program crashes, an invalid answer was entered.*"

try:
    x1 = float(raw_input("\nPlease enter the value of 'x' sub 1: "))
except:
    x1 = raw_input("Enter a number ('1' not 'one'): ")

    while not x1:
        x1 = raw_input("Please enter a number for 'x' sub 1: ")
    x1 = float(x1)
try:
    y1 = float(raw_input("\nPlease enter the value of 'y' sub 1: "))
except:
    y1 = raw_input("Enter a number ('1' not 'one'): ")

    while not y1:
        y1 = raw_input("Please enter a number for 'y' sub 1: ")
    y1 = float(y1)

    
try:
    x2 = float(raw_input("\n\nPlease enter the value of 'x' sub 2: "))
except:
    x2 = raw_input("Enter a number ('1' not 'one'): ")

    while not x2:
        x2 = raw_input("Please enter a number for 'x' sub 2: ")
    x2 = float(x2)
try:
    y2 = float(raw_input("\nPlease enter the value of 'y' sub 2: "))
except:
    y2 = raw_input("Enter a number ('1' not 'one'): ")

    while not y2:
        y2 = raw_input("Please enter a number for 'y' sub 2: ")
    y2 = float(y2)

print "\n"

point1 = (x1 + x2) / 2
point2 = (y1 + y2) / 2

print "(", x1, "+", x2, ") / 2   and   (", y1, "+", y2, ") / 2"

print x1 + x2, "/ 2   and   ", y1 + y2, "/ 2"

print "(", point1, ",", point2, ")"


print "\nThe Midpoint is (", point1, ",", point2, ").\n"

raw_input("\n\nWhen you are ready, press Enter")

square1 = (x1 - x2) * (x1 - x2)
square2 = (y1 - y2) * (y1 - y2)
square_total = square1 + square2

print "  _______________________________________________"
print "\/(", x1, "-", x2, ")^2 + (", y1, "-", y2, ")^2\n"

print "  ___________________________________________"
print "\/(", (x1 - x2), ")^2 + (", (y1 - y2), ")^2\n"

print "  ___________________________________"
print "\/(", square1, ") + (", square2, ")\n"

print "  ___________________________"
print "\/(", square1 + square2, ")\n"

print "\nThe Distance is", math.sqrt(square_total), "or the square root of", square_total

raw_input("\n\nWhen you are ready, press Enter")

rise = y2 - y1
run = x2 - x1

print "   ", y2, "-", y1
print "m = ----------"
print "   ", x2, "-", x1, "\n"

print "   ", rise
print "m = ------"
print "   ", run

if run >= 1 or run <= -1:
    print "\nThe slope is", rise / run, "or", rise, "/", run
    
if run == 0:
    print "\nThe slope is undefined or", rise, "/", run

raw_input("\n\nPress Enter to Exit")
