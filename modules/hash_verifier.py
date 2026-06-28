import hashlib


def verify_hash():

    print("\n========== HASH VERIFIER ==========\n")

    text = input("Enter original text: ")
    user_hash = input("Enter MD5 hash: ")

    generated_hash = hashlib.md5(text.encode()).hexdigest()

    print("\nGenerated MD5:")
    print(generated_hash)

    if generated_hash == user_hash:
        print("\n✅ Hash Match!")
    else:
        print("\n❌ Hash Does Not Match!")