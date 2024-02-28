
user_list = []
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
    element = input("Enter element {}: ".format(i + 1))
    user_list.append(element)

n = len(user_list)
for i in range(n):
    swapped = False
     

    for j in range(0, n-i-1):
        if user_list[j] > user_list[j+1]:
            user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
            swapped = True
    
    
    if not swapped:
        break

print("Sorted list:", user_list)
