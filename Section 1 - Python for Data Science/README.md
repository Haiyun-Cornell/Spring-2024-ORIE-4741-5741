# Section 1 Python for Data Science

In this section we'll be doing an overview of some handy tools in python for data science (namely data manipulation and visualization) that you might not have seen in a more traditional coding class. Based on the class survey, most of you have used python before so we'll assume some basic familiarity with python and jupyter notebooks. If you haven't worked with python before try a quick online tutorial (like [this](https://www.learnpython.org/)) to get familiar with basic data types and syntax.

You may find [some basic knowledge of UNIX commands](http://mally.stanford.edu/~sr/computing/basic-unix.html) helpful (and probably necessary). If you are using a Unix-like system like macOS, Ubuntu or Linux, you should already have a terminal available in system applications; for Windows 10, the terminal can be downloaded from [here](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab).  

## Part 1: Access to Python and Jupyter notebook

If you don't have Jupyter notebook installed on your computer, we recommend installing Anaconda. It is a free and open-source distribution that includes applications like Jupyter notebook and a distribution for python, and should be useful even outside this course. The installer can be found at <https://www.anaconda.com/products/individual>. 

To get started, open up a new terminal or anaconda prompt. We'll start by creating a new environment, a handy container for all our packages, and then launch a jupyter notebook. Type the following into your prompt - feel free to change the name of the environment or the packages you want (we'll be using pandas and seaborn today)

```
conda create -n ORIE4741 python=3.8
conda activate ORIE4741
conda install pandas seaborn jupyter
```
Then open Jupyter notebook by typing `jupyter notebook`. 

## Part 2: Access the Jupyter notebook for this section

The Jupyter notebooks for this section are in this folder. We will first clone this GitHub repository (if you wonder what this means, we will talk about it in a few weeks!) to your local computer and then run the notebook.

### Step 1: clone the GitHub repository

In **terminal**, clone the repository for all ORIE4741 sections by

```
git clone https://github.com/ORIE4741/section.git
```

There will be a cloned folder named "section" in your local computer at the current path.

### Step 2: Open the tutorial notebook

In terminal, again type `jupyter notebook` <sup id="a1">[1](#f1)</sup>. The terminal will start a Jupyter notebook process <sup id="a2">[2](#f2)</sup>, and you will be re-directed to the browser. Then in browser, navigate to the "section" repository you just cloned and open `Section 1 - Python for Data Science/Section 1 - Pandas Crash Course`.

<b id="f1">1</b>: The current path determines how many files you can access to in Jupyter notebook. You may want to navigate to the root or home directory before typing this command if you want to access most of the files in your local computer. 

<b id="f2">2</b>: Don't close the terminal window or terminate the process when you use Jupyter notebook.

