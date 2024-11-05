# def bubbleSort(arr):
#     for i in range(len(arr)-1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

# print(bubbleSort([2,0,2,1,1,0]))

# def selectionSort(arr):
#     for i in range(len(arr)-1):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         if i != min_index:
#             arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# print(selectionSort([2,0,2,1,1,0]))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j > -1:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

print(insertion_sort([2,0,2,1,1,0]))