class Director:
    def __init__(self,builder) -> None:
        self._builder = builder

    def construct_car(self) -> None:
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tyre()
        self._builder.add_engine()


    def get_car(self) -> object:
        return self._builder.car

class Builder:
    def __init__(self) -> None:
        self.car = None

    def create_new_car(self):
        self.car = Car()

class Car:
    def __init__(self) -> None:
        self.model = None
        self.engine = None
        self.tyre = None

    def __str__(self) -> str:
        return f"{self.model},{self.engine},{self.tyre}"

class SkylarkBuilder(Builder):
    def add_model(self) -> None:
        self.car.model = "SkyLark"

    def add_tyre(self) -> None:
        self.car.tyre = "Regular Tyre"

    def add_engine(self) -> None:
        self.car.engine = "Turbo Engine"

builder = SkylarkBuilder()
director = Director(builder)

director.construct_car()

car = director.get_car()

print(car)