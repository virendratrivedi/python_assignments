#!/usr/bin/env python
# coding: utf-8

# ## Q.Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'

# In[6]:


get_ipython().system('pip install google-colab')
from google.colab import files
uploaded = files.upload()


# #  Upload widget is only available when the cell has been executed in the current browser session. Please rerun this cell to enable.
# 
# Saving zoo.py to zoo.py
# 
# 

# In[8]:


import zoo
from importlib import reload
reload(zoo)

zoo.hours()


# ## Q. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[9]:


import zoo as menagerie
menagerie.hours()


# ## Q.Using the interpreter, explicitly import and call the hours() function from zoo.

# In[7]:


from zoo import hours
hours()


# ## Q. Import the hours() function as info and call it.

# In[ ]:


from zoo import hours as info
info()


# ## Q. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, 'c': 3, and print it out.

# In[11]:


plain = {'a': 1, 'b': 2, 'c': 3}
plain


# ## Q. Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

# In[12]:


from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy


# ## Q. Make a defaultdict called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a']

# In[13]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']


# In[ ]:




