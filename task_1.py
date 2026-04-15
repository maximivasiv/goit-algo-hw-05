def caching_fibonacci():
    cache = {}  

    def fibonacci(n):
  
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # якщо вже є в кеші - повертаємо
        if n in cache:
            return cache[n]

        # якщо немає - обчислюємо рекурсивно
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
