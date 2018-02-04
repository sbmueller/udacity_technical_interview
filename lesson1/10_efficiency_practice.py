#!/usr/bin/env python2

"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example1(manatees):
    """
    O(n) since every item in manatees gets accessed once
    """    
    for manatee in manatees:
        print manatee['name']

def example2(manatees):
    """
    O(1) since the code is independent of the length of manatees
    """
    print manatees[0]['name']
    print manatees[0]['age']

def example3(manatees):
    """
    O(nm) since all manatees and all properties of each manatee get accessed
    """
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

def example4(manatees):
    """
    O(n^2) since in worst case, for each manatee1 all other manatees have to be accessed
    """
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee
