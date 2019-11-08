# Create a function quicksort that takes a list and 
# two variables start and end as arguments.
def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1: # If end – start is not greater than 1, return.
        # Find the index of the pivot, p by calling the function partition 
        # with the list and variables start and end as arguments.
        p = partition(alist, start, end)
        quicksort(alist, start, p) # Call quicksort with the list and the variables start and p as arguments to sort the list from start to p – 1.
        quicksort(alist, p + 1, end) # Call quicksort with the list, the expression p + 1 and end as arguments to sort the list from p + 1 to end – 1.
# Define the function partition that takes a list and 
# two variables start and end as arguments.
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1
 
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)