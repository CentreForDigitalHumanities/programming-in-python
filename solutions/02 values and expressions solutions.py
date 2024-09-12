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
# # Module 2: Values and expressions
#
# ### Exercise solutions
#
# [Module 2](https://colab.research.google.com/drive/17K6C_EZoeGtRxoTbYQvygFEdpWgQ2QFp)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1s05aR4wn2dU1C3se1oXfqKz2EY5ilrno)
#
# Previous module: [1. Introduction](https://colab.research.google.com/drive/1i4wJpUIr77Fh1renWNjt00Bd51NbC1nB) - [solutions](https://colab.research.google.com/drive/1RIwG7hA-Ymjcm1dmSW6wA_hu1clDNrAd)

# %% [markdown] id="pDU1uK2Igmki"
# ## Exercise 2.1: Variables and state
#
# In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% id="FydkKnx_hUPq" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680606359445, "user_tz": -120, "elapsed": 420, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="0cce4013-6c8a-44a9-ecc8-6720dcfcb047"
flavor = 'vanilla'
print(flavor)

# %% id="LTWods50h-Ij" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680606363219, "user_tz": -120, "elapsed": 402, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="41e65fc2-80ff-45ea-dfd1-8109e8d96b95"
temperature = 70
print(flavor)

# %% [markdown] id="pmnKAg7H95BW"
# The variable `flavor` was retained from the previous code block. The variable `temperature` is not used here.

# %% id="l2vT4L7piGRf" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680606385469, "user_tz": -120, "elapsed": 450, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="472eeb4a-fe6e-4696-9817-0a481a153d5a"
print(temperature)
temperature = 35
print(temperature)

# %% [markdown] id="ElhEcRIB-EsA"
# `temperature` is first printed as it was retained from the previous code block. Then, it is reassigned and printed again.

# %% id="k1Z_yWLXiWy7" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680606390493, "user_tz": -120, "elapsed": 230, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="41a6d3ad-c50e-4bd4-f347-07eae4f8fae9"
dog_name = 'Bobby'
cat_name = 'Garfield'
dog_name = cat_name
cat_name = dog_name
print(dog_name)
print(cat_name)

# %% [markdown] id="iFkF67zp-LJk"
# On line 3, it is important to realize that `dog_name` gets *the value of* `cat_name`. There is no permanent tie between the variables. After line 3, both variables have the same value. Hence, `cat_name` cannot change into anything else on line 4. The program has effectively forgotten the value `'Bobby'`.

# %% [markdown] id="BZ50KykuAYPs"
# Before running the following code, try to explain why it does *not* output `chocolate`.

# %% id="X3xHg6K4Aicn" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680606431330, "user_tz": -120, "elapsed": 202, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="5a5e974b-cb7a-466b-f900-b8b586080212"
sweet = 'chocolate'
savory = 'cheese'
dessert = 'sweet'
print(dessert)

# %% [markdown] id="1qb27-Rf-wIH"
# On line 3, `'sweet'` is quoted, so Python considers it a string. It does not recognize it as a variable, even though we also defined a variable with that name on line 1.

# %% [markdown] id="0az3tNK7WD3G"
# In each of the following lines of code, replace `None` by a value of your choice. Make it such that `my_int` is an integer, `my_float` is a float, `my_bool` is a boolean and `my_string` is a string.

# %% id="lY-M8mfSXDfG"
my_int = 42
my_float = .5
my_bool = True
my_string = "I'm starving"

# %% [markdown] id="dvNIQh7KYuJb"
# ## Exercise 2.2: Bonus

# %% [markdown] id="GI9fyUO8XOcp"
# How could you verify in code whether the variables you wrote above have the correct type? Write this code below.
#
# Hint: scroll back to the section [Difference between types](#scrollTo=Difference_between_types).

# %% id="Om6z53RXYBoS" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680606693012, "user_tz": -120, "elapsed": 223, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="3f66fabe-bd2c-4046-d165-b6dc475ffcc2"
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))

# %% [markdown] id="h6UKIMXCj3w9"
# In the code block below, replace the question mark `?` by a variable name. Make it such that the final output is `'Hooray!'`.

# %% id="3MI6_DY7ku30" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680606893191, "user_tz": -120, "elapsed": 247, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="6a605092-cca4-41c3-dfa3-0196c98be37b"
cheer = 'Hooray!'
alarm = 'Oh no!'
anthem = 'Wilhelmus van Nassauwe'
alarm = anthem
alarm = cheer  # alarm instead of ?
cheer = anthem
anthem = alarm
print(anthem)

# %% [markdown] id="z_bXvnya5J2_"
# ## Exercise 2.3: Expressions
#
#

# %% [markdown] id="j9xhznQlbCBf"
# 1. Try to predict the value of each of the following code blocks. Can you explain any surprises?

# %% id="0QcMB4xwbSfL" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680609962892, "user_tz": -120, "elapsed": 415, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="609a5c45-cd77-4aaa-c33e-928263e14c41"
1 + 1

# %% id="eHKN9kP9bWkm" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680609965892, "user_tz": -120, "elapsed": 10, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="9b17e8cc-3a5a-4ac4-db2f-1454eae873af"
1 * 1

# %% id="uINoRNNbbXwJ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680609969742, "user_tz": -120, "elapsed": 323, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="1b281881-5bbc-476e-e38c-bda84855665d"
a = 1
b = 2
a + b

# %% id="4xyWkYlnbc_8" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680609971809, "user_tz": -120, "elapsed": 15, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="9b2dae89-2331-47de-83a5-4ac63e71a06d"
c = b
a * b * c

# %% id="7tW2T4mebljv" colab={"base_uri": "https://localhost:8080/", "height": 38} executionInfo={"status": "ok", "timestamp": 1680609976922, "user_tz": -120, "elapsed": 408, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="404d4cac-d77d-40f8-c6bc-b6f4fcf0e125"
'hakuna' + 'matata'

# %% [markdown] id="wG4N61Jz_WJV"
# If we had done `print('hakuna', 'matata')`, it would have output `hakuna matata`, with a space between the words. When we concatenate strings using `+`, Python does not take that liberty, so if we actually want to separate words with spaces, we have to add them ourselves.

# %% id="uEdPHIhBb2Mw" colab={"base_uri": "https://localhost:8080/", "height": 38} executionInfo={"status": "ok", "timestamp": 1680609981027, "user_tz": -120, "elapsed": 332, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="fc706353-8980-4baa-fc4b-cca736f757e9"
liquid = 'water~'
liquid * 3

# %% id="-D7BB50Qceo2" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680609983171, "user_tz": -120, "elapsed": 236, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="1169bc24-b2d3-41d5-b190-7e1135e3d93a"
5 - 2 - 1

# %% id="OQUGr5rGck3m" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680609985039, "user_tz": -120, "elapsed": 237, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="95e07168-7633-4cc0-f961-d8beb34e5612"
5 - (2 - 1)

# %% [markdown] id="btuLZMUG_xfJ"
# The above result is different from the previous, because Python evaluates minus operators (and most other operators) left-to-right by default.

# %% id="Jc8fawaIdCD5" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680609988715, "user_tz": -120, "elapsed": 212, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="7d524d26-14c3-439a-e78f-914552814109"
income = 100
tax = 20
net_income = income - tax
tax = 15
net_income

# %% [markdown] id="w08CSKAhADsd"
# On line 3, we set `net_income` to the outcome of *the value of* `income` minus *the value of* `tax`, which are respectively `100` and `20` at that point. `net_income` then keeps its value (`80`) until we change it directly. Hence, line 4 does not change anything about `net_income`. If we wanted to update `net_income`, we would have to run line 3 again.

# %% [markdown] id="TlLkcRv-droI"
# 2. In the code block below, change the values of `character` and `multiplier` so that the output becomes `'Goooood!'`.

# %% id="pYZUkeDJenob" colab={"base_uri": "https://localhost:8080/", "height": 38} executionInfo={"status": "ok", "timestamp": 1680610076844, "user_tz": -120, "elapsed": 406, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="97c1b7a5-adf1-4112-b0b4-9a7a826855de"
character = 'o'
multiplier = 5

begin = 'G'
middle = character * multiplier
end = 'd!'

begin + middle + end

# %% [markdown] id="G8X4n_a8a5tl"
# 3. Rewrite your Hello world-program:
#     - Build the "hello, world!" string using multiple variables.
#     - Make the program say "hello, world!" 3 times, each time on a new line

# %% id="nDUVvhDEfIVI" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680708229954, "user_tz": -120, "elapsed": 8, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="8be0c0dd-dc1e-48cc-bfae-5b3c2520efed"
# This works:
hello = 'Hello, '
world = 'world!\n'
variable = hello + world
print(3 * variable)

# This works, too:
slogan = '''Hello, world!
'''
result = 3 * slogan
print(result)

# This would also work, but uses no variables:
print('Hello, world!\n' * 3)

# %% [markdown] id="3HCqdTj2fVPK"
# ## Exercise 2.4: Bonus

# %% [markdown] id="EKFdkLkWa8EY"
# 1. Find out and describe what the following operators do:
#     - `%` (e.g. `10 % 2`)
#     - `//` (e.g. `10 // 2`)
#     - `**` (e.g. `10 ** 2`)
#     - Tip: write the expressions using variables. Change the variables and see how it affects the outcome.

# %% id="V59a7vpDfzO2"
# Regarding %, you will quickly see a pattern if you set
# the right operand to 3 and try a series of consecutive
# numbers as the left operand:

10 % 3 == 1
11 % 3 == 2
12 % 3 == 0
13 % 3 == 1
14 % 3 == 2
15 % 3 == 0
16 % 3 == 1
17 % 3 == 2
18 % 3 == 0

# Conclusion: % calculates the remainder of division.

# // is like / (division), but rounded down to an integer.
10 / 3 == 3.33333333333333333
10 // 3 == 3
5 / 4 == 1.25
5 // 4 == 1

# In general, the following equation is always true if
# a and b are integers:
(a // b) * b + a % b == a

# a ** b raises a to the power of b.
3 ** 2 == 3 * 3 == 9
3 ** 3 == 3 * 3 * 3 == 27
3 ** 4 == 3 * 3 * 3 * 3 == 81

# %% [markdown] id="o0WYIAUla-AX"
# 2. Predict what will be printed on each line in the following code block, then run the code to check your answer. If you made any mistakes, try to figure out what is causing the difference.

# %% id="Z9Vd9pdIUzT5" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680709009778, "user_tz": -120, "elapsed": 202, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="1cde1422-5f7f-460f-c537-5393acf5bb2a"
word = 'stylometry'
repeats = 3
extra = 2

print((word * repeats) + str(extra))
# Evaluated in this order:
word == 'stylometry'
repeats == 3
'stylometry' * 3 == 'stylometrystylometrystylometry'
str(extra) == '2'
'stylometrystylometrystylometry' + '2' == 'stylometrystylometrystylometry2'

print(word * (repeats + extra))
# Evaluated in this order:
word == 'stylometry'
repeats + extra == 5
'stylometry' * 5 == 'stylometrystylometrystylometrystylometrystylometry'

print(word * repeats + str(extra))
# Evaluated in the same way as line 5, just without parentheses.
# The * operator takes precedence over the + operator by default.

print((word + str(extra)) * repeats)
# Evaluated in this order:
word == 'stylometry'
str(extra) == '2'
word + str(extra) == 'stylometry2'
repeats == 3
'stylometry2' * 3 == 'stylometry2stylometry2stylometry2'

print(word + str(extra * repeats))
# Evaluated in this order:
word == 'stylometry'
extra == 2
repeats == 3
2 * 3 == 6
str(6) == '6'
'stylometry' + '6' == 'stylometry6'

print(word + str(extra) * repeats)
# Evaluated in this order:
word == 'stylometry'
extra == 2
str(2) == '2'
repeats == 3
# * operator takes precedence over +, so right subexpression first.
'2' * 3 == '222'
'stylometry' + '222' == 'stylometry222'

# %% [markdown] id="DRObBQZHgsIG"
# 3. Using just the variables `word`, `repeats` and `extra` from the previous code block, write a single big expression that evaluates to `'stylometry555stylometry'`.

# %% id="uLuiUk10gqwM"
word + str(extra + repeats) * repeats + word
# (you can add parentheses, as long as you evaluate the * before the +)

# %% [markdown] id="pvrcgKU18OrJ"
# ## Exercise 2.5: boolean expressions

# %% [markdown] id="sWdnjezoil9j"
# 1. Predict for each boolean expression below: `True` or `False`? If any of your predictions is incorrect, try to find the reason.

# %% id="RpSvrom3Z8fQ" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680614316115, "user_tz": -120, "elapsed": 394, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="d3c6bb57-e8c1-4891-c01d-850fd504e1f5"
name = 'Jelte'
height = 2

name * height == 'Jelte Jelte'
# False because string repetition does not add spaces

height < 2
# a number can never be less than itself

2 <= height
# ... but a number is always less than or equal to itself

1 < height <= 2
# Python allows you to compare the same expression on two sides

2 <= height < 1
# Both comparison must be true for the whole expression to be True

name <= 'Julian'
# Lexicographical comparison: 'Julian' is greater because
# 'u' comes after 'e'.

height * 3 + 1 >= height
# * and + take precedence over >=, so the evaluation goes in this order:
height * 3 == 6
6 + 1 == 7
height == 2
(7 >= 2) == True

# %% [markdown] id="zJiaGIlZBN_P"
# 2. Run the code block below. Did you expect this result? Can you explain it?

# %% id="_PrnFf2lioMB" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680614442403, "user_tz": -120, "elapsed": 208, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="9db936a2-9182-402b-bf50-207b3366496a"
1 == True

# 1 and True are literally the same value.
# More interesting equalities and inequalities:

0 == False
2 != True
None != False

# %% [markdown] id="q8QviA70kdQE"
# 3. Replace one value in each of the following expressions so the expression becomes `True`.

# %% id="qDQ9Ob5Zkrqm" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680614593732, "user_tz": -120, "elapsed": 320, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="af8cc847-7dbe-4ba7-fd7b-406e47d7b69d"
3 > height
0 == 0
'Julian' < 'Julian' * 2
name < 2 * name

# %% [markdown] id="YbdV7SQVmDVV"
# 4. Replace one operator in each of the following expressions so the expression becomes `True`.

# %% id="hzjXIwkAmChv" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680614702559, "user_tz": -120, "elapsed": 254, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="a1592d3e-971f-4c75-b496-13e6875e1a55"
5 > 4
2 - 1 == 1
3 + 3 == 3 * 2

# %% [markdown] id="SwyAMDzDn2_X"
# 5. The *Groot woordenboek van de Nederlandse taal* by Van Dale publishers, colloquially known as "De dikke Van Dale", is a three-tome Dutch dictionary. The first tome contains words starting a–i, the second j–q and the third r–z. In the code block below, write an expression that will tell you whether `word` should be in the second tome. Try different values of `word` to verify that your solution is correct. You do not need to check whether the word is actually Dutch!

# %% id="lmCGfx_DqMWe" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680710351970, "user_tz": -120, "elapsed": 193, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="77da4795-3001-4582-ce37-58d289b7a181"
word = 'archaïsch' # try also 'idee', 'j', 'quasi', 'r', 'ziezo'

# is it in the FIRST tome?
word < 'j'

# is it in the THIRD tome?
word >= 'r'

# is it in the SECOND tome? (opposites of the previous expressions)
word >= 'j'
word < 'r'

# combining both conditions in a single expression
'j' <= word < 'r'

# %% [markdown] id="jXSxbjf4q6q5"
# ## Next module
#
# [3. Conditionals](https://colab.research.google.com/drive/1KkZ2fS75o7giccQJakRhyvYBV7JdFnVw) - [solutions](https://colab.research.google.com/drive/1Nvvjc3fGnMg2tWvfw2W1gVn2oKKbWzGI)
