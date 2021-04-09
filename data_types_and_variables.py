#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1 
# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
# Result is $27


# In[8]:


cost_per_day = 3
the_little_mermaid = 3
brother_bear = 5
hercules = 1

result = cost_per_day * (the_little_mermaid + brother_bear + hercules)
print(result)


# In[ ]:





# In[40]:


#2
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. 
#     Google pays 400 dollars per hour, 
#     Amazon 380, and 
#     Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 
# 6 hours for Google and 
# 4 hours for Amazon.
# check = $7420


# In[12]:


google = 400
amazon = 380
facebook = 350


# In[13]:


google_hours = 6
amazon_hours = 4
facebook_hours = 10


# In[15]:


check = (google * google_hours) + (amazon * amazon_hours) + (facebook * facebook_hours)
print(check)


# In[ ]:





# In[ ]:


# 3
# A student can be enrolled to a 
# class only if the class is not full and 
# does not conflict with her current schedule.


# In[ ]:





# In[30]:


max_credits = 20
s1 = {'name':'Kady', 'credits':15, 'schedule_conflicts': False}
s2 = {'name':'Brookie', 'credits':25, 'schedule_conflicts': True}
s3 = {'name':'Luna', 'credits':12, 'schedule_conflicts': False}

def enrolled(currentStudent):
    if(currentStudent['credits'] < max_credits and currentStudent['schedule_conflicts'] == False):
        print ('{} has been enrolled'.format(currentStudent['name']))
    else:
        print ('{} has not enrolled'.format(currentStudent['name']))

enrolled(s1)
enrolled(s2)
enrolled(s3)
    


# In[31]:


class_is_full = False
schedule_conflict = True
enrollable_status = not(class_is_full or schedule_conflict)


# In[32]:


print(enrollable_status)


# In[ ]:


# 4
# A product offer can be applied only if people buys more than 2 items,
# and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.


# In[33]:


more_than_two_items = True
offer_not_expired = True
premium_membership = False
discount_elg = offer_not_expired and (more_than_two_items or premium_membership)
print(discount_elg) 


# In[95]:


# 5
# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace


# In[ ]:





# In[41]:


username = 'codeup'
password = 'notastrongpassword'

#variables
pass_charac = len(password) >= 5
pass_charac
user_charac = len(username) < 20
user_charac
is_pass_user_same = username == password
is_pass_user_same

#validation
is_valid_registation = pass_charac and user_charac and not is_pass_user_same
is_valid_registation


# In[ ]:




