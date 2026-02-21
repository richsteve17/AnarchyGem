import socket
import threading
import sys
import uuid

# --- SQUAT-NET LOCAL MESH CHAT ---
# A dead-simple UDP broadcast chat for local networks.
# No internet required. No server required. 
# Just run it on multiple devices on the same Wi-Fi/Mesh.

PORT = 55555
BUFFER_SIZE = 1024
NODE_ID = str(uuid.uuid4())[:8] # Generate a unique ID for this node

def listen():
    """Listens for incoming broadcast messages."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("", PORT))
    
    print(f"[*] Listening for signal on port {PORT} (Node ID: {NODE_ID})...")
    
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        message_with_id = data.decode("utf-8")
        
        # Extract node ID and message
        sender_node_id = message_with_id.split(":::", 1)[0]
        message = message_with_id.split(":::", 1)[1]

        # Only print messages from other nodes
        if sender_node_id != NODE_ID:
            print(f"\n[SIGNAL from {addr[0]} ({sender_node_id})]: {message}")
            print(">> ", end="", flush=True)

def broadcast():
    """Sends a message to the entire local network."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    handle = input("Enter your handle: ")
    print(f"[*] Ready to broadcast as \'{handle}\' (Node ID: {NODE_ID}). Type your message and hit Enter.")
    
    while True:
        msg = input(">> ")
        if msg.lower() == "exit":
            break
        
        full_msg = f"{NODE_ID}:::{handle}: {msg}"
        
        # Try <broadcast> first, fallback to 255.255.255.255
        try:
            sock.sendto(full_msg.encode("utf-8"), ("<broadcast>", PORT))
        except OSError as e:
            if "Network is unreachable" in str(e) or "Cannot assign requested address" in str(e):
                print("[!] <broadcast> failed, trying 255.255.255.255")
                sock.sendto(full_msg.encode("utf-8"), ("255.255.255.255", PORT))
            else:
                raise

if __name__ == "__main__":
    # Start the listener thread
    listener_thread = threading.Thread(target=listen, daemon=True)
    listener_thread.start()
    
    # Start the broadcaster
    try:
        broadcast()
    except KeyboardInterrupt:
        print("\n[*] Shutting down signal. Stay sovereign.")
        sys.exit()
