# Create a function merge_sort that takes a list and 
# two variables start and end as arguments.
def merge_sort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1: # If end – start is not greater than 1, then return.
        mid = (start + end)//2 # set mid equal to the floor of (start + end)/2.
        merge_sort(alist, start, mid) # Call merge_sort with the same list and with start = start and end = mid as arguments.
        merge_sort(alist, mid, end) # Call merge_sort with the same list and with start = mid and end = end as arguments.
        merge_list(alist, start, mid, end) # Call the function merge_list, passing the list and the variables start, mid and end as arguments.

# The function merge_list takes a list and three numbers, start, mid and end as arguments and
# assuming the list is sorted from indexes start to mid – 1 and from mid to end – 1, 
# merges them to create a new sorted list from indexes start to end – 1.
def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    r = start
    i = 0
    n = 0
    while (start + i < mid and mid + n < end):
        if (left[i] <= right[n]):
            alist[r] = left[i]
            i = i + 1
        else:
            alist[r] = right[n]
            n = n + 1
        r = r + 1
    if start + i < mid:
        while r < end:
            alist[r] = left[i]
            i = i + 1
            r = r + 1
    else:
        while r < end:
            alist[r] = right[n]
            r = r + 1
            n = n + 1
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
merge_sort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)
