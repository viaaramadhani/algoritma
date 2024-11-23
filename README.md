# Quiz 1 PAA (Sorting)
Nama : Octavia Ramadhani, NIM : F55123015

## (Pseudocode Bubble Sort:)
```
BubbleSort(arr)
    n = length(arr)
    for i from 0 to n-1
        for j from 0 to n-i-2
            if arr[j] > arr[j+1]
                swap(arr[j], arr[j+1])

```
## Analisa Time Complexity Bubble Sort:
1. Big-O (Worst Case): O(n²)
   (Karena dalam skenario terburuk, semua elemen perlu dibandingkan dan di swap dalam dua loop bersarang.)
2. Big-Theta (Average Case): Θ(n²)
   (Kompleksitas rata-rata tetap berada di O(n²), karena pengurutan tetap membutuhkan dua loop bersarang.)

## (Pseudcode Merge Sort)
```
MergeSort(arr)
    if length(arr) > 1
        mid = length(arr) / 2
        left = arr[0:mid]
        right = arr[mid:length(arr)]

        MergeSort(left)
        MergeSort(right)

        i, j, k = 0, 0, 0
        while i < length(left) and j < length(right)
            if left[i] < right[j]
                arr[k] = left[i]
                i += 1
            else
                arr[k] = right[j]
                j += 1
            k += 1

        while i < length(left)
            arr[k] = left[i]
            i += 1
            k += 1

        while j < length(right)
            arr[k] = right[j]
            j += 1
            k += 1
```
## Analisa Time Complexity Merge Sort:
1. Big-O (Worst Case): O(n log n)
   (Karena data dipecah menjadi setengah dan setiap pecahan diurutkan dalam O(n).)
2. Big-Theta (Average Case): Θ(n log n)
   (Rata-rata tetap sama dengan kompleksitas logaritmik.)