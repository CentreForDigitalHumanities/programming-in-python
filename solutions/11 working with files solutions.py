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
# ### Exercise solutions
#
# [Module 11](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/11%20working%20with%20files.ipynb)
#
# ### CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/00%20index.ipynb)
#
# Previous module: [10. Dictionaries](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/10%20-%20Dictionaries.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/10%20-%20Dictionaries%20solutions.ipynb)
#
# ### This module
#
# - Reading files
# - Writing files
# - Use existing code

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
# `print(file)` prints the File Object. There is no way to determine by printing if this is still open, or has been closed.

# %% [markdown]
# Read the file `sampledata/california_housing_test.csv'`, and print the first row containing data as a list.
#
# Are the data in the correct format? Try to fix it if not.

# %%
PATH = 'sample_data/california_housing_test.csv'
file = open(PATH)
lines = file.readlines()

# Read the first row
first_row = lines[0]
print(first_row)

# %% [markdown]
# Note that this prints the header row, as one big string. Not really what we are looking for!

# %%
# Split the file into header row and data rows
header, *data = lines
first_row = data[0]
print(first_row)
print(type(first_row))

# %% [markdown]
# This is the first actual row of data, but still as a big string.

# %%
columns = first_row.split(',')
print(columns)
print(type(columns[0]))


# %% [markdown]
# The row is split into columns. They still contain strings, not numbers. And the last value includes the newline character `\n`

# %%
def clean_value(value):
    '''
    Clean a single value. Assumes value is a string representation
    of a number.
    - remove any whitespace characters
    - convert the value into a float
    - check if it is an integer, if so, convert to an actual int
    - return the result
    '''
    clean_value = value.strip()
    float_value = float(clean_value)
    if float_value.is_integer():
        return int(float_value)
    return float_value


def clean_values(values):
    '''
    Cleans an entire row or column using clean_column.
    Assumes values is a list of string representations
    of numbers.
    '''
    cleaned_row = []
    for value in values:
        cleaned_row.append(clean_value(value))
    return cleaned_row


assert clean_values(columns) == [-122.05, 37.37, 27, 3885, 661, 1537, 606, 6.6085, 344700]

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
# #### 11.2.1

# %%
import csv
PATH = 'sample_data/california_housing_test.csv'

def read_data():
    with open(PATH) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        return list(reader)

assert len(read_data()) == 3001


# %% [markdown]
# #### 11.2.2
# This may seem like a whole load of code just to calculate some stuff.
#
# But notice that by definding general functions, we create a toolkit that we can apply to any future problems! Think ahead!

# %%
def get_row(data, row_index):
    '''
    Returns the row at row_index
    '''
    return data[row_index]


def get_column(data, column_index):
    '''
    Returns the column at column_index
    '''
    column = []
    for row in data:
        column.append(row[column_index])
    return column


def separate_headers(data):
    '''
    Separates tabular data into a header row and data rows
    '''
    header_row, *data_rows = data
    return header_row, data_rows


def multiply(num1, num2):
    return num1 * num2


def combine_columns(column_1, column_2, how):
    '''
    created a new column based on two existing columns
    how should be a function that accepts two numbers and returns a number
    column_1 and column_2 should contain numerical data
    '''
    new_column = []
    for index, value_1 in enumerate(column_1):
        value_2 = column_2[index]
        new_column.append(how(value_1, value_2))
    return new_column



def add_column(data, column_name, column_data):
    '''
    Adds an extra column to the end of the data
    Assumes data containts tabular data WITH headers
    colum_data size should match existing table
    '''
    headers, data_rows = separate_headers(data)
    headers = [headers + [column_name]]

    new_rows = []
    for index, row in enumerate(data_rows):
        new_row = row + [column_data[index]]
        new_rows.append(new_row)
    return headers + new_rows

def write_table_to_csv(data, filepath):
    with open(filepath, mode='w') as f:
        writer = csv.writer(f)

        for row in data:
            writer.writerow(row)


# read the data and get the last row
data = read_data()
last_row = get_row(data, -1)
print(last_row)

# determine the number of columns, and use this to get the last column
number_of_columns = len(last_row) - 1 # remember that list indices start at 0!
last_column = get_column(data, number_of_columns)
print(last_column)

# get the first data row
headers, data_rows = separate_headers(data)
first_row = data_rows[0]
print(first_row)

# get the index of the 'median_income' column
income_index = header.index('median_income')
# get the column data
income = get_column(data_rows, income_index)
# convert the data to numbers
income_numerical = clean_values(income)
# finally, calculate the harmonic mean
import statistics
harmonic_mean = statistics.harmonic_mean(income_numerical)
print(harmonic_mean)

# add a new column
# get households the same way we did income, this time on one line
households_numerical = clean_values(get_column(data_rows, header.index('households')))
# combine households and income by multiplying them
total_income = combine_columns(income_numerical, households_numerical, multiply)
new_data = add_column(data, 'total_income', total_income)
# finally, write to a new file
write_table_to_csv(new_data, 'sample_data/california_housing_test_expanded.csv')


# %% [markdown]
# ## Next module
#
# [12 - Functions, bis](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/12%20functions%2C%20bis.ipynb) - [solutions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/12%20Functions%2C%20bis.ipynb)
