#base case - know when to stop
#nove toward the base case
#function calls itself
#use for readability - less code
#but uses a lot of resources

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    elements = len(arrA) + len(arrB)
    #array that is as long as it needs to be
    #holds all of our elements as they are sorted
    merged_arr = [0] * elements

    # Your code here
    arrA_pointer = 0
    arrB_pointer = 0
    #compare values and add smallest to merged_arr at i
    for i in range(0, elements):
        if arrA_pointer >= len(arrA):
            merged_arr[i] = arrB[arrB_pointer]
            arrB_pointer += 1
        elif arrB_pointer >= len(arrB):
            merged_arr[i] = arrA[arrA_pointer]
            arrA_pointer += 1
        elif arrA[arrA_pointer] < arrB[arrB_pointer]:
            merged_arr[i] = arrA[arrA_pointer]
            arrA_pointer += 1
        elif arrA[arrA_pointer] > arrB[arrB_pointer]:
            merged_arr[i] = arrB[arrB_pointer]
            arrB_pointer += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #base case
    #if length of the array is less than or equal to 1.. we are done.. ready to return and combine
    if len(arr) > 1:
        #recursively keep dividing until we get down to 1.. then return

        #splitting the array to the mid-point (//2 = divide by two and round down for mid-point)
        #up to but not including midpoint
        arrA = merge_sort(arr[:(len(arr) // 2)])
        #from midpoint to the end
        arrB = merge_sort(arr[(len(arr) // 2):])
        #combining
        return merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

