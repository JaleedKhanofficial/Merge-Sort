# Step 9
# Pass right_part as the argument to the merge_sort() call you added in the last step.
def merge_sort(array):
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)        # step 9