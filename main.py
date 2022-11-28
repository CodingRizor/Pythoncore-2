# import tracemalloc
# tracemalloc.start()
import re
from collections import Counter, OrderedDict, defaultdict, ChainMap, namedtuple
"""
print("--------------")
print("Python too supports file handling and allows users to handle files i.e.," 
      "to read and write files, along with many other file handling options, to operate on files.")
print("Python treats files differently as text or binary.")
print("Opening an file")
print("Syntax- open(filename, mode)")
# Modes-
#  Modes govern the type of operations possible in the opened file. It refers to how the file will be used once it’s
#  opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which
#  defines from where the data has to be read or written in the file. There are 6 access modes in python -
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data
# then it will be overridden but if the file is not present then it creates the file as well.
# a: open an existing file for append operation. It won’t override existing data.
# r+: To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data
print("Now file is opened-")
file = open('Info.txt', 'r')
print (file)
# for each in file:
#       print (each)
print(" To read the data - file.read() ios used")
print(" It extract a string that contains all characters in the file ")
# print(file.read())
print("To read a single line - ")
print(file.readline(), end="")
print(file.readline())
print("write() mode - It manipulates the file")
print("If any previous data is present in the file, then it will clear all the data and start from a clear file")
file = open("Trail.txt", 'w')
file.write("This is the first line\n")
file.write("This is the second line")
print("append() mode - It is used to add data to the file without clearing previous data")
print("Syntax- open(filename, a) a - append")
file = open("Trail.txt", 'a')
file.write("\nThis is the third line\n")
print("To print(copy) data of one file into another -")
f1 = open("Info.txt", 'r')
f2 = open("Trail.txt", 'a')
for data in f1:
      f2.write(data)
print("Closing a file")
print("close() function closes the file and frees the memory space acquired by that file."
      " It is used at the time when the file is no longer needed or if it is to be opened in a different file mode.")
# tracemalloc.stop()
f1.close()
f2.close()
# ---Extra
# To copy a image from one file to another
# f = open('img_name', 'rb') - read binary
# f1 = open('img_name', 'wb') - write binary
# Here image name is file name
for i in f:
    f1.write(i)

# Regular Expressions
# (RegEx) is a special sequence of characters that uses a search pattern to find a string or set of strings.
# To use regex , re module is imported
line = "Dhairya Saraswat is learning python right now"
match = re.search(r'python', line)  # r stands for raw string
try:
      print("Start Index - ", match.start())
      print("End Index - ", match.end())
      print("Span - ", match.span())
except:
      print("Not found")

# re.findall()
# Return all non-overlapping matches of pattern in string, as a list of strings.
# The string is scanned left-to-right, and matches are returned in the order found.
str = "123456789 987654321"
regex = '\d+'  # To find digits
match = re.findall(regex, str)
print(match)

# re.escape()
# Returns string with all non-alphanumerics backslashed.
print(re.escape("My name is Dhairya Saraswat"))

# Matched substring
# group() - returns the part of the string for which the patterns match
s1 = "I am learning python"
res = re.search(r'\D{2}', s1)
print(res)
res = re.search(r'\D{2} ', s1)
print(res)
res = re.search(r'\D{8} p', s1)
print(res)

# Matching a pattern with a text
# re.match() - This function attempts to match pattern to whole string.
# The re.match function returns a match object on success, None on failure.
s2 = "August 29"
s3 = "29 August"
s4 = "December 5"
s5 = "October 27 January 8"
regex1 = r"([a-zA-Z]+) (\d+)"
match = re.match(regex1, s2)
print(match.group())
print(match.group(1))
print(match.group(2))  # index 0 will print whole string same as group()
match = re.match(regex1, s3)
match = re.match(regex1, s4)
# print(match.group())  # the pattern is not same so it will show error
print(match.group())
match = re.match(regex1, s5)
print(match.group())  # This pattern stops after finding the first match
"""

# Collections Module
# The collection Module in Python provides different types of containers.
# A Container is an object that is used to store different objects and provide a way to access the
# contained objects and iterate over them.
# Counter is a subclass of dict
print("Container")
print("They are objects that hold objects and provide a way to access the contained objects and iterate over them.")
print("First import by - from collections import Counter")
print(Counter(['A', 'B', 'A', 'C', 'B', 'A']))  # Output will be printed from largest to smallest
print(Counter({'A': 3, 'C': 1, 'B': 2}))  # By dictionary
print(Counter(C=1, B=2, A=3))  # By keyword arguments
# To create an empty Counter-
coun = Counter()
coun.update([1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3])
print(coun)
coun.update([1, 3, 2])
print(coun)
# Counts can be zero and negative also
c1 = Counter(A=4, B=5, C=3)
c2 = Counter(A=5, B=4, C=3)
c1.subtract(c2)
print(c1)

# OrderedDict
# It is a dictionary subclass that remembers the order that keys were first inserted.
# Dict-
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# for key, value in d.items():
#       print(key, value)
od = OrderedDict()
od['a'] = 1
od['b'] = 3
od['c'] = 2
od['d'] = 0
for key, value in od.items():
      print(key, value)
# If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.
od['c'] = 4
print("New Ordered Dict - ")
for key, value in od.items():
      print(key, value, end=" ")
print("\nDeleting c by pop")
od.pop('c')
for key, value in od.items():
    print(key, value)
print("After re-inserting")
od['c'] = 4
for key, value in od.items():
    print(key, value)

# Defaultdict
# The functionality of both dictionaries and defaultdict are almost same except
# for the fact that defaultdict never raises a KeyError.
# It provides a default value for the key that does not exists.
print("*********Default Dict***********")
# def val():
#       return "Not present"
#
# d = defaultdict(val)
d = defaultdict(lambda : "Not present")
d['a'] = 2
d['b'] = 3
print(d['a'])
print(d['c'])
# print(d.__missing__('d'))

# ChainMap
# Python contains a container called “ChainMap” which encapsulates
# many dictionaries into one unit. ChainMap is member of module “collections“.
print("---------ChainMap--------------")
d1 = {'1': 1, '2': 2, '3': 3}
d2 = {'4': 4, '5': 5, '6': 6}
d3 = {'7': 7, '8': 8, '9': 9}
d4 = {'0': 0}
cm = ChainMap(d1, d2, d3)
print(cm)
print("All keys of ChainMap", list(cm.keys()))  # Start from last dictionary
print("All values of ChainMap", list(cm.values()))
cm = cm.new_child(d4)  # This will add a new dict to the beginning
print(cm)
cm.maps = reversed(cm.maps)  # reverse a dictionary
print(cm)

# Namedtuple
print("----------NamedTuple------------")

