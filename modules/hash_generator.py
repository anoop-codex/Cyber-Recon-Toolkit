import hashlib


def generate_hash():

    print("\n========== HASH GENERATOR ==========\n")

    text = input("Enter text to hash: ")

    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    print("\n========== GENERATED HASHES ==========\n")

    print("MD5")
    print(md5_hash)

    print("\nSHA1")
    print(sha1_hash)

    print("\nSHA256")
    print(sha256_hash)