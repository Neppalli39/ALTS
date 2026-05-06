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
fruitscopy=fruits.copy()
print(fruits)
fruitscopy.append('orange')
print(fruitscopy)
print("count value:",fruitscopy.count('orange'))
fruits1=['a','b','c',]
joinfruit1=fruitscopy + fruits1
print("Join two list:",joinfruit1)
fruits2=['d','e','f',]
print("fruits2:",fruits2)
fruits2.extend(fruits1)
print("Fruits2 extend:",fruits2)
print(fruits2.index('f'))
fruits2.reverse()
print(fruits2)
fruits2.sort()
print(fruits2)
fruits2.sort(reverse=True)
print(fruits2)
numlist=[100,269,32,269,1000,21]
print("Maximum value:",max(numlist))
print("Minimum value:",min(numlist))
print("sum value:",sum(numlist))
print("Length value:",len(numlist))
print("Average value:",sum(numlist)/len(numlist))
print("Numlis value using iterator:")
for i in numlist:
    print(i,end=' ')
print('\n')
print("current fruit list",fruitscopy)
myfruits=', '.join(fruitscopy)
print(myfruits)
del fruits
print(fruits1)



      

