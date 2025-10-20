import random
class CoffeeOrder:
    def __init__(self, customer_name, drink_type, size):
        self.order_number = random.randint(1, 100)
        self.customer_name = customer_name
        self.drink_type = drink_type
        self.size = size
        self.__price = 0.0  # private attribute (encapsulated)
    
    # Public method
    def get_order_summary(self):
        self.__price = self.__calculate_price()
        return (f"\nOrder #{self.order_number}\ncustomer: {self.customer_name}\ndrink: {self.drink_type}\nsize: {self.size}\nprice: R{self.__price}")
        
    # Private method (encapsulated)
    def __calculate_price(self):
        price = 0
        if self.drink_type == "coffee":
            price = 6
        else:
            price = 4
        
        if self.size == "lg":
            price += 3
        elif self.size == "md":
            price += 2
        
        return price
    
    # Public Method to safely access the price
    def get_price(self):
        return self.__calculate_price()
    
    # Private method (encapsulated)
    def __process_order(self):
        return f"processing order #{self.order_number}..."

    def submit_order(self):
        print(f"\nOrder placed by {self.customer_name}")
        return self.__process_order()
    

# create an Order
order = CoffeeOrder("Simon", "tea", "md")

# Use abstraction to get the order summary
order_summary = order.get_order_summary()
print(order_summary)

# Use abstraction to submit order
print(order.submit_order()) 