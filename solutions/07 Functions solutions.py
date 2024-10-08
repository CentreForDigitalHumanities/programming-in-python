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
# # Module 7: Functions
#
# ### Exercise solutions
#
# [Module 7]([7. Functions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/07%20Functions.ipynb))
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [6. Loops](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/06%20Loops.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/06%20Loops%20-%20Solutions.ipynb)
#
# ### This module
#
# - Storing code in a variable so you can reuse it.
# - Being explicit about the purpose of your code.

# %% [markdown]
# ## Exercise 7.1: functions

# %% [markdown]
# 1. We have seen several standard functions during the course, such as `ord` and `len`. List as many as you can from memory. Try to list the types of the parameters and return values of each function as well. Do any of these functions have side effects?

# %% [markdown]
# Some examples:
# - `ord`: Has 1 parameter: a string of 1 character. The return value is an integer. No side effects.
# - `len`: Has 1 parameter: a list, tuple or other iterable. The return value is an integer. No side effects.
# - `input`: Has 1 optional parameter `prompt`, which should be a string. The function has a side effect, which is to wait for the user to type something. Its return value is a string (namely the text that you have entered).

# %% [markdown]
# 2. For exercise purposes, code in the following blocks may call `print` inside a function and omit a docstring. Predict the output, then run the code to see whether your prediction was right. Try to explain any discrepancies.

# %%
def greet(name):
    return 'Hello, ' + name + '!'

print(greet('Berit'))

# %%
name = 'Luka'

def exclaim(name):
    print(name + '!')

# nothing happens: we have created a function but we haven't called it!


# %%
def false():
    return True

print(False)

# we are printing the literal value `False`, which is not the same as our function `false` (all lower case)
# Capitalisation matters in python!

# %%
length = 5
width = 2

def calculate_area():
    area = length * width

print(calculate_area())

# calculate_area calculates something, but it does not make a return statement.
# So the returned value of `calculate_area()` is None

# %%
def question(name):
    return 'Who is ' + name + '?'

question('Jelte')


# %%
def add(left, right):
    return left + right

print(add('sweet', 'addition') * add(1, 1))

# add('sweet', 'addition') will return 'sweet' + addition', which concatenates
# the strings to 'sweetaddition'

# add(1, 1) becomes 1 + 1, so 2

# then 'sweetaddition' * 2 means "repeat 'sweetaddition' twice"
# hence 'sweetadditionsweetaddition'

# %%
# I've added some comments to each print statement, to explain what's happening and in what order.

name = 'Julian'
age = 36

print(name) # 1st print

# make a function. the code in the body will not be executed until we call the function below.
def example(name):
    print(name) # 5th print: we are printing the *parameter* `name` that we
    # passed on to the function when we called it, which is 'Jelte'. There is a
    # global parameter which is also called `name` (with value 'Julian'), but
    # the parameter takes precedence.

    name = 'Berit' # update the value of the *parameter*

    print(name) # 6th print: print the new value of the parameter

    print(age) # 7th print: print age. There is no `age` variable specific
    # to the function, so we refer to the global variable (36)

print(name) # 2nd print: name is unchanged. `name = 'Berit'` was part of the
# function body, it's not yet executed

print(example) # 3rd print: we are printing the function itself, not the
# returned value!

print(name) # 4th print: name is still unchanged.

example('Jelte') # we are running the function here, and now we will execute the
# print statements within its body

print(name) # 8th print: the function `example` did some stuff with its
# parameter called name, but did not do anything with the global variable name.
# So `name` is still 'Julian'

print(age) # 9th print



# %% [markdown]
# 3. In each of the following code blocks, write a docstring for the function, then add assertions and run the block to check that your documentation is correct.

# %%
def odd(number):
    '''
    Checks whether a number is odd

    Input should be an integer. Output is a boolean, True if the number is not
    divisible by two.
    '''
    return number % 2 == 1

assert odd(1) == True
assert odd(6) == False
assert odd(0) == False


# %%
def magic(word):
    '''
    Checks that the input is a nonempty string and starts with a capital letter.

    Input can be of any type: anything other than a string will return False.
    For strings, checks that the string is not empty and the first character
    is an uppercase latin character.
    '''
    if not word or type(word) != str:
        return False
    if 'A' <= word[0] <= 'Z':
        return True
    return False

assert magic(123) == False
assert magic('Hello python programmers!') == True
assert magic('python python python') == False
assert magic('🤔') == False
assert magic('') == False


# %%
def join_commas(words):
    '''
    Joins a iterable of strings into a single string, with ', ' between each item.

    Input should be an iterable of strings with at least 1 item.
    '''
    first, *rest = list(words)
    text = first
    for word in rest:
        text = text + ', ' + word
    return text

assert join_commas(['a', 'b', 'c']) == 'a, b, c'
assert join_commas(['a']) == 'a'
assert join_commas(('a', 'b', 'c')) == 'a, b, c'


# %% [markdown]
# 4. Write a function `is_number` that takes one argument. If the argument is a number, it should return `True`; otherwise, it should return `False`. Make sure to include a docstring!

# %%
# Your definition of is_number here

def is_number(value):
    '''
    Checks if the input is a number (int or float)
    '''

    number_types = [int, float]
    return type(value) in number_types

# The following lines will check your solution (no output is good)
assert is_number(0)
assert is_number(10)
assert is_number(0.5)
assert is_number(8 / 5)
assert not is_number(None)
assert not is_number('dear')
assert not is_number('123')


# %% [markdown]
# ## Exercise 7.2: bonus

# %% [markdown]
# 1. Write a function `last_a_index` that, given a string, returns the **last** index of the letter `'a'` in the string. If there is no `'a'` in the string, the function should return `None`.

# %%
# Define last_a_index here

def last_a_index(text):
    '''
    Gives the index of the last 'a' in the string.

    If there is no 'a' in the string, returns None
    '''

    a_index = None

    for (index, character) in enumerate(text):
        if character == 'a':
            a_index = index

    return a_index

assert last_a_index('banana') == 5
assert last_a_index('cherry') == None
assert last_a_index('Once upon a time, there was a dragon') == 32


# %% [markdown]
# 2. Write a function `replace` with three string arguments: `text`, `query` and `replacement`. It should return a copy of `text` in which all occurrences of `query` are replaced by `replacement`. For example, `replace('small', 'a', 'e')` should return `'smell'`. You may assume that `query` is always a single character. For an additional challenge, you can try to also handle multi-character query strings. For ultimate challenge, try to think of a way to handle the empty string!

# %%
# Define replace here

# solution one: does not work with multi-character strings
def replace(text, query, replacement):
    '''
    Replace each occurence of a character in a string

    Input:
    - text: a string in which you want to replace something
    - query: the character you wish to replace
    - replacement: the string that should replace `query`
    '''

    replaced = ''

    for character in text:
        if character == query:
            replaced = replaced + replacement
        else:
            replaced = replaced + character

    return replaced

assert replace('small', 'a', 'e') == 'smell'
assert replace('banana', 'a', 'o') == 'bonono'
assert replace('cherry', 'a', 'x') == 'cherry'


# %%
# solution 2: handle multi-character strings and empty strings

# There no clear answer for what should happen in the case of empty strings!
# It's a question that does not really make sense: replace every insstance of
# # nothing?

# Here we just return `None` when query is empty. You could also return the
# original string.

def replace(text, query, replacement):
    '''
    Replace each occurence of a substring in a string

    Input:
    - text: a string in which you want to replace something
    - query: the string you wish to replace
    - replacement: the string that should replace `query`

    If the query is empty, returns None.
    '''

    if not query:
        return None

    size = len(query)
    new_text = '' # where we build our new text
    position = 0 # our position as we move through the text

    while position < len(text):
        possible_match = text[position:position+size] # slice of text from here, the same size as the query
        if possible_match == query: #if this matches...
            new_text += replacement # put the replacement in our new string
            position += size # and skip ahead until after this slice
        else:
            # if it doesn't match, move ahead by one character
            new_text += text[position]
            position += 1

    return new_text


assert replace('small', 'a', 'e') == 'smell'
assert replace('banana', 'a', 'o') == 'bonono'
assert replace('cherry', 'a', 'x') == 'cherry'
assert replace('small', '', '?') == None
assert replace('banana', 'an', 'ab') == 'bababa'
assert replace('banana', 'banana', 'apple') == 'apple'
assert replace('banana', 'e', 'o') == 'banana'

# %% [markdown]
# ## Next module
#
# [8. Debugging](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/08%20debugging.ipynb)
