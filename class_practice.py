# 1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print("Restaurant is opening")
        

my_restaurant = Restaurant("KFC", "Fast Food")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("=" * 60)
# 2

class Restaurant2:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print("Restaurant is opening")
        
    def set_number_served(self, number_served:int):
        self.number_served = number_served
    
    def increment_number_served(self, increment_number:int):
        self.number_served += increment_number


my_restaurant = Restaurant2("KFC", "Fast Food")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(200)
my_restaurant.increment_number_served(20)
print(f"Number of dinners: {my_restaurant.number_served}")

print("=" * 60)
# 3 Inheritance
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, "Dessert")
        self.flavors = flavors
    
    def show_flavors(self):
        print(self.flavors)


my_restaurant_2 = IceCreamStand("ice", ["banana", "strawberry"])
my_restaurant_2.describe_restaurant()
my_restaurant_2.open_restaurant()
my_restaurant_2.show_flavors()    

