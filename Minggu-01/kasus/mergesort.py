def merge_sort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
 
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
