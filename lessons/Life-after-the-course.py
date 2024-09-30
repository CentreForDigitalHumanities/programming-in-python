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
# # Life after the course
#
# Entry level programming in Python - CDH
#
# Congratulations, you finished the course. During the course, you learned basic Python techniques as well as important refactoring and debugging skills. Finally, you learned how to import CSV files and obtained leads on how to conduct your own analysis.
#
# Due to the limited time, we could not cover all the basic skills that a programmer needs in order to be economic with their development time. Also, while online notebooks are a great teaching tool and we would not have been able to cover as much ground without them, you will be better able to reuse your own code if you learn how to run standalone Python programs on your own computer.
#
# In order to help you with the next steps on your learning journey, we list the concepts below and provide links to web pages where you can learn more about the topic in question. We recommend that you scroll through the entire notebook; all principles and techniques discussed here are essential best practices.

# %% [markdown]
# ## Troubleshooting
#
# Whether you are trying to install something and it is refusing or your own code is throwing errors at you, more often than not a well-chosen web search will lead you to a solution. Good queries generally include the name of the program or package that you use, the name of the feature or function that you use, and the name of the error that you get (or a concise description of the problem: "no output", "lower value than expected", etcetera). For example [`pandas read_csv EncodingError`](https://duckduckgo.com/?q=pandas+read_csv+EncodingError).
#
# In many cases, a web search will lead you to [Stack Overflow](https://stackoverflow.com) (or a related question-and-answer site). You can also post your own questions about code-related problems here. There are some [tips](https://stackoverflow.com/help/how-to-ask) to help you maximize the change that you'll get a useful answer. If somebody answers your question adequately, be sure to [accept the answer](https://stackoverflow.com/help/someone-answers). Some Reddit groups, such as [r/learnpython](https://www.reddit.com/r/learnpython/), can also be useful spaces for asking questions about your code.

# %% [markdown]
# ## Command line interface (CLI, shell)
#
# Command line interfaces (CLIs) let you control your computer by typing commands instead of by clicking with your mouse. Every PC comes with a CLI by default (including macs). On Windows, the default CLI is called Command Prompt (`cmd.exe`) while on other platforms, it is usually called Terminal. In both cases, the text-based interface running within the window is called the *shell*. Since the distinction is not so important most of the time, we often use the word "shell" or "terminal" to refer to either.
#
# You don't need to be a shell expert, but being able to navigate your file system and to run basic commands can be very useful when programming on your own PC. There are many [introductory tutorials online](https://duckduckgo.com/?q=basic+command+line+interface+tutorial). https://ss64.com is a useful cross-platform reference of standard commands and syntax.

# %% [markdown]
# ## Software needed for editing and running Python on your PC
#
# Running standalone Python on your PC is a bit different from using notebooks. At the very least, you will need a code editor and a Python interpreter. As the name suggests, a Python interpreter is a program that reads Python code and executes the program that is described in the code.
#
# Over time, programmers usually end up installing a lot of other software as well. For this reason, it is generally worthwhile to install a package manager.

# %% [markdown]
# ### Editor
#
# While there are more options, we will mention a few general-purpose code editors that are both widely used and actively maintained:
#
# - [BBEdit](https://www.barebones.com/products/bbedit/index.html) (macOS)
# - [Notepad++](https://notepad-plus-plus.org) (Windows)
# - [Sublime Text](https://www.sublimetext.com) (cross-platform)
# - [TextMate](https://macromates.com) (macOS)
# - [Visual Studio Code](https://code.visualstudio.com) (cross-platform, Edo's recommendation)
#
# There are also "integrated development environments" (IDEs) specifically targeted at Python programming, such as [Spyder](https://www.spyder-ide.org) for data scientists and [PyCharm](https://www.jetbrains.com/pycharm/) for application developers. These have lots of bells and whistles. Some people find them very convenient. We mention them here for completeness, but we recommend learning how to work without one first.

# %% [markdown]
# ### Python and a package manager
#
# macOS and Linux come with Python preinstalled by default, though this is usually an outdated version of Python. In principle, you *could* also just [download Python from the website](https://www.python.org/downloads/). However, since it is likely that you'll be installing more software alongside Python, we recommend investing some additional time to install a package manager instead, which will give you a central workflow for installing Python as well as any related software. Especially on Windows, using a package manager will likely provide a smoother experience as well.
#
# One approach to installing a package manager is [Anaconda](https://www.anaconda.com). It is specifically targeted at data scientists working with Python and it ships with many commonly used Python packages by default, as well as the Spyder IDE that we mentioned in the editor section. For a much smaller download, you can install [miniconda](https://docs.conda.io/en/latest/miniconda.html) instead, to get just Python, Anaconda's package manager (`conda`) and a small amount of supporting software. While conventient, `conda` is not a complete solution like the general purpose package managers that we discuss next.
#
# Linux distribution generally ship with a general purpose package manager by default, such as `apt-get` or `yum`. If you work with Linux, you are probably already familiar with your package manager. If you install Python through such a package manager, you might need to install a secondary package for Python *development* as well, which might for example be named `python-devel`.
#
# macOS does not ship with a package manager by default, but you can install [MacPorts](https://www.macports.org) or [HomeBrew](https://brew.sh).
#
# Windows does not follow the same conventions as Linux and macOS, but there are options. [Chocolatey](https://chocolatey.org) is a dedicated package manager for Windows. Since Windows 10, Microsoft provides its own [native package manager](https://docs.microsoft.com/en-us/windows/package-manager/) as well. At the DH Lab, we have tried neither of these options, so we cannot comment on how well they work. Alternatively, you can use the `pacman` package manager that is included with [Git for Windows](https://gitforwindows.org), which we recommend to install anyway. More about Git in a later section.

# %% [markdown]
# ## Basic workflow for running standalone Python
#
# Notebooks contain a mixture of formatted text and runnable snippets of Python code. Standalone Python programs, on the other hand, are plain text files containing only Python code (including comments) with the `.py` extension. Suppose that you copy-paste the following code into a new file using your code editor, and save it with the name `hello.py`:
#
# ```python
# print('Hello, world!')
# ```
#
# Using a shell, you can now navigate to the folder containing `hello.py` and type the following command in order to run it:
#
# ```shell
# python3 hello.py
# ```
#
# On Windows, depending on how you installed Python, you might need to run `py` instead of `python3`.
#
# *On Windows, the `python3` or `py` command will only work if your shell knows where to find Python. If you installed Python through a package manager, use the shell that ships with it, such as Anaconda Prompt. If you downloaded Python directly from the website, search the web on how to set the `PATH` environment variable and optionally also `PATHEXT`).*
#
# Typing just `python` instead of `python3` might work, too, but in some cases, this is still Python version 2 because it was installed on your PC by default. You can check the version like this:
#
# ```shell
# python --version
# ```

# %% [markdown]
# ## Modules
#
# The official name for a plain text file that contains Python code is *module*. The `hello.py` from the previous section is an example of a module. Modules are named this way because your program can consist of multiple files, so they enable *modular programming*. Spreading your code over multiple files can make it easier to find back the right piece of code (if you chunk your code in a logical way). Individual modules can also be reused in new programs.
#
# A module or group of modules that is specifically meant for reuse is called a *library*. By convention, a library is usually saved in a separate folder and we call that folder a *package*. We will discuss libraries and packages again in the section on dependencies.
#
# Suppose that we have a module named `cheerlead.py` with the following functions (the short notation used here was discussed in the "Iterables" section of the final exercise tips):

# %%
announce = 'We have a: {}'.format
yell = 'Go go {}!!!'.format

def cheer(name):
    letters = '\n'.join(map(announce, name))
    return '\n'.join([letters, yell(name)])


# %% [markdown]
# and we have a second module in the same folder, named `greet.py`, which uses the `cheer` function from `cheerlead.py`:
#
# ```python
# from cheerlead import cheer
#
# name = input('Welcome, visitor. What is your name? ')
# print(cheer(name))
# ```
#
# We can now run
#
# ```shell
# python3 greet.py
# ```
#
# While `greet.py` contains only part of the program, Python knows where to find the rest by following the `import` statements. You can read more about modules [here](https://docs.python.org/3/tutorial/modules.html).

# %% [markdown]
# ## Dependencies
#
# So far, we have used the word "package" liberally, but there are actually two kinds of "package": it can either refer to any software that you install using your package manager (such as Python itself), or to a collection of Python modules that was published for general reuse. This section is about the latter kind. When you use such a Python package in your project, this is called a dependency.
#
# All the `import` statements that we have seen in examples so far, can be roughly divided into three categories. Firstly, imports from other modules in the same directory, which are often written by the same author. The following examples appeared in previous sections:
#
# ```python
# from cheerlead import cheer
# from greet import main as greet_main
# ```
#
# Secondly, imports from *standard modules*. These modules are part of the standard library that ships with Python, so you never need to install them manually. Most of the following examples appeared in the tips:
#
# ```python
# import csv
# import os.path as op
# from operator import add
# from itertools import repeat
# from functools import reduce
# from statistics import mean, stdev
# from datetime import datetime as dt
# ```
#
# Finally, imports from *third-party packages*. These are neither part of your own code, nor of the Python standard library. The following examples appeared in the last few sections of the tips:
#
# ```python
# import pandas
# from sklearn.cluster import AgglomerativeClustering
# ```
#
# In Google Colab, many third-party packages are installed by default, so the code examples just worked. In the general case, however, third-party packages must be downloaded first. When your program requires such packages in order to run, it is necessary to document those dependencies. In the next three subsections, we discuss the main ingredients that you need in order to manage your dependencies well.

# %% [markdown]
# ### Virtual environments
#
# Once you start programming, you never stop. After your first program, there will be more projects. At some point, you might even be working on two or more projects in parallel.
#
# It is unlikely that two projects will use exactly the same packages. The packages needed for a specific project are referred to as a project's depencies. In many cases, the dependencies of one project will conflict with the dependencies of another. For this reason (and a few other reasons), it is highly recommended to keep separate sets of installed dependencies for each project. This is the job of virtual environments.
#
# A virtual environment is a folder in which you install third-party packages. You can have as many virtual environments as you want. Each virtual environment can also have its own version of Python. When you *activate* a virtual environment, its installed packages become available to you, while the packages inside all other virtual environments are invisible. When you install additional packages, they are added to the active virtual environment only.
#
# In the most basic case, you run `python3 -m venv` in the shell and tell it to create a new environment in a given directory. For example, the following command will create an environment in the folder `.env` within your current working directory:
#
# ```shell
# python3 -m venv .env
# ```
#
# After the above command, you can activate the environment like this on Linux, macOS and emulating environments like the MSYS2 included in Git for Windows:
#
# ```shell
# source .env/bin/activate
# ```
#
# and like this in the Windows Command Prompt:
#
# ```shell
# .env\Scripts\activate.bat
# ```
#
# After this you can run `deactivate` to leave the environment again. There are a couple of variations possible, such as selecting a different version of Python. You can read more about creating and using virtual environments [here](https://docs.python.org/3/tutorial/venv.html).
#
# Beyond the basic case, there are various tools that add sophistications, such as storing environments in a central place and switching between them with shorter commands. Anaconda/miniconda takes this quite far by including environment creation and switching into its own `conda` command. You can read more about that [here](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).

# %% [markdown]
# ### Installing packages
#
# By default, every virtual environment has the `pip` command, which lets you install third-party packages that were published to the [Python Package Index (PyPI)](https://pypi.org). Basically, this is a second, dedicated package manager just for Python packages. Manually installing a single package, for example `pandas`, looks like this:
#
# ```shell
# python3 -m pip install pandas
# ```
#
# Of course, it is also possible to update packages and to uninstall them again. You can read more about pip [here](https://packaging.python.org/installing/). Again, `conda` has its own way of doing things, which you can read more about [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html).

# %% [markdown]
# ### `requirements.txt`
#
# When using an external package, it is often the case that the feature you need was not yet present in an older version. It might also be removed again in a newer version. For this reason, the **versions** of the packages that you use, **are very important**. Each package itself might again depend on other packages (such indirect dependencies are automatically included when you `pip install` a package), and the versions of those indirect dependencies matter as well.
#
# It is **vitally important** to record the exact versions of all your direct and indirect dependencies, so that you can reproduce your environment at a later time or on a different computer. Without this, *it might be impossible to get your program to work again*.
#
# By convention, we store a listing of all direct and indirect dependencies with their exact versions in a file called `requirements.txt`. You can quickly create or update a `requirements.txt` based on the contents of your active virtual environment with `pip freeze`:
#
# ```shell
# python3 -m pip freeze > requirements.txt
# ```
#
# With `conda`, you can also do this:
#
# ```shell
# conda list > requirements.txt
# ```
#
# You should run either command again every time you add, update or remove a package. When publishing your code, **always** include the `requirements.txt`.
#
# You can install all the exact versions of packages specified in a `requirements.txt` using `pip install -r`:
#
# ```shell
# python3 -m pip install -r requirements.txt
# ```
#
# See [here](https://pip.pypa.io/en/latest/user_guide/#requirements-files) for more information about `requirements.txt`. There are some tools, such as [pip-tools](https://pypi.org/project/pip-tools/), that streamline the management of the `requirements.txt` and which can also automatically remove indirect dependencies that are no longer needed after an update.
#
# The `setup.py` or `setup.cfg` that comes with [`setuptools`](https://setuptools.pypa.io/en/latest/userguide/quickstart.html) is a more sophisticated alternative to the `requirements.txt`. It is recommended to convert to using `setuptools` when you consider publishing your package to PyPI. Like `requirements.txt`, it integrates well with `pip`.

# %% [markdown]
# ## The interactive Python prompt
#
# If you just enter `python3` in the shell, without passing the name of a module, Python will run in interactive mode. It shows a prompt that looks like this:
#
#     >>>
#
# After the prompt, you can enter any Python code. It can also be an `import` statement in order to retrieve functions from an existing module. Python will run the code that you enter, print any output and then present you with a new prompt. Among other things, this is useful for debugging individual functions, for using Python as an advanced calculator, or for trying out short snippets of code before typing them into a module.
#
# You can exit the interactive prompt by typing `quit()` (note that this doesn't work inside a regular module). You can also type `help()` for very helpful interactive documentation.

# %% [markdown]
# ## `main`
#
# In the example from the [Modules section](#scrollTo=Q0sFMv09Vzdp), there was a very strict task division between `cheerlead.py` and `greet.py`. `cheerlead.py` contained only reusable functions. If you were to run `python cheerlead.py`, it would silently exit without reading input or printing output. `greet.py`, on the other hand, contained *no* reusable code and was *only* fit for being run as a program. If we were to do `import greet` inside another module, that module would always ask for the same input and print the same output as `greet.py` would do, even if that other module is actually supposed to do something else. We could say that `cheerlead.py` is a reusable module while `greet.py` is a program entry point, although this isn't an official distinction.
#
# The task division doesn't have to be so strict. We can write modules that are both fit for reuse and that can also be run as a program. In order to do this, we follow the convention of defining a `main` function. All code that is supposed to run only when the module is run as a program, should go inside `main`. We can rewrite `greet.py` to follow this convention:
#
# ```python
# from cheerlead import cheer
#
# def main():
#     # same code as before, now inside main
#     name = input('Welcome, visitor. What is your name? ')
#     print(cheer(name))
#
# # call main, but only if this module was
# # run as the entry point of the program
# if __name__ == '__main__':
#     main()
# ```
#
# With the above adjustment, `python greet.py` will read input and print output as before, but the same will not happen if we do `import greet` inside another module and then run that module. Though we can still achieve that by explicitly importing and calling `main` if we want to:
#
# ```python
# from greet import main as greet_main
#
# def main():
#     print('This module is mostly doing the same as greet.py.')
#     greet_main()
#
# if __name__ == '__main__':
#     main()
# ```
#
# We could now continue to add a `main` function to `cheerlead.py` as well, and to add reusable functions to `greet.py` for importing in other modules. In this way, every module can be a reusable module and a program entry point at the same time.

# %% [markdown]
# ## Exit status (exit code)
#
# A long-standing convention in shells is that programs "return" a number when they exit, similar to how a function might return a value. So far, we have done nothing to indicate what should be this *exit status* of our program. By default, Python assumes that we want to set the exit status to `0` (zero), so that has been the implicit exit code of our programs. We can see the exit code of the last command that we ran using `echo %ERRORLEVEL%` in the Windows Command Prompt, or `echo $?` in most other shells:
#
# ```shell
# python3 greet.py
# echo $?
# ```
#
# The shell uses the exit status to detect whether a command ran successfully. Zero indicates success while non-zero exit codes indicate failure. Some programs use different numbers to indicate different ways in which they can fail.
#
# You are not required to set the exit code explicitly. If your program terminates with an error, Python will set the exit status to `1` by default, so that the shell understands that the program failed. You *can* however set the exit code explicitly using `sys.exit` (which also immediately terminates the program). A common pattern is to return a number from the `main` function and then pass this to `sys.exit`. We demonstrate this pattern in the small program below:
#
# ```python
# import sys
#
# def main():
#     # Let's see whether Python is consistent today.
#     if 1 < 2:
#         return 0 # success
#     else:
#         return 1 # failure
#
# if __name__ == '__main__':
#     sys.exit(main())
# ```

# %% [markdown]
# ## Program arguments
#
# We have previously shown the program `greet.py`, which will ask us for a name and then cheer it. Arguably, it would be a bit more efficient if we could pass the name already when calling the program, so we could skip the interactive question. Something like this:
#
# ```shell
# python3 greet.py Julian
# ```
#
# In the above example command, `Julian` is an argument to the `greet.py` program, similar to how we can pass arguments to functions.
#
# Using program arguments is a great way to make your program more flexible. For example, by making the path to a file a program argument, you make it easier to run your program with other files, or on another computer, where files might be located in a different folder.
#
# In the previous section, we saw `sys.exit`, which lets us set the program exit code; the same `sys` standard module also provides `argv`, which is a list with the program arguments, including the name of your program as the first element. Since `main` represents the program as a whole, let's extend the pattern for invoking `main` to include both program arguments and the exit status:
#
# ```python
# import sys
#
# def main(argv):
#     if len(argv) == 1:
#         print("You didn't pass any arguments.")
#         return 1
#     print('You passed these arguments:')
#     print(argv[1:])
#     return 0
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
# ```
#
# In the general case, a program may have many parameters, some of which may be optional. There is a syntax for working with named arguments as well, which would look like `python3 greet.py --name Julian` in our example above. By convention, the most important named arguments can also be abbreviated, which would look like `-n` instead of `--name`. You may also have parameters that accept a variable number of values, and then we generally expect that we can pass named arguments in any order. As you might imagine, extracting all that information correctly from `sys.argv`, which is just a simple list of strings, would be really difficult. Thankfully, you don't have to do this yourself.
#
# The `argparse` standard module gives you the means to just describe which arguments your program expects. It will read `sys.argv` for you and figure out what goes with what. The Python documentation includes an excellent [tutorial](https://docs.python.org/3/howto/argparse.html) on how to use it, so we won't do that here.
#
# Assuming that you have read that tutorial, here is a pattern that we suggest for integrating `argparse` in the invocation of your `main` function:
#
# ```python
# import sys
# import argparse
#
# # The argument parser is defined outside of the main function.
# # In a large program with many options, you might even have
# # a dedicated module just for the argument parser.
# argparser = argparse.ArgumentParser(
#     description='Description of your program',
#     # maybe you also want to define an epilog
# )
#
# def main(argv):
#     options = argparser.parse_args(argv[1:])
#     # the options object can be passed to other functions that
#     # main calls internally
#     return 0
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
# ```
#
# As a final tip, we will mention that you can save a set of arguments to a file and then pass the name of that file to your program in order to have all arguments in the file applied. This is functionality that `argparse` gives us for free. Suppose that I often want to run `python3 greet.py --name Julian`. I can write the following in a file named `greet.conf`:
#
#     --name
#     Julian
#
# If I then run `python3 greet.py @greet.conf`, it will do exactly the same as when I would run `python3 greet.py --name Julian`. In this case, the difference is not so impressive, but when you are passing more than a few arguments, this can be very convenient.

# %% [markdown]
# ## Assertions
#
# *This section is mostly redundant with module 5 of the course. It is retained for consistency with the next section.*
#
# Python has an `assert` keyword that lets you check that a condition that *should* be `True` is *actually* `True`. This is different from `if`, where the truth of the condition is optional; if you `assert` a condition and it is `False`, your program will stop with an error message. We can use this to protect ourselves and other programmers from mistakes. For example, we can add an assertion to our `cheer` function as follows:

# %%
def cheer(name):
    assert isinstance(name, str)
    letters = '\n'.join(map(announce, name))
    return '\n'.join([letters, yell(name)])


# %% [markdown]
# Now, our program will still work if used as intended, but if somebody passes a number, the program will fail with an `AssertionError`:

# %%
print(cheer('Kermit'))
print(cheer(100))


# %% [markdown]
# We can make the error more informative by adding a comma and a string that will appear when the assertion fails:

# %%
def cheer(name):
    assert isinstance(name, str), 'name must be a string'
    letters = '\n'.join(map(announce, name))
    return '\n'.join([letters, yell(name)])

print(cheer(100))


# %% [markdown]
# You can use as few or as many assertions in your code as you want. This is mostly a matter of taste. You don't need to omit them for performance; if you have a program that needs to run for a long time and you worry that the assertions might be slowing it down, just run `python3 -o program.py` instead of `python3 program.py` and all assertions will be skipped. Just keep in mind that assertions are meant for checking assumptions, rather than for reporting errors; for reporting errors there is the `raise` keyword, which you can read more about in Python's [exceptions tutorial](https://docs.python.org/3/tutorial/errors.html).
#
# There is however a special type of function that is all about writing assertions: the unittest.

# %% [markdown]
# ## Testing
#
# So far, when we wrote a function and we wanted to check that it worked, we just wrote a line in which we called the function. We did this in notebooks, and we could also use the interactive Python prompt for this purpose.
#
# ```python
# print(yell('Kermit'))
# ```
#
# We expect this line to output `Go go Kermit!!!`.
#
# If we edit the `yell` function again in the future, we will want to write such a line of code again to check that it still works. However, this would mean repeating ourselves. Better would be to save our test code in a function so we can run it as often as we want. Such a function is called a unittest. A unittest for the `yell` function might look like this:

# %%
def test_yell():
    assert yell('Kermit') == 'Go go Kermit!!!'


# %% [markdown]
# We might as well write tests for `announce` and `cheer` while we're at it and save all of our tests in a module named `cheerlead_test.py`, next to the `cheerlead.py` module:

# %%
from cheerlead import announce, yell, cheer

def test_yell():
    assert yell('Kermit') == 'Go go Kermit!!!'

def test_announce():
    assert announce('x') == 'We have a: x'

def test_cheer():
    name = 'Rose'
    output = cheer(name)
    lines = output.splitlines()
    assert len(lines) == len(name) + 1
    for index, letter in enumerate(name):
        assert lines[index] == announce(letter)
    assert lines[-1] == yell(name)

def main():
    # Note that we are putting function names in a list.
    # This is allowed! You can do it, too!
    tests = [test_yell, test_announce, test_cheer]
    for test in tests:
        test()

if __name__ == '__main__':
    main()

# %% [markdown]
# Now, whenever we change the contents of `cheerlead.py`, we only need to run `python cheerlead_test.py` in order to check that everything still works. If everything works, we get no output, otherwise we will see an `AssertionError`. We can add or update tests as desired. There is still some room for improvement, though:
#
# - It is a bit counterintuitive to remember that *no output* means that all tests *pass*. It would be nice to get some kind of explicit confirmation instead.
# - The `cheerlead_test.py` module as a whole is essentially a list of test functions, but we have to list those tests *again* in the `tests` variable inside the `main` function. We have to manually update that variable every time we add or remove a test, so we are repeating ourselves. Ideally, we should have a program that automatically detects any test functions that are present and then runs them all.
# - The `main` function will stop as soon as any assertion fails. That means that if `test_yell` fails, we get no information on whether `announce` and `cheer` are working as intended. It would be more convenient if all tests always run, even if some of them fail.
#
# The [third-party `pytest` package](https://docs.pytest.org/) solves all of these problems. If we `pip install pytest` and remember to update our `requirements.txt`, we can still write our test module the same way, but we don't need the `main` function and the `tests` variable anymore:
#
# ```python
# from cheerlead import announce, yell, cheer
#
# def test_yell():
#     assert yell('Kermit') == 'Go go Kermit!!!'
#
# def test_announce():
#     assert announce('x') == 'We have a: x'
#
# def test_cheer():
#     name = 'Rose'
#     output = cheer(name)
#     lines = output.splitlines()
#     assert len(lines) == len(name) + 1
#     for index, letter in enumerate(name):
#         assert lines[index] == announce(letter)
#     assert lines[-1] == yell(name)
# ```
#
# Now, when we run just the command `pytest`, it will do all of the following:
#
# - It recognizes all modules with a name ending in `_test.py` as test modules.
# - In every test module, it recognizes all functions with a name starting with `test_` as unittests.
# - It runs *all* tests, even if some tests fail along the way.
# - It shows which tests are being run, indicating for each whether it passed or not.
# - When an assertion fails, instead of just showing us the raw `AssertionError`, it gives us a detailed breakdown of the failing condition.
#
# On top of all that, `pytest` gives us many other tools to make testing even more flexible and efficient. For example, we can also check that functions will fail in a particular way if you pass them particular arguments. Testing with `pytest` is such a helpful, powerful tool during development that we recommend using it in every Python project. You can read all about it [here](https://docs.pytest.org/).

# %% [markdown]
# ## Version control (Git)
#
# A version control system (VCS) keeps track of the changes that you make to your code. This enables you to find back changes that you made in the past and find out why you made them. You can also use this to revert an old change, while keeping changes that came after it. VCSs do this by efficiently storing all versions of your code in a system called a *repository*.
#
# All modern VCSs also allow you to create *branches*, which you can think of as parallel series of versions, or "alternative histories" of your code. You might work on a new feature on one branch, recording several changes as you go, then switch to another branch to fix a bug that you noticed while working on the feature, but which isn't related to the feature itself. Fixing the bug on a separate branch lets you focus on the bug, without having to worry about unfinished code related to the new feature. When you finish the bugfix, you switch back to the feature branch, and when you finish that as well, you can *merge* the branches, creating a single version of your program that includes *both* the bugfix *and* the new feature.
#
# Branches are also a great tool for collaborating with other programmers. When working on a large project, you might develop one feature while another programmer is developing another feature at the same time on another branch. You don't have to see each other's changes until you merge your branches together. This is such an efficient workflow that all software development teams are using it. However, once you get used to a VCS, you'll want to use it even for a small project that you work on alone.
#
# Git is a distributed VCS (DVCS) that has become very popular. "Distributed" basically means that it can handle branches very well: developers store their branches locally and they can optionally synchronize them with collaborators. Popular platforms like GitHub, BitBucket and GitLab facilitate such collaboration (although it can also be done without such a platform). Git is by no means the only good DVCS (for example, Mercurial is also good), but if you have not chosen a DVCS yet, Git is a fine choice.
#
# The book [Pro Git](https://git-scm.com/book) is a detailed introduction to Git. You can either read it on screen, free of charge, or buy it in print. If you want to get started quickly with a short tutorial and save the book for later, [Git Immersion](https://gitimmersion.com) is a good choice.
#
# Some advice:
#
# - Save many commits (versions) with small changes between them. Don't overhaul entire modules and then record only a single new commit, because this largely defeats the purpose of having a VCS.
# - One logical change per commit. If you fix a typo, then that fix is a commit all by itself, even if you changed only a single character. If you rename a function which you happen to call in twenty different modules, then the name changes in the module where it is defined as well as in all the modules where it is called all belong together in a single commit. Other, unrelated changes that you might have made in those same modules should *not* be part of the same commit.
# - If you worked a little bit "out of order", Git has tricks that let you include only some of the changes that you made in the next commit, while keeping the remainder for subsequent commits. Look into "interactive staging" on how to do this.
# - Similarly, if you make a change that with hindsight should have been included in an earlier commit, you can fix this afterwards. Look into "interactive rebase" on how to do this. Note that you should only rebase commits that you have not shared with other people yet.
# - If, with hindsight, you combined changes in a commit that should have been in separate commits, you can also split that commit afterwards during an interactive rebase. However, keep in mind that reordering and merging small commits is much easier than breaking apart large commits. This is another reason why you should err on the side of tiny commits.
