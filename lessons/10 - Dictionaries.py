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

# %% [markdown] id="kjdcNtg3k8Aa"
# # Dictionaries
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1kFvnhumJ0tOTzDVJnIvvMDRRJ19yk9ZS)
#
# Previous module: [9. String manipulation](https://colab.research.google.com/drive/19yTpFfp9uhBb-kAuOmSQY8_LrMtj8Goq#scrollTo=y5FcFvgypMfE)
#
# ### This module
#
# - Learn about _dictionaries_, a useful way of storing and looking up data

# %% [markdown] id="CtgPyDQ6lkT4"
# ## What are dictionaries?
#
# We have already seen one type of data structure, the _list_. Lists store values in a specific _order_, and we can retrieve values by their position in the list.

# %% id="OKs8GP5zk9bM"
fruits = ['apple', 'banana', 'orange']

assert fruits is not ['banana', 'apple', 'orange'] # order matters!

print(fruits[1])

# %% [markdown] id="OOyTxS6_mv2o"
# What if we want to store some extra information about each type of fruit? That is where dictionaries come in handy. Here I save the colour of each fruit.

# %% id="d0SFY-fil7-l"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

# %% [markdown] id="RiNPElB7nj2F"
# Some vocabulary: `'apple'`, `'banana'` and `'orange'` are _keys_ of the dictionary, while `'red'`, `'yellow'` and `'orange'` are _values_. Keys and values come in pairs: `'red'` is the value for the key `'apple'`. We'll see what we can do with this in a bit.
#
# Dictionaries need not contain strings. The values of a dictionary can be anything you want. The keys are a bit more restricted: strings, numbers, and tuples are fine, but complex data structures like lists and other dictionaries are not.

# %% id="ao56gCSxnhkS"
students_by_year = {2021: ['Julian', 'Jelte'], 2022: ['Julian', 'Jelte', 'Berit']}

years_per_student = {'Jelte': [2021, 2022], 'Julian': [2021, 2022], 'Berit': 2022}

# long dictionaries can be written on multiple lines, to keep it readable
dictionaries_by_topic = {
    'fruit': fruit_colors,
    'python course': [students_by_year, years_per_student]
}

# %% id="JgfCNNoHn3uR"
# this will be rejected
shared_interests = {['Julian', 'Jelte']: ['cats', 'programming'],
                    ['Jelte', 'Berit']: 'music'}

# %% [markdown] id="1tYs_3xBqx2e"
# The keys of a dictionary should be **unique**. If you try to write something with a key that already exists, it will overwrite the old value.

# %% id="TykfEB8iq4MQ"
unambiguous_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
ambiguous_colors = {'apple': 'green', 'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
assert ambiguous_colors == unambiguous_colors

print(ambiguous_colors)

# %% [markdown] id="_3J4oaBAsTGa"
# Order does not matter for dictionaries!

# %% id="pK0eYwsasBJ9"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
fruit_colors_2 = {'banana': 'yellow',  'apple': 'red', 'orange': 'orange'}

assert fruit_colors == fruit_colors_2

# %% [markdown] id="L56hdp03r9Q6"
# You can make emtpy dictionaries too.

# %% id="da-Re3sPsyYS"
empty = {} # a dictionary with no keys / values

new_dict = dict() # constructor function

# %% [markdown] id="nksJpi6mqgXY"
# ### Accessing
#
# With lists and tuples, we access elements with the index number. In dictionaries we access them by the key.

# %% id="SzxfzTANsjGN"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
students_by_year = {2021: ['Julian', 'Jelte'], 2022: ['Julian', 'Jelte', 'Berit']}

print(fruit_colors['apple'])
print(students_by_year[2021])

# %% [markdown] id="yL7NrEzwtm_r"
# ### Assiging / reassigning
#
# You can also assign or reassign values by the key. If the key is _not_ in the dictionary yet, it creates the key-value pair.

# %% id="HEOgD62xtPQj"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
fruit_colors['apple'] = 'red or green'
print(fruit_colors)

fruit_colors['kiwi'] = 'green'
print(fruit_colors)

# be aware that misspelling a key creates a new entry
fruit_colors['bnaana'] = 'yellwo'
print(fruit_colors)

# %% [markdown] id="zeJU8wt9uY2V"
# ### Updating
# Dictionaries can be *updated* with another dictionary. This is a way to quickly add multiple key-value pairs:
#
# - `dictionary.update(other_dictionary)`
# - this happens *in-place*, the function doesn't return anything

# %% id="pyxjqy31uWEs"
students_by_year = {2021: ['Julian', 'Jelte'], 2022: ['Julian', 'Jelte', 'Berit']}
more_students = {2023: ['Sheean', 'Mees', 'Luka'], 2024: ['Hopefully a lot']}

print(students_by_year.update(more_students))
print(students_by_year)

# %% [markdown] id="FvGfwcVjuwIY"
# ### Deleting
# To delete a key-value pair: `del dictionary[key]`

# %% id="72V_U4tUupnw"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
del fruit_colors['orange']
print(fruit_colors)

# %% [markdown] id="-kH7Vw3WvgFj"
# ### Iterables
# Dictionaries have a few useful functions:
# - `dictionary.keys()` returns a list of all keys
# - `dictionary.values()` returns a list of all values
# - `dictionary.items()` returns a list of tuples: `(key, value)`

# %% id="sNwzKYOAvk-d"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

# which types of fruit do we have information about?
print(fruit_colors.keys())

# which colors do we have?
print(fruit_colors.values())

# what's in the dictionary?
print(fruit_colors.items())

# %% [markdown] id="3oBW4bxgv5JV"
# ### Checking contents
# We can use the iterables above to check the contents of a dictionary.

# %% id="ESzsmJCXv7pl"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

print('banana' in fruit_colors.keys())
print('yellow' in fruit_colors.values())

# shortcut for checking key:
print('banana' in fruit_colors)

# check an entire key-value pair:
print(('banana', 'yellow') in fruit_colors.items())

# %% [markdown] id="x2nJsta6wRGQ"
# ### Alternative ways to access elements
# - `dictionary.get(key)` returns value at key
#     - returns `None` if they key does not exist
#     - optional parameter: default return value
# - `dictionary.pop(key)` returns value of key, and deletes key.
#     - raises an error if the key does not exist
#     - optional parameter: default return value

# %% id="11lfiYMiwTct"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

print(fruit_colors.get('banana'))
print(fruit_colors.get('bnaana'))
print(fruit_colors.get('bnaana', 'yellow?'))

print(fruit_colors.pop('banana'))
print(fruit_colors)
print(fruit_colors.pop('banana', 'wait, what was banana again?'))

# %% [markdown] id="1ezL-XhlvHBq"
# ## Exercise 10.1: Dictionaries

# %% [markdown] id="xrw8tjm9WqEb"
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% id="JpVUxXa8W-yN"
{0: 0}

# %% id="62bKQZhpXQOA"
{'0': 0}

# %% id="FW2sYBJdXXWl"
{1 + 2: 3 * 4}

# %% id="KFOPs4O7Xf9a"
{'1' + '2': {3: 'Hooray!'}}

# %% id="PkuZzIm1XngU"
programming_languages = {
    'Fortran': 1957,
    'Algol 60': 1960,
    'C': 1972,
    'Perl': 1987,
    'Python': 1991,
    'Julia': 2012,
    'Mojo': 2023,
}

# %% id="j20ZYa6bbSpq"
programming_languages[Perl]

# %% id="sZC-YucJaXCa"
programming_languages[1960]

# %% id="jlTtefX6aKii"
programming_languages['Perl']

# %% id="Y-7am56bacgD"
{None: None}[None]

# %% id="SFgsCOnpapTp"
programming_languages.get('Per1', 2125)

# %% id="bx0WNXq2a7K1"
programming_languages.get('Per1')

# %% id="9dqApt0ObCuz"
programming_languages.get('Python', None)

# %% id="msMNmeGWbKRS"
programming_languages.get('Python')

# %% id="_tzsbkN5bbi0"
'Per1' in programming_languages

# %% id="6JEZlfkPbhP9"
'Fortran' in programming_languages

# %% id="dOIxLmPqbvDA"
2012 in programming_languages

# %% id="bv1WFXRab0Bv"
programming_languages.update({'Per1': 2125, 'Raku': 2015})

# %% id="idVFrA21cLc5"
2012 in programming_languages.values()

# %% id="i07oWzu5cScu"
('Per1', 'Perl') in programming_languages.items()

# %% id="xatUSQBPcr4x"
del programming_languages[2012]

for language, year in programming_languages.items():
    print(f'{language} first appeared in {year}')

# %% [markdown] id="gw7W_KMcdVqD"
# 2. The code below attempts to count the frequencies of the individual characters in our party invitation from module 6. There is a bug which prevents it from working. Fix the bug.

# %% id="s_OeNugZfG4J"
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

# %% [markdown] id="rxcz60KQximW"
# 3 . Below are two dictionaries containing information about different types of fruit. Print a nice message about each fruit stating its colour and price. For example, _An apple is red and costs € 2.50_, etc.

# %% id="yn89oAAZu33C"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
fruit_prices = {'apple': 2.50, 'banana': 2.10, 'orange': 1.50}

# your code here...

# %% [markdown] id="Gtp5V9dE0LxK"
# 4 . Here is a longer lists of fruit colours. Write a function `count_fruits` which gets a colour as input and returns the number of fruits that have that colour (according to `lots_of_fruit`).

# %% id="S7gCNyLCxdrO"
# run this first!
lots_of_fruit = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange',
                 'cucumber': 'green', 'kiwi': 'green', 'strawberry': 'red',
                 'pineapple': 'yellow','blackberry': 'black', 'cherry': 'red',
                 'gooseberry': 'green', 'raspberry': 'red', 'mandarin': 'orange',
                 'lemon': 'yellow', 'lime': 'green'}

# %% id="nScDQipK35qN"

# your code here...

# let's see if it works!
assert count_fruits('red') == 4
assert count_fruits('lavender') == 0

# %% [markdown] id="-Qp6R3Kp3GId"
# 5 . The list `fruit_basket` contains a bunch of fruits. Can you make a dictionary `fruit_counts` which gives the amount for each fruit in `fruit_basket`? (Do not count the fruits by hand!)

# %% id="awf-lLQO3N1U"
fruit_basket = ['apple', 'banana', 'banana', 'banana', 'apple', 'orange',
                'orange', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape',
                'grape', 'grape', 'grape', 'pear', 'apple', 'strawberry',
                'strawberry', 'strawberry', 'orange']

# %% id="MDpIZpbm3-BG"
# your code here..


# let's see if it works!
assert fruit_counts['apple'] == 3


# %% [markdown] id="h-kJhTO951pc"
# 6 . Here is a different list, which contains the words in a sentence. Can you use your code above to make a dictionary `word_counts` telling us how often each word occurs? (Tip: if you need to do very similar tasks, make a function!)
#
# Write a function that takes a dictionary like `word_counts` tells us the most commonly occuring item and the count. Note that there can be multiple items that occurred the most.

# %% id="mdNug4ct5645"
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

# %% id="XGY3qSEk6B9j"
# your code here...

# %% [markdown] id="y5FcFvgypMfE"
# ## Next module
#
# [11 - Working with files](https://colab.research.google.com/drive/1KsFZV-jmfaQnCFevSxIZrd7chm3Z5CJo)
