# Some Definitions:
# %timeit <code> :  Measure execution time of a code


# -------------------Rename multiple files in a directory or folder-----------------------------

import os

for dpath, dnames, fnames in os.walk('/home/ege/cascade_training/pos'):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('resized'):
            os.rename(f, f.replace('pgm', '.pgm'))


# -------------------- Files -------------------------------------------------------------------
# filename use: ../<Project name>/<File.name>  or complete path (/.../...)
'''
 Method Name 	Example 	       Explanation
 -----------  ------------             --------------------------------------------------------
 open 	      open(filename,'r')       Open a file called filename and use it for reading. This 
                                       will return a  reference to a file object.
 open 	      open(filename,'w')       Open a file called filename and use it for writing. This  
                                       will also return a reference to a file object.
 close 	      filevariable.close()     File use is complete.
 
 -----------  ----------------------   --------------------------------------------------------

 write		filevar.write(astring)  Add astring to the end of the file. filevar must 
                                       refer to a file that has been opened for writing.

 read(n)     	 filevar.read() 	 Reads and returns a string of n characters, or the 
                                       entire file as a single string if n is not provided.

 readline(n) 	 filevar.readline()     Returns the next line of the file with all text up to 
                                       and including the newline character. If n is provided 
                                       as a parameter than only n characters will be returned 
                                       if the line is longer than n.

 readlines(n) 	filevar.readlines()    Returns a list of strings, each representing a single 
                                       line of the file. If n is not provided then all lines 
                                       of the file are returned. If n is provided then n 
                                       characters are read but n is rounded up so that an 
                                       entire line is returned.
'''
# Example:
qbfile = open("qbdata.txt", "r")

# method 1
for aline in qbfile:
    values = aline.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

# 2
line = qbfile.readline()
print(line)

# 3
alllines = qbfile.read()
print(alllines[:256])

qbfile.close()



# Python Glob Module – Glob()
"""
glob(file_pattern, recursive = False)

It retrieves the list of files matching the specified pattern in the file_pattern parameter.

The file_pattern can be an absolute or relative path. It may also contain wild cards such as “*” or “?” symbols.
"""
import glob
for py in glob.glob("*.py"):
	print(py)




# Example - Bounding boxes put on the images
paths = glob.glob('data/images/*')

# mapping to access data faster
gtdic = {}
for gt in ground_truth:
gtdic[gt['filename']] = gt

# color mapping of classes
colormap = {1: [1, 0, 0], 2: [0, 1, 0], 4: [0, 0, 1]}

f, ax = plt.subplots(4, 5, figsize=(20, 10))
for i in range(20):
	x = i % 4
	y = i % 5

	filename = os.path.basename(paths[i])
	img = Image.open(paths[i])
	ax[x, y].imshow(img)

	bboxes = gtdic[filename]['boxes']
	classes = gtdic[filename]['classes']
	for cl, bb in zip(classes, bboxes):
	    y1, x1, y2, x2 = bb
	    rec = Rectangle((x1, y1), x2- x1, y2-y1, facecolor='none', 
		            edgecolor=colormap[cl])
	    ax[x, y].add_patch(rec)
	ax[x ,y].axis('off')
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------------------------------------


# --------------- Strings ----------------------------------------------------------------------

'''
 Method Name 	Parameters 	Explanation
 -----------    ----------   --------------------------------------
 upper 	        none 	     Returns a string in all uppercase
 lower 	        none 	     Returns a string in all lowercase
 capitalize 	none 	     Returns a string with first character capitalized, the rest lower
 strip 	        none 	     Returns a string with the leading and trailing whitespace removed
 lstrip 	none 	     Returns a string with the leading whitespace removed
 rstrip 	none 	     Returns a string with the trailing whitespace removed
 count 	        item 	     Returns the number of occurrences of item
 replace 	old, new     Replaces all occurrences of old substring with new
 center 	width 	     Returns a string centered in a field of width spaces
 ljust 	        width 	     Returns a string left justified in a field of width spaces
 rjust 	        width 	     Returns a string right justified in a field of width spaces
 find 	        item 	     Returns the leftmost index where the substring item is found,
                             or -1 if not found
 rfind 	        item 	     Returns the rightmost index where the substring item is found, 
                             or -1 if not found
 index 	        item 	     Like find except causes a runtime error if item is not found
 rindex 	item 	     Like rfind except causes a runtime error if item is not found
'''

# Example: upper case - lower case print

ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)

# Example: string format

person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)

# Example: discount calculate

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
print('${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice))


# Example: ASCII to decimal and reverse

print(ord("A")) # to dec, 65
print(chr(65)) # to ASCII, A

# char check
print('p' in 'apple') # true
print('i' in 'apple') # false
print('x' not in 'apple') # true

# Print ascii ...
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)


# ----------------------------------------------------------------------------------------------





# -------------------- Lists --------------------------------------------------------------------
'''
 Method Name 	Parameters     Results	     Explanation
 -----------    ----------   ------------    --------------------------
 append 	item  	      mutator        Adds a new item to the end of a list
 insert 	position,     item mutator   Inserts a new item at the position given
 pop 		none 	      hybrid 	     Removes and returns the last item
 pop 		position      hybrid 	     Removes and returns the item at position
 sort 		none 	      mutator 	     Modifies a list to be sorted
 reverse 	none 	      mutator 	     Modifies a list to be in reverse order
 index 		item 	      return idx     Returns the position of first occurrence of item
 count 		item 	      return ct      Returns the number of occurrences of item
 remove 	item 	      mutator 	     Removes the first occurrence of item
'''

# Lists comprehension
mylist = [1,2,3,4,5]
yourlist = [item ** 2 for item in mylist]
print(yourlist)

#----------------------------------------------

# List split
song = "The rain in Spain..."
wds = song.split()
print(wds)
wds = song.split('ai')
print(wds)

# List join
print("***".join(wds))
print("".join(wds))

# make a list from string
xs = list("Crunchy Frog")
print(xs)
#------------------Tuples----------------------------

# Tuple use
list1 = ("hello","world","!!")
                      #tuple:
julia = julia[:1] + ("my", 2017) + julia[2:]
print(julia)

# Tuple as return value
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

print(circleInfo(10))
# ----------------------------------------------------------------------------------------------




# --------------------- Classes and objects -----------------------------------------------------

# A class example

class Point:

    def __init__(self, initX, initY):  # self uses the instantiated object
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  # a function for print method
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)

print(mid)  # calls __str__,  output:  x=4.0, y=8.0
print(mid.getX())  #  output:  x=4.0
print(mid.getY())  #  output:  y=8.0

#--------------------------------------------------------------

# Equality test on points and lists

p = Point(4, 2)
s = Point(4, 2)
print("== on Points returns", p == s)  # by default, == does a shallow equality test here, returns false

a = [2, 3]
b = [2, 3]
print("== on lists returns",  a == b)  # by default, == does a deep equality test on lists, returns true

# ----------------------------------------------------------------------------------------------



# ------ A matrix example ------------------------------------------------------
import numpy as np
n = np.ones((5,6))
print(n)
print(n[4,:])

# ------ Random module usage example -------------------------------------------
import random

prob = random.random()
print(prob)

diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)




# -------------------- Dictionary ---------------------------------------------------------------
'''
 Method   Parameters 	   Explanation
 ------   ----------   --------------------------------------
 keys 	  none 	       Returns a view of the keys in the dictionary
 values   none 	       Returns a view of the values in the dictionary
 items 	  none 	       Returns a view of the key-value pairs in the dictionary
 get 	  key 	       Returns the value associated with key; None otherwise
 get 	  key,alt      Returns the value associated with key; alt otherwise
'''

# Example
mydict = {"cat":12, "dog":6, "elephant":23}
print(mydict["dog"])


# Example
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

# Example
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print("dog" in mydict) # true
print(23 in mydict)    # false
# ----------------------------------------------------------------------------------------------



# -------------------- Exception ---------------------------------------------------------------
def main()
  try:
    A()
  except ZeroDivisonError:
    # execute if a ZeroDivisonError message happened

def A():
  B()

def B():
  C()

def C():
  D()

def D()
  # processing code
  if something_special_happened:
    raise MyException
    
    

#----------------------------------------------
# Assertion
x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"
# ----------------------------------------------------------------------------------------------




# -------------------- Recursion examples ------------------------------------------------------

# list sum
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))


# turtle
import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
# -----------------------------------------------------------------------------------------------



# ------------ Newton's approximation method -------------------------------------------------

def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(10, 3))
print(newtonSqrt(10, 5))
print(newtonSqrt(10, 10))
# ---------------------------------------------------------------------------------------------


# ------------ Turtle, a screen drawing code piece -----------------------------
'''
 Method Name 	Parameters 	Explanation
 -----------    ----------   --------------------------------------
 Turtle 	None 	        Creates and returns a new turtle object
 forward 	distance        Moves the turtle forward
 backward 	distance 	Moves the turle backward
 right 	        angle 	 	Turns the turtle clockwise
 left 	        angle 	 	Turns the turtle counter clockwise
 up 	        None 	 	Picks up the turtles tail
 down 	        None 	 	Puts down the turtles tail
 color 	        color name 	Changes the color of the turtle’s tail
 fillcolor 	color name 	Changes the color of the turtle will use to fill a polygon
 heading 	None 	 	Returns the current heading
 position 	None 	 	Returns the current position
 goto 	        x,y 	 	Move the turtle to position x,y
 begin_fill 	None 	 	Remember the starting point for a filled polygon
 end_fill 	None 	 	Close the polygon and fill with the current fill color
 dot 	        None 	 	Leave a dot at the current position
 stamp 	        None 	 	Leaves an impression of a turtle shape at the current location
 shape 	        shape name 	Should be ‘arrow’, ‘classic’, ‘turtle’, ‘circle’ or ‘square’
'''

# Example
import turtle            # allows us to use the turtles library

wn = turtle.Screen()     # creates a graphics window
alex = turtle.Turtle()   # create a turtle named alex

alex.forward(150)        # tell alex to move forward by 150 units
alex.left(90)            # turn by 90 degrees
alex.forward(75)         # complete the second side of a rectangle
wn.exitonclick()




