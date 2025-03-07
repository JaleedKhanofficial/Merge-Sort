# Step 12
# Within the while loop, replace pass with an if statement that checks if the index of left_part is less than the index of right_part.

# Use the pass keyword in the body of the if statement.


def merge_sort(array):
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:             # step 12
            pass                                # step 12