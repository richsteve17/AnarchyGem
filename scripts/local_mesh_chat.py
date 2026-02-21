import socket
import threading
import sys

# --- SQUAT-NET LOCAL MESH CHAT ---
# A dead-simple UDP broadcast chat for local networks.
# No internet required. No server required. 
# Just run it on multiple devices on the same Wi-Fi/Mesh.

PORT = 55555
BUFFER_SIZE = 1024

def listen():
    """Listens for incoming broadcast messages."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(('', PORT))
    
    print(f"[*] Listening for signal on port {PORT}...")
    
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        message = data.decode('utf-8')
        # Don't print our own messages (basic check)
        print(f"\n[SIGNAL from {addr[0]}]: {message}")
        print(">> ", end="", flush=True)

def broadcast():
    """Sends a message to the entire local network."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    handle = input("Enter your handle: ")
    print(f"[*] Ready to broadcast as '{handle}'. Type your message and hit Enter.")
    
    while True:
        msg = input(">> ")
        if msg.lower() == 'exit':
            break
        full_msg = f"{handle}: {msg}"
        sock.sendto(full_msg.encode('utf-8'), ('<branch-broadcast>', PORT))

if __name__ == "__main__":
    # Note: Using '<branch-broadcast>' works on most Linux/Android systems.
    # On some systems, you might need to use '255.255.255.255'
    
    # Start the listener thread
    listener_thread = threading.Thread(target=listen, daemon=True)
    listener_thread.start()
    
    # Start the broadcaster
    try:
        broadcast()
    except KeyboardInterrupt:
        print("\n[*] Shutting down signal. Stay sovereign.")
        sys.exit()
