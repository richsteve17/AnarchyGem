## How to Run AnarchyGem Scripts

This guide provides simple instructions to get the AnarchyGem scripts running on various operating systems. These scripts are designed for local execution and do not require complex deployments.

### Prerequisites

1.  **Git:** To clone the repository.
2.  **Python 3:** The scripts are written in Python 3.
3.  **pip:** Python's package installer, used for dependencies.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/richsteve17/AnarchyGem.git
    cd AnarchyGem
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running Individual Scripts

Navigate to the `scripts` directory:

```bash
cd scripts
```

#### `check_eth_balance.py`

Fetches the Ethereum balance for a given address.

```bash
python check_eth_balance.py <ethereum_address>
# Example:
python check_eth_balance.py 0xYourEthereumAddressHere
```

#### `degoogle_audit.py`

Checks connectivity to common Google services.

```bash
python degoogle_audit.py
```

#### `encrypt_file.py`

Encrypts and decrypts files using a generated key.

```bash
# Generate an encryption key (filekey.key will be created)
python encrypt_file.py generate_key

# Encrypt a file
python encrypt_file.py encrypt <filepath>
# Example:
python encrypt_file.py encrypt my_secret_document.txt

# Decrypt a file
python encrypt_file.py decrypt <filepath.encrypted>
# Example:
python encrypt_file.py decrypt my_secret_document.txt.encrypted
```

#### `local_mesh_chat.py`

A dead-simple UDP broadcast chat for local networks.

```bash
python local_mesh_chat.py
```

#### `scrape_web.py`

Fetches a webpage and extracts all paragraph text.

```bash
python scrape_web.py <url>
# Example:
python scrape_web.py https://example.com
```

### Platform-Specific Notes

*   **Termux (Android):**
    Install `git` and `python` via `pkg install git python`. Then follow the general installation and running instructions.

*   **macOS:**
    Ensure Xcode Command Line Tools are installed (`xcode-select --install`). Python 3 is usually pre-installed or easily installed via Homebrew (`brew install python`). Then follow the general instructions.

*   **Windows:**
    Install Python from [python.org](https://www.python.org/downloads/). Make sure to check the option to 
add Python to PATH during installation. Then follow the general instructions.

*   **Linux:**
    Python 3 and pip are usually pre-installed. If not, install them using your distribution's package manager (e.g., `sudo apt install python3 python3-pip` on Debian/Ubuntu). Then follow the general instructions.
