# Step 10
# Now it's time to sort and merge the lists (left_part and right_part) into the original array.

# You can do this by comparing elements on both lists, and merging the smaller element to the main list. You are going to do this comparison for all the indexes in left_part and right_part.

# Create three variables: left_array_index, right_array_index, and sorted_index and set their values to 0. These variables will help you keep track of each index during the sorting process.

def merge_sort(array):
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0                # step 10
    right_array_index = 0                # step 10
    sorted_index = 0                # step 10
