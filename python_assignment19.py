#!/usr/bin/env python
# coding: utf-8

# ## Q. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?

# In[2]:


class Thing:...
    #pass


# In[3]:


obj_of_t = Thing()
print(obj_of_t)


# ## Q. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.

# In[4]:


class Thing2:
    letters = 'abc'

Thing2.letters 


# ## Q.Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this? 

# In[8]:


class Thing3:
    def __init__(self,letter):
        self.letter=letter
    def letters(self):
        print(self.letter)

Thing3('xyz').letters()        
    


# ## Q. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.

# In[14]:


class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
    def printvalue(self):
        print(self.name,self.symbol,self.number)
    

obj=Element('Hydrogen','H',1)  
obj.printvalue()
    


# ## Q. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.

# In[16]:


dict = {'name':'Hydrogen', 'symbol':'H','number': 1}
hydrogen = Element(**dict) # using dictionary unpacking **
hydrogen.printvalue()
     


# ## Q. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.

# In[17]:


class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name,self.symbol,self.number)


# hydrogen = Element('Hydrogen','H',1)
# hydrogen.dump()

# ## Q. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.

# In[19]:


class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s'% (self.name, self.symbol, self.number) )


# In[20]:


hydrogen = Element('Hydrogen','H',1)
print(hydrogen)


# ## Q. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.

# In[22]:


class Element(): 
    def __init__(self ,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return (self.__name)
    @property
    def symbol(self):
        return (self.__symbol)
    @property
    def number(self):
        return (self.__number)


# In[23]:


hydrogen = Element('Hydrogen','H',1)
hydrogen.name


# ## Q. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.

# In[24]:


class Bear:
    def eats():
        print('berries')

class Rabbit:
    def eats():
        print('clover')

class Octothorpe:
    def eats():
        print('campers')   


# In[25]:


Bear.eats()


# In[26]:


Rabbit.eats()


# In[27]:


Octothorpe.eats()


# ## Q. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.

# In[28]:


class Laser:
    def does(self):
        return('disitegrate')
class Claw:
    def does(self):
        return('crush')
class SmartPhone:
    def does(self):
        return('ring')
        
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return ('Laser is %s, Claw is %s, SmartPhone is %s' % (self.laser.does(),self.claw.does(),self.smartphone.does()))


# In[29]:


robo = Robot()


# In[30]:


robo.does()


# In[ ]:




