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

# %% [markdown] id="q2_7oxCuwonl"
# # 7a - Functions (extra exercises)
#
# This notebook contains extra exercises to help you get more familiar with writing python code, and especially making functions. It contains no new theory.
#
# There are a lot of exercises, and they can be very similar. Don't feel like you have to do everything: if the exercises start to feel repetitive, you're ready to move on to the next section.

# %% [markdown] id="KoEzBrcFxk8T"
# ## 1. Writing functions
#
# In these exercises, the instructions describe a function that you need to make. Each code block also has some assert statements that try to use your function, which you can use to verify your solution.

# %% [markdown] id="DxKNUR11yfvL"
# 1.1: Write a function `first`, which returns the first item in a list. The function should take one argument (a list).
#
# If the list if empty, `first` should return `None`.

# %% id="YtJmU-K0woBC"
# your code here...

# check your function
assert first(['apple', 'banana', 'orange']) == 'apple'
assert first(['just one item']) == 'just one item'
assert first([]) == None

# %% [markdown] id="jgxg9ecn0GkZ"
# 1.2: Write a function `check_wallet` which takes a list of items as its argument. If the list includes `'wallet'`, it should return the list as-is. If it doesn't, it should add `'wallet'` to the end of list.

# %% id="Z2Xa8C6z0BrI"
# your code here...

# check your function
assert check_wallet(['keys',  'wallet', 'phone', 'gloves']) == ['keys',  'wallet', 'phone', 'gloves']
assert check_wallet(['keys', 'phone']) == ['keys', 'phone', 'wallet']
assert check_wallet([]) == ['wallet']

# %% [markdown] id="Zx9RsFoY2o5M"
# 1.3: Write a function `round_to_10` which takes a number as its argument and returns a new number: the input rounded to the nearest multiple of 10.

# %% id="Y8M_CCuCcVZm"
# your code here...

# check your function
assert round_to_10(8) == 10
assert round_to_10(22.1) == 20
assert round_to_10(40) == 40
assert round_to_10(55) == 60

# %% [markdown] id="YKRA2X94dmfm"
# 1.4: Let's make our rounding function a bit more generic. Make a new function `round_to_n` which takes two arguments: the number that you want to round, and the unit that you want to round to. `round_to_n(35, 50)` will round 35 to the nearest multiple of 50.

# %% id="CFukYZRFeMMr"
# your code here


# check your function
assert round_to_n(8, 10) == 10
assert round_to_n(8, 20) == 0
assert round_to_n(24.3, 20) == 20

# %% [markdown] id="9C8cDTS3e62p"
# 1.5: Write a function `in_alphabet` that takes a character (a string of length 1) as a parameter. It should return `True` if the character is one of the 26 letters in the latin alphabet. Uppercase and lowercase characters should both return `True`. Otherwise, the function should return `False`.

# %% id="X9kXxwe3fD7P"
# your code here

# check your function
assert in_alphabet('a') == True
assert in_alphabet('f') == True
assert in_alphabet('A') == True
assert in_alphabet('1') == False
assert in_alphabet('✨') == False

# %% [markdown] id="lXc43yNgicoA"
# 1.6: Use your function `in_alphabet` to write a new function `clean_text`. It should take one parameter, which is a string. It should return a new string, which is like the old one but leaves out any characters that are not in the latin alphabet or the space `' '`.

# %% id="YOqKnf7rjpvW"
# your code here...

# check your function
assert clean_text('Hello, how are you?') == 'Hello how are you'
assert clean_text('Hooray! Hooray! Hooray!') == 'Hooray Hooray Hooray'
assert clean_text('Yummy!! 😋') == 'Yummy '

# %% [markdown] id="mzKQAJxNLUgV"
# 1.7: Write a function `travel_time` that estimates the travel time for a journey. It takes 3 named arguments:
# - `car`: the distance traversed by car
# - `bike`: the distance traversed by bike
# - `walk`: the distance traversed on foot
#
# Each of these will be a number (distance in km), and the default value is `0`. Calculate the travel time, assuming that:
#
# - Cars have an average speed of 80 km/h
# - Bikes have an average speed of 16 km/h
# - Walking has an average speed of 4 km/h
#
# Your function should return the travel time in hours.

# %% id="XDVlkfHyMIfE"
# your code here...

# check your function
assert travel_time(car=10, walk=0.1) == 0.15
assert travel_time(bike=10, walk=0.1) == 0.65
assert travel_time(car=55, bike=3, walk=0.3) == 0.95

# %% [markdown] id="SQHPePrYxdnG"
# 1.8: Write a function `to_time` which takes a decimal number of hours (like the output of `travel time`) and converts it to hours, minutes, and seconds. For example, 1.5 hours is 1 hours, 30 minutes and 0 seconds.
#
# The input should be a single `float` or `int`, and the output should be three numbers: hours, minutes, and seconds. The output should be given in whole numbers (`int`, not `float`).

# %% id="5cdwImkNUGcc"
# your code here...

# check your function
assert to_time(1.5) == (1, 30, 0)
assert to_time(3.6532) == (3, 39, 55)
assert to_time(0) == (0, 0, 0)

# %% [markdown] id="shtLjnOGxen9"
# 1.9: Write a function `mean` which takes one argument, a list of numbers, as input. It should return the mean value of the list (a single number).

# %% id="xJ_XTebzxfCs"
# your code here...

# check your function
assert mean([1, 2, 7 , 2]) == 3.0
assert mean([3.2, 4.5, 0.0, 2.5]) == 2.55
assert mean([0.0]) == 0.0

# %% [markdown] id="p1NF-Tbpxfs1"
# 1.10: Write a function `is_number` that checks if a string describes a number. It takes one argument (a string).
#
# It should return `True` if:
# - Every character in the string is either a digit (0-9) or a decimal point `'.'`)
# - If there is a decimal point, it should not be more than one.
#
# Otherwise, the function should return `False`.

# %% id="LsA_B5iPxgEE"
# your code here...
 
# check your function.
assert is_number('12') == True
assert is_number('0.5') == True
assert is_number('two') == False
assert is_number('1.2.3') == False


# %% [markdown] id="o55Hp9SomntG"
# ## 2. Writing `assert` checks
#
# The code blocks below contain a function definition, but are missing some `assert` statements to check if everything works. Read the docstring and try to think of some assertions you could use to check the function.
#
# Not all of these functions work as intended! For some functions, you should be able to find assert statements that should succeed, but fail.
#
# You do not have to correct the functions (but you can if you want to).

# %% id="aqngxSucow39"
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


# %% id="khwUSdMWn1CR"
def reverse(word):
    '''
    Reverses a string

    Input must be a string. Output is the same string in reverse order.
    '''

    new_word = ''

    for character in word:
        new_word = character + new_word
    
    return new_word

# write some checks!


# %% id="nkpyPnDgoxKf"
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


# %% id="yQ_-_xnuoyZ9"
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


# %% id="ArwDSoguox2j"
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


# %% id="hMIpfW_lMK0l"
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


# %% [markdown] id="aKgZVXZXoF3g"
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

# %% [markdown] id="EXgk0_mjoukf"
# 3.1: Write a function that turns a sentence into a question. The input should be a string. If the last character in the string is a `.` or `!`, it should be replaced with a `?`. Otherwise, we just want to add `?` to the end of the string (without replacing anything).

# %% id="ExH64Sbgovw0"

# %% [markdown] id="uA4PQxchxUrT"
# 3.2: Write a function that takes a year as input and tells you whether or not that year is a leap year.
#
# From [wikipedia](https://en.wikipedia.org/wiki/Leap_year):
#
# > Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.

# %% id="VIYiW1OCxVEo"

# %% [markdown] id="QzewFsCJomVB"
# 3.3: Write a function to calculate the area of a circle based on the diameter.
#
# - The _area_ is equal the _radius_ of the circle, squared, multiplied by pi. In a formula: $A = r^2 \times \pi$. 
# - The radius of a circle is half its diameter.
# - You can assume that pi is equal to 3.14

# %% id="oCID8txRotb-"

# %% [markdown] id="SoO0C4pyxSjO"
# 3.4: We want to calculate prices for an online store. Prices are calculated as follows:
# - An order will include one or more items, each with their own price. You can just represent the order as a list of prices, e.g. `[15.00, 4.40, 31.50]`
# - Customers may have a coupon that gives them 10% off all the items in their basket.
# - If the total of the order (including the coupon discount) is under € 20.00, customers need to pay € 2.00 shipping.
#
# Write a function that calculates the total of an order.

# %% id="ddWh7EWCxS6M"

# %% [markdown] id="m1bBl0RvxXe-"
# 3.5: Write a function that counts how often a string occurs within another string.

# %% id="GKRKIpKgxXwV"

# %% [markdown] id="NPXFJd95o3Ei"
# ## 4. Don't repeat yourself
#
# An important use for functions is to avoid unnecessary repetition in code. When you write two pieces of very similar code, it's often convenient to make a single function.
#
# Each of the code blocks below contains two things:
# - A section of code that has some repetition
# - Some assert statements that check if the code works as intended.
#
# For each block:
# - Try to understand what the code does, and identify the repetition.
# - At the top of the code block, add a definition for a function (or several), that can handle the shared functionality.
# - Use your functions(s) in the code, and check that everything still works.

# %% id="JFc_E5sF5rt1"
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

# %% id="lirYtOcWpJ6m"
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

# %% id="mdNug4ct5645"
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

