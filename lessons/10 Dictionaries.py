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
# # Dictionaries
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [9. String manipulation](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/09%20string%20manipulation.ipynb)
#
# ### This module
#
# - Learn about _dictionaries_, a useful way of storing and looking up data

# %% [markdown]
# ## What are dictionaries?
#
# We have already seen one type of data structure, the _list_. Lists store values in a specific _order_, and we can retrieve values by their position in the list.

# %%
fruits = ['apple', 'banana', 'orange']

assert fruits is not ['banana', 'apple', 'orange'] # order matters!

print(fruits[1])

# %% [markdown]
# What if we want to store some extra information about each type of fruit? That is where dictionaries come in handy. Here I save the colour of each fruit.

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

# %% [markdown]
# Some vocabulary: `'apple'`, `'banana'` and `'orange'` are _keys_ of the dictionary, while `'red'`, `'yellow'` and `'orange'` are _values_. Keys and values come in pairs: `'red'` is the value for the key `'apple'`. We'll see what we can do with this in a bit.
#
# Dictionaries need not contain strings. The values of a dictionary can be anything you want. The keys are a bit more restricted: strings, numbers, and tuples are fine, but complex data structures like lists and other dictionaries are not.

# %%
students_by_year = {2021: ['Julian', 'Jelte'], 2022: ['Julian', 'Jelte', 'Berit']}

years_per_student = {'Jelte': [2021, 2022], 'Julian': [2021, 2022], 'Berit': 2022}

# long dictionaries can be written on multiple lines, to keep it readable
dictionaries_by_topic = {
    'fruit': fruit_colors,
    'python course': [students_by_year, years_per_student]
}

# %%
# this will be rejected
shared_interests = {['Julian', 'Jelte']: ['cats', 'programming'],
                    ['Jelte', 'Berit']: 'music'}

# %% [markdown]
# The keys of a dictionary should be **unique**. If you try to write something with a key that already exists, it will overwrite the old value.

# %%
unambiguous_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
ambiguous_colors = {'apple': 'green', 'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
assert ambiguous_colors == unambiguous_colors

print(ambiguous_colors)

# %% [markdown]
# Order does not matter for dictionaries!

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
fruit_colors_2 = {'banana': 'yellow',  'apple': 'red', 'orange': 'orange'}

assert fruit_colors == fruit_colors_2

# %% [markdown]
# You can make emtpy dictionaries too.

# %%
empty = {} # a dictionary with no keys / values

new_dict = dict() # constructor function

# %% [markdown]
# ### Accessing
#
# With lists and tuples, we access elements with the index number. In dictionaries we access them by the key.

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
students_by_year = {2021: ['Julian', 'Jelte'], 2022: ['Julian', 'Jelte', 'Berit']}

print(fruit_colors['apple'])
print(students_by_year[2021])

# %% [markdown]
# ### Assiging / reassigning
#
# You can also assign or reassign values by the key. If the key is _not_ in the dictionary yet, it creates the key-value pair.

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
fruit_colors['apple'] = 'red or green'
print(fruit_colors)

fruit_colors['kiwi'] = 'green'
print(fruit_colors)

# be aware that misspelling a key creates a new entry
fruit_colors['bnaana'] = 'yellwo'
print(fruit_colors)

# %% [markdown]
# ### Updating
# Dictionaries can be *updated* with another dictionary. This is a way to quickly add multiple key-value pairs:
#
# - `dictionary.update(other_dictionary)`
# - this happens *in-place*, the function doesn't return anything

# %%
students_by_year = {2021: ['Julian', 'Jelte'], 2022: ['Julian', 'Jelte', 'Berit']}
more_students = {2023: ['Sheean', 'Mees', 'Luka'], 2024: ['Hopefully a lot']}

print(students_by_year.update(more_students))
print(students_by_year)

# %% [markdown]
# ### Deleting
# To delete a key-value pair: `del dictionary[key]`

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
del fruit_colors['orange']
print(fruit_colors)

# %% [markdown]
# ### Iterables
# Dictionaries have a few useful functions:
# - `dictionary.keys()` returns a list of all keys
# - `dictionary.values()` returns a list of all values
# - `dictionary.items()` returns a list of tuples: `(key, value)`

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

# which types of fruit do we have information about?
print(fruit_colors.keys())

# which colors do we have?
print(fruit_colors.values())

# what's in the dictionary?
print(fruit_colors.items())

# %% [markdown]
# ### Checking contents
# We can use the iterables above to check the contents of a dictionary.

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

print('banana' in fruit_colors.keys())
print('yellow' in fruit_colors.values())

# shortcut for checking key:
print('banana' in fruit_colors)

# check an entire key-value pair:
print(('banana', 'yellow') in fruit_colors.items())

# %% [markdown]
# ### Alternative ways to access elements
# - `dictionary.get(key)` returns value at key
#     - returns `None` if they key does not exist
#     - optional parameter: default return value
# - `dictionary.pop(key)` returns value of key, and deletes key.
#     - raises an error if the key does not exist
#     - optional parameter: default return value

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

print(fruit_colors.get('banana'))
print(fruit_colors.get('bnaana'))
print(fruit_colors.get('bnaana', 'yellow?'))

print(fruit_colors.pop('banana'))
print(fruit_colors)
print(fruit_colors.pop('banana', 'wait, what was banana again?'))

# %% [markdown]
# ## Exercise 10.1: Dictionaries

# %% [markdown]
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %%
{0: 0}

# %%
{'0': 0}

# %%
{1 + 2: 3 * 4}

# %%
{'1' + '2': {3: 'Hooray!'}}

# %%
programming_languages = {
    'Fortran': 1957,
    'Algol 60': 1960,
    'C': 1972,
    'Perl': 1987,
    'Python': 1991,
    'Julia': 2012,
    'Mojo': 2023,
}

# %%
programming_languages[Perl]

# %%
programming_languages[1960]

# %%
programming_languages['Perl']

# %%
{None: None}[None]

# %%
programming_languages.get('Per1', 2125)

# %%
programming_languages.get('Per1')

# %%
programming_languages.get('Python', None)

# %%
programming_languages.get('Python')

# %%
'Per1' in programming_languages

# %%
'Fortran' in programming_languages

# %%
2012 in programming_languages

# %%
programming_languages.update({'Per1': 2125, 'Raku': 2015})

# %%
2012 in programming_languages.values()

# %%
('Per1', 'Perl') in programming_languages.items()

# %%
del programming_languages[2012]

for language, year in programming_languages.items():
    print(f'{language} first appeared in {year}')

# %% [markdown]
# 2. The code below attempts to count the frequencies of the individual characters in our party invitation from module 6. There is a bug which prevents it from working. Fix the bug.

# %%
invitation = '''
    Dear Sheean,

    I hereby invite you for my Python party on the 11th of April.
    The bar will open at 2 PM. 🍸 Please bring pseudocode.

    Yours sincerely,
    Julian
'''

frequencies = {}
for character in invitation:
    count = frequencies.get(character, 0)
    frequencies.set(character, count + 1)
print(frequencies)

# %% [markdown]
# 3 . Below are two dictionaries containing information about different types of fruit. Print a nice message about each fruit stating its colour and price. For example, _An apple is red and costs € 2.50_, etc.

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
fruit_prices = {'apple': 2.50, 'banana': 2.10, 'orange': 1.50}

# your code here...

# %% [markdown]
# 4 . Here is a longer lists of fruit colours. Write a function `count_fruits` which gets a colour as input and returns the number of fruits that have that colour (according to `lots_of_fruit`).

# %%
# run this first!
lots_of_fruit = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange',
                 'cucumber': 'green', 'kiwi': 'green', 'strawberry': 'red',
                 'pineapple': 'yellow','blackberry': 'black', 'cherry': 'red',
                 'gooseberry': 'green', 'raspberry': 'red', 'mandarin': 'orange',
                 'lemon': 'yellow', 'lime': 'green'}

# %%

# your code here...

# let's see if it works!
assert count_fruits('red') == 4
assert count_fruits('lavender') == 0

# %% [markdown]
# 5 . The list `fruit_basket` contains a bunch of fruits. Can you make a dictionary `fruit_counts` which gives the amount for each fruit in `fruit_basket`? (Do not count the fruits by hand!)

# %%
fruit_basket = ['apple', 'banana', 'banana', 'banana', 'apple', 'orange',
                'orange', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape',
                'grape', 'grape', 'grape', 'pear', 'apple', 'strawberry',
                'strawberry', 'strawberry', 'orange']

# %%
# your code here..


# let's see if it works!
assert fruit_counts['apple'] == 3


# %% [markdown]
# 6 . Here is a different list, which contains the words in a sentence. Can you use your code above to make a dictionary `word_counts` telling us how often each word occurs? (Tip: if you need to do very similar tasks, make a function!)
#
# Write a function that takes a dictionary like `word_counts` tells us the most commonly occuring item and the count. Note that there can be multiple items that occurred the most.

# %%
# the variable sent0 contains the first sentence of The Catcher in the Rye
# split into single words
sent0 = ['If', 'you', 'really', 'want', 'to', 'hear', 'about', 'it,', 'the',
         'first', 'thing', 'you’ll', 'probably', 'want', 'to', 'know', 'is',
         'where', 'I', 'was', 'born,', 'and', 'what', 'my', 'lousy', 'childhood',
         'was', 'like,', 'and', 'how', 'my', 'parents', 'were', 'occupied',
         'and', 'all', 'before', 'they', 'had', 'me,', 'and', 'all', 'that',
         'David', 'Copperfield', 'kind', 'of', 'crap,', 'but', 'I', 'don’t',
         'feel', 'like', 'going', 'into', 'it,', 'if', 'you', 'want',
         'to', 'know', 'the', 'truth.']

# %%
# your code here...

# %% [markdown]
# ## Next module
#
# [11 - Working with files](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/11%20working%20with%20files.ipynb)
