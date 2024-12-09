def sum_negatives_between_minmax_list(arr):
    min_val = min(arr) #найдено наименьшее значение в списке
    max_val = max(arr) #найдено наибольшее значение в списке

    if min_val > max_val:
      return 0 #проверяет, больше ли минимальное значение, чем максимальное

    min_index = arr.index(min_val) #находит первый индекс минимального значения
    max_index = arr.index(max_val) #находит первый индекс максимального значения

    start = min(min_index, max_index) #позволяет найти меньшее
    end = max(min_index, max_index) #позволяет найти большее

    sub_array = arr[start:end+1] #создаёт подмассив, содержащий элементы между индексами start и end
    sum_neg = 0 #инициализирует переменную для хранения суммы отрицательных чисел
    for x in sub_array: #код повторяется через sub_array
        if x < 0:
            sum_neg += x #если элемент отрицательный, он добавляется в sum_neg
    return sum_neg

arr = [10, -5, 20, -12, 5, -3, 8]
result = sum_negatives_between_minmax_list(arr)
print(f"Sum of negative numbers between min and max: {result}") # выход -15
