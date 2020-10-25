#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#read the words in words.txt and store them as keys in a dict.
#Use the in operator to check whether a string is in the dict.


# In[1]:


file = open('words.txt', 'r')             #opens a file
f = file.readlines()                      #reads each line in the file

newList = []                              #creates a list called newList
for line in f:                            #traverses through each word in list and assigns it to line
    if line[-1] == '\n':                  #removes '\n' from each line
        newList.append(line[:-1])         #adds the word to newList
    else:                                 #if there is no '\n', it adds the word to newList
        newList.append(line)

        
# Code works so far. Use print(newList) to test


# In[2]:


d = dict()                          #creates a blank dictionary called d

for word in newList:                 #traverses through each word in newList                           
    if word not in d:                #if the word in newList is not in d, it adds it
        d[word] = word
    else:                            #if the word is already in d, continue the loop?? I'm not sure about this part.
        d[word] += word

## tested and code assigns all words as keys with a value of thier word: ('aah': 'aah')
## Not sure if that should be happening.


# In[3]:


key = 'aah'             # key value that is being looked for.

if key in d:             #traverse through dict looking for key
    print("yes")
else:
    print('no')
    

