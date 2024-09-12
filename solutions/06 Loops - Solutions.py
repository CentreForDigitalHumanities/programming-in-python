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
# # CDH course "Programming in Python"
#
# ### Exercise Solutions
#
# [Module 6](https://colab.research.google.com/drive/14qxBVO9t3w-pFFnMuS_yhggUmM5S0BnZ)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1YgmnpA7tRylvGBpp2PTFGvSV2P8tw5jl)
#
# Previous module: [5. Assertions](https://colab.research.google.com/drive/1ixrL5RCpNhtQN_MtCbpy4E5PYEG1N-qH) - [solutions](https://colab.research.google.com/drive/1yrrB0EYglFKJ0_zhb91xY7FGgJosSUFw)

# %% [markdown] id="0Gun_3cX1ey8"
# ## Exercise 1: basic `for` loops
#
# 1. Make a small change to the following code block (copied from above), so that it prints the `full_text` only at the end, when it is complete.

# %% id="nMF8WE3F19HC" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1681144232455, "user_tz": -120, "elapsed": 5, "user": {"displayName": "Mees van Stiphout", "userId": "10520931415894572279"}} outputId="7e9843ae-f3d5-43f1-b0a4-64a3c2c309c7"
words = ['A', 'very', 'short', 'sentence']
full_text = ''

for word in words:
    full_text = full_text + word + ' '
    print(word)
print(full_text)

# %% [markdown] id="8zB10pLC2ZaT"
# 2. Using a `for` loop, create a copy of the list of fruits below that has the fruits in the reverse order. Change the contents of the list on the first line to check that your solution is general.

# %% id="bAwZ_ipU28AY" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1681311205916, "user_tz": -120, "elapsed": 208, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="34d5cb4c-d675-413e-adb6-9d3f7bc41908"
fruits = ['apricot', 'banana', 'cherry', 'date']

# insert your code here
# SHOULD output ['date', 'cherry', 'banana', 'apricot']

#solution 1:
reverse_fruits = []
for fruit in fruits[-1::-1]:
    reverse_fruits.append(fruit)
print(reverse_fruits)

#solution 2 (best):
reverse_fruits = []
for fruit in fruits:
    reverse_fruits = [fruit] + reverse_fruits
print(reverse_fruits)

#solution 3:
reverse_fruits = []
for fruit in fruits:
    reverse_fruits[0:0] = [fruit]
print(reverse_fruits)

#solution 4:
reverse_fruits = []
position = -1
for fruit in fruits:
    reverse_fruits.append(fruits[position])
    position = position - 1
print(reverse_fruits)

#solution 5:
reverse_fruits = []
position = len(fruits) - 1
for fruit in fruits:
    reverse_fruits.append(fruits[position])
    position = position - 1
print(reverse_fruits)


# %% [markdown] id="-K0CvNkOLEYE"
# ## Exercise 2: more loops

# %% [markdown] id="Qj9LsMfw-RMT"
# 1. The code block below is written to help you explore what kind of "stuff" comes out of `range` and `enumerate`. Read the code from top to bottom. What stands out to you? Why do you think it was written this way?

# %% [markdown] id="otBq-xEi-SiC"
# > Things that you might notice:
# >
# > - It is possible to call `range` with one, two or three arguments.
# > - `enumerate` is always called with only one argument.
# > - Some noticed that you can write the string `'pirate'` and pass it directly to `enumerate`, without storing the string in a variable first. This is a good observation, and it is possible with all values and functions in general!
# > - The program is counting iterations. The variable `iteration_count` is initially set to `0`, incremented at every loop iteration and finally printed at the end.
# > - When the `iteration_count` is greater than `2`, the loop does not print the current `value`. In other words, the program only prints the first two values in each iterable.
# > - The program prints the type of the first value in the iterable only.
# >
# > Reasons:
# >
# > - All the various versions of `miracle` are there to illustrate the behavior of `range` and `enumerate`.
# > - We print the type of the iterable as a whole at the start, so you can see what kind of value comes out of the call to `range` or `enumerate`.
# > - We keep track of the number of iterations so you can see how many values are produced by the iterable. We could have used `enumerate` for this, but this would be confusing, since the behavior of `enumerate` itself is the topic of this exercise. Therefore, we use custom logic with the `iteration_count` variable instead.
# > - We only print the first two values in the iterable because this is enough to see a pattern. If we printed all of them, it could potentially produce a lot of output.
# > - We only print the type of the first value, on the assumption that all values in the iterable have the same type.
#
#

# %% [markdown] id="EjmxzbeY-USj"
# 2. Run the code block for each example value of `miracle`. Based on the results, describe in your own words what `range` and `enumerate` do.

# %% [markdown] id="ZyllJHKCBtoy"
# > Possible elements of a good answer for `range`:
# >
# > - If you pass only one value, this sets the exclusive end. It generates whole numbers from `0` (zero) up to but not including the end.
# > - If you pass two values, the first sets the inclusive start and the second sets the exclusive end.
# > - If you pass three values, the first sets the inclusive start, the second the exclusive end and the third a step size.
# > - If you omit the step size (so you pass only one or two arguments), it defaults to `1`.
# > - A negative step size causes the range to count "backwards" (from high numbers to low numbers).
# > - You are not allowed to pass floats; the function only supports integers.
# >
# > Possible elements of a good answer for `enumerate`:
# >
# > - It requires another iterable as argument (we see a list, a string and a range in the examples).
# > - The same values from the input iterable also appear in the output iterable, but wrapped in a tuple.
# > - In the output iterable, every tuple has a numerical index in addition to the corresponding value from the input iterable.
# > - The numerical index is the first element of the tuple, while the value is the second element.
# > - The numerical indices start at `0` (zero).
#

# %% id="7gappYcLOrsu" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1681311440820, "user_tz": -120, "elapsed": 189, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="039590e8-bbae-4ad4-c622-95110c3e9a8d"
basket = ['apricot', 'banana', 'cherry', 'date']

miracle = range(100)
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

# %% [markdown] id="2Haq4E95bN6T"
# 3. The `input` function, demonstrated below, lets you ask the human user for a string and then store it in a variable. Write a program that keeps asking the user for words until the word is `'stop'`. For each word, report to the user how many characters it contains.

# %% id="0k_YQbBccyC_" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1681313320536, "user_tz": -120, "elapsed": 6762, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="ef5102e8-4248-47f3-a59c-87a5958b41db"
#solution 1:
word = ''
while word != 'stop':
    word = input('Please give me a word: ')
    print('you wrote', word)
    print('the length is', len(word))

#solution 2:
while True:
    word = input('Please give me a word: ')
    if word == 'stop':
        break
    print('you wrote', word)
    print('the length is', len(word))

# %% [markdown] id="uyqbuhKsUlhG"
# 4. *FizzBuzz part 2* (advanced). Look back at your solution to exercise 5.3 from day 1 (*FizzBuzz part 1*). Now write a program that does the following: for each integer from `1` up to and including `100`, print `Fizz`, `Buzz`, `FizzBuzz` or the number itself, following the same rules as before. Separate the words and numbers by commas. Add a newline after every tenth number, so you print ten lines in total. The first line should start like `1, 2, Fizz, 4, Buzz, Fizz, ...` and the last line should be `91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz, `.

# %% id="BUeMXIQXaKna" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1681313256562, "user_tz": -120, "elapsed": 1068, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="0c5ddcc6-e2d0-40bb-9456-892f751320b6"
# Variant 1

for n in range(1, 101):
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

# Variant 2

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
    if not number % 10:
        print(output, end=',\n')
    else:
        print(output, end=', ')


# %% [markdown] id="0eGibfk04LI0"
# ## Next module
#
# [7. Functions](https://colab.research.google.com/drive/146De3ZjgWYldNBmKkDyu8-m_jkzUTrGg) - [solution](https://colab.research.google.com/drive/1BdBQeTKBvEPn1CTIJC5sDDY6VBMs32Sq)
