# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, color, price, storage, battery_percentage):
        self.brand = brand
        self.model = model
        self.color = color
        self.__price = price
        self.storage = storage
        self.__battery_percentage = battery_percentage

    # Encapsulation: method to access and modify private price
    def get_price(self):
        return f"Price of {self.brand} {self.model}: ${self.__price}"

    # Encapsulation: method to access private battery percentage
    def get_battery_percentage(self):
        return self.__battery_percentage

    def charge(self, amount):
        """Charge the smartphone by a certain percentage."""
        if amount < 0:
            print("Charge amount cannot be negative.")
            return
        self.__battery_percentage += amount
        if self.__battery_percentage > 100:
            self.__battery_percentage = 100
        print(f"{self.brand} {self.model} is charged to {self.__battery_percentage}%.")

    def check_battery(self):
        """Check the current battery percentage."""
        print(f"Current battery level: {self.__battery_percentage}%")

    def display_info(self):
        """Display information about the smartphone."""
        print(f"{self.brand} {self.model} ({self.color})")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.color} - {self.storage}GB Storage"

# Derived class: SmartphoneWithCamera (demonstrating inheritance)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, color, price, storage, battery_percentage, camera_quality):
        super().__init__(brand, model, color, price, storage, battery_percentage)  # Inheriting from Smartphone class
        self.camera_quality = camera_quality

    # Overriding the display_info method to include camera quality
    def display_info(self):
        super().display_info()
        print(f"Camera Quality: {self.camera_quality} MP")

    # Overriding charge method to add a unique charging message for camera phones
    def charge(self, amount):
        print("Charging with special camera optimization...")
        super().charge(amount)

# Create instances of both classes
phone1 = Smartphone("Apple", "iPhone 13", "Blue", 999, 128, 50)
phone2 = SmartphoneWithCamera("Samsung", "Galaxy S23", "Black", 849, 256, 40, 108)

# Display info and demonstrate the methods
print(phone1)
phone1.display_info()
phone1.check_battery()
phone1.charge(30)
phone1.check_battery()
print(phone1.get_price())

print("\n")

print(phone2)
phone2.display_info()
phone2.charge(20)
phone2.check_battery()
print(phone2.get_price())
