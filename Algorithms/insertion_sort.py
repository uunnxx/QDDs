def insertion_sort(lst: list) -> list:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            lst[j + 1] = key

    return lst


lst = [7, 4, 9, 2, 6, 3]
print(insertion_sort(lst))
