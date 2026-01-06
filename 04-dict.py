# Creating a Dictionary

empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


person = {
    'first_name':'Ahmnadreza',
    'last_name':'Sezavar',
    'age':180,
    'country':'Iran',
    'is_marred':False,
    'skills':['C++', 'R', 'Matlab', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(len(person)) 


print(person['first_name']) 
print(person['country'])     
print(person['skills'])     
print(person['skills'][0])   
print(person['address']['street'])  
print(person['city']) 

# Adding Items to a Dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)