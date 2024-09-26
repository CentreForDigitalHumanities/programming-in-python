# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %% [markdown] id="fqMJHzNk5yXQ"
# # Module 2: Values and Expressions
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1kFvnhumJ0tOTzDVJnIvvMDRRJ19yk9ZS)
#
# Previous module: [1. Introduction](https://colab.research.google.com/drive/1W8DqryKuOwPKflPnObv4bJtNKknRsvav)
#
# ### This module
#
# - The basic types of values that exist in Python.
# - How to store values for later use.
# - How to create values from other values.

# %% [markdown] id="AqGUR1POYVNL"
# ## Primitive types and values
#
# > In computer science, primitive data types are a set of basic data types from which all other data types are constructed. [wikipedia](https://en.wikipedia.org/wiki/Primitive_data_type)
#
# In Python:
#
# - integer - `int`
# - floating point - `float`
# - string - `str`
# - boolean - `bool`
# - none - `NoneType`
#

# %% [markdown] id="8sSOrG7FdMT5"
# ### integer
# 'whole number'

# %% id="wTlfkN-Sa_MG"
1
2
-12
289883891009329819081202
0

# %% [markdown] id="iBCZZWfDdS7o"
# ### floating point
# 'decimal number'

# %% id="2JbaI2-pbTF5"
2.1
-3.2
12.8
0.0
.8

# %% [markdown] id="om0zZYCBdd8F"
# ### string
# 'text'

# %% id="DB6KZC5Sblwy"
'hello'
'we can choose between single'
"or double quotes!"

"I don't want to do this"

# escaping difficult characters with \
"I won't say \"banana\"\\"

# line breaks are preserved
'''a long string

that can go over multiple lines'''

''
""

# %% [markdown] id="dQ6u3Syk4fS4"
# *escape characters* only show when printing

# %% id="7QCMtj3S4d6E"
# escape character: \n (newline)
print('hello \n world')
'hello \n world'

# %% [markdown] id="ouf6r2zmdjY9"
# ### boolean
# true or false

# %% id="8n81rHXFb9cl"
True
False
false
true
"True"

# %% [markdown] id="xS0efw6fdoW9"
# ### None
# 'nothing here'

# %% id="fOZdR0YUcFRb"
None
none
"none"

# %% [markdown] id="jockLUXXd2Ad"
# ## Difference between types
#
# Use `type(value)` to find the type of a value.

# %% id="lHtfczHxd89N"
type(10)
type(3.14159)
type('hello')
type(True)
type('True')
type(None)

# %% [markdown] id="kZffa20rXLOQ"
# Careful! A number in quotes is not actually a number, but a string. A string that looks like a number will **NOT** behave like a number.

# %% id="-Zv10HJFXUW8"
type('10')
type('3.14159')

# %% [markdown] id="rJ_mNXXAYIpy"
# Likewise, a string that looks like a Boolean will **NOT** behave like a boolean.

# %% id="PN0FTHz2YRPM"
type('False')

# %% [markdown] id="-0p3SmmgWdif"
# `int`, `str` etcetera can be used to convert values between different types. Careful though, not all conversions you can think of will do what you expect!

# %% id="FPeklTLXWuXl"
int('10')
float('10')
str(10)
str(False)
bool('False') # !!!
None # no conversion exists

# %% [markdown] id="YGU7CclEYz2y"
# It is useful to know that each character in a string is stored as an integer. `ord(character)` lets you retrieve that integer.

# %% id="U_63E6jfab6N"
ord('2')
ord('a')
ord('A')
ord('\n')
ord('\t')

# %% [markdown] id="0dh3t4uZa9AT"
# `chr(integer)` does the opposite: it lets you retrieve the character corresponding to a given integer.

# %% id="ffIkwHahcGv9"
chr(49)
chr(98)
chr(946)
chr(22823)
chr(129327)

# %% [markdown] id="InNZNIOpezlG"
# ## Variables
#
# - container holding a value
# - assigning
#     - `variable_name = value`
# - reassigning
#     - `name = 'sheean'`
#     - `name = 'julian'`
# - in Python, no strict type
#     - `a = 1`
#     - `a = 'hello'`

# %% id="wgaSYh4yfGCx"
a = 1
b = "hello"
c = True
d = None

print(a)

# %% [markdown] id="BD2s2EqKfQtx"
# Tip: the notebook remembers variables from previous cells, but only if you executed them.

# %% id="pJ-N_rc8fZia"
print(a)
print(b)
print(c)

# %% [markdown] id="uADEckPZgGt_"
# Anything can go in a variable, not just single values

# %% id="ehEig-sCgL48"
d = a
print(d)

e = print
e(b)

# %% [markdown] id="TaiYZ3R6ghq0"
# Beware! When we assign a value, the variable stores it at that exact moment.  
# Changing one variable does not change another.
#

# %% id="pIIq1la9g1Qr"
number = 0

container = number

print(container)

number = 1

print(container)
print(number)


# %% [markdown] id="nMn_xu6Ih3hJ"
# ### Variable names
#
# #### Rules
#
# - must start with a letter or underscore (`_`)
# - can only contain letters (`a-z`, `A-Z`), numbers (`0-9`), and underscore (`_`)
# - variable names are case sensitive. `name` is a different variable from `Name`
#
# #### Conventions
#
# Next to the rules, there are some conventions.  
# Please stick to them, so others will have no trouble reading and understanding your code.
# - lowercase
#     - DO: `name`
#     - DON'T: `Name`
#     - DON'T: `NAME`<sup>1</sup>
# - readable
#     - DO: `name`
#     - DON'T: `n_a_m_e`
#     - DON'T: `x098277`
# - multiple words<sup>2</sup>
#     - DO: `first_name` (*snake_case*)
#     - DON'T: `FirstName` (*PascalCase*)
#     - DON'T `firstName` (*camelCase*)
# - comprehensive (but short)
#     - DO: `name`
#     - DON'T: `n`
#     - DON'T: `the_name_of_the_person_i_want_to_print`  
#
# <sup>1</sup> *Fully uppercased variable names actually indicate constants, and adhere to Python conventions. We will explain this later.*  
# <sup>2</sup> *This is purely a cultural thing. Other languages (and even other concepts within Python) use different casing*

# %% id="m4pTI2BEn-Z-"

# %% [markdown] id="pDU1uK2Igmki"
# ## Exercise 2.1: Variables and state
#
# In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% id="FydkKnx_hUPq"
flavor = 'vanilla'
print(flavor)

# %% id="LTWods50h-Ij"
temperature = 70
print(flavor)

# %% id="l2vT4L7piGRf"
print(temperature)
temperature = 35
print(temperature)

# %% id="k1Z_yWLXiWy7"
dog_name = 'Bobby'
cat_name = 'Garfield'
dog_name = cat_name
cat_name = dog_name
print(dog_name)
print(cat_name)

# %% [markdown] id="BZ50KykuAYPs"
# Before running the following code, try to explain why it does *not* output `chocolate`.

# %% id="X3xHg6K4Aicn"
sweet = 'chocolate'
savory = 'cheese'
dessert = 'sweet'
print(dessert)

# %% [markdown] id="0az3tNK7WD3G"
# In each of the following lines of code, replace `None` by a value of your choice. Make it such that `my_int` is an integer, `my_float` is a float, `my_bool` is a boolean and `my_string` is a string.

# %% id="lY-M8mfSXDfG"
my_int = None
my_float = None
my_bool = None
my_string = None

# %% [markdown] id="dvNIQh7KYuJb"
# ## Exercise 2.2: Bonus

# %% [markdown] id="GI9fyUO8XOcp"
# How could you verify in code whether the variables you wrote above have the correct type? Write this code below.
#
# Hint: scroll back to the section [Difference between types](#scrollTo=Difference_between_types).

# %% id="Om6z53RXYBoS"

# %% [markdown] id="h6UKIMXCj3w9"
# In the code block below, replace the question mark `?` by a variable name. Make it such that the final output is `'Hooray!'`.

# %% id="3MI6_DY7ku30"
cheer = 'Hooray!'
alarm = 'Oh no!'
anthem = 'Wilhelmus van Nassauwe'
alarm = anthem
? = cheer
cheer = anthem
anthem = alarm
print(anthem)

# %% [markdown] id="ZXd6jCn90CA_"
# ## Expressions
#
# - An expression is a combination between *operands* and *operators*.
# - Think of arithmetic: `1 + 2`
#
#

# %% [markdown] id="s8uJy_kI9C8S"
# ### Arithmetic

# %% id="f9ACtc0e13i-"
1 + 6
5 - 2
10 / 3
5 * 5

a = 8
b = 10

c = b - a
print(c)

# %% id="w9cfOflP8DEJ"
# multiple operators
4 + (3 * 5)
(4 + 3) * 5

# %% [markdown] id="zkt9aNKm28Lc"
# ### String expressions

# %% id="6os4-rt43ThF"
"hello" + " world!"
a = "my age is: "
b = 33

a + b

# %% id="SyrelaMu42UZ"
a = 'hello'
a * 5

# %% [markdown] id="DPbfP65xXlfb"
# ## Reassigning variables
#
# - You can use a variable itself when reassigning. This is useful when trying to expand an existing variable.

# %% id="ogL2Iw3-Xs15"
a = "hello"
a = a + ", world!"
print(a)

b = 'bye'
b = b + b
print(b)

b = b + b
print(b)

# %% [markdown] id="z_bXvnya5J2_"
# ## Exercise 2.3: Expressions
#
#

# %% [markdown] id="j9xhznQlbCBf"
# 1. Try to predict the value of each of the following code blocks. Can you explain any surprises?

# %% id="0QcMB4xwbSfL"
1 + 1

# %% id="eHKN9kP9bWkm"
1 * 1

# %% id="uINoRNNbbXwJ"
a = 1
b = 2
a + b

# %% id="4xyWkYlnbc_8"
c = b
a * b * c

# %% id="7tW2T4mebljv"
'hakuna' + 'matata'

# %% id="uEdPHIhBb2Mw"
liquid = 'water~'
liquid * 3

# %% id="-D7BB50Qceo2"
5 - 2 - 1

# %% id="OQUGr5rGck3m"
5 - (2 - 1)

# %% id="Jc8fawaIdCD5"
income = 100
tax = 20
net_income = income - tax
tax = 15
net_income

# %% [markdown] id="TlLkcRv-droI"
# 2. In the code block below, change the values of `character` and `multiplier` so that the output becomes `'Goooood!'`.

# %% id="pYZUkeDJenob"
character = 'x'
multiplier = 0

begin = 'G'
middle = character * multiplier
end = 'd!'

begin + middle + end

# %% [markdown] id="G8X4n_a8a5tl"
# 3. Rewrite your Hello world-program:
#     - Build the "hello, world!" string using multiple variables.
#     - Make the program say "hello, world!" 3 times, each time on a new line

# %% id="nDUVvhDEfIVI"

# %% [markdown] id="3HCqdTj2fVPK"
# ## Exercise 2.4: Bonus

# %% [markdown] id="EKFdkLkWa8EY"
# 1. Find out and describe what the following operators do:
#     - `%` (e.g. `10 % 2`)
#     - `//` (e.g. `10 // 2`)
#     - `**` (e.g. `10 ** 2`)
#     - Tip: write the expressions using variables. Change the variables and see how it affects the outcome.

# %% id="V59a7vpDfzO2"

# %% [markdown] id="o0WYIAUla-AX"
# 2. Predict what will be printed on each line in the following code block, then run the code to check your answer. If you made any mistakes, try to figure out what is causing the difference.

# %% id="Z9Vd9pdIUzT5"
word = 'stylometry'
repeats = 3
extra = 2

print((word * repeats) + str(extra))
print(word * (repeats + extra))
print(word * repeats + str(extra))
print((word + str(extra)) * repeats)
print(word + str(extra * repeats))
print(word + str(extra) * repeats)

# %% [markdown] id="DRObBQZHgsIG"
# 3. Using just the variables `word`, `repeats` and `extra` from the previous code block, write a single big expression that evaluates to `'stylometry555stylometry'`.

# %% id="uLuiUk10gqwM"

# %% [markdown] id="QaamMzJY6ISR"
# ## Boolean expressions
# Expressions that result in `True` or `False`
#

# %% id="kLjya4Au6Ucu"
# equals
1 == 1
"hello" == 'hello'
'2' == 2

# %% id="tYNp6nUp7ixW"
# does not equal
1 != 1
"hello" != 'hello'
'2' != 2

# %% id="oixxKDHV7s5J"
# greater than
2 > 1
2 > 5
'b' > 'a'

2 > 2

# greater than (or equal)
2 >= 2

# %% id="Z198kfCf75sU"
# less than
2 < 1
2 < 5
'b' < 'a'
2 < 2

# less than (or equal)
2 <= 2

# %% [markdown] id="pvrcgKU18OrJ"
# ## Exercise 2.5: boolean expressions

# %% [markdown] id="sWdnjezoil9j"
# 1. Predict for each boolean expression below: `True` or `False`? If any of your predictions is incorrect, try to find the reason.

# %% id="RpSvrom3Z8fQ"
name = 'Sheean'
height = 2

name * height == 'Sheean Sheean'

height < 2

2 <= height

1 < height <= 2

2 <= height < 1

name <= 'Julian'

height * 3 + 1 >= height

# %% [markdown] id="zJiaGIlZBN_P"
# 2. Run the code block below. Did you expect this result? Can you explain it?

# %% id="_PrnFf2lioMB"
1 == True

# %% [markdown] id="q8QviA70kdQE"
# 3. Replace one value in each of the following expressions so the expression becomes `True`.

# %% id="qDQ9Ob5Zkrqm"
1 > height

height == 0

'Julian' > name * 2

name < 1 * name

# %% [markdown] id="YbdV7SQVmDVV"
# 4. Replace one operator in each of the following expressions so the expression becomes `True`.

# %% id="hzjXIwkAmChv"
5 < 4

2 + 1 == 1

3 + 3 == 3 + 2

# %% [markdown] id="SwyAMDzDn2_X"
# 5. The *Groot woordenboek van de Nederlandse taal* by Van Dale publishers, colloquially known as "De dikke Van Dale", is a three-tome Dutch dictionary. The first tome contains words starting a–i, the second j–q and the third r–z. In the code block below, write an expression that will tell you whether `word` should be in the second tome. Try different values of `word` to verify that your solution is correct. You do not need to check whether the word is actually Dutch!

# %% id="lmCGfx_DqMWe"
word = 'archaïsch'

# your expression here

# %% [markdown] id="jXSxbjf4q6q5"
# ## Next module
#
# [3. Conditionals](https://colab.research.google.com/drive/1Lpr5qBYk9bqtAbY6bzfYcbGzCJpWM-ox)
