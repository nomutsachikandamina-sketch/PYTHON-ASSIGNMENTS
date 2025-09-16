

Base class
class Vehicle:
    def describe(self):
        print("This is a vehicle.")

Subclass Car
class Car(Vehicle):
    def describe(self):
        print("This is a car. It has four wheels.")

Subclass Bike
class Bike(Vehicle):
    def describe(self):
        print("This is a bike. It has two wheels.")

Create objects
v = Vehicle()
c = Car()
b = Bike()

Call describe() method on each
v.describe()  # From base class
c.describe()  # Overridden in Car
b.describe()  # Overridden in bike

Question 2
A Python example that uses polymorphism to calculate the total area of different shapes (`Circle`, `Rectangle`) by defining a common interface through a base class:

import math

Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

Circle subclass
class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

Rectangle subclass
class Rectangle(Shape):
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width  self.height

Function to calculate total area
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

Example usage
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 8)
]

print("Total Area:", total_area(shapes))

Question 3

Base class
class Shape:
    def _init_(self):
        print("Shape initialized.")

    def calculate_area(self):
        # Base method (does nothing here)
        pass

Derived class
class Rectangle(Shape):
    def _init_(self, width, height):
        super()._init_()  # Call the constructor of the base class
        self.width = width
        self.height = height
        print("Rectangle initialized.")

    def calculate_area(self):
        super().calculate_area()  # Optional call to base class method
        area = self.width * self.height
        print(f"Rectangle area: {area}")
        return area

Question 4

 Define the dog clas
class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} says Woof! Woof!"

Define the cst class
class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} says Meow."

def process_sound(sound_object):
    print(sound_object.make_sound())

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print("--- Processing Dog Sound ---")
process_sound(my_dog)

print("\n--- Processing Cat Sound ---")
process_sound(my_cat)

Question 5
import abc
 Define the Abstract Base Class (ABC) for FileHandler
class FileHandler(abc.ABC):
    @abc.abstractmethod
    def read(self)
        Abstract method to read content from a file.
        Concrete subclasses must implement this.

      pass

    @abc.abstractmethod
    def write(self, data):
       
       
        pass

    def open_file(self, filename, mode):
        print(f"Opening file: {filename} in mode: {mode}")
        self._file = open(filename, mode) # Storing file object internally

    def close_file(self):
        if hasattr(self, '_file') and not self._file.closed:
            print(f"Closing file: {self._file.name}")
            self._file.close()

Concrete class for handling Text Files
class TextFileHandler(FileHandler):
    def read(self):
        if hasattr(self, '_file') and not self._file.closed:
            print("Reading text data...")
            return self._file.read()
        return "No file opened or file is closed."

    def write(self, data):
        if hasattr(self, '_file') and not self._file.closed:
            print(f"Writing text data: '{data}'")
            self._file.write(data)
        else:
            print("Cannot write. No file opened or file is closed.")

Concrete class for handling Binary Files
class BinaryFileHandler(FileHandler):
    def read(self):
        if hasattr(self, '_file') and not self._file.closed:
            print("Reading binary data...")
           
        return "No file opened or file is closed."

    def write(self, data):
        if hasattr(self, '_file') and not self._file.closed:
            print(f"Writing binary data: {data.encode('utf-8')}") # Encode to bytes for binary
            self._file.write(data.encode('utf-8')) # Assume data is string, convert to bytes
        else:
            print("Cannot write. No file opened or file is closed.")



 1. Test TextFileHandler
print("--- Text File Handler Demo ---")
text_handler = TextFileHandler()
text_handler.open_file("my_text_file.txt", "w")
text_handler.write("Hello, this is a test for text files!\n")
text_handler.close_file()

text_handler.open_file("my_text_file.txt", "r")
content = text_handler.read()
print("Read content:", content)
text_handler.close_file()

2. Test BinaryFileHandler
print("\n--- Binary File Handler Demo ---")
binary_handler = BinaryFileHandler()
binary_handler.open_file("my_binary_file.bin", "wb") # 'wb' for write binary
binary_handler.write("This is binary data.\n")
binary_handler.close_file()

binary_handler.open_file("my_binary_file.bin", "rb") # 'rb' for read binary
binary_content = binary_handler.read()
print("Read binary content (raw):", binary_content)
print("Read binary content (decoded):", binary_content.decode('utf-8'))
binary_handler.close_file()








print("Hello, World!")
