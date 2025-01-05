def merge_sort(arr):
    # Base case: if the list is of length 0 or 1, it is already sorted
    if len(arr) <= 1:
        return arr

    # Finding the middle of the array
    mid = len(arr) // 2

    # Recursively split and sort both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two lists while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are remaining elements in left or right, extend the sorted_array
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Example usage
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(array)
    print("Sorted array:", sorted_array)
