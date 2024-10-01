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
# # Module 2: Values and expressions
#
# ### Exercise solutions
#
# [Module 2](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20values%20and%20expressions.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [1. Introduction](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/01%20introduction.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/01%20introduction%20solutions.ipynb)

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

# %% [markdown]
# The variable `flavor` was retained from the previous code block. The variable `temperature` is not used here.

# %%
print(temperature)
temperature = 35
print(temperature)

# %% [markdown]
# `temperature` is first printed as it was retained from the previous code block. Then, it is reassigned and printed again.

# %%
dog_name = 'Bobby'
cat_name = 'Garfield'
dog_name = cat_name
cat_name = dog_name
print(dog_name)
print(cat_name)

# %% [markdown]
# On line 3, it is important to realize that `dog_name` gets *the value of* `cat_name`. There is no permanent tie between the variables. After line 3, both variables have the same value. Hence, `cat_name` cannot change into anything else on line 4. The program has effectively forgotten the value `'Bobby'`.

# %% [markdown]
# Before running the following code, try to explain why it does *not* output `chocolate`.

# %%
sweet = 'chocolate'
savory = 'cheese'
dessert = 'sweet'
print(dessert)

# %% [markdown]
# On line 3, `'sweet'` is quoted, so Python considers it a string. It does not recognize it as a variable, even though we also defined a variable with that name on line 1.

# %% [markdown]
# In each of the following lines of code, replace `None` by a value of your choice. Make it such that `my_int` is an integer, `my_float` is a float, `my_bool` is a boolean and `my_string` is a string.

# %%
my_int = 42
my_float = .5
my_bool = True
my_string = "I'm starving"

# %% [markdown]
# ## Exercise 2.2: Bonus

# %% [markdown]
# How could you verify in code whether the variables you wrote above have the correct type? Write this code below.
#
# Hint: scroll back to the section [Difference between types](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20values%20and%20expressions.ipynb#scrollTo=Difference_between_types).

# %%
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))

# %% [markdown]
# In the code block below, replace the question mark `?` by a variable name. Make it such that the final output is `'Hooray!'`.

# %%
cheer = 'Hooray!'
alarm = 'Oh no!'
anthem = 'Wilhelmus van Nassauwe'
alarm = anthem
alarm = cheer  # alarm instead of ?
cheer = anthem
anthem = alarm
print(anthem)

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

# %% [markdown]
# If we had done `print('hakuna', 'matata')`, it would have output `hakuna matata`, with a space between the words. When we concatenate strings using `+`, Python does not take that liberty, so if we actually want to separate words with spaces, we have to add them ourselves.

# %%
liquid = 'water~'
liquid * 3

# %%
5 - 2 - 1

# %%
5 - (2 - 1)

# %% [markdown]
# The above result is different from the previous, because Python evaluates minus operators (and most other operators) left-to-right by default.

# %%
income = 100
tax = 20
net_income = income - tax
tax = 15
net_income

# %% [markdown]
# On line 3, we set `net_income` to the outcome of *the value of* `income` minus *the value of* `tax`, which are respectively `100` and `20` at that point. `net_income` then keeps its value (`80`) until we change it directly. Hence, line 4 does not change anything about `net_income`. If we wanted to update `net_income`, we would have to run line 3 again.

# %% [markdown]
# 2. In the code block below, change the values of `character` and `multiplier` so that the output becomes `'Goooood!'`.

# %%
character = 'o'
multiplier = 5

begin = 'G'
middle = character * multiplier
end = 'd!'

begin + middle + end

# %% [markdown]
# 3. Rewrite your Hello world-program:
#     - Build the "hello, world!" string using multiple variables.
#     - Make the program say "hello, world!" 3 times, each time on a new line

# %%
# This works:
hello = 'Hello, '
world = 'world!\n'
variable = hello + world
print(3 * variable)

# This works, too:
slogan = '''Hello, world!
'''
result = 3 * slogan
print(result)

# This would also work, but uses no variables:
print('Hello, world!\n' * 3)

# %% [markdown]
# ## Exercise 2.4: Bonus

# %% [markdown]
# 1. Find out and describe what the following operators do:
#     - `%` (e.g. `10 % 2`)
#     - `//` (e.g. `10 // 2`)
#     - `**` (e.g. `10 ** 2`)
#     - Tip: write the expressions using variables. Change the variables and see how it affects the outcome.

# %%
# Regarding %, you will quickly see a pattern if you set
# the right operand to 3 and try a series of consecutive
# numbers as the left operand:

10 % 3 == 1
11 % 3 == 2
12 % 3 == 0
13 % 3 == 1
14 % 3 == 2
15 % 3 == 0
16 % 3 == 1
17 % 3 == 2
18 % 3 == 0

# Conclusion: % calculates the remainder of division.

# // is like / (division), but rounded down to an integer.
10 / 3 == 3.33333333333333333
10 // 3 == 3
5 / 4 == 1.25
5 // 4 == 1

# In general, the following equation is always true if
# a and b are integers:
(a // b) * b + a % b == a

# a ** b raises a to the power of b.
3 ** 2 == 3 * 3 == 9
3 ** 3 == 3 * 3 * 3 == 27
3 ** 4 == 3 * 3 * 3 * 3 == 81

# %% [markdown]
# 2. Predict what will be printed on each line in the following code block, then run the code to check your answer. If you made any mistakes, try to figure out what is causing the difference.

# %%
word = 'stylometry'
repeats = 3
extra = 2

print((word * repeats) + str(extra))
# Evaluated in this order:
word == 'stylometry'
repeats == 3
'stylometry' * 3 == 'stylometrystylometrystylometry'
str(extra) == '2'
'stylometrystylometrystylometry' + '2' == 'stylometrystylometrystylometry2'

print(word * (repeats + extra))
# Evaluated in this order:
word == 'stylometry'
repeats + extra == 5
'stylometry' * 5 == 'stylometrystylometrystylometrystylometrystylometry'

print(word * repeats + str(extra))
# Evaluated in the same way as line 5, just without parentheses.
# The * operator takes precedence over the + operator by default.

print((word + str(extra)) * repeats)
# Evaluated in this order:
word == 'stylometry'
str(extra) == '2'
word + str(extra) == 'stylometry2'
repeats == 3
'stylometry2' * 3 == 'stylometry2stylometry2stylometry2'

print(word + str(extra * repeats))
# Evaluated in this order:
word == 'stylometry'
extra == 2
repeats == 3
2 * 3 == 6
str(6) == '6'
'stylometry' + '6' == 'stylometry6'

print(word + str(extra) * repeats)
# Evaluated in this order:
word == 'stylometry'
extra == 2
str(2) == '2'
repeats == 3
# * operator takes precedence over +, so right subexpression first.
'2' * 3 == '222'
'stylometry' + '222' == 'stylometry222'

# %% [markdown]
# 3. Using just the variables `word`, `repeats` and `extra` from the previous code block, write a single big expression that evaluates to `'stylometry555stylometry'`.

# %%
word + str(extra + repeats) * repeats + word
# (you can add parentheses, as long as you evaluate the * before the +)

# %% [markdown]
# ## Exercise 2.5: boolean expressions

# %% [markdown]
# 1. Predict for each boolean expression below: `True` or `False`? If any of your predictions is incorrect, try to find the reason.

# %%
name = 'Jelte'
height = 2

name * height == 'Jelte Jelte'
# False because string repetition does not add spaces

height < 2
# a number can never be less than itself

2 <= height
# ... but a number is always less than or equal to itself

1 < height <= 2
# Python allows you to compare the same expression on two sides

2 <= height < 1
# Both comparison must be true for the whole expression to be True

name <= 'Julian'
# Lexicographical comparison: 'Julian' is greater because
# 'u' comes after 'e'.

height * 3 + 1 >= height
# * and + take precedence over >=, so the evaluation goes in this order:
height * 3 == 6
6 + 1 == 7
height == 2
(7 >= 2) == True

# %% [markdown]
# 2. Run the code block below. Did you expect this result? Can you explain it?

# %%
1 == True

# 1 and True are literally the same value.
# More interesting equalities and inequalities:

0 == False
2 != True
None != False

# %% [markdown]
# 3. Replace one value in each of the following expressions so the expression becomes `True`.

# %%
3 > height
0 == 0
'Julian' < 'Julian' * 2
name < 2 * name

# %% [markdown]
# 4. Replace one operator in each of the following expressions so the expression becomes `True`.

# %%
5 > 4
2 - 1 == 1
3 + 3 == 3 * 2

# %% [markdown]
# 5. The *Groot woordenboek van de Nederlandse taal* by Van Dale publishers, colloquially known as "De dikke Van Dale", is a three-tome Dutch dictionary. The first tome contains words starting a–i, the second j–q and the third r–z. In the code block below, write an expression that will tell you whether `word` should be in the second tome. Try different values of `word` to verify that your solution is correct. You do not need to check whether the word is actually Dutch!

# %%
word = 'archaïsch' # try also 'idee', 'j', 'quasi', 'r', 'ziezo'

# is it in the FIRST tome?
word < 'j'

# is it in the THIRD tome?
word >= 'r'

# is it in the SECOND tome? (opposites of the previous expressions)
word >= 'j'
word < 'r'

# combining both conditions in a single expression
'j' <= word < 'r'

# %% [markdown]
# ## Next module
#
# [3. Conditionals](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/03%20conditionals.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/03%20conditionals%20solutions.ipynb)
