#!/usr/bin/env python3
"""
██████╗ ██╗██████╗  █████╗ ████████╗███████╗    ██████╗  █████╗ ██████╗ ██╗ ██████╗
██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔══██╗██║██╔═══██╗
██████╔╝██║██████╔╝███████║   ██║   █████╗      ██████╔╝███████║██║  ██║██║██║   ██║
██╔═══╝ ██║██╔══██╗██╔══██║   ██║   ██╔══╝      ██╔══██╗██╔══██║██║  ██║██║██║   ██║
██║     ██║██║  ██║██║  ██║   ██║   ███████╗    ██║  ██║██║  ██║██████╔╝██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝

  Broadcasting Without Permission Since Forever.
  No FCC. No Licence. No Corporate Overlords.
  Just signal and noise on the local mesh.

USAGE:
  DJ/Broadcaster:  python pirate_broadcast.py --dj --station "WFUK"
  Listener:        python pirate_broadcast.py --tune
  Pick frequency:  python pirate_broadcast.py --dj --station "WFUK" --freq 91.1
"""

import socket
import threading
import sys
import argparse
import datetime
import time
import uuid
import os

# --- DEFAULT FREQUENCY MAP ---
# Frequencies (MHz) map to ports. We shift FM band to avoid privileged ports.
# 88.0 MHz -> port 8800, 107.9 MHz -> port 10790
# Default: 90.9 (anarchy's lucky number) -> port 9090
DEFAULT_FREQ = 90.9
BUFFER_SIZE = 4096
BROADCAST_INTERVAL = 0.1  # seconds between recv polls

STATION_LOGO = """
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  | P I R A T E   R A D I O  ///   |
  | ON THE WIRE. OFF THE GRID.      |
  | NO PERMISSION REQUIRED.         |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""

LISTENER_LOGO = """
  ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
  | TUNING IN... SCANNING THE MESH  |
  | RECEIVING SIGNAL FROM THE WIRE  |
  | PRESS CTRL+C TO KILL THE FEED   |
  ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
"""


def freq_to_port(freq: float) -> int:
    """Convert a frequency like 90.9 to a port like 9090."""
    return int(round(freq * 100))


def timestamp() -> str:
    return datetime.datetime.now().strftime("%H:%M:%S")


def make_packet(station: str, node_id: str, message: str) -> bytes:
    """Pack a broadcast datagram: STATION:::NODEID:::MESSAGE"""
    payload = f"{station}:::{node_id}:::{message}"
    return payload.encode("utf-8")


def unpack_packet(data: bytes):
    """Returns (station, node_id, message) or None on malformed packet."""
    try:
        parts = data.decode("utf-8").split(":::", 2)
        if len(parts) == 3:
            return parts[0], parts[1], parts[2]
    except UnicodeDecodeError:
        pass
    return None


# ─────────────────────────────────────────────────────────
# LISTENER MODE
# ─────────────────────────────────────────────────────────

def run_listener(freq: float):
    port = freq_to_port(freq)
    print(LISTENER_LOGO)
    print(f"  Frequency: {freq:.1f} FM  |  Port: {port}")
    print(f"  Scanning for pirate stations...\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("", port))
    sock.settimeout(1.0)

    seen_stations = set()

    try:
        while True:
            try:
                data, addr = sock.recvfrom(BUFFER_SIZE)
                result = unpack_packet(data)
                if result is None:
                    continue
                station, node_id, message = result

                if station not in seen_stations:
                    seen_stations.add(station)
                    print(f"\n  [NEW STATION DETECTED] >>> {station} <<< on {addr[0]}")

                print(f"  [{timestamp()}] {station}: {message}")

            except socket.timeout:
                continue

    except KeyboardInterrupt:
        print(f"\n\n  [*] Signal lost. Stay sovereign. 📻")
        sys.exit(0)


# ─────────────────────────────────────────────────────────
# BROADCASTER / DJ MODE
# ─────────────────────────────────────────────────────────

def station_beacon(sock, station: str, node_id: str, port: int, stop_event: threading.Event):
    """Sends a periodic beacon so listeners can discover the station."""
    beacon_msg = make_packet(station, node_id, f"[STATION ONLINE — {station} BROADCASTING LIVE]")
    while not stop_event.is_set():
        try:
            sock.sendto(beacon_msg, ("<broadcast>", port))
        except OSError:
            try:
                sock.sendto(beacon_msg, ("255.255.255.255", port))
            except OSError:
                pass
        stop_event.wait(15)  # beacon every 15s


def broadcast_message(sock, station: str, node_id: str, port: int, message: str):
    """Send a single message out over the broadcast channel."""
    packet = make_packet(station, node_id, message)
    try:
        sock.sendto(packet, ("<broadcast>", port))
    except OSError:
        sock.sendto(packet, ("255.255.255.255", port))


def run_dj(station: str, freq: float):
    port = freq_to_port(freq)
    node_id = str(uuid.uuid4())[:8]

    print(STATION_LOGO)
    print(f"  STATION:    {station}")
    print(f"  FREQUENCY:  {freq:.1f} FM  |  PORT: {port}")
    print(f"  NODE ID:    {node_id}")
    print(f"  BROADCAST:  UDP local mesh (no internet required)")
    print()
    print(f"  Type your message and hit ENTER to transmit.")
    print(f"  Empty line = send a dead-air separator.")
    print(f"  Ctrl+C to pull the plug on the station.\n")
    print(f"  {'─' * 50}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    stop_event = threading.Event()
    beacon_thread = threading.Thread(
        target=station_beacon,
        args=(sock, station, node_id, port, stop_event),
        daemon=True
    )
    beacon_thread.start()

    # Announce going live
    broadcast_message(sock, station, node_id, port,
                      f">>> {station} JUST WENT LIVE ON {freq:.1f} FM <<<")
    print(f"  [{timestamp()}] *** YOU ARE ON AIR ***\n")

    try:
        while True:
            try:
                msg = input(f"  {station} >> ")
            except EOFError:
                break

            if not msg.strip():
                broadcast_message(sock, station, node_id, port,
                                  "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ dead air ─ ─ ─ ─ ─ ─ ─ ─ ─ ─")
            else:
                broadcast_message(sock, station, node_id, port, msg)
                print(f"  [{timestamp()}] TRANSMITTED.")

    except KeyboardInterrupt:
        print(f"\n\n  [{timestamp()}] Signing off...")
        broadcast_message(sock, station, node_id, port,
                          f">>> {station} SIGNING OFF. STAY FREE. <<<")
        stop_event.set()
        time.sleep(0.5)
        sock.close()
        print("  Station offline. The signal dies with the transmitter. ✊")
        sys.exit(0)


# ─────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="pirate_broadcast.py",
        description="Pirate Radio — UDP mesh broadcast. No license required.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pirate_broadcast.py --dj --station "WFUK"
  python pirate_broadcast.py --dj --station "SQUAT FM" --freq 107.5
  python pirate_broadcast.py --tune
  python pirate_broadcast.py --tune --freq 107.5
        """
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--dj",
        action="store_true",
        help="Broadcaster mode. You are the station. You are the signal."
    )
    mode_group.add_argument(
        "--tune",
        action="store_true",
        help="Listener mode. Scan for pirate stations on the mesh."
    )

    parser.add_argument(
        "--station",
        type=str,
        default="WFUK",
        help="Your station call sign (DJ mode only). Default: WFUK"
    )
    parser.add_argument(
        "--freq",
        type=float,
        default=DEFAULT_FREQ,
        help=f"Broadcast frequency in FM MHz (maps to a port). Default: {DEFAULT_FREQ}"
    )

    args = parser.parse_args()

    # Validate frequency range (roughly FM band 88.0–107.9)
    if not (88.0 <= args.freq <= 107.9):
        print(f"[!] Frequency must be between 88.0 and 107.9 MHz. Got: {args.freq}")
        sys.exit(1)

    if args.dj:
        station_name = args.station.upper().strip()
        if not station_name:
            print("[!] Station name cannot be empty. Give your station a name.")
            sys.exit(1)
        run_dj(station_name, args.freq)
    elif args.tune:
        run_listener(args.freq)


if __name__ == "__main__":
    main()
