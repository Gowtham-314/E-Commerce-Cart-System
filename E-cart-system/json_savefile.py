import json
from datetime import datetime

def save_cart(cart, username, filename=f"cart_history-{datetime.now().strftime('%d-%m-%Y')}.json"):
    data = {
        "user": {
            "name": username,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "cart": [],
        "grand_total": 0
    }

    total = 0
    for item in cart:
        item_total = item[1] * item[2]
        total += item_total

        data["cart"].append({
            "item_name": item[0],
            "quantity": item[1],
            "price": item[2],
            "total": item_total
        })

    data["grand_total"] = total

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)