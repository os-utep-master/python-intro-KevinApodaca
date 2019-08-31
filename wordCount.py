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
from collections import Counter

""" TEST METHOD 1, EDIT LATER
#opening and reading file
with open ('declaration.txt') as t:
    testFile = t.read().upper()

words = re.findall(r'\w+', testFile)
capitals = [word.upper() for word in words]
count_words = Counter(capitals)
"""

"""
Simpler version test
"""
#creating dictionary
wd_frequency = {}

txt_file = open('declaration.txt', 'r') #hardcoded the text file to test, will use kwargs later for any file.
text_string = txt_file.read().lower()  #case insensitive 
match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string) #regular expression, finds all words in the bound 1 character to 15 characters, of alphabetical type
 
for word in match_pattern:
    count = wd_frequency.get(word,0)
    wd_frequency[word] = count + 1
     
frequency_list = wd_frequency.keys()
 
for words in frequency_list:
    print words, wd_frequency[words]