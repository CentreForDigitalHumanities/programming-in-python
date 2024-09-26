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
# [Module 10](https://colab.research.google.com/drive/1Dssqf65thuWCNZ9I3ezaawelaWpeaWoj)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1YgmnpA7tRylvGBpp2PTFGvSV2P8tw5jl)
#
# Previous module: [9. String manipulation](https://colab.research.google.com/drive/15djL6RWOHmSo7rpQMOLE1ga9bICxBLmm) - [solutions](https://colab.research.google.com/drive/1wOUWUUP4KdYUFzp5-fALi5t_k_4ovow1)
#
# ### This module
#
# - Learn about _dictionaries_, a useful way of storing and looking up data

# %% [markdown] id="1ezL-XhlvHBq"
# ## Exercise 10.1: Dictionaries

# %% [markdown] id="rxcz60KQximW"
# 1 . Below are two dictionaries containing information about different types of fruit. Print a nice message about each fruit stating its colour and price. For example, _An apple is red and costs € 2.50_, etc.

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
# 2 . Here is a longer lists of fruit colours. Write a function `count_fruits` which gets gets a colour as input and returns the number of fruits that have that colour (according to `lots_of_fruit`).

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
# 3 . The list `fruit_basket` contains a bunch of fruits. Can you make a dictionary `fruit_counts` which gives the amount for each fruit in `fruit_basket`? (Do not count the fruits by hand!)

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
# 4 . Here is a different list, which contains the words in a sentence. Can you use your code above to make a dictionary `word_counts` telling us how often each word occurs? (Tip: if you need to do very similar tasks, make a function!)
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
# [11 - Working with files](https://colab.research.google.com/drive/1_mDpeRCHzrGJstcxEWZgq5YMhHujPdfe) - [solutions](https://colab.research.google.com/drive/1a5fHoa8eY_ABZereDQLcSnV5w3AUYSav)
