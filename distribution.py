"""
distribution.py
Author:Daniel
Credit:  Whily Kyotee (kyle)

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
#alph1 = alph.reverse()

z = list(zip(alph,thelist))
#print(z)
zs = sorted(z, reverse = True)
#print(zs)

alph, thelist=zip(*zs)
#print(alph)

for x in alph:
    print(x*sent1.count(x))
