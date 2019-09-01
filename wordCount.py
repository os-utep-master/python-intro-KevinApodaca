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

#taking file arguments from terminal. I used this https://stackabuse.com/command-line-arguments-in-python/ resource to find out how to take arguments from the command line.
wordFile, outputFile = sys.argv[1], sys.argv[2]
word_freq = {}

#taking text file and assigning it to string.
str1 = open(wordFile, 'r').read().lower()

# I used these resources to learn about the formatting for regular expressions 
# https://docs.python.org/3/library/re.html
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html

formated_list = re.findall(r'\b[a-z]{1,15}\b', str1)

for word in formated_list:
    counter = word_freq.get(word,0)
    word_freq[word] = counter + 1 

list_of_words = sorted(word_freq.keys())

with open(outputFile, 'w') as out_file:
    for words in list_of_words:
        out_file.writelines(("%s %d\n" % (words, word_freq[words])))

