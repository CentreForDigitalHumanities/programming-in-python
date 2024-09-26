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
# [Module 9](https://colab.research.google.com/drive/15djL6RWOHmSo7rpQMOLE1ga9bICxBLmm)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1YgmnpA7tRylvGBpp2PTFGvSV2P8tw5jl)
#
# Previous module: [8. Debugging](https://colab.research.google.com/drive/1r6wuOuEHabI0vmBg15HVFBLiNKRb-jnS)
#
# ### This module
#
# - Storing code in a variable so you can reuse it.
# - Being explicit about the purpose of your code.

# %% [markdown] id="5hIj-tbVleEq"
# ## Exercise 9.1: String Utilities
# In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

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
# In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

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

# %% [markdown] id="Dntbbioh29xm"
# ## Next module
#
# [10. Dictionaries](https://colab.research.google.com/drive/1Dssqf65thuWCNZ9I3ezaawelaWpeaWoj) - [solutions](https://colab.research.google.com/drive/1j1hikQCS3Px0_q4hguuIqWSXSmyKcAiN)
