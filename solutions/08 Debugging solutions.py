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
# ### Exercise solutions
#
# [Module 8](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/08%20Debugging.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [7. Functions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/07%20Functions.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/07%20Functions%20solutions.ipynb)

# %% [markdown]
# ## Exercise 8.2.1: Gnome sort
#
# To help you solve this (solution below):
# - Use `import pdb; pdb.set_trace()` to set a breakpoint in the function.
# - Use `n` to go to the next line.
#
# ### Ask yourself
# - Where does the programme start looping forever?
# - What are the values of 'items', 'index', 'here' and 'right' at each
# iteration?
# - Why does the programme loop forever?
# - How does the programme decide whether two elements are correctly sorted?


# %% [markdown]
# ### Solution
#
# The problem is at the end of the loop, when the list is already sorted. The
# algorithm attempts to sort 'date' and 'date' and compares them using the `<`
# operator. Since they are equal, the check fails and the algorithm concludes
# that the two items are out of order. It then swaps them (which has no effect)
# and decrements the index. The index is now 3, and the algorithm compares
# 'cherry' and 'date'. Since they are in the correct order, the index is
# incremented to 4. The algorithm then compares 'date' and 'date' again, and
# the same thing happens again, and again, and again _ad infinitum_.


# %%
shuffled = ["banana", "apricot", "date", "cherry", "date"]
alphabetical = ["apricot", "banana", "cherry", "date", "date"]


def gnome_sort(items):
    """Sort `items` by changing the list in place. Not efficient."""
    stop = len(items) - 1
    index = 0
    while index < stop:
        here = items[index]
        right = items[index + 1]
        if here < right:  # The bug is here. `<=` should be used to deal with duplicates.
            index = index + 1
        else:
            items[index : (index + 2)] = [right, here]
            index = max(0, index - 1)


gnome_sort(shuffled)

print(shuffled)
assert shuffled == alphabetical
