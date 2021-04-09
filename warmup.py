#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# # Start of exercise 1:
# # Write the code that operates on a single string containing the make and model of a vehicle. 
# The first part of the string before the space is the make The last part of the string after the space is the model 
# We can assume that the strings will only have one space. Assume the input string is completely lower-cased.

# # Example inputs:

# # truck = "toyota tacoma"
# # sedan = "hyundai sonata"
# # sports_car = "lambourgini diablo"


# In[2]:


truck = "toyota tacoma"
sedan = "hyundai sonata"
sports_car = "lambourgini diablo"


# In[35]:


make_and_model = truck.split()
print(make_and_model)


# In[9]:


print(dict(make = truck.split()[0]))
print(dict(make = truck.split()[1]))


# In[13]:


make = make_and_model[0]
model = make_and_model[1]

print(make)
print(model)


# In[16]:



truck = {
    'make': make,
    'model': model
}
print(truck)

#end of exercise 1


# In[ ]:





# In[ ]:


#exercise 2:
# Write the code that takes a dictionary containing make/model for a vehicle 
# and capitalizes the first character of the make and the model:
#dictionary access syntax: 


# In[37]:


#example: 
"stuff".capitalize()

truck["make"] = truck['make'].capitalize()
truck["model"] = truck['model'].capitalize()

print(truck)


# In[ ]:





# In[ ]:


#exercise 3: 
# Create a list of 3 dictionaries where each dictionary represents a vehicle, 
# as above Write the code that operates on that list of dictionaries 
# in order to uppercase the entire make and model values.


# In[40]:


#if we are looking at a list of things - we will use a loop 
#Blow off the loop 
#How do we blow off the loop? 
# -> For now, only create a solution that works on a single item from the list 
# -> Keep it simple



# In[ ]:





# In[49]:


def dict(car1, car2, car3):
    return car1.title, car2.title, car3.title

# Step 1. make a variable that holds only the first item from our list
trucks = [
        { 
            "make": "Toyota",
            "model": "Tacoma"    
        },
        {
            "make": "Mazda",
            "model": "Rx7"
        },
        {
            "make": "Honda",
            "model": "CRV"
        }
            ]
 
# Step 2: Do whatever we need to do to this ONE item from the list
truck["make"] = truck["make"].upper()
truck["model"] = truck["model"].upper()
    
    
#step 3 we can ginally bring in the loop
#write a for loop that creates a "truck" varaianle
#then the guts of the loop are copy/pasted from teh solution we made to solve for the first truck
for truck in trucks: 
    truck["make"] = truck["make"].upper()
    truck["model"] = truck["model"].upper()
    
print(trucks)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




