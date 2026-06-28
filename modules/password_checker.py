import re


def check_password_strength():

    print("\n========== PASSWORD STRENGTH CHECKER ==========\n")

    password = input("Enter your password: ")

    score = 0

    if len(password) >= 8:
        print("✅ Length: Good")
        score += 1
    else:
        print("❌ Length: Too Short")

    if re.search(r"[A-Z]", password):
        print("✅ Uppercase Letter")
        score += 1
    else:
        print("❌ No Uppercase Letter")

    if re.search(r"[a-z]", password):
        print("✅ Lowercase Letter")
        score += 1
    else:
        print("❌ No Lowercase Letter")

    if re.search(r"\d", password):
        print("✅ Number Found")
        score += 1
    else:
        print("❌ No Number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("✅ Special Character")
        score += 1
    else:
        print("❌ No Special Character")

    print("\n==============================")

    if score == 5:
        print("🟢 Password Strength : STRONG")

    elif score >= 3:
        print("🟡 Password Strength : MEDIUM")

    else:
        print("🔴 Password Strength : WEAK")