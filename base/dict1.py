dict1 = {
    'Name' : 'KX01',
    'Age'  : 100,
    'Email': ('kx@gmail.com', 'kx@qq.com'),
    'Phone': [111111,22222,3333,4444]
}

print ("dict1['Name']: ", dict1['Name'])
print ("dict1['Age']: ", dict1['Age'])
print ("dict1['Email']: ", dict1['Email'])
print ("dict1['Phone']: ", dict1['Phone'])

dict1['Age'] = 28

print(dict1)
