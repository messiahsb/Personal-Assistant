import random

def generate_random_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

if __name__ == "__main__":
    numbers = generate_random_numbers(5)
    print(f"Generated random numbers: {numbers}")
