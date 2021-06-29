'''Factory Design Pattern Example'''

class Dog:
    '''This is dog class'''

    def __init__(self,name):
        self.name=name

    def speak(self):
        return "Woof!"


class DogFactory:
    '''Dog factory oncreate class'''

    def get_pet(self) -> Dog:
        return Dog("Hope")

    def get_food(self) -> str:
        return "Dog Food"

class PetStore:
    '''petstore houses our abstract factory'''

    def __init__(self,pet_factory=None) -> None:
        self._pet_factory = pet_factory

    def show_pet(self) -> None:
        pet = self._pet_factory.get_pet()
        food = self._pet_factory.get_food()

        print(f"PET: {pet.name}, SPEAKS: {pet.speak()}, FOOD: {food}")

factory = DogFactory()
shop = PetStore(factory)

shop.show_pet()