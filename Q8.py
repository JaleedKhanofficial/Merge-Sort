# Step 8 
# Call the merge_sort() function again. Do not pass in any argument for now.

def merge_sort(array):
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    
    merge_sort(left_part)
    merge_sort()            # step 8