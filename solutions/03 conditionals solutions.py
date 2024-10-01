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
# ### Exercise solutions
#
# [Module 3](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/03%20conditionals.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [2. Values and expressions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20values%20and%20expressions.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/02%20values%20and%20expressions%20solutions.ipynb)

# %% [markdown]
# ## Exercise 3.1: if/elif/else

# %% [markdown]
# 1. Try to predict the output of the following code blocks. Can you explain any surprises?

# %%
if 3 <= 2:
    # The first print is not executed,
    # because it is inside the conditional and
    # the condition is False.
    print('What a strange day.')

# The second print is executed, because it is
# outside of the conditional.
print('What a strange day.')

# Therefore, we see the sentence once.

# %%
if None == 0:
    # The condition is False, so this code never runs.
    # The pass statement makes no difference.
    pass
    print('I got nothing to do.')

# %%
name = 'Julian'

if name < 'Jelte':
    # This condition is False, so it does not execute.
    print('Alphabetically before Jelte')
elif name > 'Jelte':
    # This condition is True, so it does execute.
    print('Alphabetically after Jelte')
else:
    # One of the previous conditions was True, so
    # this block does not execute.
    print('Same name as Jelte')

# %% [markdown]
# 2. In the following code block, fill the condition in the `if` statement. If `value` is greater than `5`, `size` must be `'large'`; otherwise, `size` must be `'small'`. Change `value` a few times and rerun the code to check that your condition is correct.

# %%
value = 4

if value > 5:
    size = 'large'
else:
    size = 'small'

print(size)

# %% [markdown]
# 3. Write an `if`/`elif`/`else` statement like the previous, but with different cutoff points: if `value` is less than `4`, `size` must be `'small'`; if `value` is between `4` and `6` (inclusive), `size` must be `'medium'`; if `value` is greater than `6`, `size` must be `'large'`.

# %%
value = 4

# Option 1: multiple independent conditionals.
# This performs the same checks multiple times.
if value < 4:
    size = 'small'
if 4 <= value <= 6:
    size = 'medium'
if value > 6:
    size = 'large'

# Option 2: a single if-elif-else. There is
# still a little bit of overlap between the first
# and the second condition.
if value < 4:
    size = 'small'
elif 4 <= value <= 6:
    size = 'medium'
else:
    size = 'large'

# Option 3: a single if-elif-else, but now without
# any overlap between the conditions. We achieve this
# by changing the order in which we recognize the
# classifications. When the conditions are expensive
# to evaluate, this is generally the best option.
if value < 4:
    size = 'small'
elif value > 6:
    size = 'large'
else:
    size = 'medium'

print(size)

# %% [markdown]
# 4. Rewrite the conditional that checks if a letter is neither 'a' nor 'b', using a different notation.

# %%
letter = 'c'

# original
if not (letter == 'a' or letter == 'b'):
    print('neither a nor b')

# a variant in which we change all operators
if letter != 'a' and letter != 'b':
    print('neither a nor b')

# a variant using not
if not letter == 'a' and not letter == 'b':
    print('neither a nor b')

# same as above, adding parentheses to clarify
# the order in which Python evaluates the operators
if (not (letter == 'a')) and (not (letter == 'b')):
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
# Tip: use the result of *Exercise 2.4.1*!

# %%
value = 9

# A straightforward variant, in which we literally
# translate the English description to Python code.
if value % 3 == 0 and value % 5 != 0:
    print('Fizz')
elif value % 5 == 0 and value % 3 != 0:
    print('Buzz')
elif value % 5 == 0 and value % 3 == 0:
    print('FizzBuzz')
else:
    print(value)

# A more efficient variant, in which we use more "tricks":
# - We can start with an empty string and update it later.
result = ''
if value % 3 == 0:
    # - If value is divisible by 3, we ALWAYS want "Fizz",
    #   even if value is ALSO divisible by 5.
    result = result + 'Fizz'
if value % 5 == 0:
    # - If value is divisible by 5, we can add "Buzz" to
    #   the result regardless of whether it contains "Fizz".
    result = result + 'Buzz'
# - We use the short-circuiting behavior of and/or.
#   - and: stop evaluating as soon as you find a False
#          subexpression, because then the whole expression
#          must be False as well.
#   - or:  stop evaluating as soon as you find a True
#          subexpression, because then the whole expression
#          must be True as well.
#   If result is still the empty string, then it evaluates as
#   False and we print value. Otherwise, or already knows that
#   the expression will be True, so value is never evaluated
#   and result is printed instead.
print(result or value)

# %% [markdown]
# ## Next module
# [4. Datastructures](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/04%20datastructures.ipynb) - [solutions](htthttps://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/04%20datastructures%20solutions.ipynb)
