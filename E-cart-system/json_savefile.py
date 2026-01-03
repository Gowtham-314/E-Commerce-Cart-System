from datetime import datetime
import json

def save_cart(cart_items):
    data = []
    for item in cart_items:
        data.append({
            "item_name": item[0],
            "quantity": item[1],
            "price": item[2]
        })
        
    data[datetime.now().strftime('%Y-%m-%d')] = data

    with open(f"cart_history-{datetime.now().strftime('%Y-%m-%d')}.json","w") as f:
        json.dump(datetime.now().strftime('%H:%M:%S')+data, f, indent=4)
        
cart=[]
save_cart(cart)

