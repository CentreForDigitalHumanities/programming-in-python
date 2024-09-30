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

# %% [markdown] id="Buvh9v-iYeOO"
# # Module 1: Introduction
#
# ## Exercise solutions
#
# [Module 1](https://colab.research.google.com/drive/1W8DqryKuOwPKflPnObv4bJtNKknRsvav)
#
# ## CDH course "Programming in Python"
#
# [index](https://colab.research.google.com/drive/1kFvnhumJ0tOTzDVJnIvvMDRRJ19yk9ZS)

# %% [markdown] id="pKIEfocbMaIR"
# ## Exercise 1.1: Try it out

# %% id="6hlNxRNNM1fV" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680706108778, "user_tz": -120, "elapsed": 213, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="1e442ffe-2c24-468e-8f23-4dde9dae23ad"
print(1)
1

# %% id="VIm6FdRIM6OE" colab={"base_uri": "https://localhost:8080/", "height": 52} executionInfo={"status": "ok", "timestamp": 1680705583794, "user_tz": -120, "elapsed": 7, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="14982304-6483-4d06-f313-134443868ad9"
print('oops')
'oops'

# %% [markdown] id="Yz1P17hS3Dnj"
# The slight surprise in the above output is that `'oops'` is first printed without quotes, and then with quotes. `print` is meant to present data in a human-friendly way, so it strips quotes from text values (which we call strings). Bare values, on the other hand, are shown in the way in which you would type them into Python.

# %% id="_MN48xz5NAya" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680705926915, "user_tz": -120, "elapsed": 226, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="58a646e7-26cf-4eed-97fd-37bd06d300f1"
print()

# %% [markdown] id="yP3jC8AZ4Kyk"
# You are allowed to call `print` without any value. This prints a newline.

# %% id="g9WKeIA2NVIA" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680706112032, "user_tz": -120, "elapsed": 222, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="e9ca8138-4998-47b1-e2c9-3332e4e968e5"
print('apricot')
print('banana')
print('cherry')

# %% id="NCbCfbHaNafJ" colab={"base_uri": "https://localhost:8080/", "height": 38} executionInfo={"status": "ok", "timestamp": 1680597375941, "user_tz": -120, "elapsed": 237, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="db68067b-3cba-4534-ea4d-f22b424fd253"
'apricot'
'banana'
'cherry'

# %% [markdown] id="snD4bhFA4VTx"
# Normally, a bare value by itself is never shown. It is a special "service" of notebooks that the last value in a code block is shown. This is why we see only `'cherry'` and not `'apricot'` or `'banana'`.

# %% id="-ZuiJ92yNqpi"
# apricot
# banana
# cherry

# %% [markdown] id="qYUevKdW4uEc"
# Python ignores comments. From the perspective of Python, this code block is empty, so there is no output.

# %% id="b9bTbrNSNwwn" colab={"base_uri": "https://localhost:8080/", "height": 52} executionInfo={"status": "ok", "timestamp": 1680706115343, "user_tz": -120, "elapsed": 185, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="7229da45-10dc-4df7-9f14-d1c91b2f639f"
print('apricot')
'banana'
# cherry

# %% id="GYmcSm6iOAiA" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680597832375, "user_tz": -120, "elapsed": 15, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="13ce5d1a-2a9f-44e2-cb38-4736ed7db735"
# apricot
'banana'
print('cherry')

# %% [markdown] id="Nk_csoK1456t"
# `'banana'` is not the last value in the code block, so it is not shown. `print('cherry')` has no value of itself (although it causes output); this is why we see only `cherry` and not this:
#
# ```
# cherry
# 'cherry'
# ```

# %% id="sNNoSfndOSiw" colab={"base_uri": "https://localhost:8080/", "height": 135} executionInfo={"status": "error", "timestamp": 1680598147401, "user_tz": -120, "elapsed": 286, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="11ca5bd8-3235-4980-9b67-0a191d6515b3"
print(#oops)

# %% [markdown] id="4WV_vzIu6ZXo"
# EOF stands for "end of file", with "file" here referring to the code block. Python reads `print(` and then ignores the rest of the line because of the comment. Every `(` should have a matching `)`, so Python is surprised that the code ends without that matching `)` (which it ignored because it is inside the comment).

# %% id="6IZS1NUuTdOX" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1680598226349, "user_tz": -120, "elapsed": 312, "user": {"displayName": "Julian Gonggrijp", "userId": "06467962548183964912"}} outputId="04fd0ec0-61eb-4604-f9cd-0b66fb0d82bd"
print('apricot', 'banana')

# %% [markdown] id="G_aPWTsL64wW"
# You are allowed to pass more than one value to `print`. By default, it puts spaces between them. You can change the space into something else as follows:
#
# ```py
# # Use a comma instead of a space
# print('apricot', 'banana', sep=',')
#
# # Glue values together directly (no separator)
# print('apricot', 'banana', sep='')
# ```
#
# Use can use any separator you like, even very long strings.

# %% [markdown] id="Tr3wPlHMeBCI"
# ## Exercise 1.2: Hello, world!

# %% id="jN7WTVOOSq2C"
# The following would work!
# (but only in a notebook)
'Hello, world!'

# %% id="qNjQXYFc7wfF"
# This is slightly better.
print('Hello, world!')

# %% [markdown] id="zI0ohEpPUwpC"
# ## Next module
#
# [2. Values and expressions](https://colab.research.google.com/drive/1FDQgdJabqIr2sZd1PNchJ_CKGefOrPE_) - [solutions](https://colab.research.google.com/drive/1nnt2VGcmOkHlAWco7xes1O3vr2ser9dD)
