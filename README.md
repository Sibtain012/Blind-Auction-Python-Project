# 💰 SECRET AUCTION PROGRAM (Python)

A simple terminal-based Python program for running a silent auction. Users can place bids anonymously, and the program determines the highest bidder.

---

## 🚀 Built With

* Python 🐍
* ASCII Art (from `art.py`)
* Terminal/Command Line

---

## 📚 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [How It Works](#how-it-works)
* [How to Run](#how-to-run)
* [Example](#example)
* [Known Issues](#known-issues)

---

## 🧠 Overview

This project allows multiple users to place secret bids. Once all users have entered their bids, the program announces the highest bidder.

---

## ✨ Features

* Asks each user for their name and bid amount.
* Stores bids in a Python dictionary.
* Uses ASCII logo from `art.py` for a polished UI.
* Clears the screen between entries to maintain secrecy.
* Identifies and prints the highest bidder at the end.

---

## ⚙️ How It Works

1. **Display Logo**
   Imports and prints the ASCII logo from `art.py`.

2. **Collect Input**
   Repeatedly prompts users for their name and bid.

3. **Store Bids**
   Bids are saved in a dictionary `{name: price}`.

4. **Compare Bids**
   The function `find_highest_bidder()` determines the winner.

---

## 🧪 How to Run

```bash
# Ensure Python is installed
python --version

# Place the following files in one folder:
# - main.py (this code)
# - art.py (contains logo variable)

# Run the program
python main.py
```

---

## 💡 Example

```
What is your name?: Alice
What is your bid?: $300
Are there any other bidders? Type 'yes' or 'no'.
yes
... (screen clears)
What is your name?: Bob
What is your bid?: $450
Are there any other bidders? Type 'yes' or 'no'.
no

The winner is Bob with a bid of $450
```

---

## ⚠️ Known Issues

* ❌ Currently, only the last entered bid is stored due to:

  ```python
  bid_list = {name: price}
  ```

  This line **overwrites** previous entries. It should be:

  ```python
  bid_list[name] = price
  ```

---
