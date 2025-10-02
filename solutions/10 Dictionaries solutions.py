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
# ### Exercise solutions
#
# [Module 10](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/10%20-%20Dictionaries.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [9. String manipulation](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/09%20string%20manipulation.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/09%20string%20manipulation%20solutions.ipynb)
#
# ### This module
#
# - Learn about _dictionaries_, a useful way of storing and looking up data

# %% [markdown]
# ## Exercise 10.1: Dictionaries

# %% [markdown]
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %%
{0: 0}

# %% [markdown]
# A dictionary with `0` as the only key and `0` its value. The dictionary as a whole is the last value in the cell, so the notebook echoes it to us.

# %%
{'0': 0}

# %% [markdown]
# Like the previous, but with the string `'0'` as key.

# %%
{1 + 2: 3 * 4}

# %% [markdown]
# Keys and values in a literal dictionary can be expressions. They are evaluated before being stored in the dictionary.

# %%
{'1' + '2': {3: 'Hooray!'}}

# %% [markdown]
# Dictionaries can be used as values in other dictionaries (but not as keys).

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

# %% [markdown]
# Assignments cause the variable to obtain a value as a side effect. The assignment itself has no result value, so we see no output. But the notebook will remember the `programming_languages` dictionary for us, so we can use it in the following code blocks.

# %%
programming_languages[Perl]

# %% [markdown]
# If you write a word without quotes, Python attempts to find a variable with that name. We did not define one, so we get a `NameError`.

# %%
programming_languages[1960]

# %% [markdown]
# `1960` is a value that appears in the dictionary, but the `[]` notation only looks for keys.

# %%
programming_languages['Perl']

# %% [markdown]
# Third try is a blessing! `'Perl'` is, indeed, a key that appears in the dictionary, and its associated value is `1987`.

# %%
{None: None}[None]

# %% [markdown]
# The notation is valid; `None` can be both a key and a value in a dictionary. The lookup is successful and returns `None`. Notebooks only echo the last value when it is **not** `None`, so we see no output.
#
# You can verify that there is a value by wrapping the entire expression in `print()`.

# %%
programming_languages.get('Per1', 2125)

# %% [markdown]
# Note that we wrote `'Per1'`, not `'Perl'`. See the difference? Because `'Per1'` is not in the dictionary, the default (fallback) value of `2125` is used.

# %%
programming_languages.get('Per1')

# %% [markdown]
# `'Per1'` is still not in the dictionary. Since we don't supply a default in this case, we get `None`, which produces no output.

# %%
programming_languages.get('Python', None)

# %% [markdown]
# `'Python'` is in the dictionary, so we get its associated value. The default of `None` is never used.

# %%
programming_languages.get('Python')

# %% [markdown]
# The result is the same as in the previous code block, because the default value is irrelevant.

# %%
'Per1' in programming_languages

# %% [markdown]
# There's that `'Per1'` again, which is not in the dictionary.

# %%
'Fortran' in programming_languages

# %% [markdown]
# `'Fortran'`, on the other hand, is in the dictionary, hence `True`.

# %%
2012 in programming_languages

# %% [markdown]
# `2012` is in the dictionary as a value but not as a key. `in` only looks for keys.

# %%
programming_languages.update({'Per1': 2125, 'Raku': 2015})

# %% [markdown]
# `update` changes `programming_languages` as a side effect. There is no return value, so we see no output.

# %%
2012 in programming_languages.values()

# %% [markdown]
# Since we query the `.values()` of `programming_languages`, `2012` is now found.

# %%
('Per1', 'Perl') in programming_languages.items()

# %% [markdown]
# When we look `in` a dictionary's `.items()`, we query `(key, value)` pairs. `('Per1', 2125)` would return `True` and so would `('Perl', 1987)`, but not `('Per1', 1987)` or `('Perl', 2125)`.

# %%
del programming_languages[2012]

for language, year in programming_languages.items():
    print(f'{language} first appeared in {year}')

# %% [markdown]
# The first line attempts to remove the `2012` key from the dictionary, but there is none. Hence a `KeyError`. If you comment out the first line, you will find that the loop prints a nice line for each programming language.

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
    # Here is the bug: dictionaries have a .get method, but no .set.
    #frequencies.set(character, count + 1)
    # The fix is to use assignment with a square bracket lookup.
    frequencies[character] = count + 1
print(frequencies)

# %% [markdown]
# 3 . Below are two dictionaries containing information about different types of fruit. Print a nice message about each fruit stating its colour and price. For example, _An apple is red and costs € 2.50_, etc.

# %%
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
fruit_prices = {'apple': 2.50, 'banana': 2.10, 'orange': 1.50}

# The example sentence includes 'a'/'an' ('an apple' / 'a banana')
# which was a bit of an oversight: the point of this exercise
# was to loop through a dictionary and access values.
# You could make a solution like this to avoid it.

for fruit in fruit_colors:
    color = fruit_colors[fruit]
    price = fruit_prices[fruit]

    print(fruit + 's', 'are', color, 'and cost €', price, sep=' ')

# Bonus points if you DID implement a solution on when to use
# 'a' or 'an'! Here is an example of your you can do that.

print()

def starts_with_vowel(word):
    '''
    Returns True if the word (a string) starts with a vowel.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        return True
    return False


for fruit in fruit_colors:
    color = fruit_colors[fruit]
    price = fruit_prices[fruit]

    if starts_with_vowel(fruit):
        article = 'An'
    else:
        article = 'A'

    print(article, fruit, 'is', color, 'and costs €', price, sep=' ')

# %% [markdown]
# 4 . Here is a longer lists of fruit colours. Write a function `count_fruits` which gets gets a colour as input and returns the number of fruits that have that colour (according to `lots_of_fruit`).

# %%
lots_of_fruit = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange',
                 'cucumber': 'green', 'kiwi': 'green', 'strawberry': 'red',
                 'pineapple': 'yellow','blackberry': 'black', 'cherry': 'red',
                 'gooseberry': 'green', 'raspberry': 'red', 'mandarin': 'orange',
                 'lemon': 'yellow', 'lime': 'green'}


# %%
def count_fruits(color):
    '''Count the number of fruits in `lots_of_fruit` that match this colour.'''
    count = 0
    for value in lots_of_fruit.values():
        if value == color:
            count = count + 1
    return count

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
def count_items(items):
    '''
    Count the items in a list.

    Input: a list of items, such as strings
    Output: a dictionary with the total of occurences for each item.
    '''

    counts = dict() # we will keep track of our counts in here!

    for item in items:
        # the current count: either the current value in the dictionary
        # or 0 if we haven't seen this fruit yet
        current_count = counts.get(item, 0)
        new_count = current_count + 1
        counts[item] = new_count

    return counts

fruit_counts = count_items(fruit_basket)

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
word_counts = count_items(sent0) # we recycle our function from the last exercise


# %%
def most_frequent(counts):
    '''
    For a dictionary with totals, the most commonly occuring item(s) and the count.

    Input should be a dictionary with the total number of occurences for each key in some collection.
    Returns a tuple of two items. First is a list of the most frequent item(s). If the input
    is an empty dict, the list if empty. Second is the number of occurences for that item.
    '''

    if not len(counts):
        return [], 0

    max_count = max(counts.values())

    top_items = []
    for item, count in counts.items():
        if count == max_count:
            top_items.append(item)

    return top_items, max_count

words, total = most_frequent(word_counts)
print(words, total)

# here are some assert statements you could use to check your own function
# feel free to adapt them if your function gives a different output format
assert most_frequent(fruit_counts) == (['grape'], 9)
assert most_frequent(word_counts) == (['and'], 4)
assert most_frequent({}) == ([], 0)

# %% [markdown]
# ## Next module
#
# [11 - Working with files](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/11%20working%20with%20files.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/11%20working%20with%20files%20solutions.ipynb)
