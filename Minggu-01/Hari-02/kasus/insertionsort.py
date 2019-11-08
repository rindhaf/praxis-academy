# Create a function that takes a list as argument #
def insertion_sort(alist): 
# Inside the function create a loop variable i that counts
# from 1 to length of the list - 1.
    for n in range(1, len(alist)):
        temp = alist[n]
        d = n - 1 # set d equal to i - 1.
        # Create a while loop that runs as long as d is non-negative
        # and temp is smaller than the element at index d.
        while (d >= 0 and temp < alist[d]):
            alist[d + 1] = alist[d] # Set the element at index d + i equal
            d = d - 1               # to the element at index d and decrement d
        alist[d + 1] = temp # Set the element at index d + i equal to temp
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)
