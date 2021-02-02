array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def merge(lst1, lst2):
    n1, n2 = len(lst1), len(lst2)
    i = j = 0
    lst = []
    while i < n1 and j < n2:
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1

    while i < n1:
        lst.append(lst1[i])
        i += 1
    
    while j < n2:
        lst.append(lst2[j])
        j += 1

    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

print(merge_sort(array))