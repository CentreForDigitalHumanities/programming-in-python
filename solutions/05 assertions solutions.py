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
# # Module 5: Assertions
#
# ### Exercise solutions
#
# [5. Assertions](https://colab.research.google.com/drive/1ixrL5RCpNhtQN_MtCbpy4E5PYEG1N-qH)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1YgmnpA7tRylvGBpp2PTFGvSV2P8tw5jl)
#
# Previous module: [4. Datastructures](https://colab.research.google.com/drive/1CS9CxET2V1j0FQzy82AWBZZCbc8M_qWt) - [solutions](https://colab.research.google.com/drive/1mf_sQpAVxz8oRbsZnA548cC3TtVaQxmU)

# %% [markdown] id="m_FYfvXbbZXe"
# ## Exercise 5.1: Assertions
# In each of the code blocks below, try to predict what will be the output, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% id="ztDylwg9biL5"
assert True
# The assertion passes, so no output!

# %% id="0Uk4w2DBbxfD" colab={"base_uri": "https://localhost:8080/", "height": 164} executionInfo={"status": "error", "timestamp": 1681309645640, "user_tz": -120, "elapsed": 45, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="fd5ed9ba-c7ea-488a-b537-a6641517d2c0"
assert False, "The assertion fails because the value is False"

# %% id="orOWCpWVbzKf"
assert "True"

# You can think of assert as implicitly wrapping its argument in bool():
assert bool("True")
# bool() converts anything that looks like "empty" or "nothing",
# such as the integer 0 (zero), None, the empty string and the empty list,
# to False, and everything else to True.
# Hence, the string "True" is converted to the boolean True, the assertion
# passes and there is no output.

# %% id="F6NjZ7gOb05u"
assert "False", "The assertion fails because the value is False"
# The string "False" is nonempty, so bool() converts it to True
# (which, yes, is very confusing!). Hence, the assertion passes
# and we see no output.

# For comparison, the empty string results in a failing assertion:
assert bool(""), "The assertion fails because the value is False"
# while a string with just a space passes:
assert bool(" "), "The assertion fails because the value is False"

# %% id="KB_YkNSIb2KT"
assert 1
# bool(1) is True, so pass, so no output

# %% id="1iUK81Nvb3Ri"
assert 1 == True, "The number 1 is not True"
# As we saw in module 2, 1 is indeed the same value as True

# %% id="Tje6e-Jgb4rn" colab={"base_uri": "https://localhost:8080/", "height": 164} executionInfo={"status": "error", "timestamp": 1681310102072, "user_tz": -120, "elapsed": 10, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="2ffb1ccc-c2ce-4625-baea-c02403cdf947"
assert 0
# bool(0) is False, so fail, so we see an AssertionError.
# The AssertionError lacks a description because we did not
# provide one.

# %% [markdown] id="xgqh3r7Bcj_F"
# ## Exercise 5.2: Bonus - Test-driven development

# %% [markdown] id="TMWSMWg7dQqB"
# In the code block below, change the value for `b`, and create an expression for `c` using `a` and `b` so that the assert statements succeed.
#

# %% id="Q_yIUKSRdVjF"
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

# %% [markdown] id="1u_bBUpSfQr5"
# In the code block below, change `students` so that it satisfies the `assert` statements. Also, add messages to the assert statements that explain what they test (in human language).

# %% id="UOp8NFVOfR6Z"
students = ['bert', 'ernie', 'pino']


assert len(students) == 3, 'We need three student names'
assert students[0] < students[1] < students[2], 'The students must be sorted'

# %% [markdown] id="JaaguG-D3k_i"
# ## Next module
#
# [6. Loops](https://colab.research.google.com/drive/14qxBVO9t3w-pFFnMuS_yhggUmM5S0BnZ) - [solutions](https://colab.research.google.com/drive/19mQnQILY7oRREvwUsAD2SmqQHiOffgx_)
