def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    # Base case: If the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choosing the pivot (we can choose the last element as the pivot)
    pivot = arr[-1]
    less_than_pivot = []
    greater_than_pivot = []

    # Partitioning the array into two lists
    for element in arr[:-1]:  # Exclude the pivot itself
        if element <= pivot:
            less_than_pivot.append(element)
        else:
            greater_than_pivot.append(element)

    # Recursively applying quick_sort and concatenating results
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
if __name__ == "__main__":
    array_to_sort = [10, 7, 8, 9, 1, 5]
    sorted_array = quick_sort(array_to_sort)
    print("Unsorted Array:", array_to_sort)
    print("Sorted Array:", sorted_array)
