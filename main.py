#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python Katas String Practice

Code war challenges that are being used for python practice

author: TimeApollo
"""

def to_camel_case( word ):
    
    chars = list(word)
    for counter, ch in enumerate(chars):
        if ch == '_' or ch == '-':
            del chars[counter]
            chars[counter] = chars[counter].upper()
    return ''.join(chars)

def find_nth_occurrence( substring , string , occurrence ):
    index = string.find(substring)
    while index >= 0 and occurrence > 1:
        index = string.find(substring , index + 1)
        occurrence -= 1
    return index

def bumps( string ):
    bumpCount = 0
    for ch in list(string):
        if ch == 'n': bumpCount += 1
    return 'Woohoo!' if bumpCount <= 15 else 'Car Dead'

def reverse_words_in_string( string ):
    new_string = ''
    list_index = 0
    words = string.split()
    space_index = 0
    while space_index >= 0:
        next_index = string.find( ' ' , space_index + 1 )
        if next_index == -1:
            space_index = -1
            new_string += words[list_index][::-1]
        elif next_index > space_index + 1:
            space_index = next_index
            new_string += words[list_index][::-1] + ' '
            list_index += 1
        else:
            new_string += " "
            space_index = next_index
    return new_string

def kata1():
    print '\n1. _____Changing dashed strings into camel case_____'
    print '\ntesting: the-stealth-warrior'
    print 'result: ' + to_camel_case("the-stealth-warrior")
    print '\ntesting: The_Stealth_Warrior'
    print 'result: ' + to_camel_case("The_Stealth_Warrior")
    print '\ntesting: this_Has-both_DASHES-and_UnderScores'
    print 'result: ' + to_camel_case("this_Has-both_DASHES-and_UnderScores")

def kata2():
    print '\n2. _____Find Index of Nth Occurrence of Substring_____\n'

    testingSubstring = 'example'
    testingString = 'This is an example. Return the nth occurrence of example in this example string.'
    print 'testingSubstring: ' + testingSubstring
    print 'testingString: '+testingString+'\n'
    occurrence = 1
    print 'occurrence = ' + str(occurrence)
    print 'expect index: 11'
    print 'result: ' + str(find_nth_occurrence( testingSubstring , testingString , occurrence )) + '\n'
    occurrence = 2
    print 'occurrence = ' + str(occurrence)
    print 'expect index: 49'
    print 'result: ' + str(find_nth_occurrence( testingSubstring , testingString , occurrence )) + '\n'
    occurrence = 3
    print 'occurrence = ' + str(occurrence)
    print 'expect index: 65'
    print 'result: ' + str(find_nth_occurrence( testingSubstring , testingString , occurrence )) + '\n'
    occurrence = 4
    print 'occurrence = ' + str(occurrence)
    print 'expect index: -1'
    print 'result: ' + str(find_nth_occurrence( testingSubstring , testingString , occurrence )) + '\n'

    testingSubstring = 'TestTest'
    testingString = 'TestTestTestTest'
    print 'testingSubstring: ' + testingSubstring
    print 'testingString: '+testingString+'\n'
    occurrence = 1
    print 'occurrence = ' + str(occurrence)
    print 'expect index: 0'
    print 'result: ' + str(find_nth_occurrence( testingSubstring , testingString , occurrence )) + '\n'
    occurrence = 2
    print 'occurrence = ' + str(occurrence)
    print 'expect index: 4'
    print 'result: ' + str(find_nth_occurrence( testingSubstring , testingString , occurrence )) + '\n'
    occurrence = 3
    print 'occurrence = ' + str(occurrence)
    print 'expect index: 8'
    print 'result: ' + str(find_nth_occurrence( testingSubstring , testingString , occurrence )) + '\n'
    occurrence = 4
    print 'occurrence = ' + str(occurrence)
    print 'expect index: -1'
    print 'result: ' + str(find_nth_occurrence( testingSubstring , testingString , occurrence )) + '\n'

def kata3():
    print '\n3. _____Solve if car will make it home based on # of bumps (n\'s in string)_____\n'

    testString = 'n'
    print 'testString: ' + testString
    print 'expect result: Woohoo!'
    print 'result: ' + bumps(testString) + '\n'

    testString = '_nnnnnnn_n__n______nn__nn_nnn'
    print 'testString: ' + testString
    print 'expect result: Car Dead'
    print 'result: ' + bumps(testString) + '\n'

    testString = '______n___n_'
    print 'testString: ' + testString
    print 'expect result: Woohoo!'
    print 'result: ' + bumps(testString) + '\n'

def kata4():
    print '\n4. _____reverse words in string in place_____\n'

    testString = "This is an example!"
    print 'testString: ' + testString
    print 'expect result: sihT si na !elpmaxe'
    print 'result: ' + reverse_words_in_string(testString) + '\n'

    testString = "double  spaces"
    print 'testString: ' + testString
    print 'expect result: elbuod  secaps'
    print 'result: ' + reverse_words_in_string(testString) + '\n'

    testString = "works for  all   different     spaces"
    print 'testString: ' + testString
    print 'expect result: skrow rof  lla   tnereffid     secaps'
    print 'result: ' + reverse_words_in_string(testString) + '\n'


def main():
    kata1()
    kata2()
    kata3()
    kata4()

if __name__ == '__main__':
    main()