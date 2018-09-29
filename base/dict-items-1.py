dict = {
    'Name': 'Runoob',
     'Age': 7
}
print("Test Case 1")
print ("Value : %s" %  dict.items())

print("Test Case 2")
dict = {'Name': 'KX01', 'Age': 17}
for k,v in dict.items():
    print(k, ":\t", v)


print("Test Case 3")
d={
    1:"a",
    2:"b",
    3:"c"
}
result=[]
for k,v in d.items():
    result.append(k)
    result.append(v)

print(result)