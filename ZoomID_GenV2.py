import random

def generate_zoom_id():
    # Choose randomly between 9 or 10 digit formats
    format_type = random.choice(['3-3-4', '3-4-4'])

    if format_type == '3-3-4':
        return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    else:
        return f"{random.randint(100, 999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

if __name__ == "__main__":
    try:
        count = int(input("How many Zoom-like IDs do you want to generate? "))
        if count <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive integer.")
    else:
        for _ in range(count):
            print(generate_zoom_id())
