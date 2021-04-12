#!/usr/bin/env python
# coding: utf-8

# In[1]:


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# In[ ]:


# 1
# How many students are there?

print('The number of students are: ')
len(students)


# In[ ]:


# 2
# How many students prefer light coffee? For each type of coffee roast?

light = 0

for student in students:
    if student['coffee_preference'] == 'light':
        light += 1
print(light)


# In[ ]:


#2 
# For each type of coffee roast?

light_count = 0
medium_count = 0
dark_count = 0

for student in students:
    if student['coffee_preference'] == 'light':
        light_count += 1
    elif student['coffee_preference'] == 'medium':
        medium_count += 1
    elif student ['coffee_preference'] == 'dark':
        dark_count += 1
print(f'light = {light_count}')
print(f'medium = {medium_count}')
print(f'dark = {dark_count}')


# In[ ]:


# 3
# How many types of each pet are there?

horses = []
cats = []
dogs = []

for student in students:
    pets = student['pets']
    for species in pets:
        pet_species = species['species']
        if pet_species == 'horse':
            horses.append(pet_species)
        elif pet_species == 'cat':
            cats.append(pet_species)
        elif pet_species == 'dog':
            dogs.append(pet_species)
print(f'horses = {len(horses)}')
print(f'cats = {len(cats)}')
print(f'dogs = {len(dogs)}')


# In[ ]:


# 4. How many grades does each student have? Do they all have the same number of grades?

for student in students:
    grades = student['grades']
    for grade in grades:
        


# In[ ]:


for student in students:
    print(student['student'], 'has ', len(student['grades']), 'grades.')
print('\nAll students have', len(student['grades']), 'grades.')


# In[ ]:


# 5. What is each student's grade average?


# In[ ]:


for student in students:
    print(student['student'],"'s grade average is", sum(student['grades']) / len(student['grades']))


# In[ ]:


# 6. How many pets does each student have?


# In[ ]:


## ??? - getting an error noting "string indices must be integers"
for students in students:
    print(student['student'], "has the following number of pets", len(student['pets']))


# In[ ]:


# 7. How many students are in web development? data science?


# In[ ]:


web = 0
data = 0

for student in students:
    if student['course'] == 'web development':
        web += 1
    elif student['course'] == 'data science':
        data += 1
print(f'web development has {web} students')
print(f'data science has {data} students')


# In[ ]:





# In[ ]:


# 8. What is the average number of pets for students in web development?


# In[ ]:


web = 0
pets = 0

for student in students:
    if student['course'] == 'web development':
        web += 1
        pets += len(student['pets'])
print('Web development students have an average of ', (pets/web), ' pets')


# In[ ]:





# In[ ]:


# 9. What is the average pet age for students in data science?


# In[ ]:


total_age = 0
number_pets = 0

for student in students:
    if student['course'] == 'data science':
        pets = student['pets']
        for pet in pets:
            total_age += pet['age']
            number_pets += 1
average_age = (total_age / number_pets)
print(f'The average pet age for students in Data Science is {average_age}.')


# In[ ]:





# In[ ]:


# 10 
# What is most frequent coffee preference for data science students?

coffee_list = []

for student in students:
    if student['course'] == 'data science':
        coffee_preference = student['coffee_preference']
        coffee_list.append(coffee_preference)
blends = dict()
for drink in coffee_list:
    blends[drink] = coffee_list.count(drink)
blends_pref = max(blends, key = blends.get)
print(f'the most frequent coffee preference for data science students is {blends_pref}.')


# In[ ]:





# In[ ]:


# 11
# What is the least frequent coffee preference for web development students?

coffee_list = []

for student in students:
    if student['course'] == 'web development':
        coffee_preference = student['coffee_preference']
        coffee_list.append(coffee_preference)
blends = dict()
for drink in coffee_list:
    blends[drink] = coffee_list.count(drink)
blends_pref = min(blends, key = blends.get)
print(f'the least frequent coffee preference for data science students is {blends_pref}.')
    


# In[ ]:





# In[ ]:


# 12. 
# What is the average grade for students with at least 2 pets?

grades_total = 0
number_grades = 0

for student in students:
    if len(student['pets']) > 1:
        grades_total += sum(student['grades'])
        number_grades += len(student['grades'])
print(f'The average grade for students with at least 2 pets is: ', (grades_total / number_grades))


# In[ ]:





# In[ ]:


#13. 
# How many students have 3 pets?

pets_3 = 0

for student in students: 
    if len(student['pets']) == 3:
        pets_3 += 1
print(f'{pets_3} is how many student(s) have 3 pets')


# In[ ]:





# In[ ]:


for student in students:
    print(student['student'],"'s grade average is", sum(student['grades']) / len(student['grades']))


# In[ ]:


# 14. What is the average grade for students with 0 pets?

grade_total = 0
number_grades = 0

for student in students: 
    if len(student['pets']) == 0:
        grade_total += sum(student['grades']) 
        number_grades += len(student['grades'])

print(f'The average grade for students with 0 pets is:', (grade_total / number_grades))


# In[ ]:





# In[ ]:


# 15. What is the average grade for web development students? data science students?


# In[ ]:


#15 A - Web Development Students Average Grades

grade_total = 0
number_grades = 0

for student in students: 
    if student['course'] == "web development":
        grade_total += sum(student['grades']) 
        number_grades += len(student['grades'])

print(f'The average grade for Web Development students is:', (grade_total / number_grades))


# In[ ]:


#15 B - Data Science Students Average Grades

grade_total = 0
number_grades = 0

for student in students: 
    if student['course'] == "data science":
        grade_total += sum(student['grades']) 
        number_grades += len(student['grades'])

print(f'The average grade for Data Science students is:', (grade_total / number_grades))


# In[ ]:





# In[ ]:


# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark 
# coffee drinkers?

average_grades = []

for student in students: 
    if student['coffee_preference'] == "dark":
        average_grades.append(sum(student['grades']) / len(student['grades']))

print('The highest average grade for dark coffee drinker students is:', max(average_grades))
print('The lowest average grade for dark coffee drinker students is:', min(average_grades))                              


# In[ ]:





# In[ ]:


# 17. What is the average number of pets for medium coffee drinkers?

medium_drinkers = 0 
number_pets = 0

for student in students: 
    if student['coffee_preference'] == "medium":
        medium_drinkers += 1
    if student['coffee_preference'] == "medium":
        pets = student['pets']
        for pet in pets:
            number_pets +=1

print('The average number of pets for medium coffee drinkers is:', (medium_drinkers / number_pets))


# In[ ]:





# In[3]:


# 18. What is the most common type of pet for web development students?

pet_list = []
for student in students:
    if student ['course'] == 'web development':
        pets = student['pets']
        for species in pets:
            pet_species = species['species']
            pet_list.append(pet_species)
pets = dict()
for animal in pet_list:
    pets[animal] = pet_list.count(animal)
pet_pref = max(pets, key = pets.get)
print(f'The most common type of pet for web development stuents is {pet_pref}.')


# In[ ]:





# In[4]:


# 19. What is the average name length?

sum_length = 0
num_students = 0
for student in students:
    num_students += 1
    sum_length += len(student['student'].replace(' ', ''))
print('The average name length is:', (sum_length / num_students))


# In[ ]:





# In[6]:


# # 20. What is the highest pet age for light coffee drinkers?

pet_list = []
for student in students:
    if student ['coffee_preference'] == 'light':
        pets = student['pets']
        for age in pets:
            pet_age = age['age']
            pet_list.append(pet_age)
pets = dict()
for animal in pet_list:
    pets[animal] = pet_list.count(animal)
pet_pref = max(pets, key = pets.get)
print(f'The highest pet age for light coffee drinkers is {pet_pref}.')


# In[ ]:




