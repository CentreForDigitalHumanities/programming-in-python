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

# %% [markdown]
# ## `if`
#
# - Only evaluate part of the code if some condition is met
# - Syntax: `if <condition>:`
# - `<condition>` can be any expression that evaluates to `True` or `False`
# - Introducing *indented blocks*

# %%
a = 12

if a > 10:
    print('the condition is met!')

# %%
a = 15

if a < 10:
    print('everything on the same indentation level belongs to this if-condition')
    print('so this will only get printed if the condition is met')
    print('and so does this')
print('but this gets printed regardless!')

# %% [markdown]
# - For indented blocks, we sometimes need `pass` as a placeholder. It lets us create an indented block, without defining any behavior for it yet. Everything after `pass` in the same block will be ignored.

# %%
earth = 'round'

if earth == 'square':
    # TODO not sure yet how to handle this case
    pass
    print('This will not be printed.')

# %% [markdown]
# ## `else`
#
# - `if` is nice, but what if we are interested in the other case?

# %%
letter = 'b'

if letter == 'a':
    print('we found the letter a')

if letter == 'b':
    print('this is not a')

if letter == 'c':
    print('this is not a')

# %% [markdown]
# Instead of specifying *all other* cases, use `else:`

# %%
letter = 'b'

if letter == 'a':
    print('we found the letter a')
else:
    print('this is not a')

# %% [markdown]
# ## `elif`
#
# Specify extra cases with `elif <condition>:` (else if)
#
#

# %%
letter = 'a'

if letter == 'a':
    print('we found the letter a')
elif letter == 'b':
    print('we found the letter b')
else:
    print('this is neither a nor b')

# %% [markdown]
# ## Multiple conditions
# - We can *nest* conditions

# %%
number = 11

if number > 2:
    if number < 10:
        print('between 2 and 10')
    print('greater than 2, but not less than 10')

# There is a mistake in the code above, can you find
# and fix it?

# %% [markdown]
# - Even better: we can *combine* conditions
# - use `<condition1> and <condition2>`, `<condition1> or <condition2>` and `not <condition>`
#

# %%
number = 11
if number > 2 and number < 10:
    print('between 2 and 10')

letter = 'd'
if letter == 'a' or letter == 'b' or letter == 'c':
    print('a or b or c')

if not (letter == 'a' or letter == 'b'):
    print('neither a nor b')

# %% [markdown]
# - `and`, `or`, `not` are operators, just like `+` and `==`. You can use them outside conditionals.

# %%
height = 185
weight = 52

tall = height > 180
light = weight < 65

skinny = tall and light
print(skinny)

# %% [markdown]
# ## Exercise 3.1: if/elif/else

# %% [markdown]
# 1. Try to predict the output of the following code blocks. Can you explain any surprises?

# %%
if 3 <= 2:
    print('What a strange day.')
print('What a strange day.')

# %%
if None == 0:
    pass
    print('I got nothing to do.')

# %%
name = 'Julian'

if name < 'Sheean':
    print('Alphabetically before Sheean')
elif name > 'Sheean':
    print('Alphabetically after Sheean')
else:
    print('Same name as Sheean')

# %%
score = 10

if score > 9:
    verdict_1 = 'Wow, amazing!'
elif score > 5:
    verdict_1 = 'Okay, sure.'
else:
    verdict_1 = 'Pathetic.'

if score > 9:
    verdict_2 = 'Wow, amazing!'
if score > 5:
    verdict_2 = 'Okay, sure.'
else:
    verdict_2 = 'Pathetic.'

print(verdict_1)
print(verdict_2)


# %% [markdown]
# 2. In the following code block, replace `None` with your own condition in the `if` statement. If `value` is greater than `5`, `size` must be `'large'`; otherwise, `size` must be `'small'`. Change `value` a few times and rerun the code to check that your condition is correct.

# %%
value = 4

if None:
    size = 'large'
else:
    size = 'small'

print(size)

# %% [markdown]
# 3. Write an `if`/`elif`/`else` statement like the previous, but with different cutoff points: if `value` is less than `4`, `size` must be `'small'`; if `value` is between `4` and `6` (inclusive), `size` must be `'medium'`; if `value` is greater than `6`, `size` must be `'large'`.

# %%
value = 4

# your if/elif/else here

print(size)

# %% [markdown]
# 4. Rewrite the conditional that checks if a letter is neither 'a' nor 'b', using a different notation.

# %%
letter = 'c'

# original
if not (letter == 'a' or letter == 'b'):
    print('neither a nor b')

# %% [markdown]
# ## Exercise 3.2: Bonus

# %% [markdown]
# *FizzBuzz part 1* (advanced).
# Write an `if`/`elif`/`else` statement that behaves as follows:
#
# - if `value` is divisible by 3 but not by 5, print `'Fizz'`;
# - if `value` is divisible by 5 but not by 3, print `'Buzz'`;
# - if `value` is divisible by 3 *and* by 5, print `'FizzBuzz'`;
# - in all remaining cases, print `value`.
#
# Tip: use the result of [Exercise 2.4.1](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20values%20and%20expressions.ipynb#scrollTo=EKFdkLkWa8EY#scrollTo=Exercise_2_4_Bonus)!

# %%
value = 9

# Your code here

# %% [markdown]
# ## Next module
#
# [4. Datastructures](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/04%20datastructures.ipynb)
