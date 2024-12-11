def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(f"مرحله {i+1}: {arr}")
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
print("آرایه اولیه:", arr)
bubble_sort(arr)
print("آرایه مرتب شده:", arr)


# result
آرایه اولیه: [64, 34, 25, 12, 22, 11, 90]
مرحله 1: [34, 25, 12, 22, 11, 64, 90]
مرحله 2: [25, 12, 22, 11, 34, 64, 90]
مرحله 3: [12, 22, 11, 25, 34, 64, 90]
مرحله 4: [12, 11, 22, 25, 34, 64, 90]
مرحله 5: [11, 12, 22, 25, 34, 64, 90]
آرایه مرتب شده: [11, 12, 22, 25, 34, 64, 90]
