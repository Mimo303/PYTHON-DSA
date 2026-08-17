def sum(n):
    if n<10:
        return n
    return (n%10) + sum(int(n/10))

print(sum(13))