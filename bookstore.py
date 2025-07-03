import datetime

# Constants
PRODUCT_FIELDS = ["title", "author", "category", "price", "stock"]
MIN_PRODUCTS = 5

# Preloaded products
products = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Novel", "price": 15.99, "stock": 10},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian", "price": 12.50, "stock": 8},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Classic", "price": 14.00, "stock": 5},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy", "price": 18.75, "stock": 7},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "category": "History", "price": 20.00, "stock": 6}
]

sales = []

# Utility functions
def input_positive_number(prompt, is_float=False):
    while True:
        try:
            value = input(prompt)
            if is_float:
                value = float(value)
            else:
                value = int(value)
            if value <= 0:
                print("Value must be positive.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please try again.")

def input_non_empty(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("This field is required.")
        else:
            return value.strip()

def find_product(title):
    for product in products:
        if product["title"].lower() == title.lower():
            return product
    return None

def print_product(product):
    print(f"Title: {product['title']}, Author: {product['author']}, Category: {product['category']}, Price: ${product['price']:.2f}, Stock: {product['stock']}")

def print_sale(sale):
    print(f"Client: {sale['client']}, Product: {sale['product_title']}, Quantity: {sale['quantity']}, Date: {sale['date']}, Discount: {sale['discount']}%")

# Inventory management
def add_product():
    print("\n--- Add Product ---")
    title = input_non_empty("Title: ")
    if find_product(title):
        print("Product already exists.")
        return
    author = input_non_empty("Author: ")
    category = input_non_empty("Category: ")
    price = input_positive_number("Price: ", is_float=True)
    stock = input_positive_number("Stock: ")
    product = {"title": title, "author": author, "category": category, "price": price, "stock": stock}
    products.append(product)
    print("Product added successfully.")

def update_product():
    print("\n--- Update Product ---")
    title = input_non_empty("Enter product title to update: ")
    product = find_product(title)
    if not product:
        print("Product not found.")
        return
    print("Leave field empty to keep current value.")
    new_author = input("New author: ")
    new_category = input("New category: ")
    new_price = input("New price: ")
    new_stock = input("New stock: ")
    if new_author.strip():
        product["author"] = new_author.strip()
    if new_category.strip():
        product["category"] = new_category.strip()
    if new_price.strip():
        try:
            price = float(new_price)
            if price > 0:
                product["price"] = price
            else:
                print("Price must be positive. Keeping previous value.")
        except ValueError:
            print("Invalid price. Keeping previous value.")
    if new_stock.strip():
        try:
            stock = int(new_stock)
            if stock >= 0:
                product["stock"] = stock
            else:
                print("Stock must be non-negative. Keeping previous value.")
        except ValueError:
            print("Invalid stock. Keeping previous value.")
    print("Product updated.")

def delete_product():
    print("\n--- Delete Product ---")
    title = input_non_empty("Enter product title to delete: ")
    product = find_product(title)
    if not product:
        print("Product not found.")
        return
    products.remove(product)
    print("Product deleted.")

def list_products():
    print("\n--- Product List ---")
    if not products:
        print("No products available.")
        return
    for product in products:
        print_product(product)

# Sales management
def register_sale():
    print("\n--- Register Sale ---")
    client = input_non_empty("Client name: ")
    title = input_non_empty("Product title: ")
    product = find_product(title)
    if not product:
        print("Product not found.")
        return
    if product["stock"] == 0:
        print("No stock available for this product.")
        return
    quantity = input_positive_number("Quantity: ")
    if quantity > product["stock"]:
        print("Insufficient stock.")
        return
    discount = input_positive_number("Discount percentage (0 if none): ", is_float=True)
    if discount < 0 or discount > 100:
        print("Discount must be between 0 and 100.")
        return
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sale = {
        "client": client,
        "product_title": product["title"],
        "quantity": quantity,
        "date": date,
        "discount": discount
    }
    sales.append(sale)
    product["stock"] -= quantity
    print("Sale registered successfully.")

def list_sales():
    print("\n--- Sales List ---")
    if not sales:
        print("No sales registered.")
        return
    for sale in sales:
        print_sale(sale)

# Reports
def top_3_products():
    print("\n--- Top 3 Best-Selling Products ---")
    if not sales:
        print("No sales data available.")
        return
    sales_count = {}
    for sale in sales:
        title = sale["product_title"]
        sales_count[title] = sales_count.get(title, 0) + sale["quantity"]
    top3 = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)[:3]
    for i, (title, qty) in enumerate(top3, 1):
        print(f"{i}. {title} - {qty} sold")

def sales_by_author():
    print("\n--- Sales by Author ---")
    if not sales:
        print("No sales data available.")
        return
    author_sales = {}
    for sale in sales:
        product = find_product(sale["product_title"])
        if product:
            author = product["author"]
            author_sales[author] = author_sales.get(author, 0) + sale["quantity"]
    for author, qty in author_sales.items():
        print(f"Author: {author}, Total sold: {qty}")

def income_report():
    print("\n--- Income Report ---")
    if not sales:
        print("No sales data available.")
        return
    gross_income = sum(
        sale["quantity"] * find_product(sale["product_title"])["price"]
        for sale in sales
    )
    net_income = sum(
        sale["quantity"] * find_product(sale["product_title"])["price"] * (1 - sale["discount"] / 100)
        for sale in sales
    )
    print(f"Gross income (without discount): ${gross_income:.2f}")
    print(f"Net income (with discount): ${net_income:.2f}")

# Main menu
def main_menu():
    while True:
        print("\n--- Bookstore Management System ---")
        print("1. Product management")
        print("2. Register sale")
        print("3. Sales list")
        print("4. Reports")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            product_menu()
        elif choice == "2":
            register_sale()
        elif choice == "3":
            list_sales()
        elif choice == "4":
            report_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def product_menu():
    while True:
        print("\n--- Product Management ---")
        print("1. Add product")
        print("2. Update product")
        print("3. Delete product")
        print("4. List products")
        print("5. Back to main menu")
        choice = input("Choose an option: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            list_products()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

def report_menu():
    while True:
        print("\n--- Reports ---")
        print("1. Top 3 best-selling products")
        print("2. Sales by author")
        print("3. Income report")
        print("4. Back to main menu")
        choice = input("Choose an option: ")
        if choice == "1":
            top_3_products()
        elif choice == "2":
            sales_by_author()
        elif choice == "3":
            income_report()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

# Entry point
if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")