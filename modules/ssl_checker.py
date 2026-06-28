import ssl
import socket


def ssl_checker():

    print("\n========== SSL CERTIFICATE CHECKER ==========\n")

    website = input("Enter website (example: google.com): ").strip()

    try:

        context = ssl.create_default_context()

        with socket.create_connection((website, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=website) as secure_socket:

                certificate = secure_socket.getpeercert()

                print("\n========== CERTIFICATE ==========\n")

                print(f"Website     : {website}")
                print(f"Issued To   : {certificate['subject'][0][0][1]}")
                print(f"Issued By   : {certificate['issuer'][0][0][1]}")
                print(f"Valid From  : {certificate['notBefore']}")
                print(f"Valid Until : {certificate['notAfter']}")

                print("\n✅ SSL Certificate is VALID")

    except Exception as e:
        print("\n❌ Unable to retrieve SSL Certificate.")
        print(e)