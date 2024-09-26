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
# [index](https://colab.research.google.com/drive/1kFvnhumJ0tOTzDVJnIvvMDRRJ19yk9ZS)
#
# Previous module: [6. Loops](https://colab.research.google.com/drive/1wzbgGKNbZ1Ao0gHjN6jbFnWh0cxp8bQ1)
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

# %% id="wb98z1kBS9tm" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715765148268, "user_tz": -120, "elapsed": 5, "user": {"displayName": "Sheean Spoel", "userId": "10710218289228113472"}} outputId="1570596d-607d-483b-cad3-44a490cab0ee"
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
# However, for most functions, order does matter! An example you have already seen is `range`: the first argument is the _start_ and the second argument is the _stop_.

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

# %% [markdown] id="Dntbbioh29xm"
# ## Next module
# [8. Debugging](https://colab.research.google.com/drive/1Rj6qEuT3BFcQwexAxKg3zbAAD6t1cc8p)
