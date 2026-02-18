list = [1,2,3,4,5]
print("First element:", list[0])
print("last element:", list[-1])
print("Length of list:", len(list))

num = [1,2,3,4,56]
average = sum(num) / len(num)
print("Average:", average)

list = [ "apple", "orange", "banana", "mango"]
appended_list = list.append("grape")
inserted_list = list.insert(2, "grapes")
print(list)

list = [1,2,3,4,5]
remove_element = list.remove(3)
pop_element = list.pop(1)
print(list)

list = [1,2,3,4,5,5,4,2]
count_5 = list.count(5)
print("Count of 5:", count_5)

list = [ 3, 4, 53, 27, 657, 23, 1]
x = (53)
if x in list:
    print("Element found in list")
else:
    print("Element not found in list")

list = [1,2,3,4,5]
index = list.index(3)
print("Index of 3:", index)

list = [1,2,84,67,98,4,5]
list.sort()
print("sorted list:", list)
assendind_list = sorted(list)
desending_list = sorted(list, reverse=True)

list = [1,2,3,4,5,3,8,9]
list.reverse()
print("reversed list:", list)

tuple = (1,2,3,4,5)
print("first element:", tuple[0])
print("last element:", tuple[-1])

tuple = (1,2,3,4,5)
print("length of tuple:", len(tuple))

tuple = ("mango","apple" , "banana", "grape")
for fruits in tuple:
    print(fruits)

tuple = (2,3,4,5,2,8)
count_2 = tuple.count(2)
print("count of 2:", count_2)

tuple1 = (1,2,3,4,5)
tuple2 = (3,4,3,5,4)
tuple3 = tuple1 + tuple2
print("concatenated tuple:", tuple3)

tuple = (1,3,2,43,3,4,3,43,1)
count_3 = tuple.count(3)
print("countof 3:", count_3)

