#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a function called most_frequent that takes a str and prints the 
#letters in decreasing order of frequency. Find text samples from several
#different languages and see how letter frequency varies between languages.


# In[2]:


#count how many times a letter appears in a string

def most_freq(s):
    d = dict()           #creates an empty dict
    for c in s:          #traverses the str
        if c not in d:   #if c is not in dict, create new item w/key c value 1
            d[c] = 1
        else:            #if c is in dict, increment d[c]
            d[c] += 1
    return d        


# In[3]:


letters = most_freq('teleporter')
letters


# In[4]:


t = letters.items()       #This creates a list of tuples from the dict
for letter, number in t:   #traverses the list of tuples and flips the key and value 
    print(number, letter)


# In[5]:


print(sorted(t, reverse = True))  #sorts the tuples in reverse order


# In[6]:


res = []          #create new list
for freq, x in t:    #
    res.append(x)
    
print(res)


# In[7]:


res.sort(reverse = True)
print(res)


# In[8]:


#The code from this point on are my attempts to print list in reverse of freq


# In[9]:


freqLetter = {}
for letter, freq in t:
    if not freq in freqLetter:
        freqLetter[freq] = []
    else:
        freqLetter[freq].append(letter)
        
print(sorted(freqLetter, reverse = True))


# In[10]:


new = {}
for key, value in letters.items():
    if not value in new:
        new[value] = []
    new[value].append(key)


# In[11]:


print(new)


# In[12]:



print(sorted(new, reverse = True))

