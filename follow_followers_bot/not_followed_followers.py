#!/usr/bin/env python
# coding: utf-8

# In[7]:


import followers_lookup
import following_look_up
def main():
    not_following = list(set(followers_lookup.main())-set(following_look_up.main()))
    return not_following
    
# print(not_following)#they are anish's followers whom i(sanjeet) don't follow. Now will try to follow them
# for client_id in not_following: #authomatically
#     print(client_id)
if __name__=="__main__":
    c = main()
    print(c)


# In[ ]:




