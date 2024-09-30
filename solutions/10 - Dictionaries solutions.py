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

# %% [markdown] id="kjdcNtg3k8Aa"
# # Dictionaries
#
# ### Exercise solutions
#
# [Module 10](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/10%20-%20Dictionaries.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [9. String manipulation](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/09%20string%20manipulation.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/09%20string%20manipulation%20solutions.ipynb)
#
# ### This module
#
# - Learn about _dictionaries_, a useful way of storing and looking up data

# %% [markdown] id="1ezL-XhlvHBq"
# ## Exercise 10.1: Dictionaries

# %% [markdown] id="xrw8tjm9WqEb"
# 1. In each of the code blocks below, try to predict what will be printed, then run the code. If your guess was incorrect, try to figure out why the result is different. If your guess was correct, celebrate!

# %% id="JpVUxXa8W-yN" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715714039862, "user_tz": -120, "elapsed": 4, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="bbde32c6-860c-4126-a172-244f175282e6"
{0: 0}

# %% [markdown] id="sPpBbWE0gp0K"
# A dictionary with `0` as the only key and `0` its value. The dictionary as a whole is the last value in the cell, so the notebook echoes it to us.

# %% id="62bKQZhpXQOA" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715714042208, "user_tz": -120, "elapsed": 301, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="49b47fc4-4e67-4184-8e39-beff42412859"
{'0': 0}

# %% [markdown] id="-G0bkOwpg2qT"
# Like the previous, but with the string `'0'` as key.

# %% id="FW2sYBJdXXWl" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715714044063, "user_tz": -120, "elapsed": 245, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="a3bda353-9254-43d0-b86c-7ef63ad41026"
{1 + 2: 3 * 4}

# %% [markdown] id="x1YahUoBg8b-"
# Keys and values in a literal dictionary can be expressions. They are evaluated before being stored in the dictionary.

# %% id="KFOPs4O7Xf9a" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715714046544, "user_tz": -120, "elapsed": 216, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="74e94c76-17d7-4fee-848c-afe8dbce01bc"
{'1' + '2': {3: 'Hooray!'}}

# %% [markdown] id="0jUVKlMghTfe"
# Dictionaries can be used as values in other dictionaries (but not as keys).

# %% id="PkuZzIm1XngU" executionInfo={"status": "ok", "timestamp": 1715714053234, "user_tz": -120, "elapsed": 206, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
programming_languages = {
    'Fortran': 1957,
    'Algol 60': 1960,
    'C': 1972,
    'Perl': 1987,
    'Python': 1991,
    'Julia': 2012,
    'Mojo': 2023,
}

# %% [markdown] id="9d3MvUFWhZcZ"
# Assignments cause the variable to obtain a value as a side effect. The assignment itself has no result value, so we see no output. But the notebook will remember the `programming_languages` dictionary for us, so we can use it in the following code blocks.

# %% id="j20ZYa6bbSpq" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1715714087276, "user_tz": -120, "elapsed": 5, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="fc82c6f7-7d1a-4d11-85e1-dfef665fc924"
programming_languages[Perl]

# %% [markdown] id="ThPhZZ95h3k1"
# If you write a word without quotes, Python attempts to find a variable with that name. We did not define one, so we get a `NameError`.

# %% id="sZC-YucJaXCa" colab={"base_uri": "https://localhost:8080/", "height": 141} executionInfo={"status": "error", "timestamp": 1715714511221, "user_tz": -120, "elapsed": 211, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="b02048c9-f8db-470a-848b-0c65f89cb47a"
programming_languages[1960]

# %% [markdown] id="KF3rie9tjbhv"
# `1960` is a value that appears in the dictionary, but the `[]` notation only looks for keys.

# %% id="jlTtefX6aKii" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715714556065, "user_tz": -120, "elapsed": 342, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="97e6ae05-afd0-43d7-ed1e-f47d2aa09de2"
programming_languages['Perl']

# %% [markdown] id="filN8qTgjo-v"
# Third try is a blessing! `'Perl'` is, indeed, a key that appears in the dictionary, and its associated value is `1987`.

# %% id="Y-7am56bacgD" executionInfo={"status": "ok", "timestamp": 1715714649874, "user_tz": -120, "elapsed": 181, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
{None: None}[None]

# %% [markdown] id="ge0zVd8Gj_Z4"
# The notation is valid; `None` can be both a key and a value in a dictionary. The lookup is successful and returns `None`. Notebooks only echo the last value when it is **not** `None`, so we see no output.
#
# You can verify that there is a value by wrapping the entire expression in `print()`.

# %% id="SFgsCOnpapTp" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715714740486, "user_tz": -120, "elapsed": 247, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="7303d1bc-44a7-4212-f6a6-223c8fca22a8"
programming_languages.get('Per1', 2125)

# %% [markdown] id="uMuzVoj4kV3f"
# Note that we wrote `'Per1'`, not `'Perl'`. See the difference? Because `'Per1'` is not in the dictionary, the default (fallback) value of `2125` is used.

# %% id="bx0WNXq2a7K1" executionInfo={"status": "ok", "timestamp": 1715718500018, "user_tz": -120, "elapsed": 408, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
programming_languages.get('Per1')

# %% [markdown] id="_RKovP5OyqBE"
# `'Per1'` is still not in the dictionary. Since we don't supply a default in this case, we get `None`, which produces no output.

# %% id="9dqApt0ObCuz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715718563615, "user_tz": -120, "elapsed": 252, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="5258ae5f-a546-4e27-ae24-754155a5d0ce"
programming_languages.get('Python', None)

# %% [markdown] id="cFwD2Sioy7WR"
# `'Python'` is in the dictionary, so we get its associated value. The default of `None` is never used.

# %% id="msMNmeGWbKRS" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715718611228, "user_tz": -120, "elapsed": 311, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="76aa4504-1105-4e75-99cd-5b8358d737f4"
programming_languages.get('Python')

# %% [markdown] id="S-M746bSzHlB"
# The result is the same as in the previous code block, because the default value is irrelevant.

# %% id="_tzsbkN5bbi0" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715718640312, "user_tz": -120, "elapsed": 232, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="e4ebbc4d-6dfa-4a9d-feb4-b4334b7fa9aa"
'Per1' in programming_languages

# %% [markdown] id="K7P57_iGzPeq"
# There's that `'Per1'` again, which is not in the dictionary.

# %% id="6JEZlfkPbhP9" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715718682293, "user_tz": -120, "elapsed": 311, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="a2bd1f8c-ba81-4340-bf01-bdd19766870e"
'Fortran' in programming_languages

# %% [markdown] id="sMGC6TJvzY5e"
# `'Fortran'`, on the other hand, is in the dictionary, hence `True`.

# %% id="dOIxLmPqbvDA" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715718715370, "user_tz": -120, "elapsed": 271, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="c88ef4c5-371e-4dec-cc42-b0f69648155f"
2012 in programming_languages

# %% [markdown] id="_JVAdmUZzhGL"
# `2012` is in the dictionary as a value but not as a key. `in` only looks for keys.

# %% id="bv1WFXRab0Bv" executionInfo={"status": "ok", "timestamp": 1715718746520, "user_tz": -120, "elapsed": 254, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}}
programming_languages.update({'Per1': 2125, 'Raku': 2015})

# %% [markdown] id="y2Xb7qTPznzM"
# `update` changes `programming_languages` as a side effect. There is no return value, so we see no output.

# %% id="idVFrA21cLc5" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715718809806, "user_tz": -120, "elapsed": 229, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="6349d80d-1a48-440e-ac83-e7c931dcafc6"
2012 in programming_languages.values()

# %% [markdown] id="O_m_ezBaz45C"
# Since we query the `.values()` of `programming_languages`, `2012` is now found.

# %% id="i07oWzu5cScu" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715718867227, "user_tz": -120, "elapsed": 313, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="652cbcee-11a1-42c5-bf78-7760b0a9f5d1"
('Per1', 'Perl') in programming_languages.items()

# %% [markdown] id="1HSvnyW80No-"
# When we look `in` a dictionary's `.items()`, we query `(key, value)` pairs. `('Per1', 2125)` would return `True` and so would `('Perl', 1987)`, but not `('Per1', 1987)` or `('Perl', 2125)`.

# %% id="xatUSQBPcr4x" colab={"base_uri": "https://localhost:8080/", "height": 193} executionInfo={"status": "error", "timestamp": 1715719046019, "user_tz": -120, "elapsed": 244, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="055b93fb-74cb-469d-8c12-8d7fe966cf66"
del programming_languages[2012]

for language, year in programming_languages.items():
    print(f'{language} first appeared in {year}')

# %% [markdown] id="h-4AFGKW0xpM"
# The first line attempts to remove the `2012` key from the dictionary, but there is none. Hence a `KeyError`. If you comment out the first line, you will find that the loop prints a nice line for each programming language.

# %% [markdown] id="gw7W_KMcdVqD"
# 2. The code below attempts to count the frequencies of the individual characters in our party invitation from module 6. There is a bug which prevents it from working. Fix the bug.

# %% id="s_OeNugZfG4J" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1715719220003, "user_tz": -120, "elapsed": 320, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="d9a4fa37-6a44-4898-f68b-89483d9c34ab"
invitation = '''
    Dear Sheean,

    I hereby invite you for my Python party on the 11th of April.
    The bar will open at 2 PM. 🍸 Please bring pseudocode.

    Yours sincerely,
    Julian
'''

frequencies = {}
for character in invitation:
    count = frequencies.get(character, 0)
    # Here is the bug: dictionaries have a .get method, but no .set.
    #frequencies.set(character, count + 1)
    # The fix is to use assignment with a square bracket lookup.
    frequencies[character] = count + 1
print(frequencies)

# %% [markdown] id="rxcz60KQximW"
# 3 . Below are two dictionaries containing information about different types of fruit. Print a nice message about each fruit stating its colour and price. For example, _An apple is red and costs € 2.50_, etc.

# %% id="yn89oAAZu33C" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1681894457462, "user_tz": -120, "elapsed": 238, "user": {"displayName": "Luka van der Plas", "userId": "16305747382115943293"}} outputId="d6b7d53c-d22c-4499-8b59-de508579836e"
fruit_colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}
fruit_prices = {'apple': 2.50, 'banana': 2.10, 'orange': 1.50}

# The example sentence includes 'a'/'an' ('an apple' / 'a banana')
# which was a bit of an oversight: the point of this exercise
# was to loop through a dictionary and access values.
# You could make a solution like this to avoid it.

for fruit in fruit_colors:
    color = fruit_colors[fruit]
    price = fruit_prices[fruit]

    print(fruit + 's', 'are', color, 'and cost €', price, sep=' ')

# Bonus points if you DID implement a solution on when to use
# 'a' or 'an'! Here is an example of your you can do that.

print()

def starts_with_vowel(word):
    '''
    Returns True if the word (a string) starts with a vowel.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        return True
    return False


for fruit in fruit_colors:
    color = fruit_colors[fruit]
    price = fruit_prices[fruit]

    if starts_with_vowel(fruit):
        article = 'An'
    else:
        article = 'A'

    print(article, fruit, 'is', color, 'and costs €', price, sep=' ')

# %% [markdown] id="Gtp5V9dE0LxK"
# 4 . Here is a longer lists of fruit colours. Write a function `count_fruits` which gets gets a colour as input and returns the number of fruits that have that colour (according to `lots_of_fruit`).

# %% id="S7gCNyLCxdrO"
lots_of_fruit = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange',
                 'cucumber': 'green', 'kiwi': 'green', 'strawberry': 'red',
                 'pineapple': 'yellow','blackberry': 'black', 'cherry': 'red',
                 'gooseberry': 'green', 'raspberry': 'red', 'mandarin': 'orange',
                 'lemon': 'yellow', 'lime': 'green'}


# %% id="nScDQipK35qN"
def count_fruits(color):
    '''Count the number of fruits in `lots_of_fruit` that match this colour.'''
    count = 0
    for value in lots_of_fruit.values():
        if value == color:
            count = count + 1
    return count

# let's see if it works!
assert count_fruits('red') == 4
assert count_fruits('lavender') == 0

# %% [markdown] id="-Qp6R3Kp3GId"
# 5 . The list `fruit_basket` contains a bunch of fruits. Can you make a dictionary `fruit_counts` which gives the amount for each fruit in `fruit_basket`? (Do not count the fruits by hand!)

# %% id="awf-lLQO3N1U"
fruit_basket = ['apple', 'banana', 'banana', 'banana', 'apple', 'orange',
                'orange', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape',
                'grape', 'grape', 'grape', 'pear', 'apple', 'strawberry',
                'strawberry', 'strawberry', 'orange']


# %% id="MDpIZpbm3-BG"
def count_items(items):
    '''
    Count the items in a list.

    Input: a list of items, such as strings
    Output: a dictionary with the total of occurences for each item.
    '''

    counts = dict() # we will keep track of our counts in here!

    for item in items:
        # the current count: either the current value in the dictionary
        # or 0 if we haven't seen this fruit yet
        current_count = counts.get(item, 0)
        new_count = current_count + 1
        counts[item] = new_count

    return counts

fruit_counts = count_items(fruit_basket)

# let's see if it works!
assert fruit_counts['apple'] == 3


# %% [markdown] id="h-kJhTO951pc"
# 6 . Here is a different list, which contains the words in a sentence. Can you use your code above to make a dictionary `word_counts` telling us how often each word occurs? (Tip: if you need to do very similar tasks, make a function!)
#
# Write a function that takes a dictionary like `word_counts` tells us the most commonly occuring item and the count. Note that there can be multiple items that occurred the most.

# %% id="mdNug4ct5645"
# the variable sent0 contains the first sentence of The Catcher in the Rye
# split into single words
sent0 = ['If', 'you', 'really', 'want', 'to', 'hear', 'about', 'it,', 'the',
         'first', 'thing', 'you’ll', 'probably', 'want', 'to', 'know', 'is',
         'where', 'I', 'was', 'born,', 'and', 'what', 'my', 'lousy', 'childhood',
         'was', 'like,', 'and', 'how', 'my', 'parents', 'were', 'occupied',
         'and', 'all', 'before', 'they', 'had', 'me,', 'and', 'all', 'that',
         'David', 'Copperfield', 'kind', 'of', 'crap,', 'but', 'I', 'don’t',
         'feel', 'like', 'going', 'into', 'it,', 'if', 'you', 'want',
         'to', 'know', 'the', 'truth.']

# %% id="XGY3qSEk6B9j"
word_counts = count_items(sent0) # we recycle our function from the last exercise


# %% colab={"base_uri": "https://localhost:8080/"} id="iS8rDbONnVDr" executionInfo={"status": "ok", "timestamp": 1681894948452, "user_tz": -120, "elapsed": 307, "user": {"displayName": "Luka van der Plas", "userId": "16305747382115943293"}} outputId="c1313777-a4ab-477d-e428-9ae285fc28da"
def most_frequent(counts):
    '''
    For a dictionary with totals, the most commonly occuring item(s) and the count.

    Input should be a dictionary with the total number of occurences for each key in some collection.
    Returns a tuple of two items. First is a list of the most frequent item(s). If the input
    is an empty dict, the list if empty. Second is the number of occurences for that item.
    '''

    if not len(counts):
        return [], 0

    max_count = max(counts.values())

    top_items = []
    for item, count in counts.items():
        if count == max_count:
            top_items.append(item)

    return top_items, max_count

words, total = most_frequent(word_counts)
print(words, total)

# here are some assert statements you could use to check your own function
# feel free to adapt them if your function gives a different output format
assert most_frequent(fruit_counts) == (['grape'], 9)
assert most_frequent(word_counts) == (['and'], 4)
assert most_frequent({}) == ([], 0)

# %% [markdown] id="y5FcFvgypMfE"
# ## Next module
#
# [11 - Working with files](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/11%20working%20with%20files.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/11%20working%20with%20files%20solutions.ipynb)
