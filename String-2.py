# double_char

# Given a string, return a string where for every char in the original, there are two chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  output = ""
  for x in str:
    output += x*2
  return output

# count_hi

# Return the number of times that the string "hi" appears anywhere in the given string.

# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
  return str.count('hi')

# cat_dog

# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
  return (str.count('cat') == str.count('dog'))
