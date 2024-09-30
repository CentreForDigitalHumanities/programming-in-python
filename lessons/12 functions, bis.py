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

# %% [markdown] id="uHYIr4R9dWyQ"
# # Module 12: Functions, bis
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [11. Working with files](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/11%20working%20with%20files.ipynb)
#
# ### This module
#
# - Master the things you can do with functions

# %% [markdown] id="3Lx61L5B0Zqe"
# ## Refining parameters and return values

# %% [markdown] id="gRae5PaguhV9"
# ### Returning multiple values (in a tuple)

# %% id="MJqHyAI31FLZ"
def word_statistics(word):
    """ Given a string, return its length and the case of its first letter. """
    if 'A' <= word[0] <= 'Z':
        casing = 'upper'
    else:
        casing = 'lower'
    # Note how we return TWO things on the next line
    return len(word), casing

# And here, we unpack both return values.
size, initial = word_statistics('Sheean')
print(size)
print(initial)


# %% [markdown] id="1ORLASkU2Uga"
# ### Optional parameters
#
# Parameters can be made *optional* by using the notation `=None` in the parameter list.

# %% id="IuDsXgrK3rK8"
def emphasize(word, emphasis=None):
    """
    Given a string, return a version with an exclamation mark appended.

    The exclamation mark can be replaced by passing the override in a
    second argument.
    """
    if emphasis == None:
        return word + '!'
    return word + emphasis

print(emphasize('Julian'))
print(emphasize('Julian', '!!!'))


# %% [markdown] id="2gPmuYUe1nyO"
# ### Parameters with default values
#
# The notation `=None` is actually a special case. You can use any value as a default for a parameter. However, it is easy to make mistakes in this way. In case of doubt, just use `None` and add a check inside the function body, as demonstrated above.

# %% id="IqabfNzi2-XV"
# Literal strings, numbers and booleans are safe
def default_string(value='hello'):
    return value

def default_int(value=10):
    return value

def default_bool(value=True):
    return value

# Do not use variables as default values!
name = 'Julian'
def default_name(value=name):
    return value

name = 'Sheean'
print(default_name())

# Do not use data structures as default values!
def append_list(container=[], value=1):
    container.append(value)
    return container

print(append_list())
print(append_list())


# %% [markdown] id="_mTHAoog6glc"
# ### Mixing positional and named arguments
#
# So far, we demonstrated functions where every parameter has its own unique name. With such parameters, the caller is free to choose between positional arguments and named arguments. The order of named arguments can be freely chosen, but they must come after all positional arguments.

# %% id="ETGRDi8J7cyP"
def tax_rate(income, entrepreneur):
    """ Determine tax rate, given income and whether payer is entrepreneur. """
    if entrepreneur:
        return 20
    first_bracket = min(income, 50000)
    second_bracket = income - first_bracket
    return (first_bracket * 30 + second_bracket * 40) / income

print(tax_rate(40000, True))
print(tax_rate(40000, entrepreneur=True))
print(tax_rate(income=40000, entrepreneur=True))
print(tax_rate(entrepreneur=True, income=40000))
print(tax_rate(True, income=40000))
print(tax_rate(income=40000, True))


# %% [markdown] id="1jWzKu5omWUV"
# ## Functions as first-class citizens
#
# As mentioned previously, a function is just a value. That means you can do the same things with it as with other values. For example, you can pass a function as an argument to another function:

# %% id="ukVglqcwsAdT"
def exclaim(text):
    return text + '!'

fruits = ['apricot', 'banana', 'cherry']

exclaimed_fruits = map(exclaim, fruits)

print(type(exclaimed_fruits), exclaimed_fruits)

list(exclaimed_fruits)


# %% [markdown] id="l4dAFklEvdhZ"
# What is going on inside `map`? Something like this:

# %% id="V2-kY5O6xHRo"
def my_map(function, values):
    """ Repeat `function` for every value in `values`. """
    for value in values:
        result = function(value)
        # there is an additional step that we will cover later


# %% [markdown] id="TZXA2q46taZi"
# Also, a function can define another function inside its body and then use and/or return it:

# %% id="fG6-q8EatpRz"
def make_greeter(prefix, suffix):
    """ Create a function that greets a person with the given phrasing. """
    def greeter(name):
        """ Wrap the given name in a greeting. """
        return prefix + ', ' + name + suffix
    return greeter

greet_british = make_greeter('How do you do', '?')
greet_american = make_greeter('Hi there', '!')

print(greet_british('Sheean'))
print(greet_british('Julian'))
print(greet_american('Sheean'))
print(greet_american('Julian'))


# %% [markdown] id="1xUD2ZNjcqEZ"
# ## Exercise 12.1: function tricks

# %% [markdown] id="hxRC5Nx-cyM4"
# 1. In each of the code blocks below, predict the output, check your prediction by running the code, and try to explain any surprises.

# %% id="HPxio0q6c-M9"
def welcome(name=None):
    if name is None:
        return 'Welcome to my office. How can I help you?'
    return 'Please make yourself at home, ' + name + '!'

print(welcome())
print(welcome('Sheean'))


# %% id="NxXqK4ROdxva"
def table(number):
    return number, number * 2, number * 3

first, second, third = table(5)

print(third)


# %% id="EVCf3w9qfBCU"
def contact(name, job):
    return 'For ' + job + ', contact ' + name + '.'

contact_line = contact(job='naming', name='Job')
print(contact_line)


# %% id="OUSpe-hPl6-G"
def exclaim(name):
    return name + '!'

def request(name):
    return name + '?'

def tell(how):
    return 'As my mother would say: ' + how('Julian')

print(tell(request))


# %% id="uSN17qnvmoWv"
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


# %% [markdown] id="CKma4p6Egkwb"
# 2. In each of the following code blocks, something is missing in the function definition. Add the missing element.

# %% id="SaygnjMygwNF"
def combine(left, right):
    """ Compute the sum and the product of the arguments. """
    sum = left + right
    product = left * right
    return product

assert combine(2, 3) == (5, 6)


# %% id="GqIgTcG6hMuG"
def announce_time(hour, minute):
    """ Announce the time in a speaking clock manner. """
    if minute < 10:
        minute = '0' + str(minute)
    time = str(hour) + ':' + str(minute)
    return 'At the next beep, the time will be ' + time + '. BEEP!'

assert announce_time(12) == 'At the next beep, the time will be 12:00. BEEP!'


# %% id="nH77gJdOkS5b"
def echo(value):
    print(value)
    return value

assert echo('holiday') == 'holiday'

# %% [markdown] id="YG5XrO1PoIJx"
# 3. In the following code block, write a function `month`, which returns a string name for given numeric month. Month `1` is `'January'` and month `12` is `December`. When no argument is passed, it should default to the current month. **Tip:** you can avoid writing a big `if`/`elif`/`else` tree by using a list of month names and using the month number as a list index.

# %% id="TnuU_I0Tq9wQ"
# You may pretend that it is forever May
current_month = 5

# Your definition of month here

assert month(3) == 'March'
assert month(4) == 'April'
assert month(11) == 'November'
assert month() == 'May'

# %% [markdown] id="WuRrElhUsD40"
# 4. In the following code block, write a function `weekday`, which is analogous to `month` in the previous exercise. Day `1` is `'Monday'` while day `0` and day `7` are both `'Sunday'`. Can you avoid writing the string `'Sunday'` twice in your code?

# %% id="WUGQqmJysrqS"
# You may pretend it is forever Wednesday
current_weekday = 3

# Your definition of weekday here

assert weekday() == 'Wednesday'
assert weekday(0) == 'Sunday'
assert weekday(7) == 'Sunday'
assert weekday(4) == 'Thursday'

# %% [markdown] id="ZvfEq3NctoOo"
# ## Exercise 12.2: bonus

# %% [markdown] id="8au2fNRutw8i"
# 1. In exercises 12.1.4 and 12.1.5, where you just implemented `month` and `weekday`, your code was likely very similar. How could you implement both functions without repeating yourself? Check your solution with assertions.

# %% id="JFhOX_Z5uVfC"

# %% [markdown] id="Gx54DrgJuWKg"
# 2. Write a function `create_date_format`, which takes two arguments that determine how a date should be displayed. The first argument is function that transforms a weekday number to a string suitable for display, the second argument is a function that transforms a month number. Both arguments default to just displaying the number as-is. `create_date_format` returns a new function. The latter function takes any date defined by a year, month, day and weekday, and returns a string suitable for displaying that date as a whole.

# %% id="0KyXFHEWwZ45"
# For this code block, you need to have `month` and `weekday`
# in your runtime from previous exercises.

# Your definition of create_date_format here

wordy_format = create_date_format(weekday, month)
cryptic_format = create_date_format()

assert wordy_format(2023, 4, 11, 2) == 'Tuesday, April 11, 2023'
assert cryptic_format(2023, 4, 11, 2) == '2, 4 11, 2023'

# %% [markdown] id="b-p6Ct5_0I-x"
# ## Exercise 12.3: ultimate FizzBuzz (more bonus)
#
# 1. Write two functions `fizz(number)` and `buzz(number)`. If `number` is divisible by 3, `fizz` should return the string `'Fizz'`; otherwise, it should return the empty string `''`. `buzz` should work like `fizz`, but for divisibility by 5 and the string `'Buzz'`.

# %% id="407dPPK966R9"
# Your solution here

for number in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]:
    assert fizz(number) == '', str(number) + ' is not divisible by 3'
for number in [3, 6, 9, 12, 15, 18, 21, 24, 27]:
    assert fizz(number) == 'Fizz', str(number) + ' is divisible by 3'
for number in [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]:
    assert buzz(number) == '', str(number) + ' is not divisible by 5'
for number in [5, 10, 15, 20, 25, 30, 35, 40]:
    assert buzz(number) == 'Buzz', str(number) + ' is divisible by 5'

# %% [markdown] id="QCKc52-r9DrX"
# 2. Using your functions `fizz` and `buzz` from step 1, write the function `fizzbuzz(number)`, which implements the well-known rules from before, but with a slight **twist**:
#     - If the number is divisible by 3 and 5, return `'FizzBuzz'`.
#     - If the number is divisible by 3 but not by 5, return `'Fizz'`.
#     - If the number is divisible by 5 but not by 3, return `'Buzz'`.
#     - In all other cases, return the number itself **as a string**.

# %% id="NFADyIW3-7qt"
# Your solution here

for number in [1, 2, 4, 7, 8, 11, 13, 14]:
    assert fizzbuzz(number) == str(number), str(number)
for number in [3, 6, 9, 12, 18, 21, 24, 27]:
    assert fizzbuzz(number) == 'Fizz', str(number)
for number in [5, 10, 20, 25, 35, 40]:
    assert fizzbuzz(number) == 'Buzz', str(number)
for number in [15, 30, 45, 60, 75]:
    assert fizzbuzz(number) == 'FizzBuzz', str(number)

# %% [markdown] id="o_3wq4agCCZH"
# 3. Write a function `chunk10(sequence)` that takes an iterable `sequence` and returns a list of lists: the first sublist contains the first ten elements of `sequence`, the second sublist contains the next ten elements of `sequence`, and so on. You may assume that the number of values in `sequence` is an exact multiple of 10.

# %% id="4c0A4kMfDdvt"
# Your solution here

assert chunk10('Sheean!!!!!') == [list('Sheean!!!!!')]
assert chunk10('Hey Julian, let us have lunch!') == [
    list('Hey Julian'),
    list(', let us h'),
    list('ave lunch!'),
]
assert chunk10(range(20)) == [list(range(10)), list(range(10, 20))]

# %% [markdown] id="HBA4z4yVIhsn"
# 4. In step 1, you may have written definitions for `fizz` and `buzz` that look very similar to each other. Can you think of a way to avoid repeating the common elements?

# %% id="5g4BRdpLJLIc"
# Your solution here

for number in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]:
    assert fizz(number) == '', str(number) + ' is not divisible by 3'
for number in [3, 6, 9, 12, 15, 18, 21, 24, 27]:
    assert fizz(number) == 'Fizz', str(number) + ' is divisible by 3'
for number in [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]:
    assert buzz(number) == '', str(number) + ' is not divisible by 5'
for number in [5, 10, 15, 20, 25, 30, 35, 40]:
    assert buzz(number) == 'Buzz', str(number) + ' is divisible by 5'

# %% [markdown] id="BXzFYNGmPeO6"
# 5. In exercise 7.1.3, you documented the function `join_commas`. We did not actually need to write that function, because it is built into Python, although it goes by the name `', '.join`. That notation also works with other strings, as we demonstrate below. We also remind you of `map`, which appeared in the lecture.<br><br>
# Using these functions, as well as your own `fizzbuzz` from step 2 and your own `chunk10` from step 3, try to recreate (roughly) the same `FizzBuzz` output for the numbers 1 through 100 as in exercise 6.2.4, in as little code as you can.

# %% id="nDGUS26IMApD"
# The following code is just for illustration.
# You do not need it in your solution.
fruits = ['apricot', 'banana', 'cherry']
print(', '.join(fruits))
print('\n'.join(fruits))
numbers = list(range(10))
print(numbers)
strings = map(str, numbers)
print(list(strings))

# %% [markdown] id="hSkvuphJ5Sw9"
# *There is no next module. This is the end of the course!*
