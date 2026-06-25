from tools import get_order, search_products, get_product
 
passed = 0
failed = 0
 
def test(name, condition):
    global passed, failed
    if condition:
        print(f"  ✅ PASS — {name}")
        passed += 1
    else:
        print(f"  ❌ FAIL — {name}")
        failed += 1
 
# ════════════════════════════════════════════════
print("\n" + "="*50)
print("1. get_order TESTS")
print("="*50)
 
# Valid orders
result = get_order("ORD-1001")
test("Valid order ORD-1001 found",           "id" in result)
test("Status field present",                  "status" in result)
test("Product ID field present",              "product_id" in result)
test("Correct status — Delivered",            result.get("status") == "Delivered")
 
result = get_order("ORD-1002")
test("Valid order ORD-1002 found",            "id" in result)
test("ETA present for out-of-delivery order", "eta" in result)
 
# Lowercase order ID
result = get_order("ord-1001")
test("Lowercase order ID works",              "id" in result)
 
# Invalid orders
result = get_order("ORD-9999")
test("Invalid order returns error",           "error" in result)
 
result = get_order("")
test("Empty order ID returns error",          "error" in result)
 
result = get_order("RANDOM-123")
test("Random string returns error",           "error" in result)
 
 
# ════════════════════════════════════════════════
print("\n" + "="*50)
print("2. search_products TESTS")
print("="*50)
 
# Valid searches
result = search_products("shoes")
test("Search 'shoes' returns results",        "results" in result)
test("Multiple shoes found",                  len(result.get("results", [])) >= 2)
 
result = search_products("Nike")
test("Search by brand 'Nike' works",          "results" in result)
test("Nike product found",                    any(p["brand"] == "Nike" for p in result.get("results", [])))
 
result = search_products("electronics")
test("Search by category works",              "results" in result)
 
result = search_products("Sony WH-1000XM5")
test("Search by full product name works",     "results" in result)
 
# Price filter
result = search_products("shoes", max_price=5000)
test("Price filter works",                    all(p["price"] < 5000 for p in result.get("results", [])))
 
result = search_products("shoes", max_price=1000)
test("Price filter — no results handled",     "empty" in result or "results" in result)
 
# Empty search
result = search_products("xyzabc99999")
test("No results handled gracefully",         "empty" in result)
 
# Case insensitive
result = search_products("NIKE")
test("Case insensitive search works",         "results" in result)
 
 
# ════════════════════════════════════════════════
print("\n" + "="*50)
print("3. get_product TESTS")
print("="*50)
 
# Valid products
result = get_product("P-101")
test("Valid product P-101 found",             "id" in result)
test("Name field present",                    "name" in result)
test("Price field present",                   "price" in result)
test("Correct product name",                  result.get("name") == "Nike Air Max 270")
test("Reviews field present",                 "reviews" in result)
test("Features field present",                "features" in result)
test("Warranty field present",                "warranty" in result)
test("Return policy field present",           "return_policy" in result)
 
result = get_product("P-301")
test("Sony headphones found",                 result.get("name") == "Sony WH-1000XM5 Headphones")
 
# Invalid products
result = get_product("P-999")
test("Invalid product returns error",         "error" in result)
 
result = get_product("")
test("Empty product ID returns error",        "error" in result)
 
result = get_product("RANDOM")
test("Random string returns error",           "error" in result)
 
 
# ════════════════════════════════════════════════
print("\n" + "="*50)
print("4. EDGE CASE TESTS")
print("="*50)
 
# Order + Product link
order = get_order("ORD-1001")
product_id = order.get("product_id")
product = get_product(product_id)
test("Order links correctly to product",      product.get("name") == "Nike Air Max 270")
 
# Search then get product
search_result = search_products("Puma")
first_product = search_result["results"][0]
product = get_product(first_product["id"])
test("Search result ID valid for get_product", "name" in product)
 
# Cheaper alternatives exist
expensive = get_product("P-101")  # Nike ₹8999
cheaper = search_products("shoes", max_price=expensive["price"])
test("Cheaper alternatives found for Nike",   len(cheaper.get("results", [])) > 0)
 
# All orders have valid product IDs
from Database import ORDERS, PRODUCTS
all_valid = all(order["product_id"] in PRODUCTS for order in ORDERS.values())
test("All orders have valid product IDs",     all_valid)
 
# All products have required fields
required_fields = ["id", "name", "price", "category", "brand", "rating",
                   "reviews", "features", "warranty", "return_policy"]
all_have_fields = all(
    all(field in product for field in required_fields)
    for product in PRODUCTS.values()
)
test("All products have required fields",     all_have_fields)
 
 
# ════════════════════════════════════════════════
print("\n" + "="*50)
print(f"RESULTS: {passed} passed, {failed} failed")
if failed == 0:
    print("ALL TESTS PASSED ✅")
else:
    print(f"{failed} TEST(S) FAILED ❌")
print("="*50 + "\n")