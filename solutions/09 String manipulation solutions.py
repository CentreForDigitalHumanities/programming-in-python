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
# # Module 9: String manipulation
#
# ### Exercise solutions
#
# [Module 9](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/09%20string%20manipulation.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [8. Debugging](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/08%20debugging.ipynb)
#
# ### This module
#
# - Storing code in a variable so you can reuse it.
# - Being explicit about the purpose of your code.

# %% [markdown]
# ## Exercise 9.1: String Utilities
#
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %%
print(len('two'))

# %% [markdown]
# A string is an iterable, the `len` is the amount of elements (characters)

# %%
print(len(''))

# %% [markdown]
# An empty string (just like an empty list) has length of 0.

# %%
assert 'A' in 'Matilda'

# %% [markdown]
# Python is case sensitive. The capitalized `A` is not in the string.

# %%
assert 'A' in 'Matilda'.upper()

# %% [markdown]
# After capitalization of the whole string, `A` is in there.

# %%
name = 'Matilda'
assert name.upper() == 'MATILDA'

# %% [markdown]
# This is the definition of `string.upper()`

# %%
name = 'Matilda'
assert name.upper().lower() == 'Matilda'

# %% [markdown]
# This does not work. `Matilda.upper()` equals `'MATILDA'`.
#
# `'MATILDA'.lower()` equals `'matilda'`. The first captilal is lost in translation.

# %%
print('Matilda'.replace('ilda', 'ild4'))

# %% [markdown]
# `string.replace()` is not limited to single characters

# %%
print('Matilda'.replace('a', 4))

# %% [markdown]
# We can only replace strings with other strings. `'Matilda'.replace('a', '4')` would work

# %%
list_of_words = ['I', 'ate', 'a', 'banana']
sentence = 'I ate a banana'

assert sentence.split() == list_of_words

# %% [markdown]
# `string.split()` splits on all whitespace characters by default

# %%
list_of_words = ['I', 'ate', 'a', 'banana']
sentence = 'I ate a banana'

assert ''.join(list_of_words) == sentence

# %% [markdown]
# We join the words on the empty string, and not on a space. Thus, the resulting sentence contains all the words concatenated.

# %% [markdown]
# 2. In each of the code blocks below, replace each occurrence of `None` by an expression so that the assertions pass.

# %%
name = 'Julian'
other_name = name.replace('Juli', 'Shee') # ANSWER: 'Shee'
assert other_name == 'Sheean'

# %%
sentence1 = 'Edo won an argument about function parameters.'
sentence2 = 'To be or not to be, that is the question.'

def sentence_length(sentence):
    # First, we turn the string into a list of words.
    # Then, we take the length of that list.
    return len(sentence.split())

assert sentence_length(sentence1) == 7
assert sentence_length(sentence2) == 10

# %%
book_title = 'iteration, or how I did the loop thing'

words = []
for title_word in book_title.split(): # split, again
    # First character capitalized, plus remainder unmodified
    capitalized_word = title_word[0].upper() + title_word[1:]
    words.append(capitalized_word)

capitalized_title = ' '.join(words) # after split comes join

assert capitalized_title == 'Iteration, Or How I Did The Loop Thing'

# %% [markdown]
# 3. **BONUS** Write a function `bwian_speech`. Its parameter is any sentence. It should return the same sentence, but with selective replacements: the first occurrence of the character `r` after every comma should be replaced by `w`. If you succeed, challenge yourself to replace `R` by `W` as well.

# %%
original = 'Do we have a prisoner by that name, "Brian"?'
bwianized = 'Do we have a prisoner by that name, "Bwian"?'

# One possible way to do it, does not convert R to W.
# We explicitly visit every character.
def bwian_speech(text):
    """ Replace first occurrence of 'r' after every comma by 'w'. """
    # We keep track of whether we have seen a comma.
    # Initially, this is not the case.
    comma_seen = False
    # The string that will contain our result, initially empty.
    result = ''
    # Let's roll!
    for character in text:
        # We first check whether we have an 'r', because in all
        # other cases, we copy the character verbatim.
        if character == 'r' and comma_seen:
            # If you want to take uppercase R into account, you can add
            # some calculations with ord() and chr() here.
            result = result + 'w'
            # We replace only the first occurrence of 'r' after each
            # comma, so we now need to forget that we saw it.
            comma_seen = False
        else:
            result = result + character
            # Did you wonder when we would set comma_seen to True?
            # It's here.
            if character == ',':
                comma_seen = True
    return result

assert bwian_speech(original) == bwianized

# %%
original = 'Do we have a prisoner by that name, "Brian"?'
bwianized = 'Do we have a prisoner by that name, "Bwian"?'
original2 = 'Do we have a prisoner by that name, "Robert"?'
bwianized2 = 'Do we have a prisoner by that name, "Wobert"?'

# A quite different way to do it, based on string splitting.
# This one does consider both 'r' and 'R', and correctly converts
# only the first of those two that occurs.
def bwian_speech(text):
    """ Replace the first occurrence of 'r' after every comma by 'w'.

    Recognizes uppercase 'R' as well, and replaces only the first
    occurrence of either 'r' or 'R'. """
    # We first split the text in chunks between commas. The first chunk
    # is at the start of the text, the other chunks follow a comma.
    comma_chunks = text.split(',')
    # We make a new list of chunks that we will rejoin with commas at the end.
    # Since the first chunk is before any comma, we can already copy it.
    output_chunks = comma_chunks[:1]
    # Now, we loop over the remaining chunks in order to replace
    # first occurrences of 'r' or 'R'.
    for chunk in comma_chunks[1:]:
        # We split the chunk into at most two parts:
        # one before the first 'r' and maybe one after it.
        r_chunks = chunk.split('r', 1)
        # However, we do not know yet whether that 'r' should be replaced
        # by a 'w', because there might be a 'R' before it. To find out,
        # we simply try to replace such an 'R' and then compare.
        R_replaced = r_chunks[0].replace('R', 'W', 1)
        if R_replaced == r_chunks[0]:
            # Nothing changed, so 'R' was not in the first chunk.
            # We now know that we should be replacing the first 'r'.
            output_chunks.append('w'.join(r_chunks))
        else:
            # We already replaced the first 'R' by 'W', so we should not
            # replace any 'r' after it by 'w'.
            r_chunks[0] = R_replaced
            output_chunks.append('r'.join(r_chunks))
    # At this point, we have a list of chunks that all have their first
    # occurrence or 'r' or 'R' replaced. All that is left to do is to
    # glue them back together with commas.
    return ','.join(output_chunks)

assert bwian_speech(original) == bwianized
assert bwian_speech(original2) == bwianized2

# %% [markdown]
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

# %%
# string.startswith(substring) checks if a string starts with a substring
assert 'matilda'.startswith('mat')

# string.endswith(substring) checks if a string ends with a substring
assert 'matilda'.endswith('lda')

# string.strip() removes whitespace from the start and end of a string
# as an optional parameter, takes a string and removes only characters in that string
assert '   matilda '.strip() == 'matilda'
assert '..matilda?'.strip('.,') == 'matilda?'

# string.lstrip() and string.rstrip() work like string.strip()
# but only for l(eft) and r(ight) part of the string
assert '  matilda  '.rstrip() == '  matilda'
assert '  matilda  '.lstrip() == 'matilda  '

# string.title() converts a string to title case: each word starts with a capital
assert 'MATILDA by roald DaHl'.title() == 'Matilda By Roald Dahl'

# string.find(substring) returns the starting character of the substring
# if the substring is not found, return -1
assert 'matilda'.find('il') == 3

# string.split(separator, x) splits a string x times
# after x splits have been made, the rest of the string is left intact
assert 'Matilda by Roald Dahl'.split(' ', 2) == ['Matilda', 'by', 'Roald Dahl']

# %% [markdown]
# ## Exercise 9.3: String formatting
#
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %%
print('hey {}')

# %% [markdown]
# Using `{}` in a string with `.format()` leaves the curly brackets untouched.

# %%
print('hey {Julian}')

# %% [markdown]
# Again, without `.format()`, the string is untouched

# %%
print('hey {}'.format('Julian'))

# %% [markdown]
# Calling `.format()` fills the placeholders

# %%
print('hey {Julian}'.format('Julian'))

# %% [markdown]
# This doesn't work, the names placeholder expects a named parameter.
#
# `'hey {Julian}'.format(Julian='julian')` would work

# %%
print('hey {name}'.format('Julian'))

# %% [markdown]
# Same as above

# %% [markdown]
# 2. Change each of the code blocks above so that it outputs `hey Edo`. You are **not** allowed to change the contents of the strings that start with `'hey`! *The solutions are contained in the copies **below**.*

# %%
# for the first one, just add .format
print('hey {}'.format('Edo'))

# %%
# For this one, you need a named argument.
print('hey {Julian}'.format(Julian='Edo'))

# %%
# You are not allowed to change the string starting with 'hey',
# but you are allowed to change the argument to .format!
# This solution ends up being the same as the first.
print('hey {}'.format('Edo'))

# %%
# This one is the same as the second solution.
print('hey {Julian}'.format(Julian='Edo'))

# %%
# For this one, you need a named argument with the key "name",
# AND you need to change the value of the argument.
print('hey {name}'.format(name='Edo'))

# %% [markdown]
# 3. What do you think the following piece of code will do? Try it out. Can you explain the result?

# %%
name = 'Jill'
welcome = 'welcome, {}'.format
goodbye = 'farewell, {}'.format
connect = '; '.join

print(connect((welcome(name), goodbye(name))))

# %% [markdown]
# This one is quite advanced. If you are surprised, it is probably because so far, we have only seen this notation:
#
# ```py
# 'welcome, {}'.format(name)
# ```
#
# In the exercise, the last part with the parentheses `(name)` was left out. Instead, we assign the first part `'welcome, {}'.format` to a variable `welcome`. As it turns out, that variable contains a function, because we can later call it (`welcome(name)` on line 6). In a way, we did a sort of postponed function call.
#
# How does this work? In short, `'welcome, {}'.format` is an expression that returns a function. `format` by itself is a function that requires both a format string and any number of values to interpolate. The notation
#
# ```py
# 'welcome, {}'.format(name)
# ```
#
# basically means the same as if we had a free-standing `format` function that we call like this:
#
# ```py
# format('welcome, {}', name)
# ```
#
# When we omit the `(name)` at the end, we basically tell Python to remember the first argument and wait for the rest. This is called *partial application*.
#
# Python supports this trick for all methods on all values. This is why we could repeat the trick on lines 3 and 4.

# %% [markdown]
# ## Next module
#
# [10. Dictionaries](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/10%20Dictionaries.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/10%20Dictionaries%20solutions.ipynb)
