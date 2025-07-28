import random
import re

def generate_zoom_id():
    """Generates a random Zoom-like ID in one of two formats."""
    format_type = random.choice(['3-3-4', '3-4-4'])
    if format_type == '3-3-4':
        return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    else:
        return f"{random.randint(100, 999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

def is_valid_zoom_id(zoom_id):
    """Validates if a given string matches Zoom-like ID format."""
    pattern_9 = re.compile(r"^\d{3}-\d{3}-\d{4}$")    # e.g., 123-456-7890
    pattern_10 = re.compile(r"^\d{3}-\d{4}-\d{4}$")   # e.g., 123-4567-8901
    return bool(pattern_9.match(zoom_id) or pattern_10.match(zoom_id))

if __name__ == "__main__":
    try:
        count = int(input("How many Zoom-like IDs do you want to generate? "))
        if count <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive integer.")
    else:
        print("\nGenerated Zoom-like IDs:")
        generated_ids = [generate_zoom_id() for _ in range(count)]
        for zoom_id in generated_ids:
            print(zoom_id)

        # Optional validator
        while True:
            user_input = input("\nEnter a Zoom ID to validate (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            elif is_valid_zoom_id(user_input):
                print("✅ Valid Zoom-like ID format!")
            else:
                print("❌ Invalid format. Must be XXX-XXX-XXXX or XXX-XXXX-XXXX.")