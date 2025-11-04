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
# # Module 4: Data Structures
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [3. Conditionals](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/03%20conditionals.ipynb)
#
# ### This module
#
# - Working with collections of many values

# %% [markdown]
# ## Data structures
#
# - Way to organize data, to make accessing it efficient
# - Different types of data structures available
# - For now, we will work with `list` and `tuple`

# %%
student1 = 'jasmin'
student2 = 'ravi'
student3 = 'john'
# not very efficient, what if we want to add another student? Or take one out?

# %% [markdown]
# ## Lists
#
# - `list`: an ordered collection of values
# - One type of *iterable*, a collection that allows iteration over its elements
# - Syntax: `[element1, element2, ...]`
# - Empty list also exists: `[]`

# %%
students = ['jasmin', 'ravi', 'john']

print(students)

# %% [markdown]
# Lists can contain values of mixed types:

# %%
['hello', 1, False]

# %% [markdown]
# They can also contain the same value multiple times.

# %%
numbers = [1, 1, True, True, "hello", "hello"]
print(numbers)

# %% [markdown]
# Lists can also contain variables

# %%
usa = 'United States of America'
nl = 'The Netherlands'
countries = [usa, nl]

# %% [markdown]
# ### Accessing single elements
# - Every element has an *index*
# - Index goes from 0 to length of the list - 1
# - Negative index counts backwards from the last element

# %%
students = ['jasmin', 'ravi', 'john']
students[0]
students[1]
students[2]
students[-1]

# %% [markdown]
# - Lists can be *unpacked* into variables

# %%
numbers = [1, 2, 3]
one, two, three = numbers

# %% [markdown]
# ### Changing single elements
# - Assign element at index just like you would assign a value to a variable

# %%
students = ['jasmin', 'ravi', 'john']
students[0] = 'johanna'

new_student = 'mark'
students[1] = new_student

students

# %% [markdown]
# ### Adding and removing elements
# - The `+` operator works for two lists
# - The `.append(value)` and `.remove(index)` functions work on a single list

# %%
hello_world = ['hello', ',', 'world']
exclamation = ['!']

full_sentence = hello_world + exclamation
print(full_sentence)

# %%
# note: `.append()` works in-place, you don't need to reassign the variable
students = ['jasmin', 'ravi', 'john']
students.append('mark')
print(students)

students.remove('john')
# or by index:
del students[2]
print(students)

# %% [markdown]
# ### Nested lists
# - Anything goes in a list, including *another* list

# %%
small_list = [4, 5, 6]
big_list = [1, 2, 3, small_list]

print(big_list)
print(big_list[-1])
print(type(big_list[-1]))

# Access the last element of the small_list inside big_list:
print(big_list[-1][-1])

# %% [markdown]
# ### Accessing multiple elements
# - Select multiple values at once: *slicing*
# - Syntax: `list[start_index:end_index]`
# - end_index is *exclusive*, so 'up to' end

# %%
students = ['jasmin', 'ravi', 'john']
#              0         1       2      3
students[0:1]
students[0:2]


# %% [markdown]
# `start_index` and `end_index` are optional

# %%
students = ['jasmin', 'ravi', 'john']
students[1:]
students[:-1]
students[:]


# %% [markdown]
# - slices can be used to reassign list elements
#
#

# %%
students = ['jasmin', 'ravi', 'john']

students[0:2] = ['johanna', 'mark']

print(students)

# %% [markdown]
# - in this way, you can also add or remove elements in the middle

# %%
students = ['jasmin', 'ravi', 'john']

students[1:2] = []
print(students)

students[1:1] = ['ravi']
print(students)

# %% [markdown]
# ### Checking if an element is in a list
# - Use the syntax `<element> in <list>`

# %%
students = ['jasmin', 'ravi', 'john']

'ravi' in students
'Ravi' in students

# %% [markdown]
# ### Useful tricks
# - the `len` *function* (we will learn about functions later) gives us the length of a list

# %%
students = ['jasmin', 'ravi', 'john']
len(students)

# %% [markdown]
# - `list.index(<value>)` finds a value and gives us the index

# %%
students = ['jasmin', 'ravi', 'john']
students.index('ravi')

# %% [markdown]
# ## Tuples
# - Different type of *iterable*
# - Syntax: `(element1, element2, ...)`
# - Important difference: not *mutable* (cannot change elements)
# - Often used to unpack, we will work with tuples in data analysis

# %%
students = ('jasmin', 'ravi', 'john')
students[0]

# %% [markdown]
# ## Exercise 4.1: Lists
#
# 1. For each of the `print` statements below, what do you expect is printed? Run the lines to check predictions

# %%
countries = ['japan', 'hungary', 'maldives', 'gabon', 'bhutan']

print(countries[0])
print(countries[-3])
print(countries[0:1] + countries[2:4])

more_countries = countries + ['mexico', 'haiti']
print(more_countries)

countries.append(['mexico', 'haiti'])
print(countries)

# %% [markdown]
# 2. Transform the list below into `['jasmin', 'john', 'ravi']` in one line of code.
#
#

# %%
students = ['jasmin', 'ravi', 'john']

# %% [markdown]
# 3. For each of the print statements below, what do you expect is printed? Run the lines to check predictions.

# %%
random_fruit = 'pineapple'
fruits = ['apple', 'pear', random_fruit]
print(fruits)

random_fruit = 'blueberry'
print(fruits)

random_veggie = ['brussel sprouts']
veggies = ['broccoli', 'green beans', random_veggie]
print(veggies)

random_veggie.append('kale')
print(veggies)

# %% [markdown]
# ## Exercise 4.2: Bonus
#
# Below we introduce another parameter in the list slice. Try to explain what it does.

# %%
countries = ['japan', 'hungary', 'maldives', 'gabon', 'bhutan']

print(countries[0:5:1])
print(countries[0:5:2])
print(countries[-1::-1])
print(countries[-1::-2])

# %% [markdown]
# The piece of code below is supposed to recognize "fancy" words: words that are longer than 5 characters, contain at least one copy of the letter 'a' and start with an uppercase. However, the code is broken. It does not recognize any of our fancy example words.
#
# 1. Change the value of `word` into each of the examples in the comments on the first two lines and then run the code. See for yourself that the code considers none of the example words fancy. Try some other words as well.
# 3. Try to understand why the code is giving the wrong result. Can you come up with a word that the code does consider fancy?
# 4. Repair the code so that it gives the right result for all examples, and any other words that you come up with.

# %%
# fancy: Alhambra, Arthur, Jasmine, Turandot
# not so fancy: Jeep, paper, Python, Ada
word = 'Alhambra'

lengthy = len(word) > 5
has_a = 'a' in word
first_uppercase = 'A' <= word[1] <= 'Z'

if lengthy and has_a and first_uppercase:
    print('The word is fancy')
else:
    print('The word is not so fancy')

# %% [markdown]
# ## Next module
#
# [5. Assertions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/05%20Assertions.ipynb)
