import re

def evaluate_password_strength(password):
    length_score = len(password) >= 8
    upper_score = bool(re.search(r'[A-Z]', password))
    lower_score = bool(re.search(r'[a-z]', password))
    digit_score = bool(re.search(r'\d', password))
    special_score = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Count the number of conditions met
    score = sum([length_score, upper_score, lower_score, digit_score, special_score])

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = evaluate_password_strength(password)
    print(f"Password Strength: {strength}")
