import timeit


def generate_fibonacci(n):
    """Generate the first n Fibonacci numbers."""

    if not isinstance(n, int):
        raise TypeError("Number of terms must be an integer.")

    if n < 0:
        raise ValueError("Number of terms cannot be negative.")

    numbers = []

    a = 0
    b = 1

    for i in range(n):
        numbers.append(a)
        a, b = b, a + b

    return numbers


def main():

    # Valid input tests
    print("Fibonacci(5):", generate_fibonacci(5))
    print("Fibonacci(0):", generate_fibonacci(0))

    # Invalid input tests
    try:
        generate_fibonacci(-5)
    except (TypeError, ValueError) as error:
        print("Negative input:", error)

    try:
        generate_fibonacci(5.5)
    except (TypeError, ValueError) as error:
        print("Decimal input:", error)

    try:
        generate_fibonacci("5")
    except (TypeError, ValueError) as error:
        print("String input:", error)

    # Runtime benchmarks
    print("\nRuntime Benchmarks:")

    for size in [10, 100, 1000]:

        execution_time = timeit.timeit(
            lambda: generate_fibonacci(size),
            number=1000
        )

        print(
            f"Fibonacci({size}) - "
            f"{execution_time:.8f} seconds for 1000 runs"
        )


if __name__ == "__main__":
    main()
