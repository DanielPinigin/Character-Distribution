"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

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
print(thelist)

numb = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
z = zip(thelist,numb)
print(list(zip(thelist,numb)))

v = [x for (y,x) in sorted(zip(thelist,numb), key=lambda pair: pair[0])] 
print(v)

#'a string has several characters'.count('c')
