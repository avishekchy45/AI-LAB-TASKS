dict1 = {'Name': 'Avishek', 'Age': 20}
dict2 = {'Name': 'Animesh', 'Age': 10}
print("Name: ", dict1['Name'])
print("Age: ", dict1['Age'])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1['Age'] = 21
dict1['Institution'] = "Premier University"
print("Updated Age: ", dict1['Age'])
print("Institution: ", dict1['Institution'])

print(dict1.get("Name","Key Not Found"))
dict1.update(dict2)
print("Name: ", dict1['Name'])
print("Age: ", dict1['Age'])
