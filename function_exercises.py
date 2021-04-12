#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1
# Define a function named is_two. 
# It should accept one input and 
# return True if the passed input is either the number or the string 2, 
# False otherwise.

def is_two(num):
    """
    Accepts one input and returns 
    True if the passed input is either the number or the string 2
    Returns false if the passed input is not either the number 2 or string 2
    """
    if num == 2:
        return True
    if num == '2':
        return True
    else:
        return False

is_two(2)
is_two('2')   
is_two(3)
get_ipython().run_line_magic('pinfo', 'is_two')
is_two(8)


# In[55]:


#1 other method:

def is_two(x):
    return x == 2 or x == "2"

assert is_two(2) == True
assert is_two('2') == True
assert is_two(3) == False


# In[57]:


# 2
# Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.

def is_vowel(stringex):
    """
    Returns true if the passed string is a vowel, 
    False otherwise
    """
    if stringex in [('a', 'e', 'i', 'o', 'u')]:
        return True
    else: 
        return False


# In[60]:


is_vowel('e')
is_vowel('k')


# In[63]:


#other 2

def is_vowel(string):
    if type(string) == str:
        return string.lower in ['a', 'e', 'i', 'o', 'u']
    else: 
        return False
    
is_vowel('e')
is_vowel('k')


# In[ ]:


#3
#Define a function named is_consonant. 
#It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this.

def is_consonant(letter):
    """
    Returns True is the passed string is a consonant,
    False otherwise
    
    """
    if letter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return False
    else:
        return True
    
is_consonant('i')
is_consonant('k')
is_consonant('e')
is_consonant('I')
get_ipython().run_line_magic('pinfo', 'is_consonant')


# In[ ]:


#3

#WIP

def is_consonant(letter):
    if type(string) == str:
    
    if letter in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return False
    else:
        return True


# In[ ]:


# 4

def change_first_consonant(string):
    if string[0] in ('a', 'e', 'i', 'o', 'u'):
        return ("Not a valid string. Try again.")
    else: 
        return string.capitalize()
    change_first_consonant(string)
    return(change_first_consonant(string))

change_first_consonant('brooklyn')
change_first_consonant('apple')
get_ipython().run_line_magic('pinfo', 'change_first_consonant')


# In[68]:


# #5
# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.
def calculate_tip(bill, tip_percentage):
    if tip_percentage < 0 or tip_percentage > 1:
        return "Tip must be between 0 and 1 "
    tip_amount = tip_percentage * bill
    return tip_amount

calculate_tip(100,.20)


# In[8]:


# #5
# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill_total):
    if tip_percentage >= 0 and tip_percentage <= 1:
        return (tip_percentage * bill_total)
    elif tip_percentage > 1:
        return "good tipper"
    else: 
        return "bad tipper"
    
calculate_tip(2, 500)


# In[9]:


# 6
# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    if original_price > 0:
        return (original_price - (original_price * (discount_percentage/100)))
    else:
        return "wrong price"

    apply_discount(95,20)


# In[13]:


# 7
# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, 
# and return a number as output.

def handle_commas(string):
    if "," in string:
        return string.replace(",", "")
    else:
        return int(string)
    
handle_commas('100,000')


# In[69]:


# 8
# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(num):
    if num < 69:
        return 'F'
    elif num <= 79:
        return 'C'
    elif num <= 89 :
        return 'B'
    elif num <= 100:
        return 'A'
    
get_letter_grade(90)
get_letter_grade(59)
get_letter_grade(71)
get_letter_grade(80)


# In[85]:


# 9
# Define a function named remove_vowels that accepts a string 
# and returns a string with all the vowels removed.

def remove_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u') 
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")
    print(string)


# In[86]:


remove_vowels('brooklyn')


# In[74]:


# 10
# Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

import re
def normalize_name(s):
    
    s = s.replace(' ', '_')
    s = re.sub('[^0-9a-zA-Z_]', '',s)
    
    s = re.sub('^[^a-zA-Z]+', '',s)
    s = s.lower()
    return s
    


# In[75]:


print(normalize_name("45Kady!!!"))


# In[79]:


# 11
# Write a function named cumulative_sum that accepts a list of numbers 
# and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(nums_list):
    return [sum(nums_list[:i+1]) for i in range(len(nums_list))]


# In[83]:


cumulative_sum([1, 1, 1])


# In[ ]:




