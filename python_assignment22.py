#!/usr/bin/env python
# coding: utf-8

# ##  Q. What is the result of the code, and explain?
# 
#  X = 'iNeuron'
#  def func(): print(X)
#  func()

# In[1]:


X = 'iNeuron'
def func():
    print(X)
func()

#Ans. The global variables are accessible in side the functions in python. 
#But we can not access function variable out side function. 
#Since x is global variable we are able to print it in side the function solution : 'iNeuron'


# ## Q. . What is the result of the code, and explain?

# In[3]:


X = 'iNeuron'
def func():
    X = 'NI!'

func()
print(X)

#Ans. The global variables are access in side the functions in python. But we can not access function variable out side function.
# Since x is golbal variable we are able to print it out side of the function solution = 'iNeuron'


# ## Q.     What does this code print, and why?
# 
# >>> X = 'iNeuron' >>> def func(): X = 'NI' print(X)
# 
# >>> func() >>> print(X)

# In[4]:


X = 'iNeuron'
def func():
    X = 'NI!'
    print(X)

func()
print(X)

#Ans. The global variables are access in side the functions in python. But we can not access function variable out side function.
# X is updated with 'NI' which is local to function and its immutable. its name space is with in the function solution = 'NI!', 'iNeuron'
     


# ## Q. What output does this code produce? Why?
# X = 'iNeuron' >>> def func(): global X X = 'NI'
# func() >>> print(X)

# In[6]:


X = 'iNeuron'
def func():
    global X
    X = 'NI!'
    print(X)

func()
print(X)
#Ans. since the X in side function is made Global, it will be accesible out side of the function too. 
#now X will have new value.

 #solution : 'NI!', 'NI!'


# ## Q. What about this code—what’s the output, and why?
# X = 'iNeuron' >>> def func(): X = 'NI' def nested(): print(X) nested()
# func() >>> X

# In[7]:


X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)
    
nested()
func()
X

#Ans. the nested() function will print 'iNeuron', Then func() does not display anything,
# and x ='NI' is not accessible out 
#side the function.
#Solution : 'iNeuron'


# ## Q. How about this code: what is its output in Python 3, and explain?
# def func(): X = 'NI' def nested(): nonlocal X X = 'Spam' nested() print(X)
# func()

# In[8]:


def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'spam'
    nested()
    print(X)

func()

#Nonlocal variables are used in nested functions whose local scope is not defined. 
#This means that the variable can be neither in the local nor the global scope. it print the updated value from nested 
#function

#Sol : 'spam'
     


# In[ ]:




