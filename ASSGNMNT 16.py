#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT 16

# Q. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].

# In[1]:


years_list = [i for i in range(1997,1997+6)]
years_list
     


# Q. In which year in years_list was your third birthday? Remember, you were 0 years of age for your

# In[2]:


years_list[3]


# Q.In the years list, which year were you the oldest?

# In[3]:


max(years_list)
     


# Q. Make a list called things with these three strings as elements: 'mozzarella', 'cinderella','salmonella'.

# In[4]:


things = list(['mozzarella', 'cinderella','salmonella'])
things


# Q. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?

# In[6]:


for i in things:
    print(i.capitalize())
things
#Capitalize() will not update the list original values.
     



# Q. Make a surprise list with the elements "Groucho", "Chico", and "Harpo"

# In[7]:


surprise_list = ["Groucho", "Chico", "Harpo"]
surprise_list


# Q. Lowercase the last element of the surprise list, reverse it, and then capitalize it.

# In[8]:


surprise_list[-1].lower()


# In[9]:


surprise_list[-1][::-1]


# In[10]:


surprise_list[-1][::-1].upper()


# Q. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.

# In[14]:


e2f = {'dog':'chien','cat':'chat','walrus':'morse'}


# In[ ]:


Q. Write the French word for walrus in your three-word dictionary e2f


# In[15]:


e2f['walrus']


# Q. Make a French-to-English dictionary called f2e from e2f. Use the items method

# In[16]:


f2e = dict((key,value) for value,key in e2f.items())
f2e


# Q. Print the English version of the French word chien using f2e.

# In[17]:


f2e['chien']


# In[ ]:


Q. Make and print a set of English words from the keys in e2f.


# In[18]:


e2f.keys()


# Q. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

# In[19]:


life ={'animals':{'cat':['Henri', 'Grumpy', 'Lucy'], 'octopi':'', 'emus':''},
       'plants' :'',
       'other' :'' }
life


# Q. Print the top-level keys of life.

# In[ ]:





# In[20]:


life.keys()


# Q. Print the keys for life['animals'].

# In[21]:


life['animals'].keys()


# Q. Print the values for life['animals']['cat']

# In[22]:


life['animals']['cat']

