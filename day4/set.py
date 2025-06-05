# my_set = {1 ,2 ,3 ,4 , 5, 5, 5}
my_set = set()

my_set.add(5)
my_set.add(6)
my_set.add(5)

my_set.discard(9) #throw error if not found

my_list = [1 , 2 ,2 ,2, 3, 3, 1, 4 ,5]
mynew_set = set(my_list)

print(mynew_set)

# print(my_set)