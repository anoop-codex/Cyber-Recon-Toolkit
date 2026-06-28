import socket


def port_scanner():

    print("\n========== PORT SCANNER ==========\n")

    target = input("Enter website (example: google.com): ").strip()

    try:

        ip = socket.gethostbyname(target)

        print(f"\nScanning {target} ({ip})...\n")

        common_ports = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS"
        }

        for port, service in common_ports.items():

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"✅ Port {port:<5} ({service}) : OPEN")
            else:
                print(f"❌ Port {port:<5} ({service}) : CLOSED")

            sock.close()

        print("\nScan Complete ✅")

    except socket.gaierror:
        print("\n❌ Unable to resolve the domain.")