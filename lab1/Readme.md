# Theory of Operating Systems Lab 1 Intro to Python :skull:

## Description
Create a python3 program which:
- takes the name of an input file and output file
- keeps track of the total the number of times each word occurs in the text file
- excluding white space and punctuation
- is case-insensitive
- print out to the output file (overwriting if it exists) the list of words sorted in descending order with their respective totals separated by a space, one word per line

## Requirements & Assumptions 
- python 3 must be installed for proper functionality (this was tested on version 3.7.4)
- I am assuming that the smallest word is of length 1 and the largest word has length 15, otherwise I assume it is a misspelling or nonsense. If you want to change these parameters then go line 24 of `wordCount.py` and change the values of either 1 or 15, according to your needs.

## How to run
Ensure you are in the proper directory that contains the *wordCount.py* file, then simply type the following in your terminal.

`$ python3 wordCount.py <input_file.txt> <output_file.txt>`\
Where <input_file> is the text file that you want to count words for, and <output_file> is the text file that you want to be created which contains the output.

## Contributions, Resources, & Thanks :loop:
I worked with the following people on this assignment. 
- [Nicholas Venecia](https://github.com/nicholasvenecia) helped me to ensure that punctuation marks were being properly eliminated.
- [Jaime Salas](https://github.com/Josalas16) showed me how to properly format my output with the correct spacing between a word and its count.

The following are web resources that are useful.
- I used [this](https://stackabuse.com/command-line-arguments-in-python/) to find out how to take arguments from the command line.
- I used [this](https://docs.python.org/3/library/re.html) and [this one](https://www.guru99.com/python-regular-expressions-complete-tutorial.html) to understand how to use regular expressions.
- I tested my output file with the key txt using [this](https://copyleaks.com/compare) website to test the similarity between the files.

