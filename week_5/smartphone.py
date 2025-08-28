class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self._brand = brand  # Encapsulated attribute
        self._model = model
        self._storage = storage  # in GB
        self._battery_capacity = battery_capacity  # in mAh
        self._battery_level = 100  # Encapsulated with default value
        self._is_on = False  # Encapsulated with default value

    def power_on(self):
        if self._battery_level > 5:
            self._is_on = True
            return f"{self.get_full_name()} is now powered on. Battery: {self._battery_level}%"
        return "Battery too low to power on. Please charge first."

    def power_off(self):
        self._is_on = False
        return f"{self.get_full_name()} is now powered off."

    def make_call(self, number):
        if not self._is_on:
            return "Cannot make call. Phone is off."
        if self._battery_level < 3:
            return "Battery too low to make call."
        
        self._battery_level -= 2
        return f"Calling {number}... Battery remaining: {self._battery_level}%"

    def use_app(self, app_name, duration_minutes):
        if not self._is_on:
            return "Cannot use app. Phone is off."
        
        battery_drain = duration_minutes * 0.5
        if self._battery_level < battery_drain:
            return "Battery too low to use app."
        
        self._battery_level -= battery_drain
        return f"Used {app_name} for {duration_minutes} minutes. Battery remaining: {self._battery_level}%"

    def charge(self, minutes):
        charge_amount = minutes * 0.8
        self._battery_level = min(100, self._battery_level + charge_amount)
        return f"Charged for {minutes} minutes. Battery level: {self._battery_level}%"

    def get_full_name(self):
        return f"{self._brand} {self._model}"

    def get_storage_info(self):
        return f"{self._storage}GB storage"

    # Encapsulation: Getter methods for protected attributes
    def get_battery_level(self):
        return self._battery_level

    def is_powered_on(self):
        return self._is_on


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, gpu_model, cooling_system):
        super().__init__(brand, model, storage, battery_capacity)
        self._gpu_model = gpu_model
        self._cooling_system = cooling_system
        self._gaming_mode = False

    def enable_gaming_mode(self):
        self._gaming_mode = True
        return "Gaming mode enabled. Performance boosted!"

    def disable_gaming_mode(self):
        self._gaming_mode = False
        return "Gaming mode disabled."

    def play_game(self, game_name, duration_minutes):
        if not self._is_on:
            return "Cannot play game. Phone is off."
        
        # Gaming mode affects battery drain rate
        battery_drain_per_minute = 1.2 if self._gaming_mode else 0.8
        battery_drain = duration_minutes * battery_drain_per_minute
        
        if self._battery_level < battery_drain:
            return "Battery too low to play game."
        
        self._battery_level -= battery_drain
        mode_status = "with gaming mode" if self._gaming_mode else "without gaming mode"
        return f"Played {game_name} for {duration_minutes} minutes {mode_status}. Battery remaining: {self._battery_level}%"

    def get_gaming_specs(self):
        return f"GPU: {self._gpu_model}, Cooling: {self._cooling_system}"


# Demonstration
if __name__ == "__main__":
    print("=== Activity 1: Smartphone Class with Inheritance ===\n")
    
    # Create a regular smartphone
    my_phone = Smartphone("Apple", "iPhone 15", 128, 4000)
    print(my_phone.power_on())
    print(my_phone.make_call("555-1234"))
    print(my_phone.use_app("Instagram", 30))
    print(my_phone.charge(20))
    print(my_phone.get_storage_info())
    print(my_phone.power_off())
    
    print("\n" + "="*50 + "\n")
    
    # Create a gaming smartphone
    gaming_phone = GamingSmartphone("ASUS", "ROG Phone 7", 512, 6000, "Adreno 740", "Vapor Chamber Cooling")
    print(gaming_phone.power_on())
    print(gaming_phone.enable_gaming_mode())
    print(gaming_phone.play_game("Genshin Impact", 45))
    print(gaming_phone.get_gaming_specs())
    print(gaming_phone.get_storage_info())
    print(gaming_phone.power_off())