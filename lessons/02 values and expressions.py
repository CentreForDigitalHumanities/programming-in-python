# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %% [markdown]
# # Module 2: Values and Expressions
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [1. Introduction](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/01%20introduction.ipynb)
#
# ### This module
#
# - The basic types of values that exist in Python.
# - How to store values for later use.
# - How to create values from other values.

# %% [markdown]
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

# %% [markdown]
# ### integer
# 'whole number'

# %%
1
2
-12
289883891009329819081202
0

# %% [markdown]
# ### floating point
# 'decimal number'

# %%
2.1
-3.2
12.8
0.0
.8

# %% [markdown]
# ### string
# 'text'

# %%
'hello'
'we can choose between single'
"or double quotes!"

"I don't want to do this"

# escaping difficult characters with \
"I won't say \"banana\"\\"

# line breaks are preserved if you use triple quotes (''' or """)
'''a long string

that can go over multiple lines'''

"""
and here
is another one!
"""

''
""

# %% [markdown]
# *escape characters* only show when printing

# %%
# escape character: \n (newline)
print('hello \n world')
'hello \n world'

# %% [markdown]
# ### boolean
# true or false

# %%
True
False

# %% [markdown]
# Careful: the following are not booleans

# %%
false
true
"True"

# %% [markdown]
# ### None
# 'nothing here'

# %%
None

# %% [markdown]
# Careful: the following are not the same as None.

# %%
none
"none"

# %% [markdown]
# ## Difference between types
#
# Use `type(value)` to find the type of a value.

# %%
type(10)
type(3.14159)
type('hello')
type(True)
type('True')
type(None)

# %% [markdown]
# Careful! A number in quotes is not actually a number, but a string. A string that looks like a number will **NOT** behave like a number.

# %%
type('10')
type('3.14159')

# %% [markdown]
# Likewise, a string that looks like a Boolean will **NOT** behave like a boolean.

# %%
type('False')

# %% [markdown]
# `int`, `str` etcetera can be used to convert values between different types. Careful though, not all conversions you can think of will do what you expect!

# %%
int('10')
float('10')
str(10)
str(False)
bool('False') # !!!
None # no conversion exists

# %% [markdown]
# It is useful to know that each character in a string is stored as an integer. `ord(character)` lets you retrieve that integer.

# %%
ord('2')
ord('a')
ord('A')
ord('\n')
ord('\t')

# %% [markdown]
# `chr(integer)` does the opposite: it lets you retrieve the character corresponding to a given integer.

# %%
chr(49)
chr(98)
chr(946)
chr(22823)
chr(129327)

# %% [markdown]
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
# Tip: hold your mouse over a variable to see its type, or use `type(variable_name)` as shown above.

# %%
a = 1
b = "hello"
c = True
d = None

print(a)

# %% [markdown]
# Tip: the notebook remembers variables from previous cells, but only if you executed them.

# %%
print(a)
print(b)
print(c)

# %% [markdown]
# Anything can go in a variable, not just single values

# %%
d = a
print(d)

e = print
e(b)

# %% [markdown]
# Beware! When we assign a value, the variable stores it at that exact moment.  
# Changing one variable does not change another.
#

# %%
number = 0

container = number

print(container)

number = 1

print(container)
print(number)


# %% [markdown]
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

# %%

# %% [markdown]
# ## Exercise 2.1: Variables and state
#
# In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %%
flavor = 'vanilla'
print(flavor)

# %%
temperature = 70
print(flavor)

# %%
print(temperature)
temperature = 35
print(temperature)

# %%
dog_name = 'Bobby'
cat_name = 'Garfield'
dog_name = cat_name
cat_name = dog_name
print(dog_name)
print(cat_name)

# %% [markdown]
# Before running the following code, try to explain why it does *not* output `chocolate`.

# %%
sweet = 'chocolate'
savory = 'cheese'
dessert = 'sweet'
print(dessert)

# %% [markdown]
# In each of the following lines of code, replace `None` by a value of your choice. Make it such that `my_int` is an integer, `my_float` is a float, `my_bool` is a boolean and `my_string` is a string.

# %%
my_int = None
my_float = None
my_bool = None
my_string = None

# %% [markdown]
# ## Exercise 2.2: Bonus

# %% [markdown]
# How could you verify in code whether the variables you wrote above have the correct type? Write this code below.
#
# Hint: scroll back to the section [Difference between types](#scrollTo=Difference_between_types).

# %%

# %% [markdown]
# In the code block below, replace the question mark `?` by a variable name. Make it such that the final output is `'Hooray!'`.

# %%
cheer = 'Hooray!'
alarm = 'Oh no!'
anthem = 'Wilhelmus van Nassauwe'
alarm = anthem
? = cheer
cheer = anthem
anthem = alarm
print(anthem)

# %% [markdown]
# ## Expressions
#
# - An expression is a combination between *operands* and *operators*.
# - Think of arithmetic: `1 + 2`
#
#

# %% [markdown]
# ### Arithmetic

# %%
1 + 6
5 - 2
10 / 3
5 * 5

a = 8
b = 10

c = b - a
print(c)

# %%
# multiple operators
4 + (3 * 5)
(4 + 3) * 5

# %% [markdown]
# ### String expressions

# %%
"hello" + " world!"
a = "my age is: "
b = 33

a + b

# %%
a = 'hello'
a * 5

# %% [markdown]
# ## Reassigning variables
#
# - You can use a variable itself when reassigning. This is useful when trying to expand an existing variable.

# %%
a = "hello"
a = a + ", world!"
print(a)

b = 'bye'
b = b + b
print(b)

b = b + b
print(b)

# %% [markdown]
# ## Exercise 2.3: Expressions
#
#

# %% [markdown]
# 1. Try to predict the value of each of the following code blocks. Can you explain any surprises?

# %%
1 + 1

# %%
1 * 1

# %%
a = 1
b = 2
a + b

# %%
c = b
a * b * c

# %%
'hakuna' + 'matata'

# %%
liquid = 'water~'
liquid * 3

# %%
5 - 2 - 1

# %%
5 - (2 - 1)

# %%
income = 100
tax = 20
net_income = income - tax
tax = 15
net_income

# %% [markdown]
# 2. In the code block below, change the values of `character` and `multiplier` so that the output becomes `'Goooood!'`.

# %%
character = 'x'
multiplier = 0

begin = 'G'
middle = character * multiplier
end = 'd!'

begin + middle + end

# %% [markdown]
# 3. Rewrite your Hello world-program:
#     - Build the "hello, world!" string using multiple variables.
#     - Make the program say "hello, world!" 3 times, each time on a new line

# %%

# %% [markdown]
# ## Exercise 2.4: Bonus

# %% [markdown]
# 1. Find out and describe what the following operators do:
#     - `%` (e.g. `10 % 2`)
#     - `//` (e.g. `10 // 2`)
#     - `**` (e.g. `10 ** 2`)
#     - Tip: write the expressions using variables. Change the variables and see how it affects the outcome.

# %%

# %% [markdown]
# 2. Predict what will be printed on each line in the following code block, then run the code to check your answer. If you made any mistakes, try to figure out what is causing the difference.

# %%
word = 'stylometry'
repeats = 3
extra = 2

print((word * repeats) + str(extra))
print(word * (repeats + extra))
print(word * repeats + str(extra))
print((word + str(extra)) * repeats)
print(word + str(extra * repeats))
print(word + str(extra) * repeats)

# %% [markdown]
# 3. Using just the variables `word`, `repeats` and `extra` from the previous code block, write a single big expression that evaluates to `'stylometry555stylometry'`.

# %%

# %% [markdown]
# ## Boolean expressions
# Expressions that result in `True` or `False`
#

# %%
# equals
1 == 1
"hello" == 'hello'
'2' == 2

# %%
# does not equal
1 != 1
"hello" != 'hello'
'2' != 2

# %%
# greater than
2 > 1
2 > 5
'b' > 'a'

2 > 2

# greater than (or equal)
2 >= 2

# %%
# less than
2 < 1
2 < 5
'b' < 'a'
2 < 2

# less than (or equal)
2 <= 2

# %% [markdown]
# ## Exercise 2.5: boolean expressions

# %% [markdown]
# 1. Predict for each boolean expression below: `True` or `False`? If any of your predictions is incorrect, try to find the reason.

# %%
name = 'Sheean'
height = 2

name * height == 'Sheean Sheean'

height < 2

2 <= height

1 < height <= 2

2 <= height < 1

name <= 'Julian'

height * 3 + 1 >= height

# %% [markdown]
# 2. Run the code block below. Did you expect this result? Can you explain it?

# %%
1 == True

# %% [markdown]
# 3. Replace one value in each of the following expressions so the expression becomes `True`.

# %%
1 > height

height == 0

'Julian' > name * 2

name < 1 * name

# %% [markdown]
# 4. Replace one operator in each of the following expressions so the expression becomes `True`.

# %%
5 < 4

2 + 1 == 1

3 + 3 == 3 + 2

# %% [markdown]
# 5. The *Groot woordenboek van de Nederlandse taal* by Van Dale publishers, colloquially known as "De dikke Van Dale", is a three-tome Dutch dictionary. The first tome contains words starting a–i, the second j–q and the third r–z. In the code block below, write an expression that will tell you whether `word` should be in the second tome. Try different values of `word` to verify that your solution is correct. You do not need to check whether the word is actually Dutch!

# %%
word = 'archaïsch'

# your expression here

# %% [markdown]
# ## Next module
#
# [3. Conditionals](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/03%20conditionals.ipynb)
