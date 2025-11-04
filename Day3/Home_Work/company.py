import logging
from product import Product
from db_config import session

class Company:

    def add_product(self, product):
        existing = session.query(Product).filter_by(id=product.id).first()
        if existing:
            logging.warning(f"Attempted to add duplicate product with ID: {product.id}")
            print(f"Product with ID {product.id} already exists.")
            return
        session.add(product)
        session.commit()
        logging.info(f"Added product: {product}")
        print("Product added successfully.")

    def search_product(self, product_id):
        product = session.query(Product).filter_by(id=product_id).first()
        if product:
            logging.info(f"Found product: {product}")
        else:
            logging.warning(f"Product not found with ID: {product_id}")
        return product

    def update_product(self, product_id, price=None, stock=None):
        product = self.search_product(product_id)
        if not product:
            logging.warning(f"Product not found for update: ID {product_id}")
            print("Product not found.")
            return
        if price is not None:
            old_price = product.price
            product.price = price
            logging.info(f"Updated product ID {product_id} price from {old_price} to {price}")
        if stock is not None:
            old_stock = product.stock
            product.stock = stock
            logging.info(f"Updated product ID {product_id} stock from {old_stock} to {stock}")
        session.commit()
        print("Product updated successfully.")

    def delete_product(self, product_id):
        product = self.search_product(product_id)
        if product:
            session.delete(product)
            session.commit()
            logging.info(f"Deleted product: {product}")
            print("Product deleted successfully.")
        else:
            logging.warning(f"Product not found for deletion: ID {product_id}")
            print("Product not found.")

    def display_all(self):
        products = session.query(Product).all()
        if not products:
            print("Product database is empty.")
            logging.info("Displayed all products: None found")
        else:
            print("Product List:\n")
            for p in products:
                print(p)
            logging.info(f"Displayed all products: total {len(products)}")
