# 🧠 Local LLM Integration: Uncensored AI in Your Pocket

> "No cloud, no corporate filters, just raw intelligence on your terms."

Running Large Language Models (LLMs) locally on your mobile device is the ultimate act of AI sovereignty. It bypasses corporate paywalls, censorship, and data harvesting. We use `llama.cpp` and `ollama` to bring uncensored AI directly to your Termux terminal.

## 1. Llama.cpp: The Foundation
`llama.cpp` is a C/C++ port of Facebook's LLaMA model that allows for efficient inference on consumer hardware, including mobile devices. It's the engine that powers many local LLM solutions.

### 🛠️ Termux Setup (Llama.cpp)
```bash
pkg update && pkg upgrade -y
pkg install git cmake make clang -y
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
```
*   **Models**: Download compatible GGUF models (e.g., Llama 3, Mistral) from Hugging Face or other sources. Place them in the `llama.cpp/models` directory.
*   **Running Inference**:
    ```bash
    ./main -m models/your-model.gguf -p "What is digital anarchy?" -n 128
    ```

## 2. Ollama: Simplified Local LLM Management
Ollama provides a streamlined way to run, manage, and interact with LLMs locally. While primarily designed for desktop, its server component can be adapted for Termux.

### 🛠️ Termux Setup (Ollama - Advanced)
*   **Note**: Ollama's official Termux support is evolving. This is a more advanced setup.
*   **Prerequisites**: Ensure `proot-distro` is set up (see `Scavenged_Compute_Proot.md`). You'll likely run Ollama within a full Linux environment like Debian.
    ```bash
    proot-distro login debian
    # Inside Debian:
    curl -fsSL https://ollama.com/install.sh | sh
    ollama run llama3
    ```

## 🎸 DIY ETHICS
*   **Censorship Resistance**: Run models that haven't been lobotomized by corporate filters.
*   **Privacy**: Your data stays on your device. No cloud, no logs.
*   **Resourcefulness**: Leverage your mobile device's compute power to reclaim AI.

---
*Source: Scavenged from [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp) and [Ollama Documentation](https://ollama.com/)*
