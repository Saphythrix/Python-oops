# OOP in Python: Complete Interview Guide

## 1. Classes & Objects (Basics)

### Concept
A class is a blueprint; an object is an instance of that blueprint.

### Python Implementation
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Creating objects
car1 = Car("Toyota", "Camry", 2020)
car1.display_info()  # Output: 2020 Toyota Camry
```

**Key Points:**
- `__init__` is the constructor (like Java's `__init__`)
- `self` refers to the instance (like `this` in Java)
- Attributes store data, methods perform actions

---

## 2. Encapsulation (Data Hiding)

### Concept
Restrict direct access to object data; use methods instead.

### Python Implementation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private (name mangling with __)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        print(f"New balance: {self.__balance}")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)  # Output: New balance: 1500
# account.__balance  # Error: Not directly accessible
print(account.get_balance())  # Output: 1500
```

**Python Access Levels:**
- `public`: No underscore → Anyone can access
- `protected`: Single `_var` → Intended for subclasses (convention only)
- `private`: Double `__var` → Name mangling, harder to access

---

## 3. Inheritance (Reusability)

### Concept
Child class inherits properties and methods from parent class.

### Python Implementation
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):  # Override parent method
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks

cat = Cat("Whiskers")
cat.speak()  # Output: Whiskers meows
```

**Types of Inheritance:**
- Single: Child inherits from one parent
- Multiple: Child inherits from multiple parents
- Multilevel: Grandchild → Child → Parent

```python
# Multiple Inheritance
class FlyingAnimal:
    def fly(self):
        print("Flying...")

class Bird(Animal, FlyingAnimal):
    pass

bird = Bird("Eagle")
bird.speak()  # From Animal
bird.fly()    # From FlyingAnimal
```

---

## 4. Polymorphism (Many Forms)

### Concept
Same method name, different implementations across classes.

### Python Implementation
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())  # Calls appropriate area() method
```

**Duck Typing (Python-specific):**
```python
class Guitar:
    def play(self):
        print("🎸 Guitar playing")

class Piano:
    def play(self):
        print("🎹 Piano playing")

def play_instrument(instrument):
    instrument.play()  # Works with any object that has play()

guitar = Guitar()
piano = Piano()
play_instrument(guitar)  # Output: 🎸 Guitar playing
play_instrument(piano)   # Output: 🎹 Piano playing
```

---

## 5. Abstraction (Hide Complexity)

### Concept
Show only essential features; hide implementation details.

### Python Implementation
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment: ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment: ${amount}")

# You cannot instantiate abstract class
# processor = PaymentProcessor()  # Error!

cc = CreditCardProcessor()
cc.process_payment(100)  # Output: Processing credit card payment: $100

paypal = PayPalProcessor()
paypal.process_payment(50)  # Output: Processing PayPal payment: $50
```

---

## 6. Class Methods & Static Methods

### Concept
- **Instance methods**: Operate on instance data (`self`)
- **Class methods**: Operate on class data (`cls`)
- **Static methods**: No access to instance or class

### Python Implementation
```python
class Student:
    total_students = 0
    
    def __init__(self, name):
        self.name = name
        Student.total_students += 1
    
    # Instance method
    def introduce(self):
        print(f"Hi, I'm {self.name}")
    
    # Class method
    @classmethod
    def get_total_students(cls):
        return cls.total_students
    
    # Static method
    @staticmethod
    def is_valid_age(age):
        return age >= 18

s1 = Student("Alice")
s2 = Student("Bob")

s1.introduce()  # Output: Hi, I'm Alice
print(Student.get_total_students())  # Output: 2
print(Student.is_valid_age(20))  # Output: True
```

---

## 7. Special Methods (Dunder Methods)

### Concept
Python magic methods make objects behave like built-in types.

### Common Dunder Methods
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # String representation (for printing)
    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"
    
    # Official representation (for debugging)
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    
    # Comparison
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    # String length
    def __len__(self):
        return len(self.name)
    
    # Add two persons
    def __add__(self, other):
        return Person(f"{self.name} & {other.name}", (self.age + other.age) // 2)
    
    # Call object as function
    def __call__(self, greeting):
        print(f"{greeting}, {self.name}!")

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1)  # Output: Person: Alice, Age: 25
print(p1 == p2)  # Output: False
print(p1 < p2)   # Output: True (Alice is younger)
print(len(p1))   # Output: 5 (length of "Alice")
p3 = p1 + p2
print(p3.name)  # Output: Alice & Bob
p1("Hello")  # Output: Hello, Alice!
```

---

## 8. Properties (Getters/Setters)

### Concept
Control attribute access with methods while maintaining dot notation.

### Python Implementation
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Invalid temperature")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)  # Output: 25 (getter)
temp.celsius = 30    # Setter
print(temp.fahrenheit)  # Output: 86.0

# temp.celsius = -300  # Error: Invalid temperature
```

---

## 9. Super() - Accessing Parent Class

### Concept
Call parent class methods from child class.

### Python Implementation
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand)  # Call parent constructor
        self.color = color
    
    def info(self):
        super().info()  # Call parent method
        print(f"Color: {self.color}")

car = Car("Toyota", "Red")
car.info()
# Output:
# Brand: Toyota
# Color: Red
```

---

## 10. Composition (Has-A Relationship)

### Concept
Object contains other objects (alternative to inheritance).

### Python Implementation
```python
class Engine:
    def __init__(self, power):
        self.power = power
    
    def start(self):
        print(f"Engine started ({self.power} HP)")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
    
    def start(self):
        self.engine.start()

engine = Engine(150)
car = Car("Honda", engine)
car.start()  # Output: Engine started (150 HP)
```

---

# PRACTICE EXERCISES

## Exercise 1: Library Management System
Create classes for Book, Author, and Library.

**Requirements:**
- Book: title, author (Author object), isbn, pages
- Author: name, birth_year, books (list)
- Library: name, books (list of Book objects)
- Library methods: add_book(), search_by_title(), search_by_author(), get_total_pages()

**Bonus:** Use encapsulation to protect critical data.

---

## Exercise 2: Employee Hierarchy
Create Employee → Manager → Director hierarchy.

**Requirements:**
- Employee: name, salary, emp_id
  - Methods: get_salary(), work()
- Manager (inherits Employee): manages (list of employees)
  - Override: work() to include "Managing team"
  - Method: add_employee()
- Director (inherits Manager): department
  - Override: work() to include "Strategic planning"

**Bonus:** Implement polymorphism—create a function that calls work() on different employee types.

---

## Exercise 3: Shape Calculator (Polymorphism)
Create abstract Shape class with Circle, Rectangle, Triangle subclasses.

**Requirements:**
- Abstract Shape: area() and perimeter() methods
- Each shape implements area() and perimeter()
- Create a list of mixed shapes and calculate total area

```python
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
total_area = sum([shape.area() for shape in shapes])
```

---

## Exercise 4: E-Commerce Cart System
Create classes for Product, Cart, and Order.

**Requirements:**
- Product: name, price, quantity_in_stock
  - Check if enough stock before adding to cart
- Cart: items (list), add_item(), remove_item(), calculate_total()
- Order: cart, customer_name, order_id
  - Methods: place_order(), apply_discount()

**Bonus:** Implement __str__ and __repr__ for easy display.

---

## Exercise 5: Bank System (Encapsulation)
Create BankAccount with encapsulated balance.

**Requirements:**
- Private balance (double underscore)
- Methods: deposit(), withdraw(), get_balance()
- SavingsAccount (inherits): additional interest calculation
- Implement __add__() to merge two accounts
- Use properties for read-only access

---

## Exercise 6: Animal Zoo (Multiple Inheritance & Duck Typing)

**Requirements:**
- Animal: name, age
- Eater, Walker, Swimmer: methods for eating(), walking(), swimming()
- Dog, Fish, Duck: inherit from Animal + appropriate mixins
- Implement speak() method for each (polymorphism)
- Create zoo with mixed animals and call actions on all

```python
zoo = [Dog("Buddy"), Duck("Donald"), Fish("Nemo")]
for animal in zoo:
    animal.speak()
```

---

## Challenge Exercise: Design Pattern - Singleton
Implement Singleton pattern (only one instance ever created).

```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # Should be True (same instance)
```

---

# Interview Tips

1. **Inheritance vs Composition**: Know when to use each (inheritance for "is-a", composition for "has-a")
2. **SOLID Principles**: Mention Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
3. **Python-specific**: Duck typing, MRO (Method Resolution Order), properties vs getters/setters
4. **Common Mistakes to Avoid**:
   - Overusing inheritance when composition is better
   - Mixing encapsulation levels incorrectly
   - Not using abstract classes when designing extensible systems
5. **Practice Real Scenarios**: Think about systems you know (social media, e-commerce, games) and model them with OOP

---

# Quick Reference: OOP Concepts in Python vs Java

| Concept | Java | Python |
|---------|------|--------|
| Access Modifiers | `public`, `private`, `protected` | `public`, `_protected`, `__private` |
| Constructor | `ClassName()` | `__init__()` |
| Inheritance | `extends` | `class Child(Parent)` |
| Abstract Class | `abstract class` + `ABC` interface | `ABC` + `@abstractmethod` |
| Interface | `interface` | Abstract class with all abstract methods |
| Method Overriding | Explicit with `@Override` | Auto (just redefine) |
| Static Members | `static` keyword | `@staticmethod`, `@classmethod` |
| Property Access | Getters/Setters | `@property` decorator |
