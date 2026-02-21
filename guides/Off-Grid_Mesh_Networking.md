# 📡 Off-Grid Mesh Networking: Communicating Without the ISP

> "When they cut the cord, we build the web."

In a squat or an urban insurgency, you cannot rely on corporate ISPs. They are points of surveillance and single points of failure. We use **Reticulum** and **Meshtastic** to build our own infrastructure.

## 🛠️ THE TOOLS

### 1. Reticulum Network Stack (RNS)
Reticulum is the cryptography-based networking stack for building wide-area networks with zero central control. It runs over anything: LoRa, Wi-Fi, Ethernet, or even ancient serial lines.
*   **Termux Setup**:
    ```bash
    pkg install python python-cryptography -y
    pip install rns
    ```
*   **Usage**: Run `rnsd` to start the daemon. Your device is now a node in a global, encrypted, peer-to-peer network.

### 2. Meshtastic (The Hardware Layer)
For long-range, low-power communication, we use LoRa radios (like the Heltec V3 or T-Beam) running Meshtastic.
*   **Mobile Sync**: Use the **Meshtastic app (F-Droid)** to link your phone to the radio via Bluetooth.
*   **Result**: Text-based communication for miles without a cell tower in sight.

## 🏴‍☠️ SQUAT TACTICS
*   **The Bridge**: Use a phone running Termux to bridge a local Wi-Fi mesh to a long-range LoRa link.
*   **Nomadic Nodes**: Keep your radios mobile. If one node is compromised, the mesh heals itself.

---
*Source: Scavenged from [Reticulum.network](https://reticulum.network) and [Meshtastic.org](https://meshtastic.org)*
