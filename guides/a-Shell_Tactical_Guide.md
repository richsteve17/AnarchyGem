# 📱 a-Shell Tactical Guide: iOS Terminal Insurgency

> "The App Store is a cage. a-Shell is your crowbar."

a-Shell brings a powerful local terminal environment to iOS, allowing you to run Python, JavaScript, and other command-line tools directly on your device, bypassing Apple's sandbox limitations for true mobile development.

## 📥 DEPLOYMENT & SETUP
1.  **Installation**: Download a-Shell from the App Store (yes, a necessary evil for now, but the work happens *inside* the shell).
2.  **Initial Setup**: Upon first launch, a-Shell will set up its file system. This is your sovereign territory.

## 🐍 PYTHON ENVIRONMENT
a-Shell comes with Python pre-installed. This is your primary weapon for mobile scripting.

### 1. Package Management (`pip`)
While a-Shell provides many common packages, you can install more using `pip`.
```bash
pip install <package_name>
```
*   **Note**: Packages are installed locally within a-Shell's environment, not system-wide.

### 2. Virtual Environments
For project isolation, `venv` is your ally. This keeps your dependencies clean and prevents conflicts.
```bash
python -m venv my_project_env
source my_project_env/bin/activate
```

### 3. File System Access
a-Shell can access local files and cloud storage (iCloud Drive, Working Copy, etc.).
*   **`pickFolder`**: Access folders from other apps.
*   **`open`**: Open files in other apps.
*   **`edit`**: Edit files with a-Shell's built-in editor.

## 📡 NETWORK & EXTERNAL ACCESS
*   **`curl` / `wget`**: Standard tools for web requests.
*   **`ssh` / `scp`**: Connect to remote servers for true terminal guerrilla warfare.

## 🎸 DIY ETHICS
*   **Local First**: Prioritize local execution to minimize reliance on external servers.
*   **Data Sovereignty**: Keep your data on your device, under your control.
*   **Script Everything**: Automate tasks to break free from repetitive manual processes.

---
*Source: Scavenged from a-Shell documentation and community forums.*
