# Course meta-instructions

(instructions for course instructors)

This course is made for aspiring software developers, by established software developers. That means we like to follow a few good practices from our profession:

- We use [jupytext](https://github.com/mwouts/jupytext) for easy editing and diffing of the course materials. Please edit the `*.py` files rather than the `*.ipynb` files.
- We use [pip-tools](https://pypi.org/project/pip-tools/) to manage the dependencies (primarily juptext).
- We use the [git-flow](https://nvie.com/posts/a-successful-git-branching-model/) branching model. Releases are named after the name and month of the course edition, for example `2026-05`. Please make sure your git-flow implementation puts the release tag on the `main` branch and not on the temporary release branch (some implementations do this incorrectly).

The last step of cutting a release should be to regenerate the `*.pynb` files from the source `*.py` files. If necessary, first install the dependencies in a virtual environment. The dependencies do not all support Python 3.14 yet, so use Python 3.13 or earlier.

```sh
pip install -U pip
pip install pip-tools
pip-sync
```

With the dependencies installed, use the following command to update all the Jupyter notebooks.

```sh
jupytext --sync {lessons,solutions}/*.py
```
