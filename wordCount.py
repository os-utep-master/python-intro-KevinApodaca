"""
CS 4375: Theory of Operating Systems
Lab 01: Into to Python
Author: Kevin Apodaca
Description: The purpose is to have a fairly simple python assignment that introduces the basic features and tools of python.
"""
#imports 
import re
import os
import string

#taking text file and assigning it to string.
str1 = open('declaration.txt', 'r').read()
 
# create a list of words separated at whitespaces
wordList1 = str1.split(None)
 
# strip any punctuation marks and build modified word list

wordList2 = []

for word1 in wordList1:
    # testing for any punctuation marks, and if found, will be removed.
    lastchar = word1[-1:]
    if lastchar in [",", ".", "!", "?", ";", "-", ".--", ":", ".- -"]:
        word2 = word1.rstrip(lastchar)
    else:
        word2 = word1
    wordList2.append(word2.lower()) #case-insensitive
 

word_freq = {}  #dictionary to store all words. Key is the word, value is the count of the word.
for word2 in wordList2:
    word_freq[word2] = word_freq.get(word2, 0) + 1
 
# create a list of keys and sort the list
# all words are lower case already
keyList = word_freq.keys()
keyList.sort()
 
print ("Frequency of each word in the word list (sorted):")
for key2 in keyList:
  print ("%-10s %d" % (key2, word_freq[key2]))

