# 🛠️ Scavenged Compute: Turning Trash into Infrastructure

> "One person's e-waste is another's server farm."

Old Android phones are everywhere. They are high-performance, low-power Linux nodes waiting to be liberated. We use **proot-distro** to install full Linux distributions inside Termux without needing root access.

## 📥 DEPLOYMENT
1.  **Install the Manager**:
    ```bash
    pkg install proot-distro -y
    ```
2.  **Choose Your Flavor**:
    *   **Debian** (Stable/Reliable): `proot-distro install debian`
    *   **Arch** (Cutting Edge): `proot-distro install archlinux`
    *   **Alpine** (Ultra-light): `proot-distro install alpine`

## ⚡ RUNNING THE NODE
Login to your new environment:
```bash
proot-distro login debian
```
You now have a full Linux filesystem. Install a web server, a database, or a Python bot that runs 24/7 on your scavenged hardware.

## 🏴‍☠️ SQUAT TACTICS
*   **The Basement Server**: Keep the phone plugged in, screen off, running a local mesh chat or a file server for the community.
*   **Low Power, High Impact**: A phone uses 5W of power. You can run a dozen of these off a single scavenged car battery and a solar panel.

---
*Source: Scavenged from [Termux Wiki](https://wiki.termux.com/wiki/PRoot)*
