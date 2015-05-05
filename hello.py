#!/usr/bin/python
from test.test_typechecks import Integer
import sys
#lol123456
#;lkjncaksjnckanscok;nas;oiocnasokj;vcnasp981740r985ry1328984124234214242142142142---
print "hello world!"

'''
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];

dict['Name'] = 'Zoro'

print "new dict['Name'] is:", dict['Name']
dict.clear()
print dict
del dict

print dict

lookup = {"cat": 1, "dog": 2}
print(lookup["cat"])
'''
#-----------------------------------------------------------
# Create a dictionary.
data = {"a": 1, "b": 2, "c": 3}

# Loop over items and unpack each item.
for k, v in data.items():
    # Display key and value.
    print(k, v)

    
for m in data:
    print m
    print repr(m)
    if 'a' in m:
        print m, data[m]


data2 = {'a': 4, 'b': 9}
del data2['b']
data.update(data2)

for key, value in data.iteritems():
    print key
    print value
    print '{0} corresponds to {1}'.format(key, value)


data12 = {'city':'Paris', 'age':38, (102,1650,1601):'A matrix coordinate'}

print data12.keys()
print data12.values()

'''

w = "This is the left side of..."
e = "a string with a right side."

print w + e


print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


my_name = "ektor"
print "Let's talk about %s %d." % (my_name, 243), 4353
'''

'''
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
'''

'''
def print_two(*args):
    print args
ar = [432,432,432,4,432,342]
print_two(*ar)



def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

sentence = "All good things come to those who wait."
wordss = break_words(sentence)

print sort_words(wordss)
print_first_word(wordss)
print sort_words(wordss)

print "EOF"


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number




# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

'''
'''

class Thing:
    def __init__(self, lol):
        self.lol = lol
    
    def test12(self, hi):
        print hi

a = Thing(2252)
a.lol = 43
print a.lol
a.test12("hello")


'''


'''

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

try:
    print stuff[89]
except IndexError:
    print "\n out of range"

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print "There we go: ", stuff
print stuff[-2]
print stuff[-1] # whoa! fancy

print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:6]) # super stellar!

'''

'''

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']



# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]



# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
#print state
if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'if do not find it, show this: Does Not Exist')
print "The city for the state 'TX' is: %s" % city


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()



class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
'''
















