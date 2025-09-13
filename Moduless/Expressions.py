'''Regular expressions - a module for working with regular expressions in Python.
Defination - A regular expression (regex or regexp) is a sequence of characters that defines a search pattern, primarily used for string matching and manipulation.
some regular expression operations include searching, replacing, and splitting strings based on patterns.
# Example of using regular expressions in Python
# Importing the re module
# re module provides support for regular expressions in Python.
# It allows you to search, match, and manipulate strings using patterns.'''
                # [] - It represents a set of characters.
                # \t - It is used for tab character.
                # \n - It is used for newline character.
                # \d - It matches any digit character (equivalent to [0-9]).
                # .  - It defines a specific place 
                # ^  - It matches the start of a string.
                # $  - It matches the end of a string.
                # *  - It matches zero or more occurrences of the preceding element.
                # +  - It matches one or more occurrences of the preceding element.
                # ?  - It matches zero or one occurrence of the preceding element.
                # {} - It specifies a specific number of occurrences of the preceding element.  
                # /  - It is used to escape special characters in regular expressions.
import re
p = re.compile(r'\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) # ['1', '1', '4', '1', '8', '8', '6']
import re
p = re.compile(r'\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) # ['11', '4', '1886'] 
'''Special Sequences in Regular Expressions:'''
# \A - Matches the start of a string.
# \b - Matches the string at the beginning or end of a string.
# \B - Matches the string at the beginning but not at the end of a string.
# \d - Matches any digit character (equivalent to [0-9]).
# \D - Matches any non-digit character (equivalent to [^0-9]).
# \s - Matches any whitespace character (space, tab, newline).
# \S - Matches any non-whitespace character.
# \w - matches if the string contains any word characters 
# \Z - Matches the end of a string.
'''Sets'''
# [am] - Matches any character 'a' or 'm'.
# [a-m] - Matches any character from 'a' to 'm'.
# [^am] - Matches any character except 'a' or 'm'.
# [0123] - Matches any character '0', '1', '2', or '3'.
# [0-9] - Matches any digit character (equivalent to \d).
# [0-5][0-9] - Matches any digit number from 00 to 59.
import re
p = re.compile(r'[a-e]')
print(p.findall("Aye said Mr. Gibenson stark")) # ['e', 'a', 'd', 'b', 'e', 'a'] 
import re
p = re.compile(r'[A-Za-z]')
print(p.findall("Aye said Mr. Gibe234nson stark")) # ['A', 'y', 'e', 's', 'a', 'i', 'd', 'M', 'r', 'G', 'i', 'b', 'e', 'n', 's', 'o', 'n', 's', 't', 'a', 'r', 'k']
import re
p = re.compile(r'[A-Za-z0-9]')
print(p.findall("Aye said Mr. Gibe234nson stark")) # ['A', 'y', 'e', 's', 'a', 'i', 'd', 'M', 'r', 'G', 'i', 'b', 'e', '2', '3', '4', 'n', 's', 'o', 'n', 's', 't', 'a', 'r', 'k']
import re
p = re.compile(r'[A-Za-z]+')
print(p.findall("Aye said Mr. Gibenson stark")) # ['Aye', 'said', 'Mr', 'Gibenson', 'stark']
import re
p = re.compile(r'[A-Za-z0-9]+')
print(p.findall("Aye said Mr. Gibenson stark,2025")) # ['Aye', 'said', 'Mr', 'Gibenson', 'stark', '2025'] 
''''''
import re
def findMonthAndDate(string):
   regex = r"([a-zA-Z]+) (\d+)"
   match = re.match(regex, string)
     
   if match == None:
      print("Not a valid date")
      return
   print("Given Data:%s"%(match.group()))
   print("Month: %s" % (match.group(1)))
   print("Day: %s" % (match.group(2)))
#Driver code--main code
findMonthAndDate("Jun 24")
print()
findMonthAndDate("I was born on June 24")
'''the output is :
                Given Data:Jun 24
                Month: Jun
                Day: 24

                Not a valid date'''
''''''
import re
def findMonthAndDate(string):
   regex = r"([a-zA-Z]+) (\d+)"
   match = re.search(regex, string)
     
   if match == None:
      print("Not a valid date")
      return
   print("Given Data:%s"%(match.group()))
   print("Month: %s" % (match.group(1)))
   print("Day: %s" % (match.group(2)))
#Driver code--main code
findMonthAndDate("Jun 24")
print()
findMonthAndDate("I was born on June 24")
'''the output is: 
                Given Data:Jun 24
                Month: Jun
                Day: 24

                Given Data:June 24
                Month: June
                Day: 24'''
''''''
import re 
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")
if match is not None:
   print(f"Match at index {match.start()} {match.end()}")
   print(f"full month: {match.group()}")
   print(f"Month: {match.group(1)}")
   print(f"Day: {match.group(2)}")
else:
   print("The regex pattern does not match")
'''The output is:
                Match at index 14 21
                full month: June 24
                Month: June
                Day: 24'''
import re
greet = "Hello kietians how are you"
res = re.split(r'\s',greet)
print(res) # ['Hello', 'kietians', 'how', 'are', 'you'] 

greet = "Hello kietians how are you"
res = re.split(r'\s',greet,2)
print(res) # ['Hello', 'kietians', 'how are you'] 

greet = "Hello kiet how are you"
res = re.sub(r"kiet","Kietians",greet)
print(res)