"""
distribution.py
Author: Daniel
Credit:  Dennison, Kyle, Brendan

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

sent = str(input("Please enter a string of text (the bigger the better): "))

print('The distribution of characters in "{0}" is: '.format(sent))

sent1 = sent.lower()

sent1 = list(sent1)

#figure out function to identify how many times a letter in the alphabet occurs in the input sent1

thelist = [sent1.count(c) for c in string.ascii_lowercase]
#print(thelist)

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

z = list(zip(thelist,alph))
#print(z)
zs = sorted(z, reverse = True)
#print(zs)

thelist, alph=zip(*zs)
#print(alph)

def compare(a, b):
    """
    compare - generic comparison function for testing two elements.
    """
    acount = a[0]
    aletter = a[1]
    bcount = b[0]
    bletter = b[1]
    if acount > bcount:
        return True
    elif acount < bcount:
        return False
    else:
        if aletter < bletter:
            return True
        elif aletter > bletter:
            return False

def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it

    
tosort = [4, 10, 3, -1000, 30]
bsort(z, compare)
print(z)
for x, y in z:
    if x != 0:
      #  print(x*y)
