import subprocess

def run_nmap(target):
    print("\nSelect Scan Type:")
    print("1. Host Discovery")
    print("2. Port Scan (1-1000)")
    print("3. Custom Port Scan")
    print("4. Service Detection")
    print("5. OS Detection")

    choice = input("Enter choice: ").strip()

    try:
        if choice == "1":
            cmd = ["nmap", "-sn", target]

        elif choice == "2":
            cmd = ["nmap", "-p", "1-1000", target]

        elif choice == "3":
            ports = input("Enter ports (e.g 22,80,443): ").strip()
            cmd = ["nmap", "-p", ports, target]

        elif choice == "4":
            cmd = ["nmap", "-sV", target]

        elif choice == "5":
            cmd = ["sudo", "nmap", "-O", target]

        else:
            print("Invalid choice")
            return

        print("\nRunning scan...\n")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        print("--- Nmap Scan Result ---\n")
        print(result.stdout)

        if result.stderr:
            print("\n[Warnings/Errors]:")
            print(result.stderr)

    except Exception as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    target = input("Enter IP / Network (e.g 127.0.0.1 or 192.168.1.0/24): ").strip()

    if target:
        run_nmap(target)
    else:
        print("Invalid input")
