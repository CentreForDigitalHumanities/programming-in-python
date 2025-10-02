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
# # Module 5: Assertions
#
# ### Exercise solutions
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [4. Data structures](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/04%20Data%20structures.ipynb)
#
# ### This module
#
# - Interrupting the program if something isn't right, with useful output.

# %% [markdown]
# ## `assert`
#
# With an assertion, you tell Python that you want something to be `True`. This is an easy way to insert sanity checks in your code, i.e. to test whether your program is working as you expect it to.

# %%
assert 2 < 3

# %% [markdown]
# For clarity, you can describe the expectation.

# %%
sky = 'red'

assert sky == 'blue', 'We expect to be on Earth'

# %% [markdown]
# You can use `assert` statements to:
# - provide a sanity check, make sure something is true at some point in the code
# - provide test conditions for your code, make sure what you programmed actually behaves the way you wish

# %% [markdown]
# ## Exercise 5.1: Assertions
# In each of the code blocks below, try to predict what will be the output, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %%
assert True

# %%
assert False, "The assertion fails because the value is False"

# %%
assert "True"

# %%
assert "False", "The assertion fails because the value is False"

# %%
assert 1

# %%
assert 1 == True, "The number 1 is not True"

# %%
assert 0

# %% [markdown]
# ## Exercise 5.2: Bonus - Test-driven development
# [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) is a process where you **first** write some test conditions, and then write the code that should satisfy these conditions.
# Implement the following programs in these steps:
# 1. Create multiple test conditions using `assert`
# 2. Run the cell, the tests should fail (output `AssertionError`)
# 3. Write the code that satisfies the conditions
# 4. The cell should complete succesfully
#
# We have already implemented step 1 for these exercises.

# %% [markdown]
# In the code block below, change the value for `b`, and create an expression for `c` using `a` and `b` so that the assert statements succeed.
#

# %%
a = 12

# Change the value for b
b = 0

# Write an expression for c using a and b
c = 0

assert a < b, 'a should be less than b'
assert a != b, 'a and b should not be equal'
assert c == 18, 'c should be 18'

# %% [markdown]
# In the code block below, change `students` so that it satisfies the `assert` statements. Also, add messages to the assert statements that explain what they test (in human language).

# %%
students = ['ernie', 'bert']

assert len(students) == 3
assert students[0] < students[1] < students[2]

# %% [markdown]
# ## Next module
#
# [6. Loops](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/06%20Loops.ipynb)
