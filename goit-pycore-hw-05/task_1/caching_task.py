from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    # Create an empty dictionary for caching
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        try:
            # Base cases
            if n <= 0:
                return 0
            if n == 1:
                return 1

            # Check if the value is in the cache
            if n in cache:
                return cache[n]

            # Recursive call with caching
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        except Exception as e:
            # Handle any unknown errors
            print(f"An error occurred: {e}")
            return 0  # Return 0 in case of an error for consistency

    return fibonacci
