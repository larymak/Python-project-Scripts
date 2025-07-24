
# 🔐 Simple Symmetric Encryption in Python

This project demonstrates the basics of **symmetric encryption** using Python and the [`cryptography`](https://cryptography.io/en/latest/) library. It's a great starting point for beginners interested in **cybersecurity**, **cryptography**, or contributing to **open-source security tools**.

---

## 📚 What You'll Learn

- How to generate secure keys
- How to encrypt and decrypt messages
- Basic key management (saving & loading keys)
- How `Fernet` (AES-based encryption) works under the hood

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/simple-encryption-python.git
cd simple-encryption-python
```

### 2. Install Dependencies

Make sure you have Python 3.6+ installed.

Install required package using `pip`:

```bash
pip install cryptography
```

### 3. Run the Code

```bash
python simple_encryption.py
```

On first run, it will generate a `secret.key` file that is used for both encryption and decryption. Each time you run the script, it:
- Loads the existing key
- Encrypts a sample message
- Decrypts it back and displays the result

---

## 📂 File Structure

```
simple-encryption-python/
│
├── simple_encryption.py   # Main script to run encryption and decryption
├── secret.key             # Auto-generated AES-based symmetric key (DO NOT SHARE)
├── README.md              # Documentation
```

---

## 🔒 Security Note

This example is for educational purposes only. If you’re building a production-grade application:
- Never store raw keys in plaintext
- Use environment variables or secure vaults (e.g., AWS KMS, HashiCorp Vault)
- Handle exceptions and errors securely

---

## 🧠 How It Works (In Brief)

- **Fernet** is a module in the `cryptography` package that provides:
  - AES-128 in CBC mode
  - HMAC-SHA256 authentication
  - Random IVs for each encryption

- The encryption key is:
  - Generated once and saved to `secret.key`
  - Loaded on subsequent runs

- The message is:
  - Encrypted using `.encrypt()`
  - Decrypted using `.decrypt()`

---

## 💡 Sample Output

```
[*] Key loaded from 'secret.key'

Original Message: This is a secret message.
Encrypted Message: b'gAAAAABlZ...'
Decrypted Message: This is a secret message.
```

---

## 🤝 Contributing

Contributions are welcome! You can help by:
- Improving the CLI interface
- Adding file encryption support
- Implementing password-based key derivation
- Writing unit tests

To contribute:
1. Fork the repo
2. Create a new branch (`git checkout -b my-feature`)
3. Commit your changes
4. Push and create a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Afolabi Adewale**  
A data and security enthusiast exploring the intersection of Python, encryption, and open-source software.  
[GitHub Profile](https://github.com/your-username)

---

## 🔗 Related Resources

- [Python `cryptography` docs](https://cryptography.io/en/latest/)
- [Understanding Symmetric vs Asymmetric Encryption](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)
- [OWASP Crypto Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
