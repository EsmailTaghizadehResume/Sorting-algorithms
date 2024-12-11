def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("آرایه اصلی:", data)
    insertion_sort(data)
    print("آرایه مرتب شده:", data)

# result
آرایه اصلی: [12, 11, 13, 5, 6]
آرایه مرتب شده: [5, 6, 11, 12, 13]
