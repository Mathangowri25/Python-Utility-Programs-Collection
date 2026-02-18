# 📊 Marks Processing Module

The **Marks Processing Module** is a simple Python-based project that performs operations on a list of student marks. It includes utility functions to analyze and process marks efficiently.

---

## 📁 Project Structure

```
Marks Processing Module/
│
├── list_utils.py          # Contains utility functions for mark processing
├── test_list_utils.py     # Test file to run and interact with the functions
└── README.md              # Project documentation
```

---

## 🚀 Features

This module provides the following functionalities:

### 1️⃣ `top_mark(mark, n)`

* Returns a new list containing the **top `n` highest marks**
* Does **not modify** the original list
* Raises `TypeError` if:

  * `mark` is not a list
  * `n` is not an integer

### 2️⃣ `count_occurance(mark, value)`

* Returns how many times a specific mark appears in the list
* Raises `TypeError` if:

  * `mark` is not a list

### 3️⃣ `higher_score(mark, thro)`

* Returns a new list containing marks **greater than or equal to the threshold**
* Uses **list comprehension**
* Raises `TypeError` if:

  * `mark` is not a list
  * `thro` is not an integer

---

## 🧠 File Descriptions

### 📌 `list_utils.py`

Contains three main functions:

```python
top_mark(mark, n)
count_occurance(mark, value)
higher_score(mark, thro)
```

These functions handle sorting, counting, and filtering operations on a list of marks.

---

### 📌 `test_list_utils.py`

This file allows user interaction via console input:

* Takes 10 marks from the user
* Asks for:

  * Number of top marks to display
  * A value to count occurrences
  * A threshold value
* Displays:

  * Top N marks
  * Occurrence count
  * Marks above threshold

Run the file using:

```bash
python test_list_utils.py
```

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required

---

## ▶️ Example Run

```
Enter the mark 1 : 80
Enter the mark 2 : 75
...
Enter the mark 10 : 90
Enter the top higher mark : 3
Number appear in List : 75
Enter the score : 70

[95, 90, 85]
1
[80, 75, 90]
```

---

## ⚠️ Notes

* The functions perform basic type validation.
* Ensure correct data types are passed to avoid `TypeError`.
* The original marks list remains unchanged when retrieving top marks.

---
