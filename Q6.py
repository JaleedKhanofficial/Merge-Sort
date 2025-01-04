# Step 6
# Now that you've divided the array list into two separate lists, you'll keep dividing each list until every element stands alone in its own list. A list with a single number is always sorted.

# To do that, recursively call merge_sort inside your function.
def merge_sort(array):
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort()            # step 6