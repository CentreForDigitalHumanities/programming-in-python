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
# [5. Assertions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/05%20assertions.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [4. Datastructures](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/04%20datastructures.ipynb) - [solutions](htthttps://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/04%20datastructures%20solutions.ipynb)

# %% [markdown]
# ## Exercise 5.1: Assertions
# In each of the code blocks below, try to predict what will be the output, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %%
assert True
# The assertion passes, so no output!

# %%
assert False, "The assertion fails because the value is False"

# %%
assert "True"

# You can think of assert as implicitly wrapping its argument in bool():
assert bool("True")
# bool() converts anything that looks like "empty" or "nothing",
# such as the integer 0 (zero), None, the empty string and the empty list,
# to False, and everything else to True.
# Hence, the string "True" is converted to the boolean True, the assertion
# passes and there is no output.

# %%
assert "False", "The assertion fails because the value is False"
# The string "False" is nonempty, so bool() converts it to True
# (which, yes, is very confusing!). Hence, the assertion passes
# and we see no output.

# For comparison, the empty string results in a failing assertion:
assert bool(""), "The assertion fails because the value is False"
# while a string with just a space passes:
assert bool(" "), "The assertion fails because the value is False"

# %%
assert 1
# bool(1) is True, so pass, so no output

# %%
assert 1 == True, "The number 1 is not True"
# As we saw in module 2, 1 is indeed the same value as True

# %%
assert 0
# bool(0) is False, so fail, so we see an AssertionError.
# The AssertionError lacks a description because we did not
# provide one.

# %% [markdown]
# ## Exercise 5.2: Bonus - Test-driven development

# %% [markdown]
# In the code block below, change the value for `b`, and create an expression for `c` using `a` and `b` so that the assert statements succeed.
#

# %%
# One possible solution
a = 12

b = 30

c = b - a

# Another possible solution
a = 12

b = 24

c = (a + b) / 2

assert a < b, 'a should be less than b'
assert a != b, 'a and b should not be equal'
assert c == 18, 'c should be 18'

# %% [markdown]
# In the code block below, change `students` so that it satisfies the `assert` statements. Also, add messages to the assert statements that explain what they test (in human language).

# %%
students = ['bert', 'ernie', 'pino']


assert len(students) == 3, 'We need three student names'
assert students[0] < students[1] < students[2], 'The students must be sorted'

# %% [markdown]
# ## Next module
#
# [6. Loops](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/06%20Loops.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/06%20Loops%20-%20Solutions.ipynb)
