def nombrePremier(n):
    if n == 2 or n == 3:
        return True
    if n/2 == n//2:
        return False
    elif n/3 == n//3:
        return False
    elif (n-1)/6 == (n-1)//6:
        return True
    elif (n+1)/6 == (n+1)//6:
        return True
    else:
        return False


if __name__ == "__main__":
    n = 829
    print(nombrePremier(n))