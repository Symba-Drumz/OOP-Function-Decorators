APPROVED_CAT_BREEDS = [
    "Siamese",
    "Persian",
    "Maine Coon",
    "Ragdoll",
    "British Shorthair",
    "Sphynx",
    "Bengal",
    "Abyssinian",
    "Scottish Fold",
    "Russian Blue",
    "Birman",
    "American Shorthair"
]

class Cat:
    def __init__(self, name="Stixx", age=6, breed="Russian Blue"):
        self.name = name
        self.age = age
        self.breed = breed

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 20:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 20 characters long.")   

    @name.deleter
    def name(self):
        print("Resetting name to default (Stixx)...")   
        self._name = "Stixx"

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 0 <= age <= 30:
            self._age = age
        else:
            raise ValueError("Age must be an integer between 0 and 30.")
        
    @age.deleter
    def age(self):
        print("Resetting age to default (6)...")
        self._age = 6

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if isinstance(breed, str) and breed in APPROVED_CAT_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be a string from the approved list.")
        
    @breed.deleter
    def breed(self):
        print("Resetting breed to default (Russian Blue)...")
        self._breed = "Russian Blue"

def __str__(self):
    return f"Cat(name='{self.name}', age={self.age}, breed='{self.breed}')"
my_cat = Cat()    
print(my_cat.name)
print(my_cat.age)
print(my_cat.breed)
print(my_cat)