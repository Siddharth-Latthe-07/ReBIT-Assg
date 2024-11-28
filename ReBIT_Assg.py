#Q1:- Question 1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):

        return f"{self.year} {self.make} {self.model}"

car = Vehicle("Toyota", "Camry", 2022)
print(car)




#Q2:- Question 2
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):

        print(f"Vehicle Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")


car = Vehicle("Toyota", "Camry", 2022)
car.display_info()


#Q3:- Question 3

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors, engine_type):

        super().__init__(make, model, year)
        self.doors = doors
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}\nEngine Type: {self.engine_type}")


my_car = Car("Toyota", "Camry", 2022, 4, "Petrol")
my_car.display_info()


# Q4:-
class Vehicle:
    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year

    def display_info(self):

        print(f"Vehicle Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, doors, engine_type):

        super().__init__(make, model, year)
        self.doors = doors
        self.engine_type = engine_type

    def display_info(self):

        super().display_info()
        print(f"Doors: {self.doors}\nEngine Type: {self.engine_type}")

    def start_engine(self):

        print(f"The {self.engine_type} engine of the {self.make} {self.model} is starting...")


my_car = Car("Toyota", "Camry", 2022, 4, "Petrol")
my_car.display_info()
my_car.start_engine()



#Q5:- 
class Bicycle(Vehicle):
    def __init__(self, make, model, year, gear_count, bicycle_type):
        super().__init__(make, model, year)
        self.gear_count = gear_count
        self.bicycle_type = bicycle_type

    def display_info(self):
        super().display_info()
        print(f"Gear Count: {self.gear_count}\nBicycle Type: {self.bicycle_type}")

bicycle = Bicycle("Trek", "Domane", 2022, 18, "Road Bike")
bicycle.display_info()

#Q6:-
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
circle = Circle(5)
print("Circle Area:", circle.calculate_area()) 

#Q7:-
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area()) 
print("Rectangle Perimeter:", rectangle.perimeter()) 

#Q8:-
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def email_address(self):
        return f"{self.employee_id}@company.com"


#Q9:- 
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def department_details(self):
        return f"Manager of {self.department}"
    

employee = Employee("John Doe", "JD123")
print("Employee Email:", employee.email())  # Output: JD123@company.com

manager = Manager("Jane Smith", "JS456", "IT")
print("Manager Email:", manager.email())  # Output: JS456@company.com
print(manager.department_details()) 

#Q10:- 
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def multiply(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

                    #OR

class ComplexNumber:
    def __init__(self, real, imaginary):

        self.number = complex(real, imaginary)

    def add(self, other):

        return ComplexNumber(self.number.real + other.number.real, self.number.imag + other.number.imag)

    def multiply(self, other):

        result = self.number * other.number
        return ComplexNumber(result.real, result.imag)

    def __str__(self):

        return f"{self.number.real} + {self.number.imag}i"


num1 = ComplexNumber(3, 4)  
num2 = ComplexNumber(1, 2)  


sum_result = num1.add(num2)
print("Sum:", sum_result) 


multiply_result = num1.multiply(num2)
print("Product:", multiply_result)



#Q11:-
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)
        print(self.price)

    def __str__(self):
        return f"'{self.title}' by {self.author}, priced at ${self.price:.2f}"
    
book = Book("Python Programming", "John Doe", 39.99)
print(book.__str__())  # Output: 'Python Programming' by John Doe, Price: $39.99
book.apply_discount(10) 

#Q12  & 13:
class Flight:
    def __init__(self, airline, flight_number):
        self.airline = airline
        self.flight_number = flight_number
        self.passengers = []

    def add_passenger(self, name):
        self.passengers.append(name)

    def remove_passenger(self, name):
        self.passengers.remove(name)

    def flight_details(self):
        return f"Flight: {self.airline} {self.flight_number}, Passengers: {', '.join(self.passengers)}"


flight = Flight("Air India", "AI101")
flight.add_passenger("Alice")
flight.add_passenger("Bob")
print(flight.flight_details())  
flight.remove_passenger("Alice")
print(flight.flight_details())


#Q14:
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic Animal Sound")

#Q15:
class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

dog = Dog("Canine")
dog.make_sound()  # Output: Woof

cat = Cat("Feline")
cat.make_sound() 



#Q16:
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"
    
calc = Calculator()
print("Addition:", calc.add(5, 3))  
print("Subtraction:", calc.subtract(5, 3))  
print("Multiplication:", calc.multiply(5, 3))  
print("Division:", calc.divide(5, 0))  


#Q17:-
class WeatherForecast:
    def __init__(self):
        self.temperatures = []

    def add_temperature(self, temp):
        self.temperatures.append(temp)

    def average_temperature(self):
        return sum(self.temperatures) / len(self.temperatures)
    
forecast = WeatherForecast()


forecast.add_temperature(30)
forecast.add_temperature(32)
forecast.add_temperature(28)
forecast.add_temperature(35)


average_temp = forecast.average_temperature()
print(f"Average Temperature: {average_temp:.2f}°C")
    

#Q18, 19, 20:-
class Polygon:
    def perimeter(self):
        print("used by subclass")

    def area(self):
        print("Used by subclass")

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2


triangle = Triangle(3, 4, 5)
print("Triangle Perimeter:", triangle.perimeter())  
print("Triangle Area:", triangle.area())            

square = Square(4)
print("Square Perimeter:", square.perimeter())      
print("Square Area:", square.area())                



#Q21:-
import time

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            print("not started")
            return None
        return time.time() - self.start_time
    

timer = Timer()

timer.start()
print("Timer started. Performing a task...")


time.sleep(2) 

elapsed_time = timer.stop()
print(f"Elapsed Time: {elapsed_time:.2f} seconds") 



#Q22:-
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else "Queue is empty"

    def view_queue(self):
        return self.queue
    
queue = Queue()


queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Queue after enqueueing:", queue.view_queue()) 

print("Dequeued:", queue.dequeue())
print("Queue after dequeueing:", queue.view_queue())  
queue.dequeue()
queue.dequeue()
print("Dequeued from empty queue:", queue.dequeue()) 


#Q23:-
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def size(self):
        return len(self.stack)
    

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushing:", stack.size())  


print("Popped item:", stack.pop())         
print("Stack after popping:", stack.size()) 

# Check stack size
print("Stack size:", stack.size())         

# Pop until empty
stack.pop()
stack.pop()
print("Popped from empty stack:", stack.pop())  



#Q24:-
class MusicPlayer:
    def __init__(self):
        self.current_track = None

    def load_track(self, track):
        self.current_track = track
        print(f"Loaded track: {track}")

    def play(self):
        if self.current_track:
            print(f"Playing track: {self.current_track}")
        else:
            print("No track loaded")

    def stop(self):
        print("Music stopped")

player = MusicPlayer()


player.play()  

player.load_track("Imagine - John Lennon") 
player.play()                              
player.stop()                              
player.load_track("Thriller - Michael Jackson")  
player.play() 


#Q25:-
class database:
    def __init__(self,db_name):
        self.db_name= db_name
        self.connect= False

    def db_connect(self):
        if not self.connect:
            self.connect=True 
            print("Connected to{self.db_name}")
        else:
            print("Not connected")
    def db_disconnect(self):
        if self.connect:
            print("Disconnected")
        else:
            print("Not connected")

    def execute_query(self,query):
        if not self.connected:
            print("Executing {query}")
        else:
            print("Wrong")

db = database("TestDB")


db.db_connect()

db.execute_query("SELECT * FROM users")
db.db_disconnect()
db.execute_query("SELECT * FROM users")







