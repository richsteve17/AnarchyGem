# 🛡️ PGP Signing Protocol: Authenticating the Signal

> "In a world of compromised signals, a signature is your proof of truth."

To ensure the integrity and authenticity of the AnarchyGem—and any other critical intel you distribute—we use **PGP (Pretty Good Privacy)**. A PGP signature proves that the files originated from you and have not been tampered with.

## 1. Generating Your Key Pair
First, you need a public and private key pair. The private key is your identity; keep it secure. The public key is what you share for others to verify your signatures.

### 🛠️ Termux Setup (GnuPG)
```bash
pkg install gnupg -y
gpg --full-generate-key
```
*   **Key Type**: Choose `(1) RSA and RSA`.
*   **Key Size**: `4096` bits for maximum security.
*   **Expiration**: Set an expiration date (e.g., `1y` for one year) or `0` for no expiration (less secure).
*   **User ID**: Enter your name and email (e.g., `AnarchyGem <anarchygem@example.com>`).
*   **Passphrase**: **CRITICAL!** Choose a strong, memorable passphrase. This protects your private key.

## 2. Exporting Your Public Key
Share your public key so others can verify your signatures.
```bash
gpg --armor --export <your_email> > anarchygem_public_key.asc
```
Distribute `anarchygem_public_key.asc` widely (e.g., include it in the AnarchyGem, upload to a keyserver).

## 3. Signing Files
To sign a file (e.g., a manifesto), you create a detached signature file.
```bash
gpg --detach-sign <filename>
```
This will create `<filename>.sig`. Distribute this `.sig` file alongside the original file.

## 4. Verifying Signatures
Anyone with your public key can verify a signed file.
```bash
gpg --verify <filename>.sig <filename>
```
If the signature is valid, GnuPG will confirm it. If it has been tampered with, it will report an error.

## 5. Signing Git Commits (Advanced)
For ultimate transparency and authenticity, sign your Git commits.
```bash
git config --global user.signingkey <your_key_id>
git config --global commit.gpgsign true
```
Now, every commit you make will be signed, proving its origin.

## 🎸 DIY ETHICS
*   **Trust No One, Verify Everything**: PGP is your tool for trust in a trustless world.
*   **Key Management**: Guard your private key with your life. Back it up securely.
*   **Educate**: Teach others how to sign and verify. The more who use it, the stronger the signal.

---
*Source: Scavenged from [GitHub Docs on Signing Commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) and [GnuPG Documentation](https://www.gnupg.org/gph/en/manual.html)*
