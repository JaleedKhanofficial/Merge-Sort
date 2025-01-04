# Step 11
# Inside your function, create a while loop that compares an element in left_part to an element in right_part, and merges the smaller element to the main array list.

# Create two conditions for the loop: one that checks whether the left_array_index is less than the length of left_part and another condition that checks whether right_array_index is less than the length of right_part.


def merge_sort(array):
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):            # step 11
        pass                # step 11