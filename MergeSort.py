
def mergeSort(numbers, start, end):
    if start < end:
        mid = (start + end) // 2
        print("Dividing: ", numbers[start:mid+1], numbers[mid+1:end+1])
        mergeSort(numbers, start, mid)
        mergeSort(numbers, mid + 1, end)
        merge(numbers, start, mid, end)
        print("-------------------")
    return numbers

def merge(numbers, start, mid, end):

    leftArray = numbers[start:mid + 1]
    rightArray = numbers[mid + 1:end + 1]

    print("Merging: ", leftArray, rightArray)

    i = 0
    j = 0
    k = start
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            numbers[k] = leftArray[i]
            i += 1
        else:
            numbers[k] = rightArray[j]
            j += 1
        k += 1
    if i < len(leftArray):
        while i < len(leftArray):
            numbers[k] = leftArray[i]
            i += 1
            k += 1
    if j < len(rightArray):
        while j < len(rightArray):
            numbers[k] = rightArray[j]
            j += 1
            k += 1
    print("Merged:", numbers)

numbers = [170, 45, 75, 90, 802, 24, 2, 66]
print(mergeSort(numbers, 0, len(numbers)))
