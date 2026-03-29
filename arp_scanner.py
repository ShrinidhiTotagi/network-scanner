import subprocess
import platform

def arp_scan():
    try:
        print("\nFetching ARP Table...\n")

        # Detect OS
        if platform.system().lower() == "windows":
            cmd = ["arp", "-a"]
        else:
            cmd = ["arp", "-n"]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("--- ARP Table ---\n")
            print(result.stdout)

            # Count entries (basic logic)
            lines = result.stdout.split("\n")
            entries = [line for line in lines if line.strip() != ""]
            print(f"\nTotal Entries: {len(entries)}")

        else:
            print("Failed to fetch ARP table")

    except Exception as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    arp_scan()
