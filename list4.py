# list of fruits
fruits=['banana', 'orange', 'mango', 'lemon']
print(fruits)
#adding the item
fruits.append('apple')
print(fruits)
fruits.append('lemon')
print(fruits)
print(len(fruits))
print(fruits[len(fruits)-1])
print(fruits[-1])
fruits.insert(2,  'xyz')
print(fruits)

#remove
fruits.remove('xyz')
print(fruits)

#pop
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)
fruits.pop(1)
print(fruits)
#delete
del fruits[0]
print(fruits)
#clear
fruits.clear()
print(fruits)
del fruits
print(fruits)

