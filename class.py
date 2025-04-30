# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand                
        self._model = model               
        self.__storage = storage          

    def phone_info(self):
        return f"{self.brand} {self._model} with {self.__storage}GB storage"

    def perform_task(self):
        return f"{self.brand} {self._model} is performing a general task."


# Subclass
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    # Polymorphism: overriding method from base class
    def perform_task(self):
        return f"{self.brand} {self._model} is running a high-end game using {self.gpu} GPU!"


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy A52", 128)
phone2 = GamingPhone("Asus", "ROG Phone 6", 256, "Adreno 730")

# Using methods
print(phone1.phone_info())
print(phone1.perform_task())

print(phone2.phone_info())
print(phone2.perform_task())
