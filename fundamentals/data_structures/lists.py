# lists functions

my_list = [5, 20, 2, -8, 4, 5, 5, 6, 7, 3, -8, 9, 2]
print(f"original list: {my_list}")

my_list.append(50)
print(f"\nadding new element using append() function: {my_list}")

my_list.insert(1, 55)
print(f"\nadding new element using insert() function: {my_list}")

my_list[4] = 100
print(f"\nadding new element: {my_list}")

#my_list.pop(5)
print(f"\nelement {my_list.pop(5)} removed based on index using pop() function")
print(f"\nmy_list after removing the element: {my_list}")

my_list.remove(50)
print(f"\nremove() function to remove element 50: {my_list}")

print(f"\ncount() function to count number of occurrences of a value: {my_list.count(2)}")

my_list.extend(range(2))
print(f"\nextend() function: {my_list}")

print(f"\nis element 55 in my_list? {55 in my_list}")

my_list.sort()
print(f"\nmy_list sorted in ascending order: {my_list}")

my_list.reverse()
print(f"\nmy_list sorted in reverse order: {my_list}")

new_list = my_list.copy()
print(f"\ncopied list using copy() function: {new_list}")

new_list.clear()
print(f"\nclear() function to clear the list: {new_list}")

# remove duplicates
unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
print(f"new list after removing duplicates: {unique_list}")