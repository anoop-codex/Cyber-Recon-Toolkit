import socket


def dns_lookup():

    print("\n========== DNS LOOKUP ==========\n")

    domain = input("Enter domain (example: google.com): ").strip()

    try:

        ip_address = socket.gethostbyname(domain)

        hostname = socket.getfqdn(domain)

        print("\n========== RESULT ==========\n")
        print(f"Domain      : {domain}")
        print(f"IP Address  : {ip_address}")
        print(f"Hostname    : {hostname}")
        print("\n✅ Lookup Successful!")

    except socket.gaierror:

        print("\n❌ Unable to resolve domain.")