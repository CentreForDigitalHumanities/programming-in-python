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

# %% id="ZGnlpVha4WwJ"

# %% [markdown] id="fqMJHzNk5yXQ"
# # CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1s05aR4wn2dU1C3se1oXfqKz2EY5ilrno)

# %% [markdown] id="mzWET4w4lAr4"
# # 1. Loops
#
# Loops are the most primitive way to run code *repeatedly*. For example:
#
# - Run some lines of code for each word in a text.
# - Run some lines of code for each number in a list.
# - Run some lines of code until you have found the answer to a question.
#
# There are "smarter" ways to repeat code that we will cover later in the course.

# %% [markdown] id="d7GJLYfEXwfs"
# ## `while` loops
#
# A `while` loop looks like an `if` statement, but it repeats as long as the condition is `True`:

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 517, "status": "ok", "timestamp": 1667900027935, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="Fnut4-DIYmb8" outputId="91a840be-aa92-47c9-c07f-bb52cb0447bc"
name = 'Sheean'
while len(name) < 10:
    name = name + '!'
print(name)

# %% [markdown] id="p9-je4X0zkhq"
# `while` loops are impractical if you want to repeat something for every element of an iterable, such as a list.

# %% [markdown] id="BDCe1ux90B7r"
# ## `for` loops over lists
#
# Do something with every element in a list:

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 395, "status": "ok", "timestamp": 1667900112073, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="O0XEpRMI0WG2" outputId="41b9437b-26e9-45c4-ffb6-48e2d0510e0b"
the_list = [1, 'hello', True]

for element in the_list:
    print(element)

# %% [markdown] id="gdd6v6LU1DlK"
# The body of the loop is an *indented block*, just like in an `if` or `while` statement. You can have multiple lines that repeat together:

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 384, "status": "ok", "timestamp": 1667900436458, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="dpqb0qFc1u0s" outputId="9311ae9c-066d-4dbf-da9a-7c440473dac3"
words = ['A', 'very', 'short', 'sentence']
full_text = ''

for word in words:
    full_text = full_text + word + ' '
    print(word)
    print(full_text)

# %% [markdown] id="vDU53qkB2zo4"
# The loop ends when the indentation ends. Here, we calculate the sum of a list of numbers, and print the sum only at the end:

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 550, "status": "ok", "timestamp": 1667900533282, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="q6ucnoqeUnlI" outputId="461dfdab-3387-4d9e-d59e-ad73fb8993cd"
numbers = [9, 9, 4, 7, 6]
sum = 0

for number in numbers:
    sum = sum + number
print(sum)

# %% [markdown] id="0Gun_3cX1ey8"
# ## Exercise 1: basic `for` loops
#
# 1. Make a small change to the following code block (copied from above), so that it prints the `full_text` only at the end, when it is complete.

# %% id="nMF8WE3F19HC"
words = ['A', 'very', 'short', 'sentence']
full_text = ''

for word in words:
    full_text = full_text + word + ' '
    print(word)
    print(full_text)

# %% [markdown] id="8zB10pLC2ZaT"
# 2. Using a `for` loop, create a copy of the list of fruits below that has the fruits in the reverse order. Change the contents of the list on the first line to check that your solution is general.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 363, "status": "ok", "timestamp": 1667903740371, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="bAwZ_ipU28AY" outputId="6d1d0526-c780-4eaa-d9e4-2262de2691c2"
fruits = ['apricot', 'banana', 'cherry', 'date']

# insert your code here
# SHOULD output ['date', 'cherry', 'banana', 'apricot']

reverse_fruits = fruits[-1::-1]
print(reverse_fruits)

reverse_fruits = []
for fruit in fruits[-1::-1]:
    reverse_fruits.append(fruit)
    reverse_fruits = reverse_fruits + [fruit]
print(reverse_fruits)

reverse_fruits = []
for fruit in fruits:
    reverse_fruits = [fruit] + reverse_fruits
    print(fruit, reverse_fruits)
print(reverse_fruits)

reverse_fruits = []
reverse_fruits = [fruits[0]] + reverse_fruits
reverse_fruits = [fruits[1]] + reverse_fruits
reverse_fruits = [fruits[2]] + reverse_fruits
reverse_fruits = [fruits[3]] + reverse_fruits
print(reverse_fruits)

reverse_fruits = []
for fruit in fruits:
    reverse_fruits[0:0] = [fruit]
print(reverse_fruits)

reverse_fruits = []
reverse_fruits[0:0] = [fruits[0]]
reverse_fruits[0:0] = [fruits[1]]
reverse_fruits[0:0] = [fruits[2]]
reverse_fruits[0:0] = [fruits[3]]

reverse_fruits = []
for fruit in fruits:
    reverse_fruits[-1:0] = [fruit]


# %% [markdown] id="DATxv0pM2gQc"
# ## Variations on loops
#
# All of the following variations can also be combined.

# %% [markdown] id="MVcUZD4T7j4h"
# ### Infinite loop

# %% id="l40DJzDx2nCz"
while True:
    print('Hello, living lab!')

# %% [markdown] id="0axR682t-ub4"
# Generally something to avoid, but sometimes useful with `break`.

# %% [markdown] id="2xzzyBX43Rbq"
# ### Breaking out of a loop

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 439, "status": "ok", "timestamp": 1667904280773, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="kbbKDHwd4Eiq" outputId="6ff54d8a-dfa6-4995-c469-1b3177bce245"
basket = ['apricot', 'banana', 'cherry', 'date']

for fruit in basket:
    print(fruit)
    if fruit == 'elderberry':
        print('Yay, this basket has elderberry! 🤤')
        break
else:
    print('Aww no elderberry. 😞')

# %% [markdown] id="3C9WlDSd-8zw"
# `break`/`else` can be used both with `for` and `while` loops. The `else` is not required.

# %% [markdown] id="ZZGIvGNg673Z"
# ### Skipping to the next iteration

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 525, "status": "ok", "timestamp": 1667904433491, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="AyVZVJtL7nMJ" outputId="2df5b782-b01c-4bea-812f-4f17ab255e5e"
chores = ['dishwashing', 'vacuum cleaning', 'laundry']

for task in chores:
    # I really hate vacuum cleaning
    if task == 'vacuum cleaning':
        continue
    print(task)

# %% [markdown] id="3fs83n3H_J_j"
# Works both in `for` and `while`.

# %% [markdown] id="FHf46PtqBvVb"
# ### Nested loops
#
# Nesting loops is **allowed**, to arbitrary depth. `for` and `while` can be mixed. However, nesting loops has a big **disadvantage**: your code quickly becomes less readable.
#
# Below, we use nested loops to iterate over nested lists.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 527, "status": "ok", "timestamp": 1667904767636, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="WffnwizrCvPw" outputId="64cc2f10-38da-4276-a401-26eeffd95890"
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

# %% [markdown] id="DZVVVSYy8HGd"
# ### Iterating over a string

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 459, "status": "ok", "timestamp": 1667905025657, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="14DRs2jK8Po7" outputId="bd49b199-0647-4e5b-86fd-19c7d09497ee"
invitation = '''
    Dear Sheean,

    I hereby invite you for my Python party on the 9th of November.
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

# %% [markdown] id="HrfN3OhbELuM"
# ### Iterating over generated sequences
#
# *Generators* are iterables that produce one value at a time, so they do not need to store all their values at the same time.
#
# `range` creates a generator that produces consecutive numbers.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 11, "status": "ok", "timestamp": 1667905473540, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="iqNQLZVcHYRX" outputId="40591d82-d9d1-4c9c-c887-042daa2f9a81"
for number in range(5):
    print(number)

# %% [markdown] id="9GySTLd_Hq9l"
# `enumerate` creates a new iterable based on another iterable, so you get not only the values but also their indices.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 566, "status": "ok", "timestamp": 1667905472137, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="MIyn99IxH74D" outputId="0c2f832c-c245-49ef-c51c-da9903e163e5"
basket = ['apricot', 'banana', 'cherry', 'date']

for index, fruit in enumerate(basket):
    print('Fruit number', index, 'is', fruit)

# %% [markdown] id="WGlaXiuxISRX"
# There are many more ways to create generators, and many more ways to use them as well. We will see more of them later on in the course.

# %% [markdown] id="-K0CvNkOLEYE"
# ## Exercise 2: more loops
#
# 1. The code block below is written to help you explore what kind of "stuff" comes out of `range` and `enumerate`. Read the code from top to bottom. What stands out to you? Why do you think it was written this way?
#
# 2. Run the code block for each example value of `miracle`. Based on the results, describe in your own words what `range` and `enumerate` do.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 465, "status": "ok", "timestamp": 1667910549466, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="7gappYcLOrsu" outputId="6fff15b1-41c9-4798-bbb6-43c9ef12c85d"
basket = ['apricot', 'banana', 'cherry', 'date']

miracle = range(10)
# miracle = range(2, 11)
# miracle = range(2, 11, 3)
# miracle = range(11, 2, -2)
# miracle = range(0.1, 1.0, 0.1)
# miracle = enumerate(basket)
# miracle = enumerate('pirate')
# miracle = enumerate(range(10))

print(type(miracle))

iteration_count = 0
for value in miracle:
    iteration_count = iteration_count + 1
    if iteration_count > 2:
        continue
    elif iteration_count == 1:
        print(type(value))
    print(value)
print(value)
print('length:', iteration_count)

# %% [markdown] id="2Haq4E95bN6T"
# 3. The `input` function, demonstrated below, lets you ask the human user for a string and then store it in a variable. Write a program that keeps asking the user for words until the word is `'stop'`. For each word, report to the user how many characters it contains.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 6733, "status": "ok", "timestamp": 1667914234752, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="0k_YQbBccyC_" outputId="15b0c654-f047-4036-b95c-36a42d112d6b"
# word = input('Please give me a word: ')
# print('you wrote', word)
word = ''
while word != 'stop':
    word = input('Please give me a word: ')
    print('you wrote', word)
    print('the length is', len(word))

word = ''
while True:
    word = input('Please give me a word: ')
    if word == 'stop':
        break
    # else:
    print('you wrote', word)
    length = 0
    for character in word:
        length = length + 1
    print('the length is', length)

# %% [markdown] id="uyqbuhKsUlhG"
# 4. *FizzBuzz part 2* (advanced). Look back at your solution to exercise 5.3 from day 1 (*FizzBuzz part 1*). Now write a program that does the following: for each integer from `1` up to and including `100`, print `Fizz`, `Buzz`, `FizzBuzz` or the number itself, following the same rules as before. Separate the words and numbers by commas. Add a newline after every tenth number, so you print ten lines in total. The first line should start like `1, 2, Fizz, 4, Buzz, Fizz, ...` and the last line should be `91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz, `.

# %% colab={"base_uri": "https://localhost:8080/"} executionInfo={"elapsed": 674, "status": "ok", "timestamp": 1667915778770, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}, "user_tz": -60} id="BUeMXIQXaKna" outputId="2852de82-cad6-4441-8f47-5555c83f08a4"
# the end=', ' argument will help you:
print('this prints with a comma instead of a newline', end=', ')
print('this as well', end=', ')
# empty print() adds a newline:
print()
print('next line for illustration')

# iteration = 0
for n in range(1, 101):
    # iteration = iteration + 1
    if n % 15 == 0:
        print('FizzBuzz', end=', ')
    elif n % 3 == 0:
        print('Fizz', end=', ')
    elif n % 5 == 0:
        print('Buzz', end=', ')
    else:
        print(n, end=', ')
    if n % 10 == 0:
        print()

numbers = range(1, 101)
for number in numbers:
    if not number % 15:
        output = 'FizzBuzz'
    elif not number % 3:
        output = 'Fizz'
    elif not number % 5:
        output = 'Buzz'
    else:
        output = number
    if number == numbers[-1]:
        print(output, end='.')
    elif not number % 10:
        print(output, end=',\n')
    else:
        print(output, end=', ')

range(100)[10]
