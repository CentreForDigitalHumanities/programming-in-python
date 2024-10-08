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
# # Module 11: Working with files
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [10. dictionaries](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/10%20-%20Dictionaries.ipynb)
#
# ### This module
#
# - Reading files
# - Writing files
# - Use existing code

# %% [markdown]
# ## Reading files
# It is not very desirable to keep data in your code. It clutters up, making the code harder to read. Also, we want to work with some interchangeable data, that exists outside of our code.
#
# Python provides an easy way to work with files.

# %% [markdown]
# ### Read a file
# - Provide a path to the file
# - Open the file `open(<path>)`, this provides a *File Object*
# - Work with the contents

# %%
# Make sure the path is available to Python
# In notebooks, this means we need to upload the file
# (You can download this file from the Teams channel)
PATH = 'countries.csv'

file = open(PATH)
type(file)

contents = file.read()
print(type(contents))
print(contents)

lines = file.readlines()
print(type(lines))
print(lines)


# %% [markdown]
# ### Sidenote: constants
# Isn't the convention that variables are lowercased?
# Not if they are *constants*:
# - Variables that do not change during the progam
# - Often represent some 'setting' or 'constant value'
#     - `PATH = 'countries.csv'`
#     - `PI = 3.14159265358979323846264338327950288419716939937510582097`
#

# %% [markdown]
# ## Closing files
# - If a file is opened, it should also be closed (like a freezer)
# - If not, nasty things can happen
# - Call `.close()` on the File Object

# %%
# Manually close
file = open(PATH)
data = file.read()
file.close()

# %% [markdown]
# - Even better: use a *context manager*
#     - opens the file
#     - assigns it to a variable
#     - and closes once you are done with it
# - Use the `with <file object> as <variable name>` syntax

# %%
with open(PATH) as file:
    data = file.read()

print(data)

# %% [markdown]
# ## Writing files
# - Provide `mode` parameter with value `'w'` (write) to open a file in write mode
#     - note that `mode` has a default value: `'r'` (read)
# - On the file object, use `file.write(<content>)`
# - If you want to write on a new line, make sure to append `'\n'` (newline character)
# - Alternatively, use `print(<content>, file=<file object>)`

# %%
WRITE_PATH = 'myfile.txt'

with open(WRITE_PATH, mode='w') as file:
    file.write('Hello, world!\n')
    file.write('This is a new file created by write.')

with open(WRITE_PATH, mode='w') as file:
    print('Hello world!', file=file)
    print('This is a new file created by print.', file=file)

# %% [markdown]
# Append to an existing file by using `mode='a'` (append)

# %%
with open(WRITE_PATH, mode='a') as file:
    print('Another bit of text', file=file)

# %% [markdown]
# ## Exercise 11.1 - Files
# In the code block below, try to predict what will be printed, then run the code.

# %%
PATH = 'sample_data/california_housing_test.csv'
file = open(PATH)
print(file)
print(file.read())
print(file.readlines())
file.close()
print(file)

# %% [markdown]
# Read the file `'sampledata/california_housing_test.csv'`, and print the first row containing data as a list.
#
# Are the data in the correct format? Try to fix it if not.

# %%

# %% [markdown]
# ## Using existing code
# - People before you have worked with CSV files
# - Someone probably wrote and published their code
# - Available in *packages* and *libraries*
# - `csv` *module* is available in the [standard library](https://docs.python.org/3.7/library/index.html). This library is *always* available in Python.
# - Python is known for its strong ecosystem of packages
# - Many libraries from outside the standard library are preinstalled in these Notebooks

# %% [markdown]
# ### Importing existing code
# Use the `import <module>` syntax to use an entire Python file in your own code

# %%
import csv
print(csv.reader)

# %% [markdown]
# Alternatively, only import the parts your are interested in

# %%
from csv import reader
print(reader)

# %% [markdown]
# ## Working with the `csv` module
# The `reader` function has some nice utilities that make it easy to read csv files

# %%
import csv

def read_data():
    with open(PATH) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        return list(reader)

data = read_data()
print(data[0])
print(data[1])
print(data[10][3])

# %% [markdown]
# Alternatively, use the `csv.DictReader` to read the file as a list of dictionaries.

# %%
import csv

def read_data_dict():
    with open(PATH) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        return list(reader)

data = read_data_dict()
print(data[0])
print(data[1])
print(data[10]['name'])

# %% [markdown]
# ## Exercise 11.2: Bonus - working with csv datasets
# > 💡 If you wish to perform an analysis on your own dataset in the upcoming sessions, make sure you complete this exercise. The code you write here can be reused in your own analysis.
#
# 1. Upload your own dataset, or use `sample_data/california_housing_test.csv`
#     1. Read the data from the CSV file
#     2. Write functions that take the data as a parameter, and return the following items:
#         - The last row
#         - The last column
#         - The first row. If this is a header row, try if you can come up with a way to separate it from the data rows.
#         - Calculate the *harmonic mean* of a column containing numbers. Search the [standard library](https://docs.python.org/3.7/library/index.html) for a a relevant module containing the code to do so.
#     3. Add an extra column to the data (think of something that makes sense). Write the whole dataset to a new csv file.

# %% [markdown]
# ## Next module
#
# [12 - Functions, bis](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/12%20functions%2C%20bis.ipynb)
