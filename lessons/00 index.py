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
# # CDH course "Programming in Python"
#
# **October 2024 edition**
#
# https://tinyurl.com/cdh-python-course
#
# ![cdh-python-0524-400.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYEAAAGBAQMAAAC6l59nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAGUExURQAAAP///6XZn90AAAAJcEhZcwAADsMAAA7DAcdvqGQAAAO4SURBVHja7ZwxlqMwDIbFo0iZI3CU3GyAm3EUjpAyRR5a65dkZ3cbaPK0a7nJYPxlkrElW7/EkLcH83vg5cGvkXmh+2tgmneigXmjGx/0V4tEDD1/j5ml0WO/vXHxMr70zfzEkOk1Hj5uuEz0+zvifiosBSFKx6JgaTdZF9NzlEFKbERjz8RPdIKlu9yVmS12Xiy7/CAEy9Ak/kcCL0sh3mrnh94i4m2SqyTCEs1TK6HuWIaWqS848y67s41LIhxhzQh46vLyLJ6al+KpD5lzNWi0JP59gr2BwIrQVVIuFt+dubWjW2IJSrRDlLtjsexNoqLf7ZxKpATbT+IswWEJXRG804hl8KLaZ8esYuflWny7xE3dEkNgovlhDWjbnBM8NSFSekiQy2sSp4nlK8Sfh6hdu83TWKij6+CuL0mcJYa4hMW1rAdntWlbEUJAnETfDYpXEsEI3u+wbJOcple1+UqolFzepfjyNYlgBOb3Y849xhFk3tVTT5IgYBykVHVO4hTxE5Tg2kwoFmOedXfWBVRljnsx98/orjOCgxIWtVoWoLYnLJu5EaXvlsQlYg1LlPMV7ppTtxQeI9YVNcp2ZzlTj6xRUZfEHJcgT9DJMEvh2ZxDtHBCj15JhCOmKnbaWYrMU8s23N5MVOJ3EleIISox72LnZuC6IlAug1hXcNaNu/mrTok5KkGqTNRw6GYx7PER17qeyElcISgsoVsweQkbjlmWDOB6SwXld81mdEgcQQkIxdiWyape5DivMWxxAawashJi+0mcJ/grhDTLxImnpqlZqInFvv9CT0ziArEGJTwLIOkdr5NxOxfT1gXUotx+iSUsMUE7tA0VeTrcOlRP1HGqTGCBJHGamOMSiIo2L/42sGXcaw5XxckkohG8mztG9nVDfaJryJogkKZ2jvg8iWjEx4wyStaI6kMZpici/Hm41SbxjxN+17IAm1b2a00M73f+qDC9W8VWEqEItpyNPio3twqXAVmAVvRvBU8xCQpJRP3rtiyPF3/jSFWdOo7bZO+ikXASoQj31JbyMS1D18HiCQIkhUzfSOI0MXyF8OaFEYhxFpMVmU0RruUUpmUkcYbgqIQ/g1VcNLQMzdMxPHWtC7dVYrmiPgkKS+y1wlSG7vh6m9U1f+RxCNJUEheIITpRH1XH16t14WiNQE1qn8QSnfD/FGK7M0B9DlIf1VksJ5/EaWL4EmGe2rvNHVsb9ZZ8+g3Z1zWJ0wRHJax5gg74bIHQZNVt2LgftVK2T2KNSPD6C+FNEdTRqwlYAAAAAElFTkSuQmCC)
#
#
# ## Course modules
#
# 1. [Introduction](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/01%20introduction.ipynb)
# 2. [Values and expressions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/02%20values%20and%20expressions.ipynb)
# 3. [Conditionals](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/03%20conditionals.ipynb)
# 4. [Datastructures](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/04%20datastructures.ipynb)
# 5. [Assertions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/05%20assertions.ipynb)
# 6. [Loops](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/06%20Loops.ipynb)
# 7. [Functions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/07%20Functions.ipynb)
# 8. [Debugging](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/08%20debugging.ipynb)
# 9. [String manipulation](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/09%20string%20manipulation.ipynb)
# 10. [Dictionaries](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/10%20-%20Dictionaries.ipynb)
# 11. [Working with files](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/11%20working%20with%20files.ipynb)
# 12. [Functions, bis](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/12%20functions%2C%20bis.ipynb)
#
#
# ## Extra material
# - [Extra exercises for Day 1](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/Extra%20exercises%20day%201.ipynb)
# - [Extra exercises for functions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/07a%20Functions%20(extra%20exercises).ipynb)
# - [Text analysis project](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/Project%20-%20text%20analysis.ipynb)
# - [Tips](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/Tips.ipynb)
# - [Life after the course](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/lessons/Life-after-the-course.ipynb)
#
#
# ## Exercise solutions
#
# 1. [Introduction](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/01%20introduction%20solutions.ipynb)
# 2. [Values and expressions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/02%20values%20and%20expressions%20solutions.ipynb)
# 3. [Conditionals](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/03%20conditionals%20solutions.ipynb)
# 4. [Datastructures](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/04%20datastructures%20solutions.ipynb)
# 5. [Assertions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/05%20assertions%20solutions.ipynb)
# 6. [Loops](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/06%20Loops%20-%20Solutions.ipynb)
# 7. [Functions](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/07%20Functions%20solutions.ipynb)
# 8. Debugging has no solutions notebook
# 9. [String manipulation](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/09%20string%20manipulation%20solutions.ipynb)
# 10. [Dictionaries](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/10%20-%20Dictionaries%20solutions.ipynb)
# 11. [Working with files](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/11%20working%20with%20files%20solutions.ipynb)
# 12. [Functions, bis](https://colab.research.google.com/github/CentreForDigitalHumanities/programming-in-python/blob/main/solutions/12%20Functions%2C%20bis.ipynb)
#
