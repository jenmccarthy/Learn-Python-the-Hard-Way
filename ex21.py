def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b

def subtract(a, b):
  print "SUBTRACTING %d - %d" % (a, b)
  return a - b

def multiply(a, b):
  print "MULTIPLYING %d * %d" % (a, b)
  return a * b

def divide(a, b):
  print "DIVIDING %d / %d" % (a, b)
  return a / b

print "Let's do some math with just functions!"

age = add(30, 3)
height = subtract(78, 4)
weight = multiply(35, 4)
iq = divide(250, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "that becomes: ", what, "Can you do it by hand?"


