
مرتب‌سازی سریع (Quick sort) یک الگوریتم مرتب‌سازی بسیار کارآمد است که از اصل تقسیم و غلبه (divide-and-conquer) پیروی می‌کند. این الگوریتم معمولاً در عمل سریع‌تر از دیگر الگوریتم‌های O(n log n) مانند مرتب‌سازی ادغامی (merge sort) و مرتب‌سازی هپی (heap sort) عمل می‌کند.

# نحوه کار

**انتخاب یک محور (Pivot)**: یک عنصر از آرایه را به عنوان محور انتخاب کنید. استراتژی‌های مختلفی برای انتخاب محور وجود دارد، مانند انتخاب اولین عنصر، آخرین عنصر، عنصر میانه یا یک عنصر تصادفی.

**بخش‌بندی (Partitioning)**: آرایه را به گونه‌ای ترتیب دهید که تمام عناصر کمتر از محور قبل از آن و تمام عناصر بزرگ‌تر از محور بعد از آن قرار گیرند. پس از این مرحله، محور در موقعیت نهایی خود قرار دارد.

**اعمال بازگشتی**: مراحل فوق را به صورت بازگشتی بر روی زیرآرایه‌های عناصر با مقادیر کوچک‌تر و بزرگ‌تر اعمال کنید.



# مراحل پیاده‌سازی مرتب‌سازی سریع

در اینجا یک پیاده‌سازی ساده از مرتب‌سازی سریع در زبان پایتون آورده شده است:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # انتخاب محور
        left = [x for x in arr if x < pivot]  # عناصر کمتر از محور
        middle = [x for x in arr if x == pivot]  # عناصر برابر با محور
        right = [x for x in arr if x > pivot]  # عناصر بزرگ‌تر از محور
        return quick_sort(left) + middle + quick_sort(right)

# مثال استفاده
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # خروجی: [1, 1, 2, 3, 6, 8, 10]
```

# مرتب‌سازی سریع در محل (In-Place Quick Sort)

پیاده‌سازی فوق در محل نیست و از فضای اضافی استفاده می‌کند. در زیر نسخه‌ای در محل آورده شده است:

```python
def quick_sort_in_place(arr, low, high):
    if low < high:
        # بخش‌بندی آرایه
        pi = partition(arr, low, high)

        # مرتب‌سازی بازگشتی عناصر قبل و بعد از بخش‌بندی
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # انتخاب آخرین عنصر به عنوان محور
    i = low - 1  # اشاره‌گر برای عنصر کوچک‌تر
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # تعویض
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # تعویض محور
    return i + 1

# مثال استفاده
arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort_in_place(arr, 0, len(arr) - 1)
print(arr)  # خروجی: [1, 1, 2, 3, 6, 8, 10]
```

# پیچیدگی زمانی

- **حالت میانگین**: O(n log n)
- **بدترین حالت**: O(n²) (هنگامی که همیشه کوچک‌ترین یا بزرگ‌ترین عنصر به عنوان محور انتخاب شود)
- **بهترین حالت**: O(n log n)

# پیچیدگی فضایی

- O(log n) برای فضای پشته بازگشتی در حالت میانگین.

# نتیجه‌گیری

مرتب‌سازی سریع یک الگوریتم مرتب‌سازی چندمنظوره و کارآمد است که به طور گسترده‌ای در عمل استفاده می‌شود. عملکرد آن می‌تواند با به کارگیری بهینه‌سازی‌های مختلف مانند انتخاب یک محور بهتر، استفاده از رویکرد ترکیبی با مرتب‌سازی درج (insertion sort) برای زیرآرایه‌های کوچک، یا پیاده‌سازی بازگشت دمی (tail recursion) بهبود یابد.
