#!/usr/bin/env python3
"""
check_eth_balance.py — Query Ethereum balance via public JSON-RPC.
No API key. No signup. No corporate middleman.
Uses free public RPC endpoints — falls back through them if one is down.
"""

import sys
import json
import requests

# Public Ethereum JSON-RPC endpoints — no API key required.
# If one is rate-limited or dead, we try the next.
PUBLIC_RPC_ENDPOINTS = [
    "https://cloudflare-eth.com",
    "https://eth.llamarpc.com",
    "https://rpc.ankr.com/eth",
    "https://ethereum.publicnode.com",
]

WEI_PER_ETH = 10 ** 18


def wei_to_eth(wei_hex: str) -> float:
    """Convert a hex wei string (e.g. '0x1a2b3c') to ETH as a float."""
    return int(wei_hex, 16) / WEI_PER_ETH


def fetch_balance(address: str) -> float | None:
    """
    Query eth_getBalance via JSON-RPC against public nodes.
    Returns balance in ETH, or None if all endpoints fail.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1,
    }
    headers = {"Content-Type": "application/json"}

    for endpoint in PUBLIC_RPC_ENDPOINTS:
        try:
            resp = requests.post(
                endpoint,
                data=json.dumps(payload),
                headers=headers,
                timeout=8,
            )
            resp.raise_for_status()
            data = resp.json()

            if "error" in data:
                print(f"  [!] RPC error from {endpoint}: {data['error'].get('message', data['error'])}")
                continue

            balance_eth = wei_to_eth(data["result"])
            return balance_eth

        except requests.exceptions.Timeout:
            print(f"  [~] {endpoint} timed out. Trying next node...")
        except requests.exceptions.ConnectionError:
            print(f"  [~] {endpoint} unreachable. Trying next node...")
        except (KeyError, ValueError) as e:
            print(f"  [!] Bad response from {endpoint}: {e}")

    return None


def validate_address(address: str) -> bool:
    """Basic sanity check: 0x-prefixed, 42 chars total (20 bytes hex)."""
    return (
        address.startswith("0x")
        and len(address) == 42
        and all(c in "0123456789abcdefABCDEF" for c in address[2:])
    )


def main():
    print("\n  [ ETH BALANCE CHECKER — public nodes, no keys, no gatekeepers ]")
    print("  Usage: python check_eth_balance.py <ethereum_address>\n")

    if len(sys.argv) < 2:
        print("  No address provided.")
        print("  Example: python check_eth_balance.py 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
        sys.exit(1)

    address = sys.argv[1].strip()

    if not validate_address(address):
        print(f"  [!] '{address}' does not look like a valid Ethereum address.")
        print("      Expected format: 0x followed by 40 hex characters.")
        sys.exit(1)

    print(f"  Address:  {address}")
    print(f"  Querying public Ethereum nodes...\n")

    balance = fetch_balance(address)

    if balance is None:
        print("\n  [!] All public RPC endpoints failed.")
        print("      You may be offline, or all nodes are rate-limiting you.")
        print("      Try again later or run your own node.")
        sys.exit(1)

    print(f"  Balance:  {balance:.6f} ETH")
    print(f"            ({int(balance * WEI_PER_ETH):,} Wei)\n")


if __name__ == "__main__":
    main()
