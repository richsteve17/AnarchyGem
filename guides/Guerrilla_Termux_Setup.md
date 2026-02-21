# 🛠️ Guerrilla Termux Setup: Mobile Python Insurgency

> "Your phone is a mini-computer. Stop treating it like a toy and start treating it like a node of resistance."

Don't install Termux from the Play Store. It’s deprecated and restricted by corporate policies. Use the sovereign version.

## 📥 Deployment
1.  **Source**: Download the latest APK from **F-Droid** or the official **GitHub Releases**.
2.  **Permissions**: Grant storage access immediately.
    ```bash
    termux-setup-storage
    ```

## ⚡ Hardening the Environment
Update and upgrade the base system. Bypass the prompts with `-y`.
```bash
apt update -y && pkg upgrade -y
```

## 🐍 Python Guerrilla Tactics
Install the core tools for Python development and automation.
```bash
pkg install python git bash -y
```

### Tactical Packages for Insurgents:
*   **Scientific Computing**: `pkg install python-numpy python-pandas`
*   **Cryptography**: `pkg install python-cryptography`
*   **Network Analysis**: `pkg install nmap`

## 🏴‍☠️ Scavenged Automation (termux4all)
To rapidly deploy a full suite of development and security tools:
```bash
git clone https://www.github.com/shansuharban/termux4all.git
cd termux4all
chmod +x *
./t4all.sh
```

## 🎸 DIY Ethics
*   **No Root Needed**: Most tools work in the user-space.
*   **Stay Local**: Your code, your hardware.
*   **Offline First**: Code in the terminal even when the signal is jammed.

---
*Source: Intel scavenged from [termux4all](https://github.com/ShanSuharban/termux4all)*
