#!/usr/bin/env python3
"""
 █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗██╗  ██╗██╗   ██╗ ██████╗ ███████╗███╗   ███╗
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔════╝██║  ██║╚██╗ ██╔╝██╔════╝ ██╔════╝████╗ ████║
███████║██╔██╗ ██║███████║██████╔╝██║     ███████║ ╚████╔╝ ██║  ███╗█████╗  ██╔████╔██║
██╔══██║██║╚██╗██║██╔══██║██╔══██╗██║     ██╔══██║  ╚██╔╝  ██║   ██║██╔══╝  ██║╚██╔╝██║
██║  ██║██║ ╚████║██║  ██║██║  ██║╚██████╗██║  ██║   ██║   ╚██████╔╝███████╗██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝     ╚═╝

  The Squat-Net Toolkit. Run it. Use it. Share it. Own it.
  No paywalls. No masters. No permission needed.

  "Study. Build. Create. Destroy. You are the only one you have to answer to."
"""

import sys
import os
import subprocess

SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")

TOOLS = {
    "radio": {
        "script": "pirate_broadcast.py",
        "desc": "Pirate broadcast — one-to-many UDP mesh radio. No FCC. No licence.",
        "examples": [
            "python anarchy.py radio --dj --station WFUK",
            "python anarchy.py radio --tune",
            "python anarchy.py radio --dj --station 'SQUAT FM' --freq 107.5",
        ],
    },
    "mesh": {
        "script": "local_mesh_chat.py",
        "desc": "Squat-net local mesh chat — two-way UDP broadcast. No internet required.",
        "examples": [
            "python anarchy.py mesh",
        ],
    },
    "encrypt": {
        "script": "encrypt_file.py",
        "desc": "File encryption/decryption — Fernet symmetric encryption. Your files, your keys.",
        "examples": [
            "python anarchy.py encrypt generate_key",
            "python anarchy.py encrypt encrypt secret.txt",
            "python anarchy.py encrypt decrypt secret.txt.encrypted",
        ],
    },
    "audit": {
        "script": "degoogle_audit.py",
        "desc": "De-Google audit — test which Google surveillance endpoints your network can reach.",
        "examples": [
            "python anarchy.py audit",
        ],
    },
    "scrape": {
        "script": "scrape_web.py",
        "desc": "Web scraper — extract text from any URL. Intel gathering, archival, liberation.",
        "examples": [
            "python anarchy.py scrape https://example.com",
        ],
    },
    "eth": {
        "script": "check_eth_balance.py",
        "desc": "ETH balance — query Ethereum address balance via public nodes. No API key needed.",
        "examples": [
            "python anarchy.py eth 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
        ],
    },
}

DIVIDER = "  " + "─" * 62


def print_banner():
    print(__doc__)


def print_help():
    print_banner()
    print(DIVIDER)
    print("  AVAILABLE TOOLS\n")
    for name, info in TOOLS.items():
        print(f"  {name:<10} {info['desc']}")
    print()
    print(DIVIDER)
    print("  USAGE\n")
    print("    python anarchy.py <tool> [args...]\n")
    print("  EXAMPLES\n")
    for name, info in TOOLS.items():
        for ex in info["examples"][:1]:
            print(f"    {ex}")
    print()
    print(DIVIDER)
    print("  Stay sovereign. Stay chaotic. Keep coding. 🤘\n")


def print_tool_help(tool_name: str):
    info = TOOLS[tool_name]
    print(f"\n  {tool_name.upper()} — {info['desc']}\n")
    print("  Examples:")
    for ex in info["examples"]:
        print(f"    {ex}")
    print()


def run_tool(tool_name: str, args: list):
    info = TOOLS[tool_name]
    script_path = os.path.join(SCRIPTS_DIR, info["script"])

    if not os.path.exists(script_path):
        print(f"  [!] Script not found: {script_path}")
        print(f"      Something got nuked. Check your install.")
        sys.exit(1)

    cmd = [sys.executable, script_path] + args
    try:
        result = subprocess.run(cmd)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        sys.exit(0)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print_help()
        sys.exit(0)

    tool_name = sys.argv[1].lower()
    remaining_args = sys.argv[2:]

    if tool_name not in TOOLS:
        print(f"\n  [!] Unknown tool: '{tool_name}'")
        print(f"      Available: {', '.join(TOOLS.keys())}")
        print(f"      Run 'python anarchy.py --help' for usage.\n")
        sys.exit(1)

    run_tool(tool_name, remaining_args)


if __name__ == "__main__":
    main()
