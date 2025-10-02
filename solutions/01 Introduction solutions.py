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
# # Module 1: Introduction
#
# ## Exercise solutions
#
# [Module 1](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/01%20introduction.ipynb)
#
# ## CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)

# %% [markdown]
# ## Exercise 1.1: Try it out

# %%
print(1)
1

# %%
print('oops')
'oops'

# %% [markdown]
# The slight surprise in the above output is that `'oops'` is first printed without quotes, and then with quotes. `print` is meant to present data in a human-friendly way, so it strips quotes from text values (which we call strings). Bare values, on the other hand, are shown in the way in which you would type them into Python.

# %%
print()

# %% [markdown]
# You are allowed to call `print` without any value. This prints a newline.

# %%
print('apricot')
print('banana')
print('cherry')

# %%
'apricot'
'banana'
'cherry'

# %% [markdown]
# Normally, a bare value by itself is never shown. It is a special "service" of notebooks that the last value in a code block is shown. This is why we see only `'cherry'` and not `'apricot'` or `'banana'`.

# %%
# apricot
# banana
# cherry

# %% [markdown]
# Python ignores comments. From the perspective of Python, this code block is empty, so there is no output.

# %%
print('apricot')
'banana'
# cherry

# %%
# apricot
'banana'
print('cherry')

# %% [markdown]
# `'banana'` is not the last value in the code block, so it is not shown. `print('cherry')` has no value of itself (although it causes output); this is why we see only `cherry` and not this:
#
# ```
# cherry
# 'cherry'
# ```

# %%
print(#oops)

# %% [markdown]
# EOF stands for "end of file", with "file" here referring to the code block. Python reads `print(` and then ignores the rest of the line because of the comment. Every `(` should have a matching `)`, so Python is surprised that the code ends without that matching `)` (which it ignored because it is inside the comment).

# %%
print('apricot', 'banana')

# %% [markdown]
# You are allowed to pass more than one value to `print`. By default, it puts spaces between them. You can change the space into something else as follows:
#
# ```py
# # Use a comma instead of a space
# print('apricot', 'banana', sep=',')
#
# # Glue values together directly (no separator)
# print('apricot', 'banana', sep='')
# ```
#
# Use can use any separator you like, even very long strings.

# %% [markdown]
# ## Exercise 1.2: Hello, world!

# %%
# The following would work!
# (but only in a notebook)
'Hello, world!'

# %%
# This is slightly better.
print('Hello, world!')

# %% [markdown]
# ## Next module
#
# [2. Values and expressions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20Values%20and%20expressions.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/02%20Values%20and%20expressions%20solutions.ipynb)
