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

# %% [markdown] id="Buvh9v-iYeOO"
# # Module 1: Introduction
# ## CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1s05aR4wn2dU1C3se1oXfqKz2EY5ilrno)
#
# ## Welcome!
#
# ## Who are we?
#
# - Julian Gonggrijp, Sheean Spoel, Jelte van Boheemen, Luka van der Plas, Mees van Stiphout
# - Developers at the Digital Humanities Lab
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

# %% [markdown] id="STQf1EROV-4I"
# ## Python
#
# - Programming language
# - Invented by Guido van Rossum (former Benevolent Dictator For Life) in 1989
# - *High level*
#     - Far removed from machine language
#     - Written in C (slightly lower level)
# - Designed to be readable
# - Many versions, currently on major version 3.

# %% [markdown] id="rC4AwjL06k0q"
# ### Why learn Python?
#
# - (Relatively) easy to learn
# - Widely used
#     - Easy to install and run on a variety of platforms
#     - Many resources available
# - Many good packages and libraries available

# %% [markdown] id="xyNb4mPMcQCd"
# ## Notebooks 101
#
# Let's get started!

# %% [markdown] id="4lc8nYpP9mtf"
# ### Copy a notebook to your own Google Drive
#
# You can only run code in this notebook, not edit it. To edit it, you need to copy it to [your own Google Drive](https://drive.google.com) first.
#
# To do so, click on the *File* menu and choose the ninth option from the top: *Save a copy in Drive*. You can now find the copy in your drive, in the directory *Colab Notebooks*.
#
# Tip: give it a recognizable name (e.g. `Module 1 - my solutions`).
#

# %% [markdown] id="8zoSNQtC_6_v"
# ### Adjust some settings
#
# Open the *Settings*, in the *Tools* menu or by clicking the cogwheel icon in the top right. Open the *Editor* section.
#
# - Set *Indentation width in spaces* to **4**.
# - Switch *Show line numbers* **on**.
#
# The other settings are up to you.

# %% [markdown] id="qtRYKOWnB5Wl"
# ### Execute Python code
#
# Press the triangle icon in the top left corner of a code block to run it, *OR* type **ctrl-enter** when the text cursor is in the code block. Type **ctrl-shift-enter** to run only the current line.
#
# If you open a notebook for the first time, or if you have not run any code for a while, it takes a while before you see a result.

# %% id="MdA4_KyrDAsf"
print('Hello')
print('Goodbye')

# %% [markdown] id="AoBoZqIeFEru"
# ## Python 101

# %% [markdown] id="ZOqgk7VAFKnJ"
# ### `print`
#
# In the previous code block, we saw the `print` function in action. It causes Python to "talk" to us.

# %% [markdown] id="NOtudpGlFe78"
# ### Values
#
# Between the parentheses `( )` of the `print` function, we put the *value* that we want Python to show. We can also write the value without passing it to `print`.

# %% id="in8WoUafGEyK"
'Hello'

# %% [markdown] id="BHQPB7LuQ1mf"
# A bare value does not always cause output. We will explore this in the first exercise.

# %% [markdown] id="Src0ZdRKGHtl"
# ### Comments
#
# A comment starts with a hash `#` and runs until the end of the line. Python ignores comments. You can use them as notes for yourself and for other programmers.

# %% id="ssP4GWUOIxWS"
# Python will not look here!

print('Hello') # comments can start after code

# %% [markdown] id="YxXeF4u5I2c_"
# Use comments to explain *why* your code was written the way it is. You will be grateful to yourself when you read your own code after a few weeks!

# %% id="nMTlvlbbJUWu"
# Useless comment:

# Print "Hello".
print('Hello')

# Useful comment:

# Everyone writes "Hello" in this exercise, but
# I prefer something a little bit more British.
print('How do you do?')

# %% [markdown] id="ZhgCPUNTLIZX"
# ### `pass`
#
# You can write `pass` to do nothing. It behaves almost like a comment, but isn't. It is sometimes useful as a placeholder, as we will see later on in the course.

# %% id="oS7kfP3OLtJn"
pass

# %% [markdown] id="pKIEfocbMaIR"
# ## Exercise 1.1: Try it out
#
# Read each of the code blocks below. Try to predict what it will do, then run the block to check your prediction.
#
# Do you see any (subtle or not-so subtle) surprises? Can you explain them?

# %% id="6hlNxRNNM1fV"
print(1)
1

# %% id="VIm6FdRIM6OE"
print('oops')
'oops'

# %% id="_MN48xz5NAya"
print()

# %% id="g9WKeIA2NVIA"
print('apricot')
print('banana')
print('cherry')

# %% id="NCbCfbHaNafJ"
'apricot'
'banana'
'cherry'

# %% id="-ZuiJ92yNqpi"
# apricot
# banana
# cherry

# %% id="b9bTbrNSNwwn"
print('apricot')
'banana'
# cherry

# %% id="GYmcSm6iOAiA"
# apricot
'banana'
print('cherry')

# %% id="rbjHe9KbOzFb"
print('apricot')
'banana'
pass

# %% id="V1GiIP_ZNK8H"
print(pass)

# %% id="sNNoSfndOSiw"
print(#oops)

# %% id="6IZS1NUuTdOX"
print('apricot', 'banana')

# %% [markdown] id="Tr3wPlHMeBCI"
# ## Exercise 1.2: Hello, world!
#
# The classic way to demonstrate a programming language's syntax is the hello world-program. This is the minimal amount of code required to output the text "Hello, world!" to the user.  
#
# Write a hello world-program for Python.

# %% id="jN7WTVOOSq2C"
# Your solution here

# %% [markdown] id="zI0ohEpPUwpC"
# ## Next module
#
# [2. Values and expressions](https://colab.research.google.com/drive/17K6C_EZoeGtRxoTbYQvygFEdpWgQ2QFp)
