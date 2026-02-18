# 📋 City List Management System

A simple Python-based system for managing and analyzing a list of marks.
This project demonstrates list operations, input handling, sorting, counting occurrences, and filtering using list comprehension.

---

## 📁 Project Structure

```
City List Management System/
│
├── list_utils.py
└── test_list_utils.py
```

---

## 🧠 Description

This project contains utility functions to perform operations on a list of marks:

* Get top N highest marks
* Count how many times a specific mark appears
* Filter marks based on a threshold

---

## 📝 File Details

### 1️⃣ `list_utils.py`

This file contains three main functions:

### 🔹 `top_mark(mark, n)`

* Returns a new list containing the top **n highest marks**
* Does not modify the original list
* Raises `TypeError` if:

  * `mark` is not a list
  * `n` is not an integer

---

### 🔹 `count_occurance(mark, value)`

* Returns how many times a given mark appears in the list
* Raises `TypeError` if `mark` is not a list

---

### 🔹 `higher_score(mark, thro)`

* Returns a new list containing marks **greater than or equal to** a threshold
* Uses **list comprehension**
* Raises `TypeError` if:

  * `mark` is not a list
  * `thro` is not an integer

---

### 2️⃣ `test_list_utils.py`

This file is used to test the functions.

It:

1. Takes 10 marks as input from the user
2. Takes:

   * Number of top marks to display
   * A value to count occurrences
   * A threshold value
3. Prints:

   * Top N marks
   * Count of specific mark
   * Marks above threshold

---

## ▶️ How to Run the Project

### Step 1: Open the project folder in **Visual Studio Code**

### Step 2: Run the following command in terminal:

```bash
python test_list_utils.py
```

### Step 3: Enter the required inputs when prompted.

---

## 💻 Example Run

```
Enter the mark 1 : 80
Enter the mark 2 : 75
...
Enter the mark 10 : 90

Enter the top higher mark : 3
Number appear in List : 75
Enter the score : 70
```

Output:

```
[95, 90, 85]
1
[80, 75, 90, 85]
```

---

## ⚠️ Notes

* Make sure the import statement matches the filename.
  If your file is named `list_utils.py`, change:

```python
from list_utils1 import top_mark,count_occurance,higher_score
```

to:

```python
from list_utils import top_mark, count_occurance, higher_score
```

* The program expects numeric (integer) inputs only.

---

## 🚀 Features Used

* Python Functions
* Exception Handling
* Sorting Lists
* List Comprehension
* User Input Handling

---

## 📌 Requirements

* Python 3.x
* Visual Studio Code (recommended)

---
