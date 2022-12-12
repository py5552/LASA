#!/usr/bin/env python
# coding: utf-8

# # Coding tips and tricks!
# 
# Here are some `tips and tricks` for coding in Python.
# 
# ## +=, -=
# 
# This trick will save you a lot of time (x is a int or float variable, y is a also an int or float)
# 
# **Instead of writing** x = x + y or x = x - y
# 
# `Write` x += y or x -= y
# 
# 
# 
# ## How it works
# 
# In the following there is a brief section explaining what the trick is and then some code!
# 
# ## What level, beginner, intermediate or advanced?
# 
# This will have all levels!

# `Functions!`
# 
# These allow you to define certain code and call it using the function. You use **def _ ()** to call the function. _ is the name of the function. You can use **return** to return a value back to the caller. Functions often have **parameters** which are used when a function is called.
# The structure:

# In[1]:


def name_of_function(parameter1, parameter2):
    #Code goes here
    return parameter1 + parameter2
    #You can return anything you like
name_of_function(1,5)


# `Libraries`
# 
# These are collections of **pre-written code** which you can use to make certain tasks easier. For example I can use **NumPy** for more complex math. To download a library you either have to use **pip** (on windows) or **anaconda** (on mac). To use pip go to **cmd** (comand line) run it as admin and type in **pip install (the name of the library)**

# In[2]:


from numpy import *   #(this means import evething from numpy. Put at top of your code)


# There are a lot more data libaries. For more information about this, see [The Top 10 Python Libraries](https://www.interviewbit.com/blog/python-libraries/)
