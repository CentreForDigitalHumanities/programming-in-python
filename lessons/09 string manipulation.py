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

# %% [markdown] id="7_SeGArbg7Ou"
# # Module 9: String Manipulation
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [8. Debugging](hthttps://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/08%20debugging.ipynb)
#
# ### This module
#
# - String utilities
# - Formatting strings

# %% [markdown] id="oadzHVRYh1PN"
# ## String utilities
# Python provides functions for common string operations. When working with text, these are very useful. Try to learn them by heart!

# %% [markdown] id="3KZGnQuWiM1X"
# ### Counting characters
#
# Strings are *iterables*, just like lists. We can use this information to quickly give us the length (number of characters) of a string:
# `len(string)`

# %% id="u-gFos5wii5k"
print(len('Matilda'))
print(len('The Catcher in the Rye'))

# %% [markdown] id="r0ZiGq36ipEo"
# ### Check for substrings
# Again wielding the knowledge about strings being *iterables*, we can use the `in` keyword to check if some sequence occurs in the string:
# `substring in string`

# %% id="yOOOzh3WjCGc"
print('a' in 'Matilda')
print('til' in 'Matilda')
print('in' in 'The Catcher in the Rye')

# %% [markdown] id="A4Wfxuj_jRAW"
# ### Casing
# Convert a string to lowercase or uppercase:
#
# `string.lower()` and `string.upper()`

# %% id="uErzYzBHjbND"
print('Matilda'.upper())
print('The Catcher in the Rye'.lower())

# %% [markdown] id="AsVvV-dtjxSD"
# ### Replacement
# Replace certain sequences with another sequence:
#
# `string.replace(replacement)`

# %% id="2iIwX0phj4Wt"
catcher = 'The Catcher in the Rye'
replaced = catcher.replace('e', '3')
print(replaced)

# optional parameter 'count'
replaced_max = catcher.replace('e', '3', 1)
print(replaced_max)

# %% [markdown] id="OQ07Frl4j_H_"
# ### Converting to list
# There are two ways to convert a string into a list:
# - `list(string)`
# - `string.split(separator)`
#
# The latter is more flexible, because it allows you to choose on which character the string should be split.

# %% id="xtsuwTrikrpk"
catcher = 'The Catcher in the Rye'
tabbed_catcher = catcher.replace(' ', '\t') # here we replace spaces by the tab character
sentence = 'This is some sentence that we wish to split into words.'

# use list()
print(list(catcher))

# using string.split()
# default: split on any whitespace
print(catcher.split())
print(tabbed_catcher.split())
print(sentence.split())

# optional parameter: separator
list_string = 'jelte,julian,berit'
print(list_string.split(','))

# any separator works, separator is not included in the result:
print(list_string.split('e'))

# %% [markdown] id="UM5FtDPBlBGx"
# ### Join an iterable into a string
# The reverse of splitting is of course also possible: take each element of an *iterable* (such as a list), and glue them together into a string. You can choose which character to put between each element:
#
# `string.join(iterable)`

# %% id="CqxglgPOlDfe"
words = ['The', 'Catcher', 'in', 'the', 'Rye']

# choose a string that should be put between the words
print(' '.join(words))
print(','.join(words))
print(''.join(words))

# %% id="z7p9kwjBlakE"
# split and join are opposites
sep = ' '
title = 'The Catcher in the Rye'
split_title = title.split(sep)
join_title = sep.join(split_title)
assert join_title == title

# %% [markdown] id="5hIj-tbVleEq"
# ## Exercise 9.1: String utilities
#
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% id="02q-FgvVlxEj"
print(len('two'))

# %% id="cvCrnnn9l-oH"
print(len(''))

# %% id="UlWWF0k7mA62"
assert 'A' in 'Matilda'

# %% id="Ui3gmvCNmHfB"
assert 'A' in 'Matilda'.upper()

# %% id="1tDEnzrumNdO"
name = 'Matilda'
assert name.upper() == 'MATILDA'

# %% id="BUpf6LglmZ4n"
name = 'Matilda'
assert name.upper().lower() == 'Matilda'

# %% id="sgfEH2jImlwz"
print('Matilda'.replace('ilda', 'ild4'))

# %% id="BEE94VVBmf7T"
print('Matilda'.replace('a', 4))

# %% id="BVKc0bQAnGYq"
list_of_words = ['I', 'ate', 'a', 'banana']
sentence = 'I ate a banana'

assert sentence.split() == list_of_words

# %% id="R4U_8kVtmpHE"
list_of_words = ['I', 'ate', 'a', 'banana']
sentence = 'I ate a banana'

assert ''.join(list_of_words) == sentence

# %% [markdown] id="Y34UdLQVQY_B"
# 2. In each of the code blocks below, replace each occurrence of `None` by an expression so that the assertions pass.

# %% id="CMOb-BiRQkVd"
name = 'Julian'
other_name = name.replace('Juli', None)
assert other_name == 'Sheean'

# %% id="gmAD4po2RIAo"
sentence1 = 'Edo won an argument about function parameters.'
sentence2 = 'To be or not to be, that is the question.'

def sentence_length(sentence):
    return None

assert sentence_length(sentence1) == 7
assert sentence_length(sentence2) == 10

# %% id="VXHa1AIMSZW-"
book_title = 'iteration, or how I did the loop thing'

words = []
for title_word in None: # use book_title
    # on the next line, use title_word twice
    capitalized_word = None + title_word[1:]
    words.append(capitalized_word)

capitalized_title = None # use words

assert capitalized_title == 'Iteration, Or How I Did The Loop Thing'

# %% [markdown] id="4dXMIBAUUk5T"
# 3. **BONUS** Write a function `bwian_speech`. Its parameter is any sentence. It should return the same sentence, but with selective replacements: the first occurrence of the character `r` after every comma should be replaced by `w`. If you succeed, challenge yourself to replace `R` by `W` as well.

# %% id="kT34vyPcVwNQ"
original = 'Do we have a prisoner by that name, "Brian"?'
bwianized = 'Do we have a prisoner by that name, "Bwian"?'

# your definition of bwian_speech here

assert bwian_speech(original) == bwianized

# %% [markdown] id="mRATbQdclrcX"
# ## Exercise 9.2: Additional utilities
# For each of the string functions below, find out what they do. If they take any parameters, describe what these do:
# - `string.startswith()`
# - `string.endswith()`
# - `string.strip()`
# - `string.lstrip()`
# - `string.rstrip()`
# - `string.title()`
# - `string.find()`
# - `string.split(',', x)` (describe what 'x' does. It should be a number)
#
#

# %% id="NyrzV4VGUJWK"

# %% [markdown] id="8YAcMdHpnuKw"
# ## String formatting
# We have seen a (not very convenient) way of building strings:

# %% id="pl5hfOYmnzF2"
name = 'Julian'
shoutout = 'Hey ' + name + '!'
print(shoutout)

# %% [markdown] id="SjWVj2R5n1XR"
# Luckily, there is a better (easier, more flexible) way: `string.format()`:
# - create a string with *placeholders*: `{}`
# - fill these placeholders with some value

# %% id="EQ9u1CX6n_TN"
shoutout_template = 'Hey {}!'
print(shoutout_template)

filled_template = shoutout_template.format('Sheean')
print(filled_template)

names = ['Julian', 'Sheean', 'Jelte', 'Mees']
for name in names:
    print(shoutout_template.format(name))

# %% [markdown] id="B1_gS-UaoEy0"
# ### Multiple placeholders
# Not limited to one placeholder, you can have an arbitrary amount

# %% id="8KMQfVXGoHq5"
shoutout_template = 'Hey {}! {}'
name = 'Julian'
followup = 'How are you?'

print(shoutout_template.format(name, followup))
print(shoutout_template.format(name))
print(shoutout_template.format(name, followup, 'Where are you going?'))

# %% [markdown] id="3lMa3IDjoMZP"
# ### Named placeholders
# Can also give placeholders names, and supply named parameters to `string.format()`.

# %% id="re9x0TNLoM4Q"
shoutout_template = 'Hey {name}! {followup}'
julian = 'Julian'
question = 'How are you?'

print(shoutout_template.format(name=julian, followup=question))
print(shoutout_template.format(followup=question, name=julian))
print(shoutout_template.format(followup=julian, name=question))

# %% [markdown] id="lxJqWxlRfIxd"
# ### F-strings
# Similar to placeholders, expressions can also be directly combined within a string by putting `f` in front of a string:

# %% id="ThZE6YnXfIxd"
name = 'Sheean'
weeks = 2
text = f'Hi {name}, your next appointment is in {weeks * 7} days.'

print(text)

# %% [markdown] id="avcqgDAAoq-w"
# ## Exercise 9.3: String formatting
#
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% id="BIa0VOX_owF4"
print('hey {}')

# %% id="81GUitOZo0l2"
print('hey {Julian}')

# %% id="96Dq4eSCpAji"
print('hey {}'.format('Julian'))

# %% id="h43fjzPco4V_"
print('hey {Julian}'.format('Julian'))

# %% id="wA18AIPKpFAH"
print('hey {name}'.format('Julian'))

# %% [markdown] id="PkBMT-kYiIqd"
# 2. Change each of the code blocks above so that it outputs `hey Edo`. You are **not** allowed to change the contents of the strings that start with `'hey`!

# %% [markdown] id="ArVJo3y0jJ8T"
# 3. What do you think the following piece of code will do? Try it out. Can you explain the result?

# %% id="iAkugK6wjqfl"
name = 'Jill'
welcome = 'welcome, {}'.format
goodbye = 'farewell, {}'.format
connect = '; '.join

print(connect((welcome(name), goodbye(name))))

# %% [markdown] id="y5FcFvgypMfE"
# ## Next module
#
# [10 - Dictionaries](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/10%20-%20Dictionaries.ipynb)
