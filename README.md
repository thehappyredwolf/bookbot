# BookBot

BookBot is a Python command-line tool that analyzes text files (like novels) and prints a report of word and character usage.

## What It Does
- Counts total words
- Counts occurrences of each alphabetical character
- Sorts character statistics from most to least frequent
- Accepts a file path as a command-line argument

## Example
```bash
python3 main.py books/frankenstein.txt
```

Output:
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============

```

## How to Run
```bash
git clone https://github.com/thehappyredwolf/bookbot
cd bookbot
```

Make sure Python 3 is installed:

```bash
python3 --version
```

Edit or add your own `.txt` books to the `books/` directory.

## Notes

Tested with public-domain books from Project Gutenberg.