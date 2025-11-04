import bisect

def lis_length(arr):
    lis = []

    for num in arr:
        pos = bisect.bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num

        print(num, "=>", lis)

    print("Długość LIS:", len(lis))
    return len(lis)


arr = [10, 9, 2, 5, 3, 7, 101, 18]
lis_length(arr)
