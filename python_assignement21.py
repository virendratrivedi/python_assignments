#!/usr/bin/env python
# coding: utf-8

# ## Q. Add the current date to the text file today.txt as a string.

# In[1]:


import datetime
from datetime import date
now = date.today()
cur_date = now.isoformat()
cur_date


# In[2]:


with open('today.txt','w') as file:
    file.write(cur_date)


# ## Q. Read the text file today.txt into the string today_string

# In[3]:


with open('today.txt','r') as file:
    today_string = file.read()
today_string


# ## Q. Parse the date from today_string.

# In[4]:


from datetime import datetime
format = '%Y-%m-%d'
datetime.strptime(today_string,format)


# ## Q. List the files in your current directory

# In[5]:


import os
os.listdir('.')


# ## Q.  Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.

# In[6]:


import multiprocessing

def printsec(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())
    
if __name__ == '__main__':
    import random    
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=printsec, args=(seconds,))
        proc.start()
     


# In[ ]:


get_ipython().system('python abc.py')


# ## Q. Create a date object of your day of birth

# In[8]:


my_dob = date(1985,8,7)
my_dob


# ## Q. What day of the week was your day of birth?

# In[9]:


my_dob.weekday()


# ## Q. When will you be (or when were you) 10,000 days old?

# In[10]:


from datetime import timedelta
day10000 = my_dob + timedelta(days=10000)
day10000


# In[ ]:




