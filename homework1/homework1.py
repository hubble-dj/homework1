# File: homework1.py
# --- Variables and Data Types ---
a = 10 
print(a)
print(type(a)) # a is an integer 

b = 1.5
print(b)
print(type(b)) # b is a float

c=3j
print(c)
print(type(c)) # c is a complex number 

d = "hello"
print(d)
print(type(d)) # d is a string 

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list 

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dict

g = (1,2)
print(g)
print(type(g)) # g is a tuple

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list 

i = True 
print(i)
print(type(i)) # i is a bool 

j = None
print(j)
print(type(j)) # j is a NoneType

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list 

l = str(14)
print(l)
print(type(l)) # l is an string

m = (1e4)
print(m)
print(type(m)) # m is a float 

# 1. I found 9 different data types 
# 2. String, float, list, bool, dict, integer, NoneType, tuple, complex number 
# 3. b and m, d and l, k h e, 
# 4. It's data type is string. It's not an integer because str() makes any data after it into a string. 

z = range(300)
print(z)
print(type(z)) # z is a range 

# --- Booleans --- # 

print(10>9) # True, 10 is greater than 9 
print(10==9) #False, 10 is not equal to 9
print (10<=9) #False, 10 is not less than or equal to 9 
print(bool("abc")) # True, non-empty is truthy 
print (bool(123)) # True, non-zero 
print(bool(["apple", "cherry", "banana"])) # True, non-empty is truthy
print(bool(True)) # True, already converted to boolean 
print(bool(False)) # False, already converted to boolean 
print(bool(0)) # False, zero value 
print(bool("")) # False, empty string
print(bool(" ")) # True, there's a space in there 
print(bool(())) # False, tuple empty 
print(bool([])) # False, list empty 
print(bool({})) # False, dictionary empty
print(bool(True and False)) # False, right side is false 
print(bool(True and True)) # True, both sides of and are true 
print(bool(False and False)) # False, both sides of and are false 
print(bool(True or False)) # True, at least one side is true 
print(bool(True or True)) # True, both sides are true 
print(bool(False or False)) # False, both sides of or are false 
print(bool(not(False))) # True, not flips the value
print(bool(not(True)))# False, not flips the value

# 1. More frequently boolean True values are taken just from there being a value present or a certain logic line work. 
# 2. The bool(" ") being true, didn't expect the space to count 
print(bool(not(False) or False)) # Not False makes one side of the or true, returning a True value
print(bool(not(False) and False)) # Flipping the or to an and requires both side of the and to be true, which is false. 

# --- Operators --- #

print (10+5) # 15, + performs addition
print(10-5) # 5, - performs subtraction 
print(2*4) # 8, * performs multiplication 
print(6/3) # 2.0, / performs division 
print(5 % 2) # 1, % finds the remainder 
print((3**2)) # 9, ** is exponential 
print(15//2) # 7, // divides and rounds 
print(5==2) # False,  == is equal 
print(10!=10) # False, ! is factorial 
print(2<5) # True, < is less than
print(12>5) # True, > is greater than
print(5<=6) # True, <= is less than or equal to
print(1>=10) # False, >= is greater than or equal to
x=5
x+=5
print(x) # 10, += adds 5 to x and saves the change
x-=4
print(x) # 6, -= removes 6 to x and saves the change
x *= 3
print(x) # 18, #= multiplies x by 3 and saves the change

# Logical Operators
# and determines if two things are True and converts into boolean. bool(True and False)
# or determines if either one of two things are True and converts into boolean. bool(False or False)
# not flips the boolean value. bool(not(True))

# More Questions 
# / divides and // divides then rounds to nearest integer
# % Finds the remainder, // does not 
# print(5%2)
# They perform an operation then save the change to the variable 

# -- Strings -- # 
my_string = "Danuta"
print(my_string) # Prints Danuta
print(my_string[0]) # Prints D, first term
print(my_string[1]) # Prints a, second term
print(my_string[2]) # Prints n, third term
print(my_string[3]) # Prints u, fourth term
print(my_string[4]) # Prints t, fifth term
print(my_string[-1]) # Prints a, first term on the right side 
print(my_string[0:5:2]) # Prints Dnt, 0 and 5 establish range, 2 slices the data every other
print(len(my_string)) # 6, length of string 
print(my_string+" goodbye") # Danuta goodbye, adds it 
print(my_string * 7) # DanutaDanutaDanutaDanutaDanutaDanutaDanuta, multiplies the string 

# Slicing is manipulating which set of terms you take out of a data set. Ussed it for [0:5:2]
name = "Oski"
print("Hello, my name is", name) # Hello, my name is Oski. Again added the strings together
print(f"Hello, my name is {name}") # Same result, but weirder 
#f-strings allow you to embed a variable within a string

# cd
#Changes directories 
# Example: cd homework1 

# ls 
# lists files and directories where you are 
# Example: ls 

#ls -a
# Shows all hidden files 
# Example:  ls -a 

# mkdir
# Makes directories 
# Example: mkdir homework2 

# cat 
# prints the content of the file on the terminal
# Example: cat homework1 

#pwd 
# prints working directory, where you are basically 
# Example: pwd 

# cd ..
# moves up one directory 
# Example: cd ..

# cd . 
#you just stay in your current directory 
# Example: cd . 

# cd ~
# home directory 
# Example: cd ~

# cp
#Copies a file and puts it somewhere else 
# Example: cp homework1.py ../tralalalala.py

# mv 
# moves a file or renames it 
# Example: mv homework1 ../downloads 

#rm
#deletes files 
# Example: rm mysleepschedule.txt 

# clear
# just clears the terminal 
# Example: clear

#grep 
#searches for key phrases and prints every line with that phrase 
# Example: grep "bool" homework1

# 1. touch, like nano but doesn't open a text file. which, tells you where you're running a command. diff, compares differences between two files. 
# 2. ls -a looks for hidden files 
# 3. Any file starting with a .   Hidden to reduce clutter
# 4. -l, shows full list and detailed info, "long format", -m attaches a message, -i leaves an interactive thingie at the end 
