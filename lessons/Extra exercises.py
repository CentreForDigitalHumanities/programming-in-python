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
# Here are some additional exercises, organised by module.

# %% [markdown]
# # Module 2: Values and expressions
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
# Python is a 'dynamically typed' language, which means that the type of a variable can vary based on its context. A variable's type is determined by the value it holds. For example, if you assign an integer value to a variable, its type will be `int`. If you later assign a string value to the same variable, its type will change to `str`.
# 
# It is also possible to 'coerce' (i.e. explicitly convert) a variable from one type to another, by using `float()`, `int()`, `str()` or the like. For example, you can coerce an integer to a float like this.

# %%
example_integer = 2  # Declare an integer variable.
example_integer = "hello" # Now it is a string.
example_integer = 3 # Now it is an integer again.

print(example_integer, type(example_integer)) # Print the integer and its type.

coerced_float = float(example_integer) # Coerce the integer to a float.
print(coerced_float, type(coerced_float))

# %% [markdown]
# You can coerce these types manually, but sometimes Python does it automatically, for example when you try and execute operations on a variable that requires a certain type. For instance, if you try to add the integer and float above, the result of that operation will be a float. Python automatically coerces the integer to a float to complete the addition.
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
# ## Logical Operators
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

# %% [markdown]
# # Module 3: Conditionals

# %% [markdown]
# 1. **Age Category Classifier**: Write a conditional statement that 
# categorises people by age:
# - If age is less than 13: print "Child"
# - If age is between 13 and 17 (inclusive): print "Teenager"  
# - If age is between 18 and 64 (inclusive): print "Adult"
# - If age is 65 or older: print "Senior"

# %%
age = 25  # Try changing this value to test different cases.

## Your code here

# %% [markdown]
# 2. **Grade Calculator**: Write a conditional statement that updates the 
# variable `letter_grade` and prints a comment based on a numerical score between 0 and 100.
#
# For the letter grade, use the following scale:
# - For a score between 90-100, the grade should be "A".
# - For a score between 80-89, the grade should be "B".
# - For a score between 70-79, the grade should be "C".
# - For a score between 60-69, the grade should be "D".
# - For a score below 60, the grade should be "F".
#
# If the grade is D or better, print "PASSED". Otherwise, print "FAILED".

# %%
score = 85  # Try different scores to test your logic.

letter_grade = None

## Your code here

# %% [markdown]
# 3. **Weather Decision Maker**: Write a program that suggests activities based on weather and temperature:
# - If it's sunny:
#   - Temperature above 25°C: "Go to the beach!"
#   - Temperature 15-25°C: "Perfect for a picnic!"
#   - Temperature below 15°C: "Take a sunny walk!"
# - If it's rainy:
#   - Temperature above 20°C: "Warm rain - maybe garden work?"
#   - Temperature below 20°C: "Stay inside with a book!"
# - If it's snowy:
#   - Always suggest: "Build a snowman or go skiing!"
# - For any other weather: "No forecast today."

# %%
weather = "sunny"  # Try: "sunny", "rainy", "snowy", or "cloudy"
temperature = 22   # Try different temperatures

# %% [markdown]
# # Module 4: Data structures

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
# # Module 6: Loops

# %% [markdown]
# 1. Here is another list. Use a 'for' loop to print each element in the list.

# %%
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# %% [markdown]
# 2. Instead of simply printing the elements, see if you can print the result of an operation with each element (for example, print the element + 1). Alternatively, see if you can print the type of each element in the list.

# %%
## Space for exercise

# %% [markdown]
# 3. Now, try to sum all elements in the list. Use the variable `total` to store the sum, and print it at the end.

# %%
total = 0

# %% [markdown]
# # Module 7: Functions
#
# Here are more exercises to help you get more familiar with writing Python code, and especially making functions. It contains no new theory.
#
# There are a lot of exercises, and they can be very similar. Don't feel like you have to do everything: if the exercises start to feel repetitive, you're ready to move on to the next section.

# %% [markdown]
# ## 1. Writing functions
#
# In these exercises, the instructions describe a function that you need to make. Each code block also has some assert statements that try to use your function, which you can use to verify your solution.

# %% [markdown]
# 1.1: Write a function `first`, which returns the first item in a list. The function should take one argument (a list).
#
# If the list if empty, `first` should return `None`.

# %%
# your code here...

# check your function
assert first(['apple', 'banana', 'orange']) == 'apple'
assert first(['just one item']) == 'just one item'
assert first([]) == None

# %% [markdown]
# 1.2: Write a function `check_wallet` which takes a list of items as its argument. If the list includes `'wallet'`, it should return the list as-is. If it doesn't, it should add `'wallet'` to the end of list.

# %%
# your code here...

# check your function
assert check_wallet(['keys',  'wallet', 'phone', 'gloves']) == ['keys',  'wallet', 'phone', 'gloves']
assert check_wallet(['keys', 'phone']) == ['keys', 'phone', 'wallet']
assert check_wallet([]) == ['wallet']

# %% [markdown]
# 1.3: Write a function `round_to_10` which takes a number as its argument and returns a new number: the input rounded to the nearest multiple of 10. (Hint: use the 'modulo' operator (%) from [Exercise 2.4 (Module 2)](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20Values%20and%20expressions.ipynb#scrollTo=13bf4e73).)

# %%
# your code here...

# check your function
assert round_to_10(8) == 10
assert round_to_10(22.1) == 20
assert round_to_10(40) == 40
assert round_to_10(55) == 60

# %% [markdown]
# 1.4: Let's make our rounding function a bit more generic. Make a new function `round_to_n` which takes two arguments: the number that you want to round, and the unit that you want to round to. `round_to_n(35, 50)` will round 35 to the nearest multiple of 50.

# %%
# your code here


# check your function
assert round_to_n(8, 10) == 10
assert round_to_n(8, 20) == 0
assert round_to_n(24.3, 20) == 20

# %% [markdown]
# 1.5: Write a function `in_alphabet` that takes a character (a string of length 1) as a parameter. It should return `True` if the character is one of the 26 letters in the latin alphabet. Uppercase and lowercase characters should both return `True`. Otherwise, the function should return `False`.

# %%
# your code here

# check your function
assert in_alphabet('a') == True
assert in_alphabet('f') == True
assert in_alphabet('A') == True
assert in_alphabet('1') == False
assert in_alphabet('✨') == False

# %% [markdown]
# 1.6: Use your function `in_alphabet` to write a new function `clean_text`. It should take one parameter, which is a string. It should return a new string, which is like the old one but leaves out any characters that are not in the latin alphabet or the space `' '`.

# %%
# your code here...

# check your function
assert clean_text('Hello, how are you?') == 'Hello how are you'
assert clean_text('Hooray! Hooray! Hooray!') == 'Hooray Hooray Hooray'
assert clean_text('Yummy!! 😋') == 'Yummy '


# %% [markdown]
# 1.7: Write a function `to_time` which takes a decimal number of hours (like the output of `travel time`) and converts it to hours, minutes, and seconds. For example, 1.5 hours is 1 hours, 30 minutes and 0 seconds.
#
# The input should be a single `float` or `int`, and the output should be three numbers: hours, minutes, and seconds. The output should be given in whole numbers (`int`, not `float`).

# %%
# your code here...

# check your function
assert to_time(1.5) == (1, 30, 0)
# Floats are not exact, so we need to allow for a small margin of error here.
assert to_time(3.6532) in ((3, 39, 11), (3, 39, 12))
assert to_time(0) == (0, 0, 0)

# %% [markdown]
# 1.8: Write a function `mean` which takes one argument, a list of numbers, as input. It should return the mean value of the list (a single number).

# %%
# your code here...

# check your function
assert mean([1, 2, 7 , 2]) == 3.0
assert mean([3.2, 4.5, 0.0, 2.5]) == 2.55
assert mean([0.0]) == 0.0

# %% [markdown]
# 1.9: Write a function `is_number` that checks if a string describes a number. It takes one argument (a string).
#
# It should return `True` if:
# - Every character in the string is either a digit (0-9) or a decimal point `'.'`)
# - If there is a decimal point, it should not be more than one.
#
# Otherwise, the function should return `False`.

# %%
# your code here...
 
# check your function.
assert is_number('12') == True
assert is_number('0.5') == True
assert is_number('two') == False
assert is_number('1.2.3') == False


# %% [markdown]
# ## 2. Writing `assert` checks
#
# The code blocks below contain a function definition, but are missing some `assert` statements to check if everything works. Read the docstring and try to think of some assertions you could use to check the function.
#
# Not all of these functions work as intended! For some functions, you should be able to find assert statements that should succeed, but fail.
#
# You do not have to correct the functions (but you can if you want to).

# %%
def distance(a, b):
    '''
    Gives the distance between two numbers.

    Distance is absolute, i.e. always positive.
    '''

    if a <= b:
        return b - a
    else:
        return a - b

# write some checks!


# %%
def reverse(word):
    '''
    Reverses a string

    Input must be a string. Output is the same string in reverse order.
    '''

    new_word = ''

    for character in word:
        new_word = character + new_word
    
    return new_word



# %%
def every_third_item(items):
    '''
    Returns every third item in a list.

    Input should be a list, the output is a new list. Always returns the first
    item - after that, returns every third item.
    '''

    result = []

    for index in range(0, len(items), 3):
        result.append(items[index])
    
    return result

# write some checks!


# %%
def grade(score):
    '''
    Gives a letter grade (F, D, C, B, A) based on a score from 0-100.

    Scores over 60 get grade D, scores over 70 get grade C, etc.
    '''
    if score >= 60:
        return 'D'
    elif score >= 70:
        return 'C'
    elif score >= 80:
        return 'B'
    elif score >= 90:
        return 'A'
    else:
        return 'F'

# write some checks!


# %%
def is_prime(number):
    '''
    Checks if a int is a prime number.

    Prime numbers are numbers that are NOT the product
    of two smaller numbers (2, 3, 5, 7, 11, are prime numbers)
    '''

    for smaller_number in range(2, number):
        if number % smaller_number == 0:
            return False

    return True    

# write some checks!


# %% [markdown]
# ## 3. Writing functions with checks
#
# For the functions in section 1, we provided some assert statements, but when you write your own programs, you usually don't have those. Instead, you have _something you want to do_, and it is up to you to make your own `assert` checks.
#
# For the exercises below, we describe what your function should do. It is up to you to make both the function and the assert statements.
#
# For each exercise, consider the following:
#
# - What should the function be callled?
# - What are the input parameters? What type should they be?
# - What is the output? What type should the output be?
# - What are some checks you could write?
# - What should be in the body of the function? How does it work?

# %% [markdown]
# 3.1: Write a function that turns a sentence into a question. The input should be a string. If the last character in the string is a `.` or `!`, it should be replaced with a `?`. Otherwise, we just want to add `?` to the end of the string (without replacing anything).

# %%

# %% [markdown]
# 3.2: Write a function that takes a year as input and tells you whether or not that year is a leap year.
#
# From [wikipedia](https://en.wikipedia.org/wiki/Leap_year):
#
# > Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.

# %%

# %% [markdown]
# 3.3: Write a function to calculate the area of a circle based on the diameter.
#
# - The _area_ is equal to the _radius_ of the circle, squared, multiplied by pi. In a formula: $A = r^2 \times \pi$.
# - The radius of a circle is equal to half its diameter.
# - You can assume that pi is equal to 3.14

# %%

# %% [markdown]
# 3.4: We want to calculate prices for an online store. Prices are calculated as follows:
# - An order will include one or more items, each with their own price. You can just represent the order as a list of prices, e.g. `[15.00, 4.40, 31.50]`
# - Customers may have a coupon that gives them 10% off all the items in their basket.
# - If the total of the order (including the coupon discount) is under € 20.00, customers need to pay € 2.00 shipping.
#
# Write a function that calculates the total of an order.

# %%

# %% [markdown]
# 3.5: Write a function that counts how often a string occurs within another string.

# %%

# %% [markdown]
# ## 4. Don't repeat yourself
#
# An important use for functions is to avoid unnecessary repetition in code.
# When you write two pieces of very similar code, it's often convenient to make
# a single function instead, and call that function in both places.
#
# Each of the code blocks below contains two things:
# - a section of code that has some repetition
# - some assert statements that check if the code works as intended
#
# For each block:
# - try to understand what the code does, and identify the repetition;
# - at the top of the code block, add a definition for a function (or several), that can handle the shared functionality;
# - use your function(s) in the code, and check that everything still works.


# %%
small_pizza_price = 9.00
small_pizza_slices = 6

small_pizza_price_per_slice = small_pizza_price / small_pizza_slices
print('The small pizza costs €', small_pizza_price_per_slice, 'per slice')

medium_pizza_price = 12.00
medium_pizza_slices = 8

medium_pizza_price_per_slice = medium_pizza_price / medium_pizza_slices
print('The medium pizza costs €', medium_pizza_price_per_slice, 'per slice')

large_pizza_price = 16.00
large_pizza_slices = 8

large_pizza_price_per_slice = large_pizza_price / large_pizza_slices
print('The large pizza costs €', large_pizza_price_per_slice, 'per slice')

# check if everything works
assert small_pizza_price_per_slice == 1.5
assert medium_pizza_price_per_slice == 1.5
assert large_pizza_price_per_slice == 2.0

# %%
fruit_basket = ['apple', 'banana', 'banana', 'banana', 'apple', 'orange',
                'orange', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape',
                'grape', 'grape', 'grape', 'pear', 'apple', 'strawberry',
                'strawberry', 'strawberry', 'orange']

apples = 0
for fruit in fruit_basket:
    if fruit == 'apple':
        apples += 1

oranges = 0
for fruit in fruit_basket:
    if fruit == 'orange':
        oranges += 1

apples_to_oranges = apples / oranges

# check if everything works
assert apples_to_oranges == 1

# %%
weather_this_month = ['rain', 'rain', 'sun', 'sun', 'cloudy', 'cloudy', 'rain',
    'cloudy', 'rain', 'rain', 'cloudy', 'sun', 'cloudy', 'sun', 'sun', 'sun',
    'rain', 'cloudy', 'cloudy', 'sun', 'cloudy', 'rain', 'rain', 'cloudy',
    'cloudy', 'cloudy', 'sun', 'cloudy', 'sun', 'sun']

rain_followed_by_sun = 0
rain_followed_by_cloudy = 0
rain_followed_by_rain = 0

for index, weather in enumerate(weather_this_month):
    not_last = index < len(weather_this_month) - 1
    if weather == 'rain' and not_last:
        weather_next_day = weather_this_month[index + 1]
        if weather_next_day == 'sun':
            rain_followed_by_sun += 1
        elif weather_next_day == 'cloudy':
            rain_followed_by_cloudy += 1
        else:
            rain_followed_by_rain += 1

print('Days with rain were followed by:')
print('Sun:', rain_followed_by_sun, 'times')
print('Clouds:', rain_followed_by_cloudy, 'times')
print('Rain:', rain_followed_by_rain, 'times')
print()

sun_followed_by_sun = 0
sun_followed_by_cloudy = 0
sun_followed_by_rain = 0

for index, weather in enumerate(weather_this_month):
    not_last = index < len(weather_this_month) - 1
    if weather == 'sun' and not_last:
        weather_next_day = weather_this_month[index + 1]
        if weather_next_day == 'sun':
            sun_followed_by_sun += 1
        elif weather_next_day == 'cloudy':
            sun_followed_by_cloudy += 1
        else:
            sun_followed_by_rain += 1

print('Days with sun were followed by:')
print('Sun:', sun_followed_by_sun, 'times')
print('Clouds:', sun_followed_by_cloudy, 'times')
print('Rain:', sun_followed_by_rain, 'times')
print()

sun_preceded_by_sun = 0
sun_preceded_by_cloudy = 0
sun_preceded_by_rain = 0


for index, weather in enumerate(weather_this_month):
    not_first = index > 0
    if weather == 'sun' and not_first:
        weather_prev_day = weather_this_month[index - 1]
        if weather_prev_day == 'sun':
            sun_preceded_by_sun += 1
        elif weather_prev_day == 'cloudy':
            sun_preceded_by_cloudy += 1
        else:
            sun_preceded_by_rain += 1

print('Days with sun were preceded by:')
print('Sun:', sun_preceded_by_sun, 'times')
print('Clouds:', sun_preceded_by_cloudy, 'times')
print('Rain:', sun_preceded_by_rain, 'times')
print()

# check if everything works
assert rain_followed_by_sun == 1
assert rain_followed_by_cloudy == 4
assert rain_followed_by_rain

assert sun_followed_by_sun == 4
assert sun_followed_by_cloudy == 4
assert sun_followed_by_rain == 1

assert sun_preceded_by_sun == 4
assert sun_preceded_by_cloudy == 5
assert sun_preceded_by_rain == 1


# %% [markdown]
# ## Module 12: Functions, bis
#
# 1. Add a couple of assertion statements to the function (which has a default argument) below. Find out if the function works as intended and fix any bugs you find.
#

# %%
def exclude_short_words(words, min_length=5):
    '''
    Filters all short words (shorter than min_length) out of a list

    Input should be a list of words (strings). Returns a new list
    with only the words longer than min_length.
    '''

    long_words = []

    for word in words:
        if len(word) < 5:
            long_words.append(word)
    
    return long_words

# write some checks!


# %% [markdown]
# 2: Write a function `travel_time` that estimates the travel time for a journey. It takes 3 named arguments:
# - `car`: the distance traversed by car
# - `bike`: the distance traversed by bike
# - `walk`: the distance traversed on foot
#
# Each of these will be a number (distance in km), and the default value should be `0`. Calculate the travel time, assuming that:
#
# - Cars have an average speed of 80 km/h
# - Bikes have an average speed of 16 km/h
# - Walking has an average speed of 4 km/h
#
# Your function should return the travel time in hours.

# %%
# your code here...

# check your function
assert travel_time(car=10, walk=0.1) == 0.15
assert travel_time(bike=10, walk=0.1) == 0.65
assert travel_time(car=55, bike=3, walk=0.3) == 0.95
