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
# # Module 4: Datastructures
#
# ### Exercise solutions
#
# [Module 4](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/04%20datastructures.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [3. Conditionals](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/03%20conditionals.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/03%20conditionals%20solutions.ipynb)

# %% [markdown]
# ## Exercise 4.1: Lists
#
# 1. For each of the `print` statements below, what do you expect is printed? Run the lines to check predictions

# %%
countries = ['japan', 'hungary', 'maldives', 'gabon', 'bhutan']

print(countries[0])
# Index 0 is the FIRST element of the list, so 'japan'.

print(countries[-3])
# Third element from the end (where 'bhutan' is first),
# so 'maldives'.

print(countries[0:1] + countries[2:4])
# In a slice, the first index is inclusive while the last
# index is exclusive. Hence, we have two sublists:
# 1. starting at the first element, up to but not including the second
#    ['japan']
# 2. starting at the third element, up to but not including the fifth
#    ['maldives', 'gabon']
# and then we concatenate those to ['japan', 'maldives', 'gabon'].

more_countries = countries + ['mexico', 'haiti']
print(more_countries)
# By concatenating two lists, we create a new, longer list,
# with all elements of the original lists at the same level.

countries.append(['mexico', 'haiti'])
print(countries)
# Appending a list to another list makes the former
# a nested single element of the latter.

# %% [markdown]
# 2. Transform the list below into `['jasmin', 'john', 'ravi']` in one line of code.
#
#

# %%
students = ['jasmin', 'ravi', 'john']

# Option 1: modify students in place by
# reassinging a slice of it.
students[1:3] = [students[2], students[1]]

# Option 2: create a new list based on students.
new_students = students[:1] + students[2:] + students[1:2]

# If you figured out stepped slices in the bonus exercise,
# you have a few more interesting options:

# Variant of option 1
students[1:3] = students[:-3:-1]

# Variant of option 2
new_students = students[:1] + students[:-3:-1]

# %% [markdown]
# 3. For each of the print statements below, what do you expect is printed? Run the lines to check predictions.

# %%
random_fruit = 'pineapple'
fruits = ['apple', 'pear', random_fruit]
print(fruits)
# ['apple', 'pear', 'pineapple']

random_fruit = 'blueberry'
print(fruits)
# Still the same. The value of random_fruit was
# copied into fruits on line 2, but there is no
# permanent tie between the variables.

random_veggie = ['brussel sprouts']
veggies = ['broccoli', 'green beans', random_veggie]
print(veggies)
# There is a subtle difference with lines 1-3 here:
# the last element of veggies is not a string, but
# a nested list with a single string as element.

random_veggie.append('kale')
print(veggies)
# BOOM! Somehow, veggies changed along with the content
# of the random_veggie list. How can that be?
# The reason is that lists are values that can change
# by themselves. If we had reassigned random_veggie with
# a new value, similar to lines 6-7, we would not have
# seen it in veggies:

random_veggie = 'pumpkin'
print(veggies)

# %% [markdown]
# ## Exercise 4.2: Bonus
#
# Below we introduce another parameter in the list slice. Try to explain what it does.

# %%
countries = ['japan', 'hungary', 'maldives', 'gabon', 'bhutan']

print(countries[0:5:1])
# This does not behave differently from countries[0:5].
# From this, you could deduce that the third parameter is 1
# by default.

print(countries[0:5:2])
# This skips every second country.

print(countries[-1::-1])
# This prints countries in reverse.

print(countries[-1::-2])
# This prints countries in reverse, skipping every second element.

# Conclusion: the third parameter sets the step distance, which
# defaults to 1. If you give Python a slice [BEGIN:END:STEP], it
# visits the indices as follows:
# 1. Set the index to BEGIN.
# 2. If (STEP < 0 and index not after END)
#    or (STEP >= 0 and index not before END): stop.
# 3. Visit the index in the given list or other iterable.
# 4. Set the index to index + STEP.
# 5. Repeat from step 2.

# %% [markdown]
# The piece of code below is supposed to recognize "fancy" words: words that are longer than 5 characters, contain at least one copy of the letter 'a' and start with an uppercase. However, the code is broken. It does not recognize any of our fancy example words.
#
# 1. Change the value of `word` into each of the examples in the comments on the first two lines and then run the code. See for yourself that the code considers none of the example words fancy. Try some other words as well.
# 3. Try to understand why the code is giving the wrong result. Can you come up with a word that the code does consider fancy?
# 4. Repair the code so that it gives the right result for all examples, and any other words that you come up with.

# %% [markdown]
# > In step 2, you should find two reasons for failure which we highlight in code comments below. Once you understand these reasons, you should be able to construct words that the code does consider fancy: they must have length greater than 5, an uppercase letter in the *second* position, and a *lowercase* `'a'`. For example `'aRthur'`.
#
# > This exercise holds an important lesson: you need to fully understand why code is broken, before you can fix it!

# %%
# fancy: Alhambra, Arthur, Jasmine, Turandot
# not so fancy: Jeep, paper, Python, Ada
word = 'Alhambra'

# The first subcondition was entirely correct.
lengthy = len(word) > 5

# The second subcondition did not take into account
# that the 'a' might be uppercase.
has_a = 'a' in word
# Fix for this subcondition:
has_a = 'a' in word or 'A' in word

# The third subcondition used the wrong index: 1 instead of 0.
first_uppercase = 'A' <= word[1] <= 'Z'
# Fix for this subcondition:
first_uppercase = 'A' <= word[0] <= 'Z'

# The condition as a whole was formulated correctly.
if lengthy and has_a and first_uppercase:
    print('The word is fancy')
else:
    print('The word is not so fancy')

# %% [markdown]
# ## Next module
#
# [5. Assertions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/05%20assertions.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/05%20assertions%20solutions.ipynb)
