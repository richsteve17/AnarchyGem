## How to Run AnarchyGem Scripts

Scripts can be run individually or through the unified launcher at the root of the repo.

### Prerequisites

1. **Python 3.8+**
2. **pip** for installing dependencies

### Installation

```bash
git clone https://github.com/richsteve17/AnarchyGem.git
cd AnarchyGem
pip install -r requirements.txt
```

---

### Unified Launcher (Recommended)

From the repo root, use `anarchy.py` to access all tools:

```bash
python anarchy.py --help
```

Available tools: `radio`, `mesh`, `encrypt`, `audit`, `scrape`, `eth`

---

### Running Scripts Individually

Navigate to the `scripts` directory:

```bash
cd scripts
```

#### `pirate_broadcast.py` — Pirate Radio

One-to-many UDP broadcast over the local mesh. No internet. No licence. No FCC.

```bash
# Start broadcasting as a station (DJ mode)
python pirate_broadcast.py --dj --station "WFUK"

# Use a different frequency (maps to a different port)
python pirate_broadcast.py --dj --station "SQUAT FM" --freq 107.5

# Listen to any station broadcasting on the default frequency
python pirate_broadcast.py --tune

# Tune to a specific frequency
python pirate_broadcast.py --tune --freq 107.5
```

Frequency range: 88.0–107.9 MHz (maps to ports 8800–10790).
Multiple listeners can tune in simultaneously — it's broadcast, not unicast.

#### `local_mesh_chat.py` — Squat-Net Mesh Chat

Two-way UDP broadcast chat. No server. No internet.

```bash
python local_mesh_chat.py
```

Run on multiple devices on the same Wi-Fi or mesh network.

#### `encrypt_file.py` — File Encryption

Symmetric file encryption using Fernet (AES-128-CBC + HMAC-SHA256).

```bash
# Generate an encryption key (saved to filekey.key)
python encrypt_file.py generate_key

# Encrypt a file
python encrypt_file.py encrypt my_secret_document.txt

# Decrypt a file
python encrypt_file.py decrypt my_secret_document.txt.encrypted
```

Keep `filekey.key` safe — it's excluded from git by `.gitignore`.

#### `degoogle_audit.py` — De-Google Audit

Test which Google surveillance endpoints your current network can reach.

```bash
python degoogle_audit.py
```

#### `scrape_web.py` — Web Scraper

Fetch and extract text content from any URL.

```bash
python scrape_web.py <url>
# Example:
python scrape_web.py https://example.com
```

#### `check_eth_balance.py` — Ethereum Balance

Query any Ethereum address balance using free public JSON-RPC nodes.
No API key. No Etherscan account. Falls back through multiple public nodes.

```bash
python check_eth_balance.py <ethereum_address>
# Example:
python check_eth_balance.py 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
```

---

### Platform Notes

- **Termux (Android):** `pkg install git python` then follow standard instructions.
- **macOS:** Python 3 via Homebrew (`brew install python`) or system Python 3.
- **Linux:** Python 3 + pip usually pre-installed. `sudo apt install python3 python3-pip` if not.
- **iOS (a-Shell):** See [a-Shell Tactical Guide](../guides/a-Shell_Tactical_Guide.md).
- **Windows:** Install from [python.org](https://www.python.org/downloads/). Add to PATH.
