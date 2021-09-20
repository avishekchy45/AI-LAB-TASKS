list_dict = [
    {'Name': 'Avishek Chy', 'Age': 10},
    {'Name': 'Bill Gates', 'Age': 110},
    {'Name': 'Steve Jobs', 'Age': 210},
    {'Name': 'Mark Zuckerberg', 'Age': 310},
    {'Name': 'Sundar Pichai', 'Age': 410}
]
n = len(list_dict)

for index in range(n):
    print("List[", index, "] Name: ", list_dict[index]['Name'])
    print("List[", index, "] Age: ", list_dict[index]['Age'])

for index in range(n):
    print("List[", index, "] : ", list_dict[index].items())
