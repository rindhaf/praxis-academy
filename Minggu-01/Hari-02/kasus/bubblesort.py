# Create a function bubble_sort that takes a list as argument.
def bubble_sort(alist):
    # Inside the function create a loop with a loop variable i 
    # that counts from the length of the list – 1 to 1.
    for i in range(len(alist) - 1, 0, -1):
        no_swap = True
    # Create an inner loop with a loop variable that counts from 0 up to i – 1.
        for j in range(0, i): 
            if alist[j + 1] < alist[j]:
    # if the elements at indexes j and j + 1 are out of order, then swap them.
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                no_swap = False
    # If in one iteration of the inner loop there were no swaps, 
    # then the list is sorted and one can return prematurely.
        if no_swap:
            return
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
bubble_sort(alist)
print('Sorted list: ', end='')
print(alist)