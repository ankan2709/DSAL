def merge(list1, list2):
    i = 0
    j = 0
    combined = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined

def merge_sort(my_list):

    if len(my_list) == 1:
        return my_list

    mid = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)

print(merge_sort([1,5,2,10,8]))