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
# # Module 9: String manipulation
#
# ### Exercise solutions
#
# [Module 9](https://colab.research.google.com/drive/19yTpFfp9uhBb-kAuOmSQY8_LrMtj8Goq)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1kFvnhumJ0tOTzDVJnIvvMDRRJ19yk9ZS)
#
# Previous module: [8. Debugging](https://colab.research.google.com/drive/1Rj6qEuT3BFcQwexAxKg3zbAAD6t1cc8p)
#
# ### This module
#
# - Storing code in a variable so you can reuse it.
# - Being explicit about the purpose of your code.

# %% [markdown] id="5hIj-tbVleEq"
# ## Exercise 9.1: String Utilities
#
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% id="02q-FgvVlxEj"
print(len('two'))

# %% [markdown] id="dZ8S2UialXke"
# A string is an iterable, the `len` is the amount of elements (characters)

# %% id="cvCrnnn9l-oH"
print(len(''))

# %% [markdown] id="6vDjjHzIlcEY"
# An empty string (just like an empty list) has length of 0.

# %% id="UlWWF0k7mA62"
assert 'A' in 'Matilda'

# %% [markdown] id="K_daSu19liik"
# Python is case sensitive. The capitalized `A` is not in the string.

# %% id="Ui3gmvCNmHfB"
assert 'A' in 'Matilda'.upper()

# %% [markdown] id="i2bI-L6glqzO"
# After capitalization of the whole string, `A` is in there.

# %% id="1tDEnzrumNdO"
name = 'Matilda'
assert name.upper() == 'MATILDA'

# %% [markdown] id="1pbJz3qElujM"
# This is the definition of `string.upper()`

# %% id="BUpf6LglmZ4n"
name = 'Matilda'
assert name.upper().lower() == 'Matilda'

# %% [markdown] id="Rq3LXgkMlywN"
# This does not work. `Matilda.upper()` equals `'MATILDA'`.
#
# `'MATILDA'.lower()` equals `'matilda'`. The first captilal is lost in translation.

# %% id="sgfEH2jImlwz"
print('Matilda'.replace('ilda', 'ild4'))

# %% [markdown] id="GhUlBMfPmGb3"
# `string.replace()` is not limited to single characters

# %% id="BEE94VVBmf7T"
print('Matilda'.replace('a', 4))

# %% [markdown] id="qsPQT5VGlNZ2"
# We can only replace strings with other strings. `'Matilda'.replace('a', '4')` would work

# %% id="BVKc0bQAnGYq"
list_of_words = ['I', 'ate', 'a', 'banana']
sentence = 'I ate a banana'

assert sentence.split() == list_of_words

# %% [markdown] id="xdueWI-yk_ME"
# `string.split()` splits on all whitespace characters by default

# %% id="R4U_8kVtmpHE"
list_of_words = ['I', 'ate', 'a', 'banana']
sentence = 'I ate a banana'

assert ''.join(list_of_words) == sentence

# %% [markdown] id="ZpepgX5Lk0Mk"
# We join the words on the empty string, and not on a space. Thus, the resulting sentence contains all the words concatenated.

# %% [markdown] id="Y34UdLQVQY_B"
# 2. In each of the code blocks below, replace each occurrence of `None` by an expression so that the assertions pass.

# %% id="CMOb-BiRQkVd" executionInfo={"status": "ok", "timestamp": 1715696821132, "user_tz": -120, "elapsed": 3, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
name = 'Julian'
other_name = name.replace('Juli', 'Shee') # ANSWER: 'Shee'
assert other_name == 'Sheean'

# %% id="gmAD4po2RIAo" executionInfo={"status": "ok", "timestamp": 1715696871810, "user_tz": -120, "elapsed": 452, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
sentence1 = 'Edo won an argument about function parameters.'
sentence2 = 'To be or not to be, that is the question.'

def sentence_length(sentence):
    # First, we turn the string into a list of words.
    # Then, we take the length of that list.
    return len(sentence.split())

assert sentence_length(sentence1) == 7
assert sentence_length(sentence2) == 10

# %% id="VXHa1AIMSZW-" executionInfo={"status": "ok", "timestamp": 1715697085419, "user_tz": -120, "elapsed": 409, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
book_title = 'iteration, or how I did the loop thing'

words = []
for title_word in book_title.split(): # split, again
    # First character capitalized, plus remainder unmodified
    capitalized_word = title_word[0].upper() + title_word[1:]
    words.append(capitalized_word)

capitalized_title = ' '.join(words) # after split comes join

assert capitalized_title == 'Iteration, Or How I Did The Loop Thing'

# %% [markdown] id="4dXMIBAUUk5T"
# 3. **BONUS** Write a function `bwian_speech`. Its parameter is any sentence. It should return the same sentence, but with selective replacements: the first occurrence of the character `r` after every comma should be replaced by `w`. If you succeed, challenge yourself to replace `R` by `W` as well.

# %% id="kT34vyPcVwNQ" executionInfo={"status": "ok", "timestamp": 1715698315133, "user_tz": -120, "elapsed": 226, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
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

# %% id="Mbps1JIeh8cS" executionInfo={"status": "ok", "timestamp": 1715699637307, "user_tz": -120, "elapsed": 355, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
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

# %% [markdown] id="Xbi4ATS0mQzp"
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

# %% id="ZYHALHE7mU4-"
# string.startswith(substring) checks if a string starts with a substring
assert 'matilda'.startswith('mat')

# string.endswith(substring) checks if a string ends with a substring
assert 'matilda'.endswith('lda')

# string.strip() removes whitespace from the start and end of a string
# as an optional parameter, takes a string and removes only characters in that string
assert '   matilda '.strip() == 'matilda'
assert '..matilda?'.strip('.,') == 'matilda?'

# string.lstrip() and string.rstrip() work like string.split()
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

# %% [markdown] id="avcqgDAAoq-w"
# ## Exercise 9.3: String formatting
#
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 7, "status": "ok", "timestamp": 1681825929769, "user": {"displayName": "Jelte van Boheemen", "userId": "01262930844892157638"}, "user_tz": -120} id="BIa0VOX_owF4" outputId="ddc080fa-bf11-4064-c5f4-efcbef9b9a64"
print('hey {}')

# %% [markdown] id="SDnzz_IYoqRP"
# Using `{}` in a string with `.format()` leaves the curly brackets untouched.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 3, "status": "ok", "timestamp": 1681825932026, "user": {"displayName": "Jelte van Boheemen", "userId": "01262930844892157638"}, "user_tz": -120} id="81GUitOZo0l2" outputId="6be221d0-52b7-47f9-8269-991811402ff7"
print('hey {Julian}')

# %% [markdown] id="-HFk3OAAoyyy"
# Again, without `.format()`, the string is untouched

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 267, "status": "ok", "timestamp": 1681825967240, "user": {"displayName": "Jelte van Boheemen", "userId": "01262930844892157638"}, "user_tz": -120} id="96Dq4eSCpAji" outputId="7e3086d7-4e02-4b98-d96e-d91257f65fb5"
print('hey {}'.format('Julian'))

# %% [markdown] id="OFmrf_lto6_k"
# Calling `.format()` fills the placeholders

# %% id="h43fjzPco4V_"
print('hey {Julian}'.format('Julian'))

# %% [markdown] id="XP3dKwEXpAir"
# This doesn't work, the names placeholder expects a named parameter.
#
# `'hey {Julian}'.format(Julian='julian')` would work

# %% id="wA18AIPKpFAH"
print('hey {name}'.format('Julian'))

# %% [markdown] id="LI43JmY2pcIg"
# Same as above

# %% [markdown] id="PkBMT-kYiIqd"
# 2. Change each of the code blocks above so that it outputs `hey Edo`. You are **not** allowed to change the contents of the strings that start with `'hey`! *The solutions are contained in the copies **below**.*

# %% id="rHlCJXILrOfX"
# for the first one, just add .format
print('hey {}'.format('Edo'))

# %% id="zBrCVWsErOfZ"
# For this one, you need a named argument.
print('hey {Julian}'.format(Julian='Edo'))

# %% id="g8KtBFyirOfa"
# You are not allowed to change the string starting with 'hey',
# but you are allowed to change the argument to .format!
# This solution ends up being the same as the first.
print('hey {}'.format('Edo'))

# %% id="FdoISOiWrOfb"
# This one is the same as the second solution.
print('hey {Julian}'.format(Julian='Edo'))

# %% id="EnizWx77rOfc"
# For this one, you need a named argument with the key "name",
# AND you need to change the value of the argument.
print('hey {name}'.format(name='Edo'))

# %% [markdown] id="ArVJo3y0jJ8T"
# 3. What do you think the following piece of code will do? Try it out. Can you explain the result?

# %% id="iAkugK6wjqfl" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715700086149, "user_tz": -120, "elapsed": 294, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="bb998fe7-45dc-4ad0-9a2b-04bc2faff77a"
name = 'Jill'
welcome = 'welcome, {}'.format
goodbye = 'farewell, {}'.format
connect = '; '.join

print(connect((welcome(name), goodbye(name))))

# %% [markdown] id="OLzxrMb9svd_"
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

# %% [markdown] id="Dntbbioh29xm"
# ## Next module
#
# [10. Dictionaries](https://colab.research.google.com/drive/1w2s28vLo26hzppP0Z-kSqniU2eoXJNU3) - [solutions](https://colab.research.google.com/drive/1ZvLc2Jrkh9uosmliA8IpT4q7YE-amvkW)
