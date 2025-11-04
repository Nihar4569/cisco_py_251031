import logging
from product import Product
from company import Company

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def main():
    cmp = Company()
    while True:
        print("==========Ecommerce Product Management===========")
        print("1. Add Product")
        print("2. Search Product")
        print("3. Update Product Price/Stock")
        print("4. Delete Product")
        print("5. Display All Products")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                id = int(input("Enter Product ID: "))
                name = input("Enter Name: ")
                desc = input("Enter Description: ")
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock Quantity: "))
                tags = input("Enter Tags (comma separated): ")
                product = Product(id=id, name=name, description=desc, price=price, stock=stock, tags=tags)
                cmp.add_product(product)

            case 2:
                id = int(input("Enter Product ID to search: "))
                product = cmp.search_product(id)
                if product:
                    print("Product found:\n", product)
                else:
                    print("Product not found.")

            case 3:
                id = int(input("Enter Product ID to update: "))
                price = input("Enter new Price (or leave blank): ")
                stock = input("Enter new Stock (or leave blank): ")
                price_val = float(price) if price else None
                stock_val = int(stock) if stock else None
                cmp.update_product(id, price=price_val, stock=stock_val)

            case 4:
                id = int(input("Enter Product ID to delete: "))
                cmp.delete_product(id)

            case 5:
                cmp.display_all()

            case 6:
                print("Thank you for using the Ecommerce Product Management System")
                break

            case _:
                print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
