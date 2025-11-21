# Base class Vehicle
class Vehicle:
    def __init__(self, vehicle_id: str, base_rate: float):
        self._vehicle_id = vehicle_id   # protected attribute
        self._base_rate = base_rate     # protected attribute

    def display_details(self):
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate:.2f}"

    def rental_charge(self):
        # Placeholder method to be overridden
        return 0.0


# Subclass Car
class Car(Vehicle):
    def __init__(self, vehicle_id: str, base_rate: float, num_seats: int):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self):
        # Daily rental charge = base_rate * num_seats
        return self._base_rate * self.num_seats


# Subclass Bike
class Bike(Vehicle):
    def __init__(self, vehicle_id: str, base_rate: float, bike_type: str):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        # Daily rental charge = base_rate * 0.5
        return self._base_rate * 0.5


# Polymorphic function
def calculate_rental(vehicle: Vehicle):
    return vehicle.rental_charge()


# Demonstration
if __name__ == "__main__":
    car1 = Car("CAR001", 100.0, 4)       # Sedan with 4 seats
    bike1 = Bike("BIKE001", 80.0, "Scooter")

    print(car1.display_details())        # Vehicle ID: CAR001, Base Rate: 100.00
    print("Car Rental Charge:", calculate_rental(car1))   # 400.0

    print(bike1.display_details())       # Vehicle ID: BIKE001, Base Rate: 80.00
    print("Bike Rental Charge:", calculate_rental(bike1)) # 40.0
