# Bookstore Management System

This is a robust console-based system for managing a national bookstore's inventory, sales, and reports. The program is written in Python and designed for interactive use via the command line.

## Features

- **Inventory Management**: Add, update, delete, and list products (books) with fields: title, author, category, price, and stock.
- **Sales Registration**: Register sales by associating a client, product, quantity, date, and discount. Stock is validated and updated automatically.
- **Reports Module**:
  - Top 3 best-selling products
  - Sales report grouped by author
  - Gross and net income calculation (with and without discounts)
- **Advanced Validations**: Ensures positive numbers, correct formats, required fields, and prevents sales with insufficient stock.
- **Modular Design**: All functionalities are encapsulated in functions with clear parameters and return values. Lambda functions are used for aggregate calculations.
- **Data Storage**: Uses nested dictionaries and lists for products and sales. Efficient grouping and searching methods are applied.
- **Preloaded Data**: The system starts with at least 5 preloaded products.
- **Exception Handling**: The code handles exceptions gracefully to prevent abrupt program termination.
- **All interactions and messages are in English.**

## How to Use

1. **Save the code** in a file, e.g., `bookstore.py`.
2. **Run the program** from your terminal:
   ```
   python bookstore.py
   ```
3. **Follow the interactive menu** to manage products, register sales, and view reports.

## Requirements
- Python 3.x

## Good Coding Practices
- Clear function definitions and modular structure
- Use of constants and validations
- Exception handling for robust execution

## Example Menu
```
--- Bookstore Management System ---
1. Product management
2. Register sale
3. Sales list
4. Reports
5. Exit
```
