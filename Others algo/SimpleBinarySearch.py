if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]
    numbers.sort()
    n = 9
    l = 0
    r = len(numbers) - 1
    while l <= r:
        mid = (l + r) // 2
        if numbers[mid] == n:
            print(mid)
            break
        elif numbers[mid] > n:
            r = mid - 1
        elif numbers[mid] < n:
            l = mid + 1
