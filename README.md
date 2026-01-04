# 🛒 E-Commerce Cart System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-yellow?style=for-the-badge)

A simple yet feature-rich command-line E-Commerce Cart System built with Python. This tool allows users to manage a virtual shopping cart, generate receipts, and save transaction history.

---

## 🌟 Features

- **🛍️ Add Items**: Easily add items to your cart with Name, Quantity, and Price.
- **👀 View Cart**: Display your current cart items in a clean, formatted table.
- **🧾 Print Receipt**: Generate a professional text-based receipt (e.g., `cart_details_20231025123000.txt`).
- **💾 Auto-Save**: Automatically saves your cart details to a JSON file (e.g., `cart_history-2023-10-25.json`) upon exit.
- **👤 Guest/User Mode**: Supports personalized user names or quick guest access.
- **🎨 Colorful UI**: Enhanced user experience using the `termcolor` library.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed on your system. You also need to install the required dependency:

```bash
pip install termcolor
```

### Installation

1. Clone this repository or download the source code.
2. Navigate to the source code directory:

```bash
cd E-cart-system
```

### Usage

Run the main script to start the application:

```bash
python main.py
```

Follow the on-screen prompts to navigate the menu:

1. **Add Item to Cart**: Input item details (Format: `ItemName, Quantity, Price`).
2. **View Cart Items**: See what's in your cart.
3. **Print Cart Details**: Save a receipt to a text file.
4. **Exit**: Save data to JSON and close the application.

---

## 📂 Project Structure

```text
E-Commerce-Cart-System/
├── README.md          # Project documentation
└── E-cart-system/     # Source code directory
    ├── main.py        # Entry point of the application
    ├── models.py      # Core logic for User and Cart management
    └── json_savefile.py # Handles saving cart data to JSON
```

---

## 👥 Authors

Developed by **@Coding_group**:

- **Kruthik BT**
- **Gowtham Gowda C B**
- **Akash B V**
- **Rohith S J**

---

<p align="center">
  Made with ❤️ by the Coding Group
</p>
