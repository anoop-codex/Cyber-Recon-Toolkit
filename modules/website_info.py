import requests
import socket
import time


def website_information():

    print("\n========== WEBSITE INFORMATION ==========\n")

    website = input("Enter website (example: google.com): ").strip()

    if not website.startswith("http://") and not website.startswith("https://"):
        url = "https://" + website
    else:
        url = website

    try:

        start_time = time.time()

        response = requests.get(url, timeout=5)

        end_time = time.time()

        domain = website.replace("https://", "").replace("http://", "").split("/")[0]

        ip_address = socket.gethostbyname(domain)

        print("\n========== RESULT ==========")
        print(f"Website      : {domain}")
        print(f"IP Address   : {ip_address}")
        print(f"Status Code  : {response.status_code}")
        print(f"Server       : {response.headers.get('Server', 'Unknown')}")
        print(f"Response Time: {(end_time-start_time)*1000:.2f} ms")

        if url.startswith("https://"):
            print("HTTPS        : Enabled ✅")
        else:
            print("HTTPS        : Not Enabled ❌")

    except requests.exceptions.RequestException:
        print("\n❌ Unable to connect to the website.")