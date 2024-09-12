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
# # Module 7: Functions
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1s05aR4wn2dU1C3se1oXfqKz2EY5ilrno)
#
# Previous module: [6. Loops](https://colab.research.google.com/drive/1AZY4ESmsKKMvbalBDLlMrezAM5NzXXxV)
#
# ### This module
#
# - Storing code in a variable so you can reuse it.
# - Being explicit about the purpose of your code.

# %% [markdown] id="mnc8HshNPLte"
# ## (Re)Introducing functions
#
# A function is a reusable piece of code, stored in a variable. You *call* a function by passing it a list of *arguments* between parentheses. The function *returns* a value, which you can then use in an expression or store in another variable. We have already seen several functions:

# %% id="IP2mOWYgR-QA"
result = ord('🎵')
print(type(result), result)

result = len([1, 2, 3])
print(type(result), result)

result = str(ord)
print(type(result), result)

# %% [markdown] id="u_YUDiccZKwh"
# The fact that functions are variables, is illustrated by the fact that you can store them in variables and even reassign them:

# %% id="Mct6Hy3HZa5H"
my_ord = ord
print(my_ord('a'))
ord = chr
print(ord(97))

# don't do this with 'list'!!!!!

# back to sanity!
ord = my_ord

# this can also restore sanity
# %reset_selective ord

# reset resets everything
# %reset

ord('a')

# %% [markdown] id="hBgqVL7sSyFx"
# The list of arguments may be empty. For example, if you pass no arguments to `list`, it returns an empty list:

# %% id="wb98z1kBS9tm"
result = list()
print(result)

# %% [markdown] id="Byutz190TEH-"
# You can also pass multiple arguments (depending on the function).

# %% id="N7YW9_X_UOuB"
result = max(3, 4, 5)
print(result)

# %% [markdown] id="H0SocqBbXQ6f"
# A *named argument* or *keyword argument*, prefixed with `name=`, makes the purpose of the argument explicit. Below, the argument with the name `end` has the value `' '`.

# %% id="uTk4InjdXg5g"
print('one', end=' ')
print('two')

# %% [markdown] id="dCUHGgepctcp"
# Arguments *without* a name are called *positional* arguments, because their roles are determined by the order in which they are supplied.
#
# In our example of `max(3, 4, 5)` above, `3`, `4`, and `5` are positional arguments. In this case, the order of the numbers does not actually matter (the maximum is the same, no matter what).
#
# However, for most functions, this is not the case! An example you have already seen is `range`: the first argument is the _start_ and the second argument is the _stop_.

# %% id="yCyPbsvAd5PB"
assert max(3, 4, 5) is max(4, 3, 5)

assert range(1, 5) is not range(5, 1)

# %% [markdown] id="ECGJttnRUX_J"
# A function may return "nothing", i.e., `None`.

# %% id="gAMO-QD4Uuxe"
result = print('hello')
print(result)

# %% [markdown] id="Bj4diwbcU1Q7"
# A function may even return multiple results, i.e., a tuple. We can *unpack* those directly into multiple variables, but we can also store the whole tuple in a single variable.

# %% id="yYRQIGnoVHWA"
my_tuple = tuple(['Jelte', 'Julian'])
result1, result2 = my_tuple
print(my_tuple)
print(result1)
print(result2)

# %% [markdown] id="xMHYhvPhVXet"
# Some functions have *side effects*: apart from taking arguments and returning results, they also have some other external effect.

# %% id="OKEha-rwVo99"
result1 = input('Please enter PIN: ') # returns input from user
result2 = print(result1) # returns nothing
print(result2)
print(result1)

# %% [markdown] id="emAs76qOagVF"
# ## Functions are awesome!
#
# The following code, which does *not* use enough functions, is **bad**:

# %% id="n0UOjklcbEHQ"
print('"banana" has 6 characters and starts with a lowercase')
print('"Ada" has 3 characters and starts with an uppercase')
print('"epigraph" has 8 characters and starts with a lowercase')

# %% [markdown] id="vAt_0PfecAGK"
# Problems:
#
# - repetitive
# - not explicit
# - unmaintainable
#
# To some extent, we can address these problems with a loop:

# %% id="MeUnr3KNcaVZ"
words = ['banana', 'Ada', 'epigraph']

for word in words:
    quoted = '"' + word + '"'
    length = len(word)
    first_character = word[0]
    if 'A' <= first_character <= 'Z':
        initial = 'an uppercase'
    else:
        initial = 'a lowercase'
    print(quoted, 'has', length, 'characters and starts with', initial)


# %% [markdown] id="FL0w8VMkeLm7"
# BUT
#
# - still not explicit
# - still repetitive, need to repeat the loop if I want to do this elsewhere

# %% [markdown] id="bBiz8La8jv81"
# Functions let us solve all problems!

# %% id="HOjpPJBNiSvr"
def describe(word):
    quoted = '"' + word + '"'
    length = str(len(word))
    first_character = word[0]
    if 'A' <= first_character <= 'Z':
        initial = 'an uppercase'
    else:
        initial = 'a lowercase'
    return quoted + ' has ' + length + ' characters and starts with ' + initial

words = ['banana', 'Ada', 'epigraph']

for word in words:
    print(describe(word))


# %% [markdown] id="y77LwKKjk-2D"
# ## Basic function definitions
#
# At a minimum, you need the keyword `def`, a name, a pair of parentheses, a colon, and an indented block. The indented block is called the *function body*. It can contain anything!

# %% id="Ph3RsaBbllvB"
# Defining the function with the name "example"
def example():
    pass # ah, that placeholder again

# Calling the function with the name "example"
result = example()
print(result)


# %% [markdown] id="6Esxqtn0y1Ai"
# Keep in mind that a function *definition* only stores the code of the function body inside a variable with the name of the function. The code **does not run** until you *call* the function.

# %% id="vBfiX0-WzWQg"
def example():
    # Don't call print inside a function!
    # We only do this here for demonstration purposes.
    print('Hello, world!')

print(type(example), example)


# %% [markdown] id="S3cY2mRgl9z8"
# Between the parentheses, we list the *parameters*, the "slots" that can be filled by passing arguments when calling the function.
#
# The parameters (and any new variables that you make within the function body) have limited _scope_: they only live within the body of the function.

# %% id="fWAzMGqfnC8p"
def example(name, age):
    print(name)
    print(age)

name = 'Sheean'
age = 36

print(name)
print(age)

result = example('Julian', 35)
print(result)

print(name)
print(age)


# %% [markdown] id="J5Pd_TjZqnwj"
# At the end of the function body, a function will implicitly return `None`. The `return` keyword lets you return a different value, return before the end of the body, or both. You can use the keyword multiple times, but **a function can return only once**, so an early return will skip the remainder of the function body.

# %% id="48ARWWmvrgjz"
def heaviness(item, weight):
    if type(weight) not in (int, float):
        # early return, implicit None
        return
    if weight >= 5:
        # early return, different value
        return 'heavy'
    # final return, different value
    return 'light'

result = heaviness('letter', 'paper weight')
print(result)

result = heaviness('feather', 0.01)
print(result)

result = heaviness('bowling ball', 8)
print(result)


# %% [markdown] id="kOlF8tonzwZr"
# Functions should **not** have side effects unless that is the very purpose of the function (like with `print` and `input`). Most functions should return a value rather than printing something to the screen!

# %% id="EHX1V-E71EkI"
# GOOD: function returns a value
def exclaim(text):
    return text + '!'

value = exclaim('Julian')
print(value)

# BAD: function prints to the screen
def exclaim(text):
    print(text + '!')

value = exclaim('Julian')
print(value)

# OK: function is intended as a special print wrapper
def fancy_print(text):
    print('>>>', text, '<<<')

fancy_print('Julian')


# %% [markdown] id="spLYBkqtvDmF"
# It is a good habit to start a function with a *documentation string*, **docstring** for short. A docstring should explain the parameters and possible return values of the function, as well as any rules or side effects that apply.
#
# A docstring should start with a short description of the function that fits on a single line. If there is more to explain, add the rest after a blank line.
#
# By convention, docstrings use three double quotes.

# %% id="DR6t3PCCvSEX"
def heaviness(item, weight):
    """
    Given the name of an item and its weight in kg, classify its heaviness.

    If the weight is not a number, it cannot be classified. Otherwise, the
    classification is returned as a string: either 'light' or 'heavy'.
    """
    if type(weight) not in (int, float):
        return
    if weight >= 5:
        return 'heavy'
    return 'light'

print(heaviness.__doc__)

print(len.__doc__)
print(ord.__doc__)
print(print.__doc__)


# %% [markdown] id="aPFGhEVz40JP"
# ## Exercise 7.1: functions

# %% [markdown] id="hfcz-cSEKZWW"
# 1. We have seen several standard functions during the course, such as `ord` and `len`. List as many as you can from memory. Try to list the types of the parameters and return values of each function as well. Do any of these functions have side effects?

# %% [markdown] id="BUnMsiUzKbws"
# 2. For exercise purposes, code in the following blocks may call `print` inside a function and omit a docstring. Predict the output, then run the code to see whether your prediction was right. Try to explain any discrepancies.

# %% id="_3va9jT5O0H7"
def greet(name):
    return 'Hello, ' + name + '!'

print(greet('Berit'))

# %% id="vdTIwoGxM_JV"
name = 'Luka'

def exclaim(name):
    print(name + '!')


# %% id="30fv8SAMOblV"
def false():
    return True

print(False)

# %% id="ongrNaZFNNmV"
length = 5
width = 2

def calculate_area():
    area = length * width

print(calculate_area())


# %% id="MSkOCMMyNoUO"
def question(name):
    return 'Who is ' + name + '?'

question('Sheean')


# %% id="72DDRhD5OQ0g"
def add(left, right):
    return left + right

print(add('sweet', 'addition') * add(1, 1))

# %% id="L0GlJecf8ntf"
name = 'Julian'
age = 36

print(name)

def example(name):
    print(name)
    name = 'Berit'
    print(name)
    print(age)

print(name)
print(example)
print(name)
example('Jelte')
print(name)
print(age)


# %% [markdown] id="Rwvwlpp0-Hrt"
# 3. In each of the following code blocks, write a docstring for the function, then add assertions and run the block to check that your documentation is correct.

# %% id="ajcRnvzQQ9c5"
def odd(number):
    return number % 2 == 1


# %% id="giU_bIKrRME4"
def magic(word):
    if not word or type(word) != str:
        return False
    if 'A' <= word[0] <= 'Z':
        return True
    return False


# %% id="pAChbRWn-SKS"
def join_commas(words):
    first, *rest = list(words)
    text = first
    for word in rest:
        text = text + ', ' + word
    return text


# %% [markdown] id="mc9RtAeATiHw"
# 4. Write a function `is_number` that takes one argument. If the argument is a number, it should return `True`; otherwise, it should return `False`. Make sure to include a docstring!

# %% id="Ap33-rF-UbsB"
# Your definition of is_number here

# The following lines will check your solution (no output is good)
assert is_number(0)
assert is_number(10)
assert is_number(0.5)
assert is_number(8 / 5)
assert not is_number(None)
assert not is_number('dear')
assert not is_number('123')

# %% [markdown] id="apA7o120TYRl"
# ## Exercise 7.2: bonus

# %% [markdown] id="nM43w3VlB3-O"
# 1. Write a function `last_a_index` that, given a string, returns the **last** index of the letter `'a'` in the string. If there is no `'a'` in the string, the function should return `None`.

# %% id="I5s4_a53ENJC"
# Define last_a_index here

assert last_a_index('banana') == 5
assert last_a_index('cherry') == None
assert last_a_index('Once upon a time, there was a dragon') == 32

# %% [markdown] id="z4z3-dOaVROx"
# 2. Write a function `replace` with three string arguments: `text`, `query` and `replacement`. It should return a copy of `text` in which all occurrences of `query` are replaced by `replacement`. For example, `replace('small', 'a', 'e')` should return `'smell'`. You may assume that `query` is always a single character. For an additional challenge, you can try to also handle multi-character query strings. For ultimate challenge, try to think of a way to handle the empty string!

# %% id="kyQwfz-mYvfW"
# Define replace here

assert replace('small', 'a', 'e') == 'smell'
assert replace('banana', 'a', 'o') == 'bonono'
assert replace('cherry', 'a', 'x') == 'cherry'


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
    return len(word), casing

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
# As mentioned previously, a function is just a variable. That means you can do the same things with it as with other values. For example, you can pass a function as an argument to another function:

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
# ## Exercise 7.3: function tricks

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
# You may pretend that it is forever April
current_month = 4

# Your definition of month here

assert month(3) == 'March'
assert month(4) == 'April'
assert month(11) == 'November'
assert month() == 'April'

# %% [markdown] id="WuRrElhUsD40"
# 4. In the following code block, write a function `weekday`, which is analogous to `month` in the previous exercise. Day `1` is `'Monday'` while day `0` and day `7` are both `'Sunday'`. Can you avoid writing the string `'Sunday'` twice in your code?

# %% id="WUGQqmJysrqS"
# You may pretend it is forever Tuesday
current_weekday = 2

# Your definition of weekday here

assert weekday() == 'Tuesday'
assert weekday(0) == 'Sunday'
assert weekday(7) == 'Sunday'
assert weekday(4) == 'Thursday'

# %% [markdown] id="ZvfEq3NctoOo"
# ## Exercise 7.4: bonus

# %% [markdown] id="8au2fNRutw8i"
# 1. In exercises 7.3.4 and 7.3.5, where you just implemented `month` and `weekday`, your code was likely very similar. How could you implement both functions without repeating yourself? Check your solution with assertions.

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
# ## Exercise 7.5: ultimate FizzBuzz (more bonus)
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
# Using these functions, as well as your own `fizzbuzz` from step 2 and your own `chunk10` from step 3, try to recreate (roughly) the same `FizzBuzz` output for the numbers 1 through 100 as in [exercise 6.2.4](https://colab.research.google.com/drive/1AZY4ESmsKKMvbalBDLlMrezAM5NzXXxV#scrollTo=uyqbuhKsUlhG), in as little code as you can.

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

# %% [markdown] id="Dntbbioh29xm"
# ## Next module
#
# [8. Debugging](https://colab.research.google.com/drive/1yQskT6SyKvXtXewx5kCla2NOmasgP8Vi)
