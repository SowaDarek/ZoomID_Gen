import random

def generate_random_number():
    # Choose a format randomly
    format_type = random.choice(['3-3-4', '3-4-4'])

    if format_type == '3-3-4':
        part1 = random.randint(100, 999)
        part2 = random.randint(100, 999)
        part3 = random.randint(1000, 9999)
        return f"{part1}-{part2}-{part3}"
    
    else:  # '3-4-4'
        part1 = random.randint(100, 999)
        part2 = random.randint(1000, 9999)
        part3 = random.randint(1000, 9999)
        return f"{part1}-{part2}-{part3}"

# Example: generate and print 10 random numbers
if __name__ == "__main__":
    for _ in range(10):
        print(generate_random_number())
