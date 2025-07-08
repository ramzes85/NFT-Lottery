# 🎲 NFT Lottery Blockchain (Python)

**NFT Lottery Blockchain** is a simple Python-based application that simulates a fair lottery system using basic blockchain principles. Each round allows users to enter their names as "NFT tickets". The system creates a new block that includes all participants, and selects a winner based on a cryptographic hash of the block's data — ensuring fairness, transparency, and immutability.

This project is ideal for learning how blockchain data structures work, especially how hashes can be used for trustless randomness without external dependencies.

---

## 🔧 How It Works

- Users enter their names via terminal input.
- A new block is created with:
  - a unique index
  - a timestamp
  - a list of participants
  - the hash of the previous block
- The hash of the block is used to randomly (and fairly) choose a winner.
- The blockchain stores the full immutable history of all lottery rounds.

---

## ✅ Features

- Simple blockchain logic (no external libraries)
- Fair, hash-based winner selection
- Terminal-based user input
- Transparent, tamper-proof history of all rounds
- Easy to extend into full web or NFT app

---

## 🚀 Installation & Usage

1. **Clone or download this repository**:

   ```bash
   git clone https://github.com/ramzes85/NFT-Lottery.git
   cd NFT-Lottery

2. **Run the application using**:

   ```bash
   python main.py

