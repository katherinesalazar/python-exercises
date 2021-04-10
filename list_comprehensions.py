#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]


# In[1]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits


# In[3]:


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers


# In[ ]:


# Example for loop solution to add 1 to each number in the list


# In[ ]:


numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

print(numbers_plus_one)


# In[ ]:


# Example of using a list comprehension to create a list of the numbers plus one.

numbers_plus_one = [number + 1 for number in numbers]
print(numbers_plus_one)


# In[6]:


# Example code that creates a list of all of the list of strings in fruits and uppercases every string

output = []
for fruit in fruits: 
    output.append(fruit.upper())
print(output)


# In[ ]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]


# In[12]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits


# In[14]:


uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)


# In[ ]:


# Exercise 2 - create a variable named capitalized_fruits and 
# use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]


# In[19]:


capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)


# In[ ]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.


# In[28]:


fruit1 = 'mango'
print(fruit1)


# In[34]:


len([letter for letter in fruit1 if letter in 'aeiou'])


# In[40]:


fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len([letter for letter in fruit if letter in 'aeiou']) >2]
print(fruits_with_more_than_two_vowels)


# In[ ]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. 
# The result should be ['mango', 'kiwi', 'strawberry']


# In[41]:


fruits_with_only_two_vowels = [fruit for fruit in fruits if len([letter for letter in fruit if letter in 'aeiou'])==2]


# In[43]:


print(fruits_with_only_two_vowels)


# In[ ]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters


# In[44]:


[fruit for fruit in fruits if len(fruit) > 5]


# In[ ]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters


# In[45]:


[fruit for fruit in fruits if len(fruit) == 5]


# In[ ]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters


# In[46]:


[fruit for fruit in fruits if len(fruit) < 5]


# In[ ]:


# Exercise 8 - Make a list containing the number of characters in each fruit. 
# Output would be [5, 4, 10, etc... ]


# In[47]:


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers


# In[48]:


[len(fruit) for fruit in fruits]


# In[ ]:


# Exercise 9 - Make a variable named fruits_with_letter_a 
# that contains a list of only the fruits that contain the letter "a"


# In[52]:


fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit ]
print(fruits_with_letter_a)


# In[ ]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 


# In[55]:


even_numbers = [num for num in numbers if num %2 == 0]
print(even_numbers)


# In[ ]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers


# In[56]:


odd_numbers = [num for num in numbers if num % 2 == 1]
print(odd_numbers)


# In[ ]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers


# In[58]:


positive_numbers = [num for num in numbers if num >1]
print(positive_numbers)


# In[ ]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers


# In[60]:


negative_numbers = [num for num in numbers if num < 0]
print(negative_numbers)


# In[ ]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a 
# list of numbers with 2 or more numerals


# In[63]:


# base 10 method
numbers_plus2_numerals = [num for num in numbers if not (-10 < num <10)]
print(numbers_plus2_numerals)


# In[64]:


# string method
[num if (num < 0 and len(str(num))>2) else num for num in numbers if len(str(num)) >1]


# In[ ]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. 
# Output is [4, 9, 16, etc...]


# In[71]:


numbers_squared = [num ** 2 for num in numbers]
print(numbers_squared)


# In[ ]:


# Exercise 16 - Make a variable named odd_negative_numbers that 
# contains only the numbers that are both odd and negative.


# In[75]:


odd_negative_number = [num for num in numbers if num % 2 == 1 and num < 0]
print(odd_negative_number)


# In[ ]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 


# In[77]:


numbers_plus_5 = [num + 5 for num in numbers]
print(numbers_plus_5)


# In[ ]:


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.


# In[78]:


def isprime(num):
    if num >= 2:
        for n in range(2, num):
            if not ( num % n == 0 ):
                return False
    else: 
        return False
    


# In[79]:


isprime(24)


# In[80]:


isprime(4)


# In[85]:


[num for num in numbers if isprime(num)]


# In[ ]:




