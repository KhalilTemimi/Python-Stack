# 1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']='Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

# 2 Iterate Through a List of Dictionaries

def iterateDictionary (some_list):
    for i in range(len(some_list)):
        print(f"first_name : {some_list[i]['first_name']}, last-name : {some_list[i]['last_name']}")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

# 3 Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for i in range (len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2("last_name",students)

# 4 Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(len(val),key)
        for i in range (len(val)):
            print (val[i])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)