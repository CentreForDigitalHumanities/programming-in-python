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
# # Module 4: Data Structures
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1YgmnpA7tRylvGBpp2PTFGvSV2P8tw5jl)
#
# Previous module: [3. Conditionals](https://colab.research.google.com/drive/1qQzRBD1e-1yCKtUNAt8L2lRb8tGjYpkR)
#
# ### This module
#
# - Working with collections of many values

# %% [markdown] id="rDdBkbX5kmUD"
# ## Data structures
#
# - Way to organize data, to make accessing it efficient
# - Different types of data structures available
# - For now, we will work with `list` and `tuple`

# %% id="bmAaWSOPm87H"
student1 = 'jasmin'
student2 = 'ravi'
student3 = 'john'
# not very efficient, what if we want to add another student? Or take one out?

# %% [markdown] id="8Vl5wbRunR82"
# ## Lists
#
# - `list`: an ordered collection of values
# - One type of *iterable*, a collection that allows iteration over its elements
# - Syntax: `[element1, element2, ...]`
# - Empty list also exists: `[]`

# %% id="sewvhM8JnhJZ"
students = ['jasmin', 'ravi', 'john']

print(students)

# %% [markdown] id="zmKyJPoQnwmK"
# Lists can contain values of mixed types:

# %% id="Bp6_Mev2nzZV"
['hello', 1, False]

# %% [markdown] id="dt_IOpu_rqbk"
# Lists can also contain variables

# %% id="TTCPoO7QrtVy"
usa = 'United States of America'
nl = 'The Netherlands'
countries = [usa, nl]

# %% [markdown] id="uYR5FBUEoR0P"
# ### Accessing elements
# - Every element has an *index*
# - Index goes from 0 to length of the list - 1
# - Negative index counts backwards from the last element

# %% id="2eL0BOUJodLK"
students = ['jasmin', 'ravi', 'john']
students[0]
students[1]
students[2]
students[-1]

# %% [markdown] id="cyX0YcO5uZRa"
# - Lists can be *unpacked* into variables

# %% id="m6ETvPPXuc4z"
numbers = [1, 2, 3]
one, two, three = numbers

# %% [markdown] id="KvOEQrqRrS0T"
# ### Changing elements
# - Assign element at index just like you would a variable

# %% id="wFyceuSArcEB"
students = ['jasmin', 'ravi', 'john']
students[0] = 'johanna'

new_student = 'mark'
students[1] = new_student

students

# %% [markdown] id="DixopwTyr6gN"
# ### Adding and removing elements
# - The `+` operator works for two lists
# - The `.append(value)` and `.remove(index)` functions works on a list

# %% id="nPyn0UHcsDbG"
hello_world = ['hello', ',', 'world']
exclamation = ['!']

full_sentence = hello_world + exclamation
print(full_sentence)

# %% id="Y2B57KQRsO2a"
# note: .append() works in-place, you don't need to reassign the variable
students = ['jasmin', 'ravi', 'john']
students.append('mark')
print(students)

students.remove('john')
# or by index:
del students[2]
print(students)

# %% [markdown] id="kUUwwkDVtXOC"
# ### Nested lists
# - Anything goes in a list, including *another* list

# %% id="EPxrRcL0tbpN"
small_list = [4, 5, 6]
big_list = [1, 2, 3, small_list]

print(big_list)
print(big_list[-1])
print(type(big_list[-1]))

# Access the last element of the small_list inside big_list:

# %% [markdown] id="1HDqXMbWwmbk"
# ### Accessing multiple elements
# - Select multiple values at once: *slicing*
# - Syntax: `list[start_index:end_index]`
# - end_index is *exclusive*, so 'up to' end

# %% id="wIS3jCYlw2P6"
students = ['jasmin', 'ravi', 'john']
#              0         1       2      3
students[0:1]
students[0:2]


# %% [markdown] id="BblECQZfw7Uy"
# `start_index` and `end_index` are optional

# %% id="6fIsX2VvxEq9"
students = ['jasmin', 'ravi', 'john']
students[1:]
students[:-1]
students[:]


# %% [markdown] id="n9lZQ72ExR4Z"
# - slices can be used to reassign list elements
#
#

# %% id="C5AIMJEHxWnX"
students = ['jasmin', 'ravi', 'john']

students[0:2] = ['johanna', 'mark']

print(students)

# %% [markdown] id="CPHEdywi-IuC"
# - in this way, you can also add or remove elements in the middle

# %% id="Tzhdcojp-TTn"
students = ['jasmin', 'ravi', 'john']

students[1:2] = []
print(students)

students[1:1] = ['ravi']
print(students)

# %% [markdown] id="nfpm1orRO34Q"
# ### Checking if an element is in a list
# - Use the syntax `<element> in <list>`

# %% id="0A9JACKJPCYt"
students = ['jasmin', 'ravi', 'john']

'ravi' in students
'Ravi' in students

# %% [markdown] id="2NX28b3sZscv"
# ### Useful tricks
# - the `len` *function* (we will learn about functions later) gives us the length of a list

# %% id="A7UHSeTtZ2nw"
students = ['jasmin', 'ravi', 'john']
len(students)

# %% [markdown] id="cO6hX3FBZ6cC"
# - `list.index(<value>)` finds a value and gives us the index

# %% id="VPmLssc7aByj"
students = ['jasmin', 'ravi', 'john']
students.index('ravi')

# %% [markdown] id="ZyOZeS2SuRJ6"
# ## Tuples
# - Different type of *iterable*
# - Syntax: `(element1, element2, ...)`
# - Important difference: not *mutable* (cannot change elements)
# - Often used to unpack, we will work with tuples in data analysis

# %% id="etiZVM_puu4Z"
students = ('jasmin', 'ravi', 'john')
students[0]

# %% [markdown] id="70aMsClGPRy9"
# ## Exercise 4.1: Lists
#
# 1. For each of the `print` statements below, what do you expect is printed? Run the lines to check predictions

# %% id="KMUxwcSqPlU1"
countries = ['japan', 'hungary', 'maldives', 'gabon', 'bhutan']

print(countries[0])
print(countries[-3])
print(countries[0:1] + countries[2:4])

more_countries = countries + ['mexico', 'haiti']
print(more_countries)

countries.append(['mexico', 'haiti'])
print(countries)

# %% [markdown] id="TyebsOIpU6hv"
# 2. Transform the list below into `['jasmin', 'john', 'ravi']` in one line of code.
#
#

# %% id="H8o6vsHKVKoq"
students = ['jasmin', 'ravi', 'john']

# %% [markdown] id="HMU5X7XFWbCw"
# 3. For each of the print statements below, what do you expect is printed? Run the lines to check predictions.

# %% id="u_RWc8wBWgMT"
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

# %% [markdown] id="3BfUO-jKS_u1"
# ## Exercise 4.2: Bonus
#
# Below we introduce another parameter in the list slice. Try to explain what it does.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 627, "status": "ok", "timestamp": 1681202305255, "user": {"displayName": "Mees van Stiphout", "userId": "10520931415894572279"}, "user_tz": -120} id="Y9oxyQb7TIPI" outputId="158288d5-94e0-4068-d13e-af2a5c85177f"
countries = ['japan', 'hungary', 'maldives', 'gabon', 'bhutan']

print(countries[0:5:1])
print(countries[0:5:2])
print(countries[-1::-1])
print(countries[-1::-2])

# %% [markdown] id="Mb6CvHt3CaA0"
# The piece of code below is supposed to recognize "fancy" words: words that are longer than 5 characters, contain at least one copy of the letter 'a' and start with an uppercase. However, the code is broken. It does not recognize any of our fancy example words.
#
# 1. Change the value of `word` into each of the examples in the comments on the first two lines and then run the code. See for yourself that the code considers none of the example words fancy. Try some other words as well.
# 3. Try to understand why the code is giving the wrong result. Can you come up with a word that the code does consider fancy?
# 4. Repair the code so that it gives the right result for all examples, and any other words that you come up with.

# %% id="QQyGzsqCCe3o"
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

# %% [markdown] id="HiEWGB1V1W4U"
# ## Next module
#
# [5. Assertions](https://colab.research.google.com/drive/1ixrL5RCpNhtQN_MtCbpy4E5PYEG1N-qH)
