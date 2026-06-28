from modules.website_info import website_information

from modules.password_generator import generate_password

def main():

    while True:

        print("\n" + "=" * 45)
        print("        CYBER RECON TOOLKIT")
        print("=" * 45)

        print("1. Website Information")
        print("2. Password Generator")
        print("3. Password Strength Checker")
        print("4. Hash Generator")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            website_information()

        elif choice == "2":
            generate_password()

        elif choice == "3":
            print("\n🚧 Password Strength Checker module is under development.")

        elif choice == "4":
            print("\n🚧 Hash Generator module is under development.")

        elif choice == "5":
            print("\nThank you for using Cyber Recon Toolkit!")
            break

        else:
            print("\n❌ Invalid option! Please try again.")


if __name__ == "__main__":
    main()