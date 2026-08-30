# User Management System (CLI)

A lightweight **Command Line Interface (CLI)** application built with Python to manage user records using **CRUD** (Create, Read, Update, Delete) operations. This project features a dynamic typewriter effect with ANSI color support for enhanced user experience.

---

## 🚀 Features

* **Full CRUD Operations:** View, Add, Update, and Delete users.
* **Dynamic UI:** Includes a "typewriter" animation effect for console output.
* **Color-Coded Feedback:**
    * 🟢 **Green:** Success messages.
    * 🔴 **Red:** Error messages and exit alerts.
* **Input Validation:** Ensures only numeric inputs are processed for actions.
* **Error Handling:** Robust `try-except` blocks to prevent crashes during runtime.

---

## 🛠️ Project Structure

```text
├── main.py              # Entry point of the application
├── crud/
│   └── views.py         # User model and view logic
└── services/
    └── action.py        # Logic mapping inputs to CRUD functions

```

---

## 💻 Installation & Usage

1. **Clone the repository:**
```bash
git clone [https://github.com/yourusername/user-management-python.git](https://github.com/yourusername/user-management-python.git)
cd user-management-python

```


2. **Run the application:**
```bash
python main.py

```

## 📖 Menu Options

Upon launching, select an option by typing the corresponding number:

| Option | Action | Description |
| --- | --- | --- |
| **1** | **Show users list** | Displays all registered users. |
| **2** | **Add user** | Opens a prompt to create a new user profile. |
| **3** | **Update user** | Modifies existing user details. |
| **4** | **Delete user** | Removes a user from the system. |
| **5** | **Quit** | Safely closes the application. |

---

## ⚙️ Technical Highlights

### Visual Effects

The system uses the `sys.stdout` buffer to print characters one by one for a typewriter effect, combined with **ANSI escape codes** for coloring:

* **Green (`\033[92m`)**: Used for successful operations.
* **Red (`\033[91m`)**: Used for errors and exit messages.

### Logic Flow

The program verifies that the input is a digit before processing, preventing common input errors.

```python
if action.isdigit():
    actions(action, User)
else:
    print("Enter the action number.")

```

---

## 📝 License

This project is open-source and available under the **MIT License**.