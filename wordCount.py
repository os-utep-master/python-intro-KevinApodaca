#! /usr/bin/env python3
"""
CS 4375: Theory of Operating Systems
Lab 01: Into to Python
Author: Kevin Apodaca
Description: The purpose is to have a fairly simple python assignment that introduces the basic features and tools of python. This program will take a text file and determine the frequency of the
words used, displaying the words (in alphabetical order) as well as the amount of times they appear.
"""

#imports 
import re, os, sys
import string

#taking file arguments from terminal
wordFile = sys.argv[1]
outputFile = sys.argv[2]

#taking text file and assigning it to string.
str1 = open(wordFile, 'r').read()
wordList1 = str1.split(None)
wordList2 = []

for word1 in wordList1:
    # testing for any punctuation marks, and if found, will be removed.
    lastchar = word1[-1:]
    if lastchar in [",", ".", "!", "?", ";", "-", ".--", ":", ".- -", "'"]:
        word2 = word1.rstrip(lastchar)
    else:
        word2 = word1
    wordList2.append(word2.lower()) #case-insensitive

word_freq = {}  #dictionary to store all words. Key is the word, value is the count of the word.
for word2 in wordList2:
    word_freq[word2] = word_freq.get(word2, 0) + 1
#make list of words from frequency list and sort them alphabetically using sort function.
word_list = word_freq.keys()
word_list.sort()

with open(outputFile, 'w') as out_file:
    for words in word_list:
        out_file.writelines(("%s %d\n" % (words, word_freq[words])))

