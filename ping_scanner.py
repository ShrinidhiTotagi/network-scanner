import subprocess
import platform

def ping_host(host):
    # Detect OS
    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        print(f"\nScanning {host}...\n")

        result = subprocess.run(
            ["ping", param, "4", host],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print(f"[+] {host} is UP")
        else:
            print(f"[-] {host} is DOWN")

        print("\n--- Ping Output ---\n")
        print(result.stdout)

    except subprocess.TimeoutExpired:
        print("[!] Request timed out")
    except Exception as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    target = input("Enter IP / Hostname: ").strip()
    if target:
        ping_host(target)
    else:
        print("Invalid input")
