# 📘 Copy Behavior Investigation

A Python project that demonstrates the difference between **shallow copy** and **deep copy**, and how nested lists behave when modified.

This project helps understand how Python handles memory references and object copying.

---

## 📁 Project Structure

```
Copy Behavior Investigation/
│
├── list_utils3.py
└── test_list_utils3.py
```

---

## 🧠 Project Objective

The goal of this project is to:

* Understand the difference between shallow copy and deep copy
* Observe how modifying copied data affects the original list
* Work with nested lists
* Practice using Python's built-in `copy` module

---

## 📝 File Description

---

### 1️⃣ `list_utils.py`

This file contains three main functions:

---

### 🔹 `shallow_copy(data: list)`

* Creates a **shallow copy** of the list using `copy.copy()`
* Modifies an element in the copied list
* Prints both the original and copied list
* Demonstrates how shallow copy behaves

📌 Important:
A shallow copy creates a new outer list, but nested objects are still shared.

---

### 🔹 `deep_copy(data: list)`

* Creates a **deep copy** of the list using `copy.deepcopy()`
* Modifies an element in the copied list
* Prints both the original and copied list
* Demonstrates that deep copy creates completely independent objects

📌 Important:
A deep copy duplicates all nested objects, so changes do not affect the original.

---

### 🔹 `nested_list(data, value)`

* Searches for the first nested list inside the given list
* Appends a value to that nested list
* Stops after modifying the first nested list found

---

### 2️⃣ `test_list_utils3.py`

This file is used to test the copy functions.

It:

1. Takes 6 integer inputs from the user
2. Takes one additional number
3. Calls:

   * `shallow_copy()`
   * `deep_copy()`
   * `nested_list()`

---

## ▶️ How to Run the Project

### Step 1: Open the project folder in **Visual Studio Code**

### Step 2: Run the following command in terminal:

```bash
python test_list_utils3.py
```

### Step 3: Enter the required values when prompted.

---

## 💻 Example Execution

```
Enter the value : 1
Enter the value : 2
Enter the value : 3
Enter the value : 4
Enter the value : 5
Enter the value : 6
Enter the number : 10
```

The program will display:

* The original list
* The shallow copied list after modification
* The deep copied list after modification
* Changes made to nested lists (if present)

---

## ⚠️ Important Note

Make sure your import statement matches the filename.

If your file is named `list_utils.py`, update this line in `test_list_utils3.py`:

```python
from list_utils3 import shallow_copy, deep_copy, nested_list
```

to:

```python
from list_utils import shallow_copy, deep_copy, nested_list
```

---

## 📚 Concepts Covered

* Python Lists
* Shallow Copy (`copy.copy`)
* Deep Copy (`copy.deepcopy`)
* Nested Lists
* Memory References
* User Input Handling

---

## 🛠 Requirements

* Python 3.x
* Visual Studio Code (recommended)

