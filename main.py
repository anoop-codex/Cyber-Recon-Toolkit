from banner import show_banner
from modules.website_info import website_information
from modules.dns_lookup import dns_lookup
from modules.password_generator import generate_password
from modules.password_checker import check_password_strength
from modules.hash_generator import generate_hash
from modules.hash_verifier import verify_hash
from modules.port_scanner import port_scanner
from modules.ssl_checker import ssl_checker


def main():
    show_banner()

    while True:

        print("\n" + "=" * 70)
        print("                     MAIN MENU")
        print("=" * 70)

        print("\n🔑 PASSWORD TOOLS")
        print("  1. Password Generator")
        print("  2. Password Strength Checker")

        print("\n🌐 WEB RECON")
        print("  3. Website Information")
        print("  4. DNS Lookup")
        print("  5. SSL Certificate Checker")
        
        print("\n🔐 CRYPTOGRAPHY")
        print("  6. Hash Generator")
        print("  7. Hash Verifier")

        print("\n📡 NETWORK")
        print("  8. Port Scanner")

        print("\n❌ EXIT")
        print(" 9. Exit")

        print("=" * 70)
        choice = input("\nChoose an option: ")

        if choice == "1":
            generate_password()

        elif choice == "2":
            check_password_strength()

        elif choice == "3":
            website_information()

        elif choice == "4":
            dns_lookup()

        elif choice == "5":
            ssl_checker()

        elif choice == "6":
            generate_hash()

        elif choice == "7":
            verify_hash() 

        elif choice == "8":
            port_scanner()       

        elif choice == "9":
            print("\nThank you for using Cyber Recon Toolkit!")
            break

        else:
            print("\n❌ Invalid option! Please try again.")


if __name__ == "__main__":
    main()