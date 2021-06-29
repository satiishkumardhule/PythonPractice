'''Factory Design Pattern Example'''

class Dog:
    '''This is dog class'''

    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Woof!")


class Cat:
    '''This is cat class'''

    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Meew!")


def get_pet(pet="dog"):
    '''Tis method returs pet object '''
    pets = dict(dog = Dog("hope"), cat = Cat("Silence"))

    return pets[pet]

d = get_pet("dog")
d.speak()

d = get_pet("cat")
d.speak()