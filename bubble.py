def bubble_sort(arr):
    n = len(arr)
    # مرحله‌ای که تعداد عناصر آرایه را کم می‌کنیم
    for i in range(n):
        # مرحله‌ای که عناصر را به صورت جفت‌های مجاور مقایسه می‌کنیم
        for j in range(n-i-1):
            # مرحله‌ای که جفت‌های مجاور را مقایسه کرده و در صورت نیاز جاهایشان را عوض می‌کنیم
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)