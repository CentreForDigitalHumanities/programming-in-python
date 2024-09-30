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
#     language: python
#     name: python3
# ---

# %% [markdown]
# Here are some additional exercises for the day 1 modules!

# %% [markdown]
# # Types
# ## Exercise A
# useful for after 1.4
#
# 1. Create one variable each for every following type (replace None with an example):
#  - Integer (`int`)
#  - Floating point (`float`)
#  - Boolean (`bool`)
#  - String (`str`)

# %%
example_int = None
example_float = None
example_bool = None
example_string = None

# %% [markdown]
# Did you know that you can check the type of a variable in Python? If you are ever unsure of the type of a variable, use the `type()` function to check, e.g.:

# %%
print(type(1))
print(type(1.0))
print(type(False))
print(type('one'))

# %% [markdown]
# 2. Now try and check the types of the examples you just declared using the method above:

# %%
## Space for exercise

# %% [markdown]
# Python is a 'dynamically typed' language, which means that the type of a variable can vary based on its context or user coercion. For example, you can coerce an integer to a float by declaring:

# %%
example_integer = 2  # declare example integer
print(example_integer, type(example_integer)) #print the integer and its type

coerced_float = float(example_integer)
print(coerced_float, type(coerced_float))

# %% [markdown]
# You can coerce these types manually or Python sometimes does it automatically, for example when you try and execute operations on a variable that requires a certain type. For instance, if you try to add the integer and float above, the result of that operation will be a float. Python automatically coerces the integer to a float to complete the addition.
#
# 3. For this exercise, try to perform some operations on these variables below. Which types can be automatically added together? And what type is the result of their operation? What happens when you try a different operation, such as subtraction?

# %%
ex_int = 1
ex_float = 2.0
ex_string = 'three'
ex_bool = True

ex_result = ex_int + ex_float  # example operation
print(ex_result, type(ex_result))

# %% [markdown]
# # Lists
# ## Exercise B
# Let's make some lists! 
# 1. Start by declaring an empty list (`empty_list = []`).

# %%
my_list = None

# %% [markdown]
# You can check the length of the list with the `len()` function:

# %%
print(len(my_list))

# %% [markdown]
# 2. Now, add some elements to your list. Then check the length of the list again!

# %%
## Space for exercise

# %% [markdown]
# # Loops
# ## Exercise C

# %% [markdown]
# 1. Now that you have your list, let's walk through it and print every element in it. Hint: use the `for` loop.

# %%
## Space for exercise

# %% [markdown]
# 2. Instead of simply printing the elements, see if you can print the result of an operation with each element (for example, print the element + 1). Alternatively, see if you can print the type of each element in the list.

# %%
## Space for exercise

# %% [markdown]
# # Logical Operators
# ## Exercise D
# Python allows the use of several logical operators, so to get you in the mindset of a computer, see if you can determine whether an expression is going to return `True` or `False`. After you have given your answer, run the code in the cell to see if you were correct!

# %%
# Declaration of the variables used in the exercise
n1 = 1
n2 = 2
n3 = 3.4
n4 = 4.5
s1 = 'Hello'
s2 = 'World'
s3 = 'Hallo'
s4 = 'Wereld'
l1 = [n1, n2, n3, n4]
l2 = [s1, s2, s3, s4]

# %%
#Example 1
n1 == n2

# %% [markdown]
# True or False?

# %%
#Example 2
n1 + n2 == 3

# %%
#Example 3
n1 + n3 != 3.4

# %% [markdown]
# True or False?

# %%
#Example 4
s1 + s2 == "Hello World"

# %% [markdown]
# True or False?

# %%
#Example 5
s3 == "hallo"

# %% [markdown]
# True or False?

# %%
#Example 6
len(l1) == len(l2)

# %% [markdown]
# True or False?

# %%
#Example 7
len(s3) == len(s1)

# %%
##Example 8
for item in l2:
    print(len(item) == 5)
