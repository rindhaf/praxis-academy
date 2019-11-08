# Python program for implementation of Selection 
# Create a function selection_sort that takes a list as argument.
def selection_sort(alist):
# Inside the function create a loop with a loop variable i 
# that counts from 0 to the length of the list – 1.
    for i in range(0, len(alist) - 1):
        smallest = i # Create a variable smallest with initial value i.
        # Create an inner loop with a loop variable j that counts from i + 1 
        # up to the length of the list – 1.
        for j in range(i + 1, len(alist)):
            # if the elements at index j is smaller than the element at index smallest, 
            # then set smallest equal to j.
            if alist[j] < alist[smallest]:
                smallest = j
        # swap the elements at indexes i and smallest.
        alist[i], alist[smallest] = alist[smallest], alist[i]
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)
