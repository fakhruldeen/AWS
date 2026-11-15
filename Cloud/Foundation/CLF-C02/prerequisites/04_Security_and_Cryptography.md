# 04. Security & Cryptography Foundations Prerequisite

## 1. Authentication vs. Authorization (AuthN vs AuthZ)
- **Authentication (AuthN):** Verifying *who you are* (Username + Password, Multi-Factor Authentication token, SSH key, SSL Client certificate).
- **Authorization (AuthZ):** Determining *what you are allowed to do* once verified (IAM Policies, Role permissions, Bucket Policies).

## 2. Symmetric vs. Asymmetric Cryptography
- **Symmetric Encryption (Single Secret Key):**
  - Same key encrypts and decrypts data (e.g., AES-256).
  - Extremely fast; used for encrypting bulk data at rest (S3 SSE-S3, EBS encryption, RDS encryption).
- **Asymmetric Encryption (Public / Private Key Pair):**
  - Data encrypted with the Public Key can only be decrypted by the Private Key (e.g., RSA, ECC).
  - Used for digital signatures, TLS handshakes, and SSH key pairs (`.pem` files for EC2).

## 3. Envelope Encryption: How AWS KMS Protects Enterprise Data
Encrypting large files directly with a master key across the network is slow and introduces security risks. AWS KMS utilizes **Envelope Encryption**:
1. AWS KMS holds the **Customer Managed Key (KMS Key)**.
2. When an instance wants to encrypt data, KMS generates a unique **Data Key (DEK)**.
3. KMS sends two versions of the DEK: a *Plaintext DEK* and a *Ciphertext DEK* (encrypted under the KMS Key).
4. The application uses the Plaintext DEK to encrypt data locally, then immediately deletes the Plaintext DEK from RAM.
5. The Ciphertext DEK is stored alongside the encrypted data. To read the data, KMS decrypts the DEK.
