import concurrent.futures
import socket
import time

# CONFIGURATIA
TARGET = input("Enter target IP (e.g., 127.0.0.1): ") or "127.0.0.1"
PORT_RANGE = range(1, 1025)
THREADS = 100


# Functia de scanare
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((TARGET, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception as e:
        pass


def main():
    print(f"Scanning target: {TARGET}")
    print(f"Scanning ports 1-1024 with {THREADS} threads....\n")

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(scan_port, PORT_RANGE)

    end_time = time.time()

    print("\nScan complete.")
    print(f"Time taken: {round(end_time - start_time, 2)} seconds")


if __name__ == "__main__":
    main()
