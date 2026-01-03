from datetime import datetime
import json

    

def save_cart(cart_items):
    data = []
    for item in cart_items:
        data.append({
            "item_name": item.item_name,
            "quantity": item.quantity,
            "price": item.price
        })

    with open(f"Json_File_{datetime.now().strftime('%Y%m%d%H%M%S')}.json","w",encoding="utf-8") as f:
        json.dump(data, f, indent=4)

