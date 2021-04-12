#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1 
# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours


# In[12]:


# query for days of the week

day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

what_day_is_it = "wednesday"

if day == ("tuesday", "wednesday", "thursday", "friday", "saturday"):
    print("it is not monday")
elif day ==("monday"):
    print("lets get this bread, it/'s monday")
else:
    print("its not a day")


# In[ ]:


# query for days of the week

days_of_the_week = ["tuesday", "wednesday", "thursday", "friday", "saturday"]

day = "wednesday"
day = "monday"
day = "monday"

if day in days_of_the_week == ["tuesday", "wednesday", "thursday", "friday", "saturday"]:
    print("it is not monday")
if day ==("monday"):
    print("lets get this bread, it/'s monday")


# In[13]:


# A
# promting user for days of the week

day_of_the_week = input("Please input a day of week: ")

if day_of_the_week in ["tuesday", "wednesday", "thursday", "friday", "saturday"]:
    print("it is not monday")
if day_of_the_week ==("monday"):
    print("lets get this bread, it/'s monday")
else:
    print('it is not a day')


# In[27]:


# prompt the user for a day of the week, print out whether the day is Monday or not

days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

current_day = "tuesday"

if current_day == ("tuesday"):
    print("it is not monday")
if current_day == ("wednesday"):
     print("it is not monday")
if current_day == ("thursday"):
     print("it is not monday")  
if current_day == ("friday"):
     print("it is not monday") 
if current_day == ("saturday"):
     print("it is not monday") 
if current_day == ("sunday"):
     print("it is not monday") 
elif current_day ==("monday"):
    print("lets get this bread, it\'s monday")


# In[14]:


# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

current_day = "sunday"

if current_day ==("monday"):
    print("it is a weekday")
if current_day == ("tuesday"):
    print("it is a weekday")
if current_day == ("wednesday"):
     print("it is a weekday")
if current_day == ("thursday"):
     print("is a weekday")  
if current_day == ("friday"):
     print("it isa a weekday") 
if current_day == ("saturday"):
     print("it is the weekend") 
if current_day == ("sunday"):
     print("it is a weekend") 


# In[19]:


# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekends = ["saturday", "sunday"]

day = input("Please note the day of the week ")

if day in weekdays == ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("it is a weekday")
if day in weekends == ["saturday", "sunday"]:
    print("it is a weekend")


# In[45]:


# C
# create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours



hours_worked = 48
hourly_rate = 100

if hours_worked > 40:
    hourly_rate = hourly_rate * 1.5
    check_amt = hours_worked * hourly_rate
    print(check_amt)
elif hours_worked <= 40:
    check_amt = hours_worked * hourly_rate
    print(check_amt)

    


# In[ ]:





# In[9]:


# 2
#Loop Basics

# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.


# In[46]:


i = 5

while i <= 15:
    print(i)
    i += 1


# In[48]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

i = 0 

while i <= 100:
    print(i)
    i += 2


# In[49]:


# Alter your loop to count backwards by 5's from 100 to -10.

k = 100
while k >= -10:
    print(k)
    k -= 5


# In[52]:


# Create a while loop that starts at 2, 
# and displays the number squared on each line while the number is less than 1,000,000. 
# Output should equal:
#  2
#  4
#  16
#  256
#  65536

## WIP

l = 2
while l < 1_000_000:
    print(l)
    l **= 2


# In[57]:


# # Write a loop that uses print to create the output shown below.
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

i = 100
while i >= 5:
     print(i)
     i += -5
   
    


# In[ ]:


# b 

# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# In[72]:


proposed_num = input('Please insert a positive integer ')


# In[73]:


type(proposed_num)


# In[74]:


proposed_num = int(proposed_num)


# In[75]:


type(proposed_num)


# In[76]:


for n in range(1,11):
    print(f'{proposed_num} X {n} = {proposed_num * n}')


# In[ ]:


# Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


# In[77]:


for n in range(1,10):
    print(str(n) *n)


# In[ ]:





# In[ ]:


# c
# break and continue

# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input.
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.


# In[80]:


while True: 
    posited_num = input('Please insert an odd number between 1 and 50: ')
    if posited_num.isdigit():
        if int(posited_num) % 2 == 1 and int(posited_num) <= 50:
            break
        


# In[83]:


posited_num


# In[85]:


posited_num = int(posited_num)
for num in range(1, 50, 2):
    if num == posited_num:
        print('Skipping a number!', num)
    else:
        print('Here is an odd number: ', num)


# In[79]:


# d
# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, 
# so you'll need to convert this to a numeric type.)


# In[88]:


while True: 
    posited_num = input('please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
posited_num = int(posited_num)
for num in range(0, posited_num +1 ):
    print(num)


# In[ ]:


# Write a program that prompts the user for a positive integer.
# Next write a loop that prints out the numbers from the number the user entered down to 1.


# In[90]:


while True: 
    posited_num = input('please insert positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
posited_num = int(posited_num)
for num in range(posited_num, 0, -1):
    print(num)


# In[ ]:





# In[ ]:


# Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".


# In[93]:


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# In[ ]:





# In[3]:


#4
# Display a table of powers.

while True:
    posited_num = input('please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
proceed = input('Do you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number | squared | cubed')
    print('------ | ------  | ------')
    for i in range(1, posited_num +1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f'{i: 6}) | {i_squared: 7} | {i_cubed: 5}')


# In[ ]:





# In[8]:


#Bonus

#Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

while True:
    user_number = input("Please enter a numerical between 0 and 100")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number < 0 or user_number > 100: 
            continue
        break


# In[ ]:


if 60 < grade < 67:
    print('yup')


# In[ ]:


if grade in range(60):
    grade = 'F'
elif grade in range(60,67):
    grade = 'D'
elif grade in range(67,80):
    grade = 'C'
elif grade in range(80,88):
    grade = 'B'
else:
    grade = 'A'

