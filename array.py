def sum_negatives_between_minmax_list(arr):
    min_val = min(arr)
    max_val = max(arr)

    if min_val > max_val:
      return 0

    min_index = arr.index(min_val)
    max_index = arr.index(max_val)

    start = min(min_index, max_index)
    end = max(min_index, max_index)

    sub_array = arr[start:end+1]
    sum_neg = 0
    for x in sub_array:
        if x < 0:
            sum_neg += x
    return sum_neg

arr = [10, -5, 20, -12, 5, -3, 8]
result = sum_negatives_between_minmax_list(arr)
print(f"Sum of negative numbers between min and max: {result}") # Output: -15