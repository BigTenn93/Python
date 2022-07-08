# 1. Update Values in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ]
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # 1.
# x[1][0] = 15
# print(x)

# # 2.
# students[0]["last_name"] = "Bryant"
# print(students)


# # 3.
# sports_directory["soccer"][0] = "Andres"
# print(sports_directory)


# # 4.
# z[0]["y"] = 30
# print(z)

# 2. Iterate Through a List of Dictionaries

# iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

from curses import keyname


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(some_list):
#     for i in range(len(some_list)):
#         for key in some_list[i].keys():
#             print(key, some_list[i][key])
# iterateDictionary(students)

# 3. Get Values From a List of Dictionaries

# def iterateDictionary2(key_name, some_list):
#     for ls in some_list:
#         print(ls[key_name])
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        val_length = len(some_dict[key])
        key_name = key.upper()

        print(val_length, key_name)

        for i in range(val_length):
            print(some_dict[key][i])

printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
