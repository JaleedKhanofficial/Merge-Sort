# Step 5
# Use the slice syntax to extract the right half of array and assign it to a variable named right_part.

def merge_sort(array):
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]           # step 5
