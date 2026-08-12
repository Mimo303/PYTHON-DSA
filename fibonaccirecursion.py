def fibonacci_memo(n, memo={}):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n-1, memo) + (fibonacci_memo(n-2, memo))
    return memo[n]

print(fibonacci_memo(50))