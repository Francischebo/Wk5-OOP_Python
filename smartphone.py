# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        # Private attributes (encapsulation)
        self._brand = brand
        self._model = model
        self._battery_life = battery_life  # in hours

    # Method to display smartphone details
    def display_info(self):
        print(f"Brand: {self._brand}, Model: {self._model}, Battery Life: {self._battery_life} hours")

    # Method to simulate calling
    def make_call(self, number):
        print(f"Calling {number} from {self._brand} {self._model}...")

# Derived class: GamingPhone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system  # Specific attribute for GamingPhone

    # Overriding the display_info method (polymorphism)
    def display_info(self):
        super().display_info()
        print(f"Cooling System: {self.cooling_system}")

    # New method specific to GamingPhone
    def launch_game(self, game_name):
        print(f"Launching {game_name} with enhanced cooling on {self._brand} {self._model}...")

# Example usage
phone1 = Smartphone("Apple", "iPhone 14", 18)
phone1.display_info()
phone1.make_call("123-456-7890")

gaming_phone = GamingPhone("Asus", "ROG Phone 6", 20, "Vapor Chamber")
gaming_phone.display_info()
gaming_phone.launch_game("PUBG Mobile")
