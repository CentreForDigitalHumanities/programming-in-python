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
# # Module 6: Loops
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [5. Assertions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/05%20assertions.ipynb)

# %% [markdown]
# # 1. Loops
#
# Loops are the most primitive way to run code *repeatedly*. For example:
#
# - Run some lines of code for each word in a text.
# - Run some lines of code for each number in a list.
# - Run some lines of code until you have found the answer to a question.
#
# There are "smarter" ways to repeat code that we will cover later in the course.

# %% [markdown]
# ## `while` loops
#
# A `while` loop looks like an `if` statement, but it repeats as long as the condition is `True`:

# %%
name = 'Julian'
while len(name) < 10:
    name = name + '!'
print(name)

# %% [markdown]
# `while` loops are impractical if you want to repeat something for every element of an iterable, such as a list.

# %% [markdown]
# ## `for` loops over lists
#
# For loops do something for every element in a list, so the length of the list is the number of iterations. What is especially useful about for-loops is that for every iteration, the item in the list can be used in the indented code block. This means that you can do a certain action for each item in the list without having to provide the index for that item. For example:

# %%
the_list = [1, 'hello', True]

for element in the_list:
    print(element)

# %% [markdown]
# The body of the loop is an *indented block*, just like in an `if` or `while` statement. You can have multiple lines that repeat together:

# %%
words = ['A', 'very', 'short', 'sentence']
full_text = ''

for word in words:
    full_text = full_text + word + ' '
    print(word)
    print(full_text)

# %% [markdown]
# The loop ends when the indentation ends. Here, we calculate the sum of a list of numbers, and print the sum only at the end:

# %%
numbers = [9, 9, 4, 7, 6]
sum = 0

for number in numbers:
    sum = sum + number
print(sum)

# %% [markdown]
# ## Exercise 1: basic `for` loops
#
# 1. Make a small change to the following code block (copied from above), so that it prints the `full_text` only at the end, when it is complete.

# %%
words = ['A', 'very', 'short', 'sentence']
full_text = ''

for word in words:
    full_text = full_text + word + ' '
    print(word)
    print(full_text)

# %% [markdown]
# 2. Using a `for` loop, create a copy of the list of fruits below that has the fruits in the reverse order. Change the contents of the list on the first line to check that your solution is general.

# %%
fruits = ['apricot', 'banana', 'cherry', 'date']

# insert your code here
# SHOULD output ['date', 'cherry', 'banana', 'apricot']


# %% [markdown]
# ## Variations on loops
#
# All of the following variations can also be combined.

# %% [markdown]
# ### Infinite loop

# %%
while True:
    print('Hello, living lab!')

# %% [markdown]
# Generally something to avoid, but sometimes useful with `break`.

# %% [markdown]
# ### Breaking out of a loop
# You can break out of a loop by using the `break` statement. If Python encounters a `break` statement, it immediately exits the loop, and continues with the code after the loop. It will stop iterating even if the loop condition is still `True` (in case of a `while` loop) or there are still items left in the iterable (in case of a `for` loop).
#

# %%
basket = ['apricot', 'banana', 'elderberry', 'cherry', 'date']

for fruit in basket:
    print(fruit)
    if fruit == 'elderberry':
        print('Yay, this basket has elderberry! 🤤')
        break

# %% [markdown]
# Using `break` can be useful in combination with `while` to avoid infinite loops:

# %%
counter = 0
while True:
    print('The counter is now', counter)
    counter = counter + 1
    if counter >= 5:
        print('Counter reached 5, stopping the loop.')
        break


# %% [markdown]
# You can also use `else` (which we also saw in Module 3 about conditionals) in combination with `for` and `while` loops. With `for` and `while`, the `else` block will be executed if the loop finishes "naturally", i.e. without encountering a `break` statement. The `else` block is skipped if the loop is exited with a `break` statement. You can remember this as "break, or else!".

# %%
basket = ['apricot', 'banana', 'cherry', 'date']

for fruit in basket:
    print(fruit)
    if fruit == 'elderberry':
        print('Yay, this basket has elderberry! 🤤')
        break
else:
    print('Aww no elderberry. 😞')


# %%
# The same example, but now with a while loop.
basket = ['apricot', 'banana', 'elderberry', 'cherry', 'date']
index = 0

while index < len(basket):
    fruit = basket[index]
    print(fruit)
    if fruit == 'elderberry':
        print('Yay, this basket has elderberry! 🤤')
        break
    # Update index so we avoid an infinite loop if there is no elderberry in the list.
    index = index + 1
else:
    print('Aww no elderberry. 😞')


# %% [markdown]
# ### Skipping to the next iteration

# %%
chores = ['dishwashing', 'vacuum cleaning', 'laundry']

for task in chores:
    # I really hate vacuum cleaning
    if task == 'vacuum cleaning':
        continue
    print(task)

# %% [markdown]
# Works both in `for` and `while` loops.

# %% [markdown]
# ### Nested loops
#
# Nesting loops is **allowed**, to arbitrary depth. `for` and `while` can be mixed. However, nesting loops has a big **disadvantage**: your code quickly becomes less readable.
#
# Below, we use nested loops to iterate over nested lists.

# %%
table = [
    ['bread', 'fluffy', 'light brown'],
    ['olives', 'savory', 'dark green'],
    ['grapes', 'sweet', 'shiny red'],
]

for row in table:
    print('new row:')
    for cell in row:
        print(cell, end='; ') # does not finish with a linebreak
    print() # puts a linebreak

# %% [markdown]
# ### Iterating over a string
# Note here that when you iterate over a string, python treats the string as if it were a list with characters, including whitespaces. If you want to iterate over the words in a string, you can use the `.split()` function to split the string into a list of strings where each item is one word (separated by whitespace in the original string).

# %%
invitation = '''
    Dear Sheean,

    I hereby invite you for my Python party on the 11th of April.
    The bar will open at 2 PM. 🍸 Please bring pseudocode.

    Yours sincerely,
    Julian
'''

lowercase = 0
uppercase = 0
other = 0
for character in invitation:
    if 'a' <= character <= 'z':
        lowercase = lowercase + 1
    elif 'A' <= character <= 'Z':
        uppercase = uppercase + 1
    else:
        other = other + 1

print(lowercase, 'lowercase,', uppercase, 'uppercase and', other, 'other.')

long_words = 0
short_words = 0
for word in invitation.split():
    if len(word) > 5:
      long_words = long_words + 1
    else:
      short_words = short_words + 1
print(short_words, 'short words', long_words, 'long words')

# %% [markdown]
# ### Iterating over generated sequences
#
# *Generators* are iterables that produce one value at a time, so they do not need to store all their values at the same time.
#
# `range` creates a generator that produces consecutive numbers.

# %%
for number in range(5):
    print(number)

# %% [markdown]
# `enumerate` creates a new iterable based on another iterable, so you get not only the values but also their indices.

# %%
basket = ['apricot', 'banana', 'cherry', 'date']

for index, fruit in enumerate(basket):
    print('Fruit number', index, 'is', fruit)

# %% [markdown]
# There are many more ways to create generators, and many more ways to use them as well. We will see more of them later on in the course.

# %% [markdown]
# ## Exercise 2: more loops
#
# 1. The code block below is written to help you explore what kind of "stuff" comes out of `range` and `enumerate`. Read the code from top to bottom. What stands out to you? Why do you think it was written this way?
#
# 2. Run the code block for each example value of `miracle`. Based on the results, describe in your own words what `range` and `enumerate` do.

# %%
basket = ['apricot', 'banana', 'cherry', 'date']

miracle = range(10)
# miracle = range(2, 11)
# miracle = range(2, 11, 3)
# miracle = range(11, 2, -2)
# miracle = range(0.1, 1.0, 0.1)
# miracle = enumerate(basket)
# miracle = enumerate('pirate')
# miracle = enumerate(range(10))

print('type of miracle:', type(miracle))

iteration_count = 0
for value in miracle:
    iteration_count = iteration_count + 1
    if iteration_count > 2:
        continue
    elif iteration_count == 1:
        print('type of first iteration:', type(value))
    print('value of current iteration:', value)

print('number of iterations:', iteration_count)

# %% [markdown]
# 3. The `input` function, demonstrated below, lets you ask the human user for a string and then store it in a variable. Write a program that keeps asking the user for words until the word is `'stop'`. For each word, report to the user how many characters it contains.

# %%
word = input('Please give me a word: ')
print('you wrote', word)


# %% [markdown]
# 4. *FizzBuzz part 2* (advanced). Look back at your solution to exercise 3.2 (*FizzBuzz part 1*). Now write a program that does the following: for each integer from `1` up to and including `100`, print `Fizz`, `Buzz`, `FizzBuzz` or the number itself, following the same rules as before. Separate the words and numbers by commas. Add a newline after every tenth number, so you print ten lines in total. The first line should start like `1, 2, Fizz, 4, Buzz, Fizz, ...` and the last line should be `91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz, `.

# %%
# the end=', ' argument will help you:
print('this prints with a comma instead of a newline', end=', ')
print('this as well', end=', ')
# empty print() adds a newline:
print()
print('next line for illustration')


# %% [markdown]
# ## Next module
#
# [7. Functions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/07%20Functions.ipynb)
