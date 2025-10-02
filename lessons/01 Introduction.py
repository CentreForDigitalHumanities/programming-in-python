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
# ## CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# ## Welcome!
#
# ## Who are we?
#
# - Developers at the Centre for Digital Humanities (CDH)
#
# ## Who are you?
#
# - Entry level course, no previous experience required
# - If you have some experience, parts of the course may be familiar. Challenge yourself with some difficult exercises!
#
# ## Goals
#
# - Introduce the basics of the Python programming language
# - Write simple computer programs
# - Simple data analysis on your own data
# - Teach good practices that you can apply to all your future programming, and make you a self-reliant programmer
#
# ## Colab Notebooks
#
# - Runs Python code in your web browser, no installing required
# - If you do not have a Google account, please make one
# - Presenting straight from Colab, so you can follow our example
# - Copy the notebooks to edit them, instructions in exercise 1

# %% [markdown]
# ## Python
#
# - Programming language
# - Invented by Guido van Rossum (former Benevolent Dictator For Life) in 1989
# - *High level*
#     - Far removed from machine language
#     - Written in C (slightly lower level)
# - Designed to be readable
# - Many versions, currently on major version 3.

# %% [markdown]
# ### Why learn Python?
#
# - (Relatively) easy to learn
# - Widely used
#     - Easy to install and run on a variety of platforms
#     - Many resources available
# - Many good packages and libraries available

# %% [markdown]
# ## Notebooks 101
#
# Let's get started!

# %% [markdown]
# ### Copy a notebook to your own Google Drive
#
# You can only run code in this notebook, not edit it. To edit it, you need to copy it to [your own Google Drive](https://drive.google.com) first.
#
# To do so, click on the *File* menu and choose the ninth option from the top: *Save a copy in Drive*. You can now find the copy in your drive, in the directory *Colab Notebooks*.
#
# Tip: give it a recognizable name (e.g. `Module 1 - my solutions`).
#

# %% [markdown]
# ### Adjust some settings
#
# Open the *Settings*, in the *Tools* menu or by clicking the cogwheel icon in the top right. Open the *Editor* section.
#
# - Set *Indentation width in spaces* to **4**.
# - Switch *Show line numbers* **on**.
#
# In the *AI Assistance* section:
# - Switch "Show AI-powered inline completions" **off**.
# - Switch "Consented to use generative AI features" **off**.
#
# The other settings are up to you.

# %% [markdown]
# ### Execute Python code
#
# Press the triangle icon in the top left corner of a code block to run it, *OR* type **ctrl-enter** when the text cursor is in the code block. Type **ctrl-shift-enter** to run only the current line.
#
# If you open a notebook for the first time, or if you have not run any code for a while, it takes a while before you see a result.

# %%
print('Hello')
print('Goodbye')

# %% [markdown]
# ## Python 101

# %% [markdown]
# ### `print`
#
# In the previous code block, we saw the `print` function in action. It causes Python to "talk" to us.

# %% [markdown]
# ### Values
#
# Between the parentheses `( )` of the `print` function, we put the *value* that we want Python to show. We can also write the value without passing it to `print`.

# %%
'Hello'

# %% [markdown]
# A bare value does not always cause output. We will explore this in the first exercise.

# %% [markdown]
# ### Comments
#
# A comment starts with a hash `#` and runs until the end of the line. Python ignores comments. You can use them as notes for yourself and for other programmers.

# %%
# Python will not look here!

print('Hello') # comments can start after code

# %% [markdown]
# Use comments to explain *why* your code was written the way it is. You will be grateful to yourself when you read your own code after a few weeks!

# %%
# Useless comment:

# Print "Hello".
print('Hello')


# Useful comment:

# Everyone writes "Hello" in this exercise, but
# I prefer something a little bit more British.
print('How do you do?')

# %% [markdown]
# ## Exercise 1.1: Try it out
#
# Read each of the code blocks below. Try to predict what it will do, then run the block to check your prediction.
#
# Do you see any (subtle or not-so subtle) surprises? Can you explain them?

# %%
print(1)
1

# %%
print('oops')
'oops'

# %%
print()

# %%
print('apricot')
print('banana')
print('cherry')

# %%
'apricot'
'banana'
'cherry'

# %%
# apricot
# banana
# cherry

# %%
print('apricot')
'banana'
# cherry

# %%
# apricot
'banana'
print('cherry')

# %%
print(#oops)

# %%
print('apricot', 'banana')

# %% [markdown]
# ## Exercise 1.2: Hello, world!
#
# The classic way to demonstrate a programming language's syntax is the hello world-program. This is the minimal amount of code required to output the text "Hello, world!" to the user.  
#
# Write a hello world-program for Python.

# %%
# Your solution here

# %% [markdown]
# ## Next module
#
# [2. Values and expressions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20values%20and%20expressions.ipynb)
