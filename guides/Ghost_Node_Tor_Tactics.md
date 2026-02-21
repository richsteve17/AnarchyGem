# 🕵️ Ghost Node: Tor Tactics for Mobile Terminals

> "Visibility is a liability. The Ghost Node is your shroud."

Don't just code; code in the shadows. We use **Orbot** and **Tor** to ensure that our terminal traffic—whether it's `git push`, `curl`, or `pip install`—never reveals our physical location or identity.

## 📥 DEPLOYMENT
1.  **Source**: Install **Orbot** from F-Droid.
2.  **Configuration**: Enable "VPN Mode" in Orbot and select **Termux** or **a-Shell** in the "App VPN Mode" settings.
3.  **The Bridge**: If Tor is blocked by the local ISP, use "Snowflake" or "Obfs4" bridges within Orbot settings to bypass the jammer.

## ⚡ TERMINAL HARDENING (Termux)
To force all traffic through the Tor network without using the global VPN mode:
```bash
pkg install tor torsocks -y
```
Run any command through the shroud:
```bash
torsocks git push origin main
```

## 🎸 DIY ETHICS
*   **No Metadata**: Tor strips your IP, but your code might still have your name. Scrub your Git config!
*   **Stay Anonymous**: Use a fresh identity in Orbot frequently.
*   **Onion Services**: Host your own local documentation or chat as a `.onion` site to keep it hidden from the public web.

---
*Source: Scavenged from [The Tor Project](https://torproject.org) and [Guardian Project](https://guardianproject.info)*
