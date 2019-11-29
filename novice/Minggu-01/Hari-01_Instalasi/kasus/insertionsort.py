def insertion_sort(alist):
    for n in range(1, len(alist)):
        temp = alist[n]
        d = n - 1
        while (d >= 0 and temp < alist[d]):
            alist[d + 1] = alist[d]
            d = d - 1
        alist[d + 1] = temp
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)
