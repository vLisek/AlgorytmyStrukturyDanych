def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        print(i, "   ", arr[i], "   ", current_sum, "   ", max_sum, "   ", arr[temp_start:i+1])

    print("Maksymalna suma:", max_sum)
    print("Podciąg:", arr[start:end+1])


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray(arr)