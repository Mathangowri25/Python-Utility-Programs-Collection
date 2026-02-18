# 📊 Sales Data Analyzer Module

A simple Python module designed to analyze and manipulate sales data using list operations.

This project demonstrates filtering, slicing, reversing, copying, and sorting lists in Python.

---

## 📁 Project Structure

```
Sales Data Analyzer Module/
│
├── list_utils4.py
└── test_list_utils4.py
```

---

## 🧠 Project Objective

The goal of this project is to:

* Filter sales based on a threshold value
* Extract specific portions of a sales list
* Reverse a list using slicing
* Copy and sort a list without modifying the original

---

## 📝 File Description

---

### 1️⃣ `list_utils4.py`

This file contains the core sales analysis functions.

---

### 🔹 `sales_above(sale: list, threshold)`

* Returns a list of sales values greater than the threshold.
* Iterates through the list using a loop.
* Does not modify the original list.

Example:

```python
sales_above([100, 200, 150], 120)
# Output: [200, 150]
```

---

### 🔹 `sales_summary(sale: list, first: int, last: int)`

* Returns a tuple containing:

  * First portion of the list (`sale[:first]`)
  * Last portion of the list (`sale[last:]`)
* Uses list slicing.

Example:

```python
sales_summary([10,20,30,40,50], 2, 3)
# Output: ([10,20], [40,50])
```

---

### 🔹 `sales_reversed(sale: list)`

* Returns the reversed version of the list.
* Uses slicing method (`[::-1]`).

Example:

```python
sales_reversed([1,2,3])
# Output: [3,2,1]
```

---

### 🔹 `sales_copy_sort(sale: list)`

* Creates a copy of the original list.
* Sorts the copied list.
* Returns the sorted list.
* The original list remains unchanged.

Example:

```python
sales_copy_sort([30,10,20])
# Output: [10,20,30]
```

---

### 2️⃣ `test_list_utils4.py`

This file is used to test the module functions.

It:

1. Takes 6 sales values from the user
2. Takes:

   * Threshold value
   * First index value
   * Last index value
3. Calls all sales functions
4. Prints the results

---

## 💻 Example Execution

```
Enter the value : 100
Enter the value : 200
Enter the value : 150
Enter the value : 300
Enter the value : 250
Enter the value : 180

Enter the threshold value : 180
Enter the first appear integer : 2
Enter the last appear integer : 4
```

Output:

```
[200, 300, 250]
([100, 200], [250, 180])
[180, 250, 300, 150, 200, 100]
[100, 150, 180, 200, 250, 300]
```

---

## 📚 Concepts Covered

* Python Lists
* For Loops
* Conditional Statements
* List Slicing
* List Copying
* Sorting Lists
* Returning Tuples
* User Input Handling

---

## 🛠 Requirements

* Python 3.x
* Visual Studio Code (recommended)

---
