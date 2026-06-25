USERS = {
    "9876543210": {
        "id": "user001",
        "name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "phone": "9876543210",
        "orders": ["ORD-1001", "ORD-1003"]
    },
    "9123456789": {
        "id": "user002",
        "name": "Priya Singh",
        "email": "priya@gmail.com",
        "phone": "9123456789",
        "orders": ["ORD-1002"]
    },
    "9999900000": {
        "id": "user003",
        "name": "Amit Kumar",
        "email": "amit@gmail.com",
        "phone": "9999900000",
        "orders": ["ORD-1004", "ORD-1005"]
    }
}
 
ORDERS = {
    "ORD-1001": {
        "id": "ORD-1001",
        "status": "Delivered",
        "product_id": "P-101",
        "date": "2025-06-15",
        "address": "Jaipur, Rajasthan"
    },
    "ORD-1002": {
        "id": "ORD-1002",
        "status": "Out for Delivery",
        "product_id": "P-201",
        "date": "2025-06-22",
        "address": "Mumbai, Maharashtra",
        "eta": "Today by 8 PM"
    },
    "ORD-1003": {
        "id": "ORD-1003",
        "status": "Processing",
        "product_id": "P-301",
        "date": "2025-06-23",
        "address": "Jaipur, Rajasthan"
    },
    "ORD-1004": {
        "id": "ORD-1004",
        "status": "Shipped",
        "product_id": "P-501",
        "date": "2025-06-20",
        "address": "Delhi, NCR",
        "eta": "Tomorrow by 6 PM"
    },
    "ORD-1005": {
        "id": "ORD-1005",
        "status": "Delivered",
        "product_id": "P-402",
        "date": "2025-06-10",
        "address": "Delhi, NCR"
    }
}
 
PRODUCTS = {
    "P-101": {
        "id": "P-101",
        "name": "Nike Air Max 270",
        "category": "shoes",
        "price": 8999,
        "brand": "Nike",
        "rating": 4.5,
        "sizes": ["6", "7", "8", "9", "10", "11"],
        "colors": ["Black/White", "All Red", "Triple White"],
        "description": "Lightweight running shoe with Max Air cushioning for all-day comfort.",
        "in_stock": True,
        "warranty": "6 Months Manufacturer Warranty",
        "return_policy": "10 days easy return",
        "features": [
            "Max Air cushioning unit in heel",
            "Breathable mesh upper",
            "Rubber outsole for durability",
            "Lightweight foam midsole",
            "Padded collar for comfort"
        ],
        "reviews": [
            {"user": "Arjun M", "rating": 5, "comment": "Very comfortable for daily use!"},
            {"user": "Pooja S", "rating": 4, "comment": "Good quality but runs slightly small"},
            {"user": "Rahul T", "rating": 5, "comment": "Best Nike shoe in this price range"}
        ]
    },
    "P-201": {
        "id": "P-201",
        "name": "Adidas Ultraboost 22",
        "category": "shoes",
        "price": 12999,
        "brand": "Adidas",
        "rating": 4.3,
        "sizes": ["6", "7", "8", "9", "10"],
        "colors": ["Core Black", "Cloud White", "Navy Blue"],
        "description": "Premium running shoe with Boost midsole for incredible energy return.",
        "in_stock": True,
        "warranty": "6 Months Manufacturer Warranty",
        "return_policy": "10 days easy return",
        "features": [
            "Boost midsole for energy return",
            "Primeknit+ upper for adaptive fit",
            "Continental rubber outsole",
            "Linear Energy Push system",
            "Lightstrike midsole"
        ],
        "reviews": [
            {"user": "Sneha R", "rating": 5, "comment": "Amazing for long runs, super comfortable"},
            {"user": "Karan P", "rating": 4, "comment": "Great shoe but expensive"},
            {"user": "Meera T", "rating": 4, "comment": "Best running shoe I have owned"}
        ]
    },
    "P-301": {
        "id": "P-301",
        "name": "Sony WH-1000XM5 Headphones",
        "category": "electronics",
        "price": 24999,
        "brand": "Sony",
        "rating": 4.8,
        "colors": ["Black", "Silver"],
        "description": "Industry-leading noise cancelling headphones with 30hr battery life.",
        "in_stock": True,
        "warranty": "1 Year Manufacturer Warranty",
        "return_policy": "7 days easy return",
        "features": [
            "Industry-leading noise cancellation",
            "30 hour battery life",
            "Multipoint connection — connect 2 devices at once",
            "Quick charge — 3 mins = 3 hours playback",
            "Foldable lightweight design",
            "Crystal clear hands-free calling"
        ],
        "reviews": [
            {"user": "Rohit K", "rating": 5, "comment": "Best headphones I have ever used!"},
            {"user": "Sneha M", "rating": 5, "comment": "Noise cancellation is absolutely incredible"},
            {"user": "Vikram S", "rating": 4, "comment": "Great sound quality, a bit pricey"}
        ]
    },
    "P-401": {
        "id": "P-401",
        "name": "Puma Softride Enzo",
        "category": "shoes",
        "price": 3499,
        "brand": "Puma",
        "rating": 4.1,
        "sizes": ["6", "7", "8", "9", "10"],
        "colors": ["Black", "Grey", "Navy"],
        "description": "Everyday comfort shoe with SoftFoam+ sockliner for superior cushioning.",
        "in_stock": True,
        "warranty": "3 Months Manufacturer Warranty",
        "return_policy": "7 days easy return",
        "features": [
            "SoftFoam+ sockliner for cushioning",
            "Lightweight mesh upper",
            "Flexible rubber outsole",
            "Slip-on design for easy wear",
            "EVA midsole for comfort"
        ],
        "reviews": [
            {"user": "Amit S", "rating": 4, "comment": "Great value for money!"},
            {"user": "Riya K", "rating": 4, "comment": "Very comfortable for casual wear"},
            {"user": "Dev P", "rating": 5, "comment": "Best budget shoe, highly recommend"}
        ]
    },
    "P-402": {
        "id": "P-402",
        "name": "Skechers GoWalk 6",
        "category": "shoes",
        "price": 4299,
        "brand": "Skechers",
        "rating": 4.2,
        "sizes": ["6", "7", "8", "9", "10", "11"],
        "colors": ["Black", "White", "Grey"],
        "description": "Ultra-lightweight walking shoe with 5GEN cushioning technology.",
        "in_stock": True,
        "warranty": "3 Months Manufacturer Warranty",
        "return_policy": "10 days easy return",
        "features": [
            "5GEN cushioning technology",
            "Ultra-lightweight construction",
            "Air-cooled Goga Mat insole",
            "Washable design",
            "Slip-on style"
        ],
        "reviews": [
            {"user": "Sunita M", "rating": 5, "comment": "Perfect for long walks, no fatigue"},
            {"user": "Rajesh K", "rating": 4, "comment": "Very comfortable and lightweight"},
            {"user": "Priya L", "rating": 4, "comment": "Good quality for the price"}
        ]
    },
    "P-501": {
        "id": "P-501",
        "name": "boAt Rockerz 450",
        "category": "electronics",
        "price": 1499,
        "brand": "boAt",
        "rating": 4.0,
        "colors": ["Black", "Blue", "Red"],
        "description": "Wireless headphone with 15hr playback and powerful 40mm drivers.",
        "in_stock": True,
        "warranty": "1 Year Manufacturer Warranty",
        "return_policy": "7 days easy return",
        "features": [
            "40mm dynamic drivers for powerful bass",
            "15 hour battery life",
            "Foldable design",
            "Bluetooth 5.0",
            "Built-in microphone for calls"
        ],
        "reviews": [
            {"user": "Nikhil T", "rating": 4, "comment": "Great bass, amazing value for money"},
            {"user": "Anjali S", "rating": 4, "comment": "Good sound quality at this price"},
            {"user": "Varun M", "rating": 4, "comment": "Comfortable fit, good battery life"}
        ]
    },
    "P-502": {
        "id": "P-502",
        "name": "JBL Tune 510BT",
        "category": "electronics",
        "price": 2999,
        "brand": "JBL",
        "rating": 4.2,
        "colors": ["Black", "White", "Blue", "Pink"],
        "description": "Wireless on-ear headphones with 40hr battery and JBL Pure Bass sound.",
        "in_stock": True,
        "warranty": "1 Year Manufacturer Warranty",
        "return_policy": "7 days easy return",
        "features": [
            "JBL Pure Bass sound",
            "40 hour battery life",
            "Bluetooth 5.0 multipoint connection",
            "Foldable flat design",
            "Voice assistant compatible",
            "Speed charge — 5 mins = 2 hours"
        ],
        "reviews": [
            {"user": "Sanjay R", "rating": 4, "comment": "Excellent battery life and good sound"},
            {"user": "Kavya P", "rating": 5, "comment": "Best headphones under 3000!"},
            {"user": "Mohit L", "rating": 4, "comment": "JBL quality at affordable price"}
        ]
    }
}