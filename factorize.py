import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_list(numbers):
    result = []
    for number in numbers:
        result.append(factorize(number))
    return result

if __name__ == "__main__":
    numbers = [128, 256, 512, 1024, 2048]

    # Вимірюємо час виконання синхронної версії
    start_time = time.time()
    result_sync = factorize_list(numbers)
    end_time = time.time()
    print("Synchronous execution time:", end_time - start_time)
    print("Result (synchronous):", result_sync)