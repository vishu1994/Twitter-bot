#!/usr/bin/env python
# coding: utf-8

# In[2]:


import followers_lookup
import following_look_up
def main():
    not_following = list(set(followers_lookup.main())-set(following_look_up.main()))
    return not_following
    
if __name__=="__main__":
    c = main()
    if c == []:
        print("Everything is up to date")
    else:
        print(c)

