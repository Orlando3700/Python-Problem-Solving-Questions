def find_middle_elements(arr):
    result = []
    n = len(arr)

    # Check if the size of the list is even or odd
    if n % 2 == 0:
        # If even, append two middle elements to the result list
        result.append(arr[n // 2 - 1])
        result.append(arr[n // 2])
    else:
        # If odd, append the single middle element to the result list
        result.append(arr[n // 2])

    return result

if __name__ == "__main__":
    # Sample list
    arr = [1, 2, 3, 4, 5]

    # Find middle elements using the function
    middle_elements = find_middle_elements(arr)

    # Display the middle element(s)
    print("Middle Element(s):", end=" ")
    for num in middle_elements:
        print(num, end=" ")
    print()