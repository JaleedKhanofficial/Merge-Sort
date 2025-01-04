# Step 3
# The merge sort algorithm mainly performs three actions:

# Divide an unsorted sequence of items into sub-parts
# Sort the items in the sub-parts
# Merge the sorted sub-parts
# The above happens recursively until the sub-parts are merged into the complete sorted sequence. Let's start by dividing the sequence.

# First, replace the pass keyword with a variable middle_point. Use the integer division operator (//) to divide the length of the array list by 2 and assign the result to your new middle_point variable. Remember to indent your code.


def merge_sort(array):
    middle_point = len(array) // 2              # step 3