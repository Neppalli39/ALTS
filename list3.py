#built in function or constructor
empty_list = list()
print(len(empty_list))


#using square bracket
empty_list = []
print(len(empty_list))

fruits=['banana', 'orange', 'mango', 'lemon']                     # list of fruits
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)


first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
all_fruits = fruits[0:4]
print(all_fruits)
print(fruits[0:3])

fruits = ['banana','orange','mango','lemon']
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]
