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
# # Module 12: Functions, bis
#
# ### Exercise solutions
#
# [Module 12](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/12%20functions%2C%20bis.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [11 - Working with files](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/11%20working%20with%20files.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/11%20working%20with%20files%20solutions.ipynb)

# %% [markdown]
# ## Exercise 12.1: function tricks

# %% [markdown]
# 1. In each of the code blocks below, predict the output, check your prediction by running the code, and try to explain any surprises.

# %%
def welcome(name=None):
    if name is None:
        return 'Welcome to my office. How can I help you?'
    return 'Please make yourself at home, ' + name + '!'

print(welcome()) # default option
print(welcome('Sheean'))


# %%
def table(number):
    return number, number * 2, number * 3 #return three numbers

first, second, third = table(5) # table(5) is (5, 10, 15) ; unpack these into three variables

print(third) #print the third


# %%
def contact(name, job):
    return 'For ' + job + ', contact ' + name + '.'

contact_line = contact(job='naming', name='Job') # we use named arguments, so we can supply `name` and `job` in any order
print(contact_line)


# %%
def exclaim(name):
    return name + '!'

def request(name):
    return name + '?'

def tell(how):
    return 'As my mother would say: ' + how('Julian')

print(tell(request))

# tell(request) will return `'As my mother would say: ' + how('Julian')`
# `how` is whatever we pass on as the argument to `tell`, in this case the function `request`
# so we can fill in `how('Julian')` as `request('Julian')`
# now we can look at the body of `request` to see what it does (it puts a
# question mark behind the name)

# %%
def make_enumerate(separator):
    def enumerate(items):
        if not len(items):
            return ''
        result = items[0]
        for item in items[1:]:
            result = result + separator + item
        return result
    return enumerate

with_semicolon = make_enumerate('; ')
fruits = with_semicolon(['apricot', 'banana', 'cherry'])
print(fruits)

# with_semicolon is the output of make_enumerate: another function.
# This function takes a list of strings as input and joins them with a semicolon
# between them. we can then call `with_semicolon` on the list of fruits.

# %% [markdown]
# 2. In each of the following code blocks, something is missing in the function definition. Add the missing element.

# %%
def combine(left, right):
    """ Compute the sum and the product of the arguments. """
    sum = left + right
    product = left * right
    return sum, product #return both the sum and the product

assert combine(2, 3) == (5, 6)


# %%
def announce_time(hour, minute=0): # minute should be optional, so we add a default value.
    """ Announce the time in a speaking clock manner. """
    if minute < 10:
        minute = '0' + str(minute)
    time = str(hour) + ':' + str(minute)
    return 'At the next beep, the time will be ' + time + '. BEEP!'

assert announce_time(12) == 'At the next beep, the time will be 12:00. BEEP!'


# %%
def echo(value):
    print(value)
    return value

assert echo('holiday') == 'holiday'

# %% [markdown]
# 3. In the following code block, write a function `month`, which returns a string name for given numeric month. Month `1` is `'January'` and month `12` is `December`. When no argument is passed, it should default to the current month. **Tip:** you can avoid writing a big `if`/`elif`/`else` tree by using a list of month names and using the month number as a list index.

# %%
# You may pretend that it is forever May
current_month = 5

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def month(number=current_month):
    '''
    Return the name of a month based on an number.

    Input should be an integer between 1 and 12. Returns None if this is not the case.
    If no month number is given, defaults to November.

    Returns a string with the name of the Month.
    '''

    if type(number) is not int or number < 1 or number > 12:
        return None

    index = number - 1
    return months[index]

assert month(3) == 'March'
assert month(4) == 'April'
assert month(11) == 'November'
assert month() == 'May'

# %% [markdown]
# 4. In the following code block, write a function `weekday`, which is analogous to `month` in the previous exercise. Day `1` is `'Monday'` while day `0` and day `7` are both `'Sunday'`. Can you avoid writing the string `'Sunday'` twice in your code?

# %%
# You may pretend it is forever Wednesday
current_weekday = 3

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def weekday(number=current_weekday):
    '''
    Return the name of a weekday based on an number.

    Input should be an integer between 0 and 7. Returns None if this is not the case.
    If no weekday number is given, defaults to Wednesday.

    Returns a string with the name of the weekday. Day 1 is 'Monday' while day 0
    and day 7 are both 'Sunday'.
    '''
    if type(number) is not int or number < 0 or number > 7:
        return None

    index = (number - 1) % 7
    return weekdays[index]

assert weekday() == 'Wednesday'
assert weekday(0) == 'Sunday'
assert weekday(7) == 'Sunday'
assert weekday(4) == 'Thursday'


# %% [markdown]
# ## Exercise 12.2: bonus

# %% [markdown]
# 1. In exercises 12.1.4 and 12.1.5, where you just implemented `month` and `weekday`, your code was likely very similar. How could you implement both functions without repeating yourself? Check your solution with assertions.

# %%
def make_namer(names, default):
    '''
    Make a function to give names (months, weekdays, etc) based on a number.

    Input:
    - A list of names (strings)
    - A default input value for the function

    Returns a function that takes a number and returns the corresponding name.
    1 is the first list in the name, etc.
    '''
    size = len(names)

    def name(number=default):
        '''
        Gives the name corresponding to a number
        '''
        if type(number) is not int or number < 0 or number > size:
            return None

        index = (number - 1) % size
        return names[index]

    return name

# now we can make our month and weekday functions based on make_namer

current_month = 11
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

current_weekday = 3
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

month = make_namer(months, current_month)
weekday = make_namer(weekdays, current_weekday)

# repeat the assert statements above to show everything still works

assert month(3) == 'March'
assert month(4) == 'April'
assert month(11) == 'November'
assert month() == 'November'

assert weekday() == 'Wednesday'
assert weekday(0) == 'Sunday'
assert weekday(7) == 'Sunday'
assert weekday(4) == 'Thursday'


# %% [markdown]
# 2. Write a function `create_date_format`, which takes two arguments that determine how a date should be displayed. The first argument is function that transforms a weekday number to a string suitable for display, the second argument is a function that transforms a month number. Both arguments default to just displaying the number as-is. `create_date_format` returns a new function. The latter function takes any date defined by a year, month, day and weekday, and returns a string suitable for displaying that date as a whole.

# %%
# For this code block, you need to have `month` and `weekday`
# in your runtime from previous exercises.

def create_date_format(weekday_formatter=str, month_formatter=str):
    '''
    Creates a function that formats dates.

    Input:
    - weekday_formatter: a function that converts the day of the week (number) to a string
    - month_formatter: a function that converts the month (number) to a string

    If these functions are not supplied, the month and day are shown as-is.

    Output: A function that takes integers for the year, month, day of the
    month, and day of the week, and returns a string with the formatted date.
    '''

    def format_date(year, month, day_of_month, day_of_week):
        '''
        Format a date in a nice string.
        '''

        day_string = weekday_formatter(day_of_week)
        month_string = month_formatter(month)

        nice_string = day_string + ', ' + month_string + ' ' + str(day_of_month) + ', ' + str(year)
        return nice_string

    return format_date

# Your definition of create_date_format here

wordy_format = create_date_format(weekday, month)
cryptic_format = create_date_format()

assert wordy_format(2023, 4, 11, 2) == 'Tuesday, April 11, 2023'
assert cryptic_format(2023, 4, 11, 2) == '2, 4 11, 2023'


# %% [markdown]
# ## Exercise 12.3: ultimate FizzBuzz (more bonus)
#
# 1. Write two functions `fizz(number)` and `buzz(number)`. If `number` is divisible by 3, `fizz` should return the string `'Fizz'`; otherwise, it should return the empty string `''`. `buzz` should work like `fizz`, but for divisibility by 5 and the string `'Buzz'`.

# %%
# Your solution here

def fizz(number):
    '''
    Returns 'Fizz' if a number is divisible by 3, otherwise the empty string
    '''

    if number % 3 == 0:
        return 'Fizz'
    else:
        return ''

def buzz(number):
    '''
    Returns 'Buzz' if a number is divisible by 5, otherwise the empty string
    '''

    if number % 5 == 0:
        return 'Buzz'
    else:
        return ''

for number in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]:
    assert fizz(number) == '', str(number) + ' is not divisible by 3'
for number in [3, 6, 9, 12, 15, 18, 21, 24, 27]:
    assert fizz(number) == 'Fizz', str(number) + ' is divisible by 3'
for number in [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]:
    assert buzz(number) == '', str(number) + ' is not divisible by 5'
for number in [5, 10, 15, 20, 25, 30, 35, 40]:
    assert buzz(number) == 'Buzz', str(number) + ' is divisible by 5'


# %% [markdown]
# 2. Using your functions `fizz` and `buzz` from step 1, write the function `fizzbuzz(number)`, which implements the well-known rules from before, but with a slight **twist**:
#     - If the number is divisible by 3 and 5, return `'FizzBuzz'`.
#     - If the number is divisible by 3 but not by 5, return `'Fizz'`.
#     - If the number is divisible by 5 but not by 3, return `'Buzz'`.
#     - In all other cases, return the number itself **as a string**.

# %%
# Your solution here

def fizzbuzz(number):
    '''
    Turns a number into a fizzbuzz string.

    - If the number is divisible by 3 and 5, returns 'FizzBuzz'.
    - If the number is divisible by 3 but not by 5, returns 'Fizz'.
    - If the number is divisible by 5 but not by 3, returns 'Buzz'.
    - In all other cases, returns the number itself as a string.
    '''

    fizzbuzzed = fizz(number) + buzz(number)

    if fizzbuzzed:
        return fizzbuzzed
    else:
        return str(number)

for number in [1, 2, 4, 7, 8, 11, 13, 14]:
    assert fizzbuzz(number) == str(number), str(number)
for number in [3, 6, 9, 12, 18, 21, 24, 27]:
    assert fizzbuzz(number) == 'Fizz', str(number)
for number in [5, 10, 20, 25, 35, 40]:
    assert fizzbuzz(number) == 'Buzz', str(number)
for number in [15, 30, 45, 60, 75]:
    assert fizzbuzz(number) == 'FizzBuzz', str(number)


# %% [markdown]
# 3. Write a function `chunk10(sequence)` that takes an iterable `sequence` and returns a list of lists: the first sublist contains the first ten elements of `sequence`, the second sublist contains the next ten elements of `sequence`, and so on. You may assume that the number of values in `sequence` is an exact multiple of 10.

# %%
# Your solution here

def chunk10(sequence):
    '''
    Splits a sequence into chunks of 10 elements
    '''

    items = list(sequence)
    chunks = []

    for position in range(0, len(sequence), 10):
        chunk = items[position: position + 10]
        chunks.append(chunk)

    return chunks

assert chunk10('Jelte!!!!!') == [list('Jelte!!!!!')]
assert chunk10('Hey Julian, let us have lunch!') == [
    list('Hey Julian'),
    list(', let us h'),
    list('ave lunch!'),
]
assert chunk10(range(20)) == [list(range(10)), list(range(10, 20))]


# %% [markdown]
# 4. In step 1, you may have written definitions for `fizz` and `buzz` that look very similar to each other. Can you think of a way to avoid repeating the common elements?

# %%
# Your solution here

def fizz_or_buzz(number, message='Fizz', denominator=3):
    '''
    If number is divisible by denominator, return the message. Otherwise, return the empty string.
    '''
    if number % denominator == 0:
        return message
    else:
        return ''

def fizz(number):
    return fizz_or_buzz(number)

def buzz(number):
    return fizz_or_buzz(number, 'Buzz', 5)

for number in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]:
    assert fizz(number) == '', str(number) + ' is not divisible by 3'
for number in [3, 6, 9, 12, 15, 18, 21, 24, 27]:
    assert fizz(number) == 'Fizz', str(number) + ' is divisible by 3'
for number in [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]:
    assert buzz(number) == '', str(number) + ' is not divisible by 5'
for number in [5, 10, 15, 20, 25, 30, 35, 40]:
    assert buzz(number) == 'Buzz', str(number) + ' is divisible by 5'

# %% [markdown]
# 5. In *exercise 7.1.3*, you documented the function `join_commas`. We did not actually need to write that function, because it is built into Python, although it goes by the name `', '.join`. That notation also works with other strings, as we demonstrate below. We also remind you of `map`, which appeared in the lecture.<br><br>
# Using these functions, as well as your own `fizzbuzz` from step 2 and your own `chunk10` from step 3, try to recreate (roughly) the same `FizzBuzz` output for the numbers 1 through 100 as in *exercise 6.2.4*, in as little code as you can.

# %%
# The following code is just for illustration.
# You do not need it in your solution.
fruits = ['apricot', 'banana', 'cherry']
print(', '.join(fruits))
print('\n'.join(fruits))
numbers = list(range(10))
print(numbers)
strings = map(str, numbers)
print(list(strings))

# %%
chunks = chunk10(range(100))

for chunk in chunks:
    fizzbuzzed = map(fizzbuzz, chunk)
    print(', '.join(fizzbuzzed))

# %% [markdown]
# *There is no next module. This is the end of the course!*
