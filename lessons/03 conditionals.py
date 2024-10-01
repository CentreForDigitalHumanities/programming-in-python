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
# # Module 3: Conditionals
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [2. Values and expressions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20values%20and%20expressions.ipynb)
#
# ### This module
#
# - Execute code only under specific conditions.

# %% [markdown] id="SshSsbtF8ldm"
# ## `if`
#
# - Only evaluate part of the code if some condition is met
# - Syntax: `if <condition>:`
# - `<condition>` can be any expression that evaluates to `True` or `False`
# - Introducing *indented blocks*

# %% id="Va6X8kIz9ey0"
a = 12

if a > 10:
    print('the condition is met!')

# %% id="ADXv-2u090ql"
a = 15

if a < 10:
    print('everything on the same indentation level belongs to this if-condition')
    print('so this will only get printed if the condition is met')
    print('and so does this')
print('but not this!')

# %% [markdown] id="5gqn2ac_sg7Y"
# - For indented blocks, we sometimes need `pass` as a placeholder. It lets us create an indented block, without defining any behavior for it yet.

# %% id="ZdH7HnL6tDpS"
earth = 'round'

if earth == 'square':
    # TODO not sure yet how to handle this case
    pass

# %% [markdown] id="sQxxBZwm-FYm"
# ## `else`
#
# - `if` is nice, but what if we are interested in the other case?

# %% id="atRhlkGq-Mh1"
letter = 'b'

if letter == 'a':
    print('we found the letter a')

if letter == 'b':
    print('this is not a')

if letter == 'c':
    print('this is not a')

# %% [markdown] id="O1repWSS-3Y0"
# Instead of specifying *all other* cases, use `else:`

# %% id="4n9ksUuH-8kE"
letter = 'b'

if letter == 'a':
    print('we found the letter a')
else:
    print('this is not a')

# %% [markdown] id="Rg1ohowkAGFh"
# ## `elif`
#
# Specify extra cases with `elif <condition>:` (else if)
#
#

# %% id="JbiihBgdANIM"
letter = 'a'

if letter == 'a':
    print('we found the letter a')
elif letter == 'b':
    print('we found the letter b')
else:
    print('this is not a or b')

# %% [markdown] id="lVOu8HvVIEj6"
# ## Multiple conditions
# - We can *nest* conditions

# %% id="MH_RrrBRIPh4"
number = 11

if number > 2:
    if number < 10:
        print('between 2 and 10')
    print('greater than 2, but not less than 10')

# There is a mistake in the code above, can you find
# and fix it?

# %% [markdown] id="8Lvam7rpIms6"
# - Even better: we can *combine* conditions
# - use `<condition1> and <condition2>`, `<condition1> or <condition2>` and `not <condition>`
#

# %% id="zJ8rBgcfIw4I"
number = 11
if number > 2 and number < 10:
    print('between 2 and 10')

letter = 'd'
if letter == 'a' or letter == 'b' or letter == 'c':
    print('a or b or c')

if not (letter == 'a' or letter == 'b'):
    print('neither a nor b')

# %% [markdown] id="SmsIZBLEtg9r"
# - `and`, `or`, `not` are operators, just like `+` and `==`. You can use them outside conditionals.

# %% id="XMWJeaujt2lj"
height = 185
weight = 52

tall = height > 180
light = weight < 65

skinny = tall and light
print(skinny)

# %% [markdown] id="tvXa9KWXAwge"
# ## Exercise 3.1: if/elif/else

# %% [markdown] id="pKBuViM9u7ZC"
# 1. Try to predict the output of the following code blocks. Can you explain any surprises?

# %% id="sEQyw2xJvzQN"
if 3 <= 2:
    print('What a strange day.')
print('What a strange day.')

# %% id="FnCFfEb_v-0Y"
if None == 0:
    pass
    print('I got nothing to do.')

# %% id="arta4ZQ0vDSC"
name = 'Julian'

if name < 'Sheean':
    print('Alphabetically before Sheean')
elif name > 'Sheean':
    print('Alphabetically after Sheean')
else:
    print('Same name as Sheean')

# %% [markdown] id="4SVSiqHSu4WX"
# 2. In the following code block, replace `None` with your own condition in the `if` statement. If `value` is greater than `5`, `size` must be `'large'`; otherwise, `size` must be `'small'`. Change `value` a few times and rerun the code to check that your condition is correct.

# %% id="czmdFacjeUaL"
value = 4

if None:
    size = 'large'
else:
    size = 'small'

print(size)

# %% [markdown] id="sEOwMi04e6WW"
# 3. Write an `if`/`elif`/`else` statement like the previous, but with different cutoff points: if `value` is less than `4`, `size` must be `'small'`; if `value` is between `4` and `6` (inclusive), `size` must be `'medium'`; if `value` is greater than `6`, `size` must be `'large'`.

# %% id="8HeaY6l9f9iA"
value = 4

# your if/elif/else here

print(size)

# %% [markdown] id="TWzbez_2RUh4"
# 4. Rewrite the conditional that checks if a letter is neither 'a' nor 'b', using a different notation.

# %% id="XsIg1MD4JrPX"
letter = 'c'

# original
if not (letter == 'a' or letter == 'b'):
    print('neither a nor b')

# %% [markdown] id="-XEYQZJ1ya1j"
# ## Exercise 3.2: Bonus

# %% [markdown] id="POVFwRu_f91I"
# *FizzBuzz part 1* (advanced).
# Write an `if`/`elif`/`else` statement that behaves as follows:
#
# - if `value` is divisible by 3 but not by 5, print `'Fizz'`;
# - if `value` is divisible by 5 but not by 3, print `'Buzz'`;
# - if `value` is divisible by 3 *and* by 5, print `'FizzBuzz'`;
# - in all remaining cases, print `value`.
#
# Tip: use the result of [Exercise 2.4.1](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20values%20and%20expressions.ipynb#scrollTo=EKFdkLkWa8EY#scrollTo=Exercise_2_4_Bonus)!

# %% id="SZGeQtqEhiAK"
value = 9

# Your code here

# %% [markdown] id="YBC4OfihzFho"
# ## Next module
#
# [4. Datastructures](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/04%20datastructures.ipynb)
