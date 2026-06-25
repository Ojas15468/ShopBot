from Database import ORDERS, PRODUCTS

def get_order(order_id: str) -> dict:
    order = ORDERS.get(order_id.upper())  # Change the order_id to uppercase to match the keys in ORDER dictionary
    
    if not order:
        return {"error": f"Order '{order_id}' Not Found!"}
    
    return order


def search_products(query: str, max_price: int = None) -> dict:
    words = query.lower().split()
    
    results = [
        product
        for product in PRODUCTS.values()
        if any(
            word in product["name"].lower() or
            word in product["category"].lower() or
            word in product["brand"].lower()
            for word in words
        )
    ]
    
    # Price filter — agar max_price diya ho
    if max_price:
        results = [p for p in results if p["price"] < max_price]
    
    # Price se sort karo — sabse sasta pehle
    results = sorted(results, key=lambda p: p["price"])
    
    if not results:
        return {"empty": True, "message": f"No products found for '{query}'"}
    
    return {"results": results}


def get_product(product_id: str) -> dict:
    product = PRODUCTS.get(product_id)
    
    if not product:
        return {"error": f"Product '{product_id}' Not Found!"}
    
    return product



if __name__ == "__main__":
    print(get_order("ORD-1001"))
    print(get_order("ORD-9999"))   
    print(search_products("shoes"))
    print(get_product("P-101"))