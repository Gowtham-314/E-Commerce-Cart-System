""""<!--- E-Commerce Cart System
    This program allows users to add items to a shopping cart, view the cart contents,
    Systemed by Kruthik BT , Gowtham Gowda  C B , Akash B V , Rohith S J
    @Coding_group--->"""
    
    
from termcolor import colored
from models import user, CartSys
from json_savefile import save_cart

def E_cart_system():    
    
    cart_obj = CartSys()
    user_obj=user(input("\nEnter your Name, (Press Enter ↩ to Guest User) : "))
    print("\n","-"*60,colored(f"\n|{" "*18}E-Commerce Cart System {" "*18}|\n", "red", attrs=["bold"]),"-"*60)
    print("\n","-"*60,colored(f"\nWelcome to E-Commerce Cart System ⫸\n{colored(user_obj.name, 'red', attrs=['bold'])}!", "cyan", attrs=["bold"]),"\n","-"*60)

    while True:
        
        print(colored("\nChoice the Actions to perform:", "green", attrs=["bold"]))
        print(colored('''1. Add Item to Cart\n2. View Cart Items\n3. Print Cart Details\n4. Exit''', "green"))
        
        try:
            choice = int(input(colored("Enter your choice: ", "cyan")))
            if not choice in [1,2,3,4]:
                print(colored("Invalid choice. Please try again.", "red"),"\n","-"*60)
                continue
        except ValueError:
            print(colored("Invalid input. Please enter a number between 1 and 4.", "red"),"\n","-"*60)
            continue
        
        
        match choice:
            
            case 1:
            
                try:
                    no_items = int(input("\nEnter the No. of items to add: "))
                    for _ in range(no_items):
                        try:
                            items, qty, rate = input("Enter item Name, Quantity and Price (Separated by Commas): ").split(',')
                            qty = int(qty)
                            rate = float(rate)

                            if qty <= 0 or rate <= 0:
                                raise ValueError
                            
                        except ValueError:
                            print(colored("Invalid item details. Quantity and price must be positive numbers. Enter in the correct format.","red"),"\n","-"*60)
                            continue
                            
                        cart_obj.add_item(items, qty, rate)      
                except ValueError:
                    print(colored("Invalid input. Please enter the valid number of items.", "red"),"\n","-"*60)
                    continue
                    
            case 2:
                if cart_obj.cart:
                    cart_obj.view_cart()
                else:
                    print(colored("Your cart is empty. Please Choice 1 to add Items.", "red", attrs=["bold"]))
                    continue
            case 3:
                if cart_obj.cart:
                    cart_obj.cart_print(user_obj.name)
                    save_cart(cart_obj.cart)
                else:
                    print(colored("Your cart is empty. Please Choice 1 to add Items.", "red", attrs=["bold"]))
                    continue
            case 4:
                if cart_obj.cart:
                    save_cart(cart_obj.cart)
                    print(colored("Your cart has been saved to a JSON file before exiting.", "yellow", attrs=["bold"]))
                print(colored("\nExiting the E-Commerce Cart System. Thank you!", "red", attrs=["bold"]))    
                break
                    
            case _:
                print(colored("Invalid choice. Please try again.", "red"),"\n","-"*60)
    

if __name__ == "__main__":
    E_cart_system()