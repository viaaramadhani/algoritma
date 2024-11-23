import random
import time

arr_bubble = [random.randint(1, 1000) for _ in range(100)]
arr_merge = [random.randint(1, 1000) for _ in range(100)]

# Bubble Sort
def bubble_sort(arr_bubble):
    n = len(arr_bubble)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr_bubble[j] > arr_bubble[j+1]:
                arr_bubble[j], arr_bubble[j+1] = arr_bubble[j+1], arr_bubble[j]

#pseudcode Bubble Sort
# BubbleSort(arr)
#     n = length(arr)
#     for i from 0 to n-1
#         for j from 0 to n-i-2
#             if arr[j] > arr[j+1]
#                 swap(arr[j], arr[j+1])


# Merge Sort 
def merge_sort(arr_merge):
    if len(arr_merge) > 1:
        mid = len(arr_merge) // 2
        left = arr_merge[:mid]
        right = arr_merge[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr_merge[k] = left[i]
                i += 1
            else:
                arr_merge[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr_merge[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr_merge[k] = right[j]
            j += 1
            k += 1

#pseudocode Merge Sort
# MergeSort(arr)
#     if length(arr) > 1
#         mid = length(arr) / 2
#         left = arr[0:mid]
#         right = arr[mid:length(arr)]

#         MergeSort(left)
#         MergeSort(right)

#         i, j, k = 0, 0, 0
#         while i < length(left) and j < length(right)
#             if left[i] < right[j]
#                 arr[k] = left[i]
#                 i += 1
#             else
#                 arr[k] = right[j]
#                 j += 1
#             k += 1

#         while i < length(left)
#             arr[k] = left[i]
#             i += 1
#             k += 1

#         while j < length(right)
#             arr[k] = right[j]
#             j += 1
#             k += 1



#time complexity untuk bubble
start_time_bubble_sort = time.perf_counter()
bubble_sort(arr_bubble)
end_time_bubble_sort = time.perf_counter()
time_complexity_bubble = end_time_bubble_sort - start_time_bubble_sort

#time complexity untuk merge
start_time_merge_sort = time.perf_counter()
merge_sort(arr_merge)
end_time_merge_sort = time.perf_counter()
time_complexity_merge = end_time_merge_sort - start_time_merge_sort



print(f"Hasil perhitungan dari bubble sort adalah sebagai berikut: {arr_bubble}\n")
print(f"Hasil perhitungan dari merge sort adalah sebagai berikut: {arr_merge}\n")

print(f"Time Complexity untuk Bubble Sort {time_complexity_bubble:.10f} detik \n")
print(f"Time Complexity untuk Merge Sort  {time_complexity_merge:.10f} detik \n")