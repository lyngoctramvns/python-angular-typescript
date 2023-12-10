users = ['test','new','list']

emptyList = []

print('test'in users)
print('test' in emptyList)
print(users[0])

# Find out index of an element in list
print(users.index('list'))
print(users[1:])
print(len(users))
users.append('Jason')
print(users)
newList = ['more','people']
users.extend(newList)

print(users)

