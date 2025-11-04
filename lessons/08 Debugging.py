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
# # Module 8: Debugging
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [7. Functions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/07%20Functions.ipynb)
#
# ### This module
#
# - How to see exactly what is going on in your program.
# - Using this to solve problems with code.

# %% [markdown]
# ## Stepping with the debugger
#
# The following "magic line", which you can insert anywhere in your code (preferably inside a function), will create a *breakpoint*:
#
# ```py
# import pdb; pdb.set_trace()
# ```
#
# > ⚠️ In notebooks, you *need* to put the breakpoint inside a function. Standalone Python also allows them outside of functions.
#
# > 💡 There exist other ways to set breakpoints, some of which look less like magic. The one shown here works in all situations.
#
# When Python encounters a breakpoint, it pauses execution of the program and hands control to you. You "enter the debugger". This enables you to see what is going on inside the program. Some useful commands to remember:
#
# - `l` or `list`: show the code around the current line.
# - `p <name>` or `print <name>`: show the value of the variable with the given `<name>`.
# - `pp <name>`: *pretty* print a value (nice for long strings and for data structures).
# - `n` or `next`: execute the current line and stop at the next line.
# - `s` or `step`: step into the next function call and stop at its first line.
# - `r` or `return`: finish executing the current function and stop at the line after its call.
# - `c` or `cont` or `continue`: resume the program until the next breakpoint, or until the end.
# - `help`: show the list with available commands.
#
# Demonstration below!

# %%
def scream(name):
    """ Using at least one bang (!), make `name` at least 10 chars long. """
    # import pdb; pdb.set_trace()
    name = name + '!'
    while len(name) < 10:
        name = name + '!'
    return name

name = 'Julian'
exclamation = scream(name)
print(exclamation)


# %% [markdown]
# ## Exercise 8.1: Debugging

# %% [markdown]
# ### 1. Building muscle memory
#
# In the definition of `scream` above, uncomment the breakpoint and step through the code. Make the debugger print two different values of `name`, then allow it to complete the program until the end.

# %% [markdown]
# ### 2. Known bugs
#
# Each of the code blocks below has a function, a `print` statement and an assertion. The assertion should pass, but it fails because of a bug in the function. For each code block, take the following steps:
#
# 1. Read the code. Can you predict what will be printed and why the assertion will fail?
# 2. Run the code. Are you surprised? Can you explain the result?
# 3. Uncomment the breakpoint. Step through the code and make very sure that you understand what is going wrong.
# 4. Fix the broken function and check that the assertion now passes.

# %%
def echo(word):
    """ Make the given word sound like an echo. """
    # import pdb; pdb.set_trace()
    repeated = word + ',' + word
    tail_off = repeated + '...'
    return tail_off

my_echo = echo('Mees')
print(my_echo)
assert my_echo == 'Mees, Mees...'

# %%
# Remember that letters have a numeric ordinal?
# We can use these to convert a lowercase to
# uppercase and vice versa!
uppercase_offset = ord('A') - ord('a')

def uppercase(lowercase_letter):
    """ Convert a lowercase letter to uppercase. """
    # import pdb; pdb.set_trace()
    lowercase_ordinal = ord(lowercase_letter)
    uppercase_ordinal = lowercase_ordinal - uppercase_offset
    uppercase_letter = chr(uppercase_ordinal)
    return uppercase_letter

upper_a = uppercase('a')
print(upper_a)
assert upper_a == 'A'


# %% [markdown]
# ### 3. Unknown bugs
#
# Like in the previous exercises, the following code blocks have a function with a bug and an assertion. However, the assertion passes, because it does not demonstrate the bug. For each code block, take the following steps:
#
# 1. Run the code and see for yourself that the assertion passes.
# 2. Read the code. Do you have any suspicion of what might be wrong? Do not change the code yet.
# 3. Add more assertions until you discover one that should pass, but doesn't. If you had a suspicion in step 2, try to confirm it with your new assertions. If you had no suspicion yet (or if you cannot comfirm it), it is also fine to "blind guess".
# 4. Once you have found an assertion that fails, comment out all other assertions, so only the problematic one will run.
# 5. By your own judgment, insert a breakpoint in the code that should help you to diagnose the bug. Step through the code with the debugger until you fully understand the bug.
# 6. Outcomment your breakpoint and fix the bug. **Tip:** you may reuse code from previous exercises, if you think this would be useful.
# 7. Uncomment all assertions that you previously outcommented, so that all assertions are checked when you run the code block.
# 8. Run the code block and verify that your fixed version of the function passes all the assertions.

# %%
# Python has a built-in function for reversing strings,
# so normally you would not need to write it yourself.

def reverse_string(text):
    """ Given any string, return a reversed copy. """
    reversed = text[0]
    for next_letter in text[1:]:
        reversed = next_letter + reversed
    return reversed

assert reverse_string('abc') == 'cba'


# %%
vowels = 'aeiouy'

def count_vowels(text):
    """ Given any string, return the number of vowels. """
    count = 0
    for character in text:
        if character in vowels:
            count = count + 1
    return count

assert count_vowels('The quick fox jumps over the lazy dog.') == 11

# %% [markdown]
# ## Exercise 8.2: Bonus

# %% [markdown]
# ### 1. Gnome sort
#
# Gnome sort is possibly the simplest way to sort a list. It can be understood by imagining that a gnome (indicated below by the `^`) is standing next to the list.
#
# ```
# -------------
# | 2 | 3 | 1 |
# -------------
#   ^
# ```
#
# The gnome looks at the element closest to herself, as well as at the element to the right of it (here `2` and `3`). When those elements are already sorted, the gnome walks one element to the right and looks again:
#
# ```
# -------------
# | 2 | 3 | 1 |
# -------------
#       ^
# ```
#
# When the current element and the one right of it are *not* sorted, like here, the gnome swaps those elements and walks one place to the left:
#
# ```
# -------------
# | 2 | 1 | 3 |
# -------------
#   ^
# ```
#
# The gnome continues doing this, taking care not to walk off the left edge of the list:
#
# ```
# -------------
# | 1 | 2 | 3 |
# -------------
#   ^
# ```
#
# ```
# -------------
# | 1 | 2 | 3 |
# -------------
#       ^
# ```
#
# ```
# -------------
# | 1 | 2 | 3 |
# -------------
#           ^
# ```
#
# When there is no more element to the right, the gnome stops. If we make sure to start the gnome at the leftmost element of the list, this will sort the entire list.
#
# Below, we implemented gnome sort in Python, but we made one mistake. The program never finishes. Step with the debugger to find the mistake.
#
# > ⚠️ If you need to sort something "for real", Python has ready-to-use solutions, so you do not normally need to write your own sorting code!

# %%
shuffled = ['banana', 'apricot', 'date', 'cherry', 'date']
alphabetical = ['apricot', 'banana', 'cherry', 'date', 'date']

def gnome_sort(items):
    """ Sort `items` by changing the list in place. Not efficient. """
    stop = len(items) - 1
    index = 0
    while index < stop:
        here = items[index]
        right = items[index + 1]
        if here < right:
            index = index + 1
        else:
            items[index:(index + 2)] = [right, here]
            index = max(0, index - 1)

gnome_sort(shuffled)

print(shuffled)
assert shuffled == alphabetical

# %% [markdown]
# ### 2. Debugging your own algorithm
#
# Write a completely new function (or multiple) that does something useful. For inspiration, here are some suggestions:
#
# - Compute the average word length in a text.
# - Given a string, return `True` if it is a palindrome and `False` otherwise. A palindrome is a string that reads the same if you reverse it. For example, `'abcba'` and `'ab cc ba'` are palindromes, `'abcabc'` is not.
# - In a list of strings, find the first one that does not contain the word `'the'`.
#
# If you feel these examples are too complicated, a simpler algorithm is also fine.
#
# Once you have written your function(s), add multiple assertions to check that your code works as you intended. Run your code and see whether you have any failing assertions.
#
# If all of your assertions pass, try adding more assertions and see whether you can still find a bug. It is very uncommon for new code to work correctly on the first try! If it seems you have written perfect code on the first try, give yourself a pat on the shoulder, then pick a more complicated algorithm. You need to create code with a bug!
#
# Once you have written code with a failing assertion, step with the debugger to understand why the assertion is failing. Fix the bug only after you fully understand the cause. Finally, check that all your assertions pass after the fix. If you still have failing assertions, step with the debugger again. Repeat until all assertions pass.

# %%
# maybe some test data here

# your own function(s) here

# your own assertions here

# %% [markdown]
# ## Next module
#
# [9. String manipulation](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/09%20String%20manipulation.ipynb)
