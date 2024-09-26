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

# %% [markdown] id="kIc3b-0fqM6n"
# # Project - Text Analysis
# In this series of exercises you will develop a text analysis tool. The steps roughly simulate real-life Digital Humanities projects:
# - Obtaining data
# - Cleaning data
# - Running analyses
#
#

# %% [markdown] id="OSpUjXmAqJI9"
# > 💡 The exercises are very useful and fun if you would like to analyse textual data. The code you write here can be reused in your own analysis.
#
# > ⚠️ The exercises are difficult and may take you some time to complete. Consider them a bonus, study them at home, and don't be hestitant to contact the instructors, during or after the course. If you are not interested in text-analysis, ask the instructors for similarly challenging projects on a different topic, or pursue your own ideas!
#

# %% [markdown] id="v1MTwBNTpTcN"
# ## Exercise 1: Cleaning interpunction
# Implement the function `clean_interpunction` in a way that satisfies the docstrings and assertions

# %% id="fOZBq4OLp2Lz"
def clean_interpunction(string):
    """Pads words and sentence-ending interpunction with a space.
    Other interpunction should be removed.

    The following characters are considered sentence-ending interpunction:
    - .
    - ?
    - !

    Other interpunction that should be removed:
    - ,
    - ;
    - :
    """
    output_string = None # replace this line by your own lines of code
    return output_string

simple_sent = 'A sentence.'
complex_sent = 'A sentence, with a dependent clause.'
assert clean_interpunction(simple_sent) == 'A sentence .'
assert clean_interpunction(complex_sent) == 'A sentence with a dependent clause .'
print('All cases passed! The function works.')


# %% [markdown] id="U8QVnwgwqTR6"
# ## Exercise 2: only_periods
# Add an optional parameter named `only_periods` to `clean_interpunction`.  
# When this parameter is `True`, all sentence-ending interpunction should be changed to a period.  
# The use of this will become clear in the next exercise.

# %% id="TdLKVbsvqhGb"
def clean_interpunction(string, only_periods=None):
    """Pads words and sentence-ending interpunction with a space.
    Other interpunction should be removed.
    If only_periods is True, replace all sentence ending interpunction by a period.

    The following characters are considered sentence-ending interpunction:
    - .
    - ?
    - !

    Other interpunction that should be removed:
    - ,
    - ;
    - :
    """
    output_string = None # replace this line by your own lines of code
    return output_string

simple_sent = 'A sentence?'
complex_sent = 'A sentence, with a dependent clause!'
assert clean_interpunction(simple_sent) == 'A sentence ?'
assert clean_interpunction(complex_sent) == 'A sentence with a dependent clause !'
assert clean_interpunction(simple_sent, only_periods=True) == 'A sentence .'
assert clean_interpunction(complex_sent, only_periods=True) == 'A sentence with a dependent clause .'
print('All cases passed! The function works.')


# %% [markdown] id="f5q3jw66q3EG"
# ## Exercise 3: Split into sentences
# Using the results of the previous exercises, implement a function that satisfies the docstring and assertions:

# %% id="5lTZXUgwq6lW"
def split_sentences(text):
    """Takes a single string and splits it into sentences.
    Sentences are lists containing words (as strings).
    Sentences are split on periods.
    Other interpunction is removed.

    Returns a nested list of sentences and words
    """
    # your code here
    # use your implementation of clean_interpunction
    sentences = None

    # return the nested list
    return sentences



text = 'The novel details two days in the life of 16-year-old Holden Caulfield after he has been expelled from prep school. Confused and disillusioned, Holden searches for truth and rails against the “phoniness” of the adult world.'
expected = [['The', 'novel', 'details', 'two', 'days', 'in', 'the', 'life', 'of', '16-year-old', 'Holden', 'Caulfield', 'after', 'he', 'has', 'been', 'expelled', 'from', 'prep', 'school'], 
            ['Confused', 'and', 'disillusioned', 'Holden', 'searches', 'for', 'truth', 'and', 'rails', 'against', 'the', '“phoniness”', 'of', 'the', 'adult', 'world'], 
    ]

# If no errors occur, you solved it correctly!
split_text = split_sentences(text)
assert len(split_text) == 2
assert split_text == expected

# %% [markdown] id="Um-nFxcTq1WA"
# ## Exercise 4 - Putting it all together

# %% [markdown] id="YNbDTnBrheRq"
# ### The data
# In the `class materials` section of the [Teams channel](https://teams.microsoft.com/l/channel/19%3aAlr7pcE2v9p1eaKT1BtNxJAB9mgCFT1olZvAMswJlEc1%40thread.tacv2/Algemeen?groupId=7fd15384-6748-4852-8646-d96963fb3524&tenantId=d72758a0-a446-4e0f-a0aa-4bf95a4a10e7) you will find three `.txt`files:
#
#
# - `catcher_chapter1.txt`, containing the first chapter of The Catcher in the Rye by J.D. Salinger
# - `matilda_chapter1.txt`, containing the first chapter of Matilda by Roald Dahl
# - `ij_chapter1.txt`, containing a part of the first chapter (the chapters are way too long) of Inifite Jest by David Foster Wallace.
#
# Write some code that loads the whole content of each of these files into its corresponding variable, see code cell below.
#
# We will use these variables in the rest of the notebook. Make sure you've executed this cell at least once.
#

# %% id="q_58MJYQadJO"
catcher_chapter1 = ''
matilda_chapter1 = ''
ij_chapter1 = ''

# %% [markdown] id="EuaRmuhwhTIZ"
# ### Writing functions
# Implement a few function to use in the final analysis:
#
# 1. Implement a function that counts the total number of words given a string containing a full text.
# 2. Implement a function that calculates the average sentence length of a text. The sentence length is defined as the number of words in a sentence. Use your implementation of `split_sentences`.<sup>1</sup>
# 3. Implement a function that calculates the average word length of a text. Again, use your implementation of `split sentences`.<sup>1</sup>
# 4. Bonus: implement a function that calculates the [automated readability index](https://en.wikipedia.org/wiki/Automated_readability_index) of a text.
#
# <sup>1</sup> *You can and may combine 2. and 3. into a single function that returns two values.*
#
#
#
#

# %% [markdown] id="SSnrAH0xjUx8"
# ### Output
# Implement a function that calls 1-3 (and optionally 4) for each of the novels, and outputs their results. Try to format it in a nice way, so that it is clear what the output is.
