import re

def analyze_password_strength(password):
    """Evaluates password strength and returns a score with suggestions."""
    score = 0
    suggestions = []

    # 1. Check password length
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
        suggestions.append("Consider making your password at least 12 characters long.")
    else:
        score += 1
        suggestions.append("Your password is too short. Use 12 or more characters.")

    # 2. Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 2
    else:
        suggestions.append("Add at least one uppercase letter.")

    # 3. Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 2
    else:
        suggestions.append("Add at least one lowercase letter.")

    # 4. Check for numbers
    if re.search(r'\d', password):
        score += 2
    else:
        suggestions.append("Include numbers to increase complexity.")

    # 5. Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    else:
        suggestions.append("Include special characters like @, #, or $ for extra strength.")

    # 6. Identify predictable or common passwords
    common_patterns = ["password", "12345", "qwerty", "admin", "letmein"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score = 1
        suggestions.append("Avoid common or predictable passwords—try something unique.")

    # Determine strength category
    if score <= 3:
        strength = "WEAK"
    elif score <= 6:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    return strength, suggestions


def main():
    print("Password Strength Analyzer")
    password = input("Enter a password to test its strength: ")

    strength, suggestions = analyze_password_strength(password)

    print(f"\nYour password strength: {strength}")
    if suggestions:
        print("\nSuggestions for improvement:")
        for tip in suggestions:
            print(f"• {tip}")

    print("\nRemember: A strong password should be long, unpredictable, and unique.")

if __name__ == "__main__":
    main()