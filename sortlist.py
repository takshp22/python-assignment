# Define a list to be sorted
user_list = []
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
    element = input("Enter element {}: ".format(i + 1))
    user_list.append(element)
# Perform bubble sort algorithm
n = len(user_list)
for i in range(n):
    # Flag to check if any swapping occurs in this iteration
    swapped = False
     

    for j in range(0, n-i-1):
        # Swap if the element found is greater than the next element
        if user_list[j] > user_list[j+1]:
            user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
            swapped = True
    
    # If no two elements were swapped in the inner loop, the list is sorted
    if not swapped:
        break

# Display the sorted list
print("Sorted list:", user_list)
