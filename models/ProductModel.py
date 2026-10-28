from models.Product import Product

class ProductModel:
    products = [
        Product("Apple", "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=800&q=85", 10, 4.5),
        Product("Banana", "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=800&q=85", 15, 4.8),
        Product("Orange", "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&w=800&q=85", 12, 4.2 )
    ]

    @staticmethod
    def get_all_products():
        return ProductModel.products

    @staticmethod
    def get_product_by_id(id):
        if 0 <= id < len(ProductModel.products):
            return ProductModel.products[id]
        return None

    @staticmethod
    def create_product(product):
        ProductModel.products.append(product)