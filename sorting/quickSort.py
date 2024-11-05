def swap(mylist, index1, index2):
    mylist[index1], mylist[index2] = mylist[index2], mylist[index1]

def pivot(mylist, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist, swap_index, i)
    swap(mylist, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1 , right)

    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

print(quick_sort([4,6,1,7,3,2,5]))