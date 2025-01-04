# Step 4
# In the previous step, you got the mid point. You can use it to divide array into two and assign each part to new variables.

# Use the slice syntax to extract the left half of array and assign it to a variable named left_part.

def merge_sort(array):
    middle_point = len(array) // 2
    left_part = array[:middle_point]                # step 4
