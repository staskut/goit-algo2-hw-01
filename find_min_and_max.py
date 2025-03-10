def find_min_and_max(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[1], arr[0]
        else:
            return arr[0], arr[1]
    elif len(arr) == 1:
        return arr[0], arr[0]
    mid = len(arr)//2
    left, right = arr[:mid], arr[mid:]
    left_res, right_res = find_min_and_max(left), find_min_and_max(right)
    min_val, max_val = merge(left_res, right_res)
    return min_val, max_val

def merge(left, right):
    if left[0] < right[0]:
        min_el = left[0]
    else:
        min_el = right[0]
    if left[1] > right[1]:
        max_el = left[1]
    else:
        max_el = right[1]
    return min_el, max_el

print(find_min_and_max([1, 2, 3, -1, -2, -3, 10]))