# type of variables

first_name = "Mario"
age = 25
salary = 1350.50
is_married = False
skills = ["codec", "deep learning", "C++"]
person_info ={
    "student" : True,
    "city": "Lisbon",
}


# iterate over list and dict
print("List info: \n")
for s in skills:
    print(s)

print("\ndict info: \n")
for k,v in person_info.items():
    print(k,v)