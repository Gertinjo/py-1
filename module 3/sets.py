my_set = {1 , 2, 3}

my_set = set([1 ,2 ,3])

my_set = set()

my_set1 = set([1 , 1 , 2, 2, 3, 3])
print(my_set1)

my_set2 = {1 , 2 , 3}
my_set3 = {3 ,4 ,5}

union_result_method = my_set2.union(my_set3)
union_result_operator = my_set2 | my_set3

print("Union of set1 and set 2 method:", union_result_method)
print("Union of set1 and set 2 operator:", union_result_operator)

intersection_result_method = my_set2.intersection(my_set3)
intersection_result_operator = my_set2 & my_set3

print("intersection of set1 and set 2 method:", intersection_result_method)
print("intersection of set1 and set 2 operator:", intersection_result_operator)

difference_result_method = my_set2.difference(my_set3)
difference_result_operator = my_set2 - my_set3

print("difference of set1 and set 2 method:", difference_result_method)
print("difference of set1 and set 2 operator:", difference_result_operator)

symmetric_difference_result_method = my_set2.symmetric_difference(my_set3)
symmetric_difference_result_operator = my_set2 ^ my_set3

print("symmetric difference of set1 and set 2 method:", symmetric_difference_result_method)
print("symmetric difference of set1 and set 2 operator:", symmetric_difference_result_operator)






my_set4 = {1, 2 , 3}

my_set4.add(7)

my_set4.remove(3)

my_set4.discard(8)

print(my_set4)

my_set4.clear()

set_length = len(my_set4)
print(set_length)

my_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = set(my_list)

unique_list = list(unique_list)

print(unique_list)

user1_interests = {"music" , "movies", "travel"}
user2_interests = {"music" , "reading", "cooking"}
common_interests = user1_interests.intersection(user2_interests)
print(common_interests)

colors = {"red", "green", "blue"}
color= "green"
print(color in colors)
print(color not in colors)

w