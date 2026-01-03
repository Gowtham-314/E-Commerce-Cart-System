from termcolor import colored
from datetime import datetime
from json_savefile import save_cart

class user:
    def __init__(self,name):
        if not name.strip():
            self.name = "Guest User"
        else:
            self.name = name.capitalize()
            
class item():
        
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        
class CartSys:
    
    def __init__(self):
        self.cart = []
        
    def add_item(self, item_name, quantity, price):
        new_item = item(item_name, quantity, price)
        self.cart.append(new_item)
        save_cart(self.cart)
        
    def total_price(self):
        total_sum = sum(item.quantity * item.price for item in self.cart)
        return total_sum
        
        
    def view_cart(self):
        
        print("\n","-"*60,colored("\nViewing the Items in the Cart:\n", "blue"),'-'*40)
        print(f"{'Product':<20} {'Qty':<5} {'Price':<10}\n","-" * 40)
        
        for item in self.cart: 
            print(f"{item.item_name:<20} {item.quantity:<5} ₹{item.price:.2f}\n")
            
        print("-" * 60,colored("\nCalculating the Total Price of the Items in the Cart:", "yellow"))
        print(f"\nTotal Price: ₹ {self.total_price()}\n","-"*60)
        
    
    def cart_print(self, user_name):
        
        print("-"*60,colored("\nPrinting the Cart Details:", "magenta"))
        
        with open(f"cart_details_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt","w",encoding="utf-8") as f:
            
            f.write("="*35+"\n")
            f.write(f"|{" "*8}E-COMMERCE RECEIPT{" "*7}|\n")
            f.write("="*35+"\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"User: {user_name}\n")
            f.write("-"*35+"\n")
            f.write(f"{'Product':<20} {'Qty':<5} {'Price':<10}\n")
            f.write("-"*35+"\n")
            
            for item in self.cart:
                f.write(f"{item.item_name:<20} {item.quantity:<5} ₹{item.price:<10}\n")
            
            f.write("="*35+"\n")
            f.write(f"GRAND TOTAL:    ₹{self.total_price():.2f}\n")
            f.write("="*35)
            
        print(colored("Cart details have been printed Successfully to the file.","green"),"\n","-"*60)
        
        