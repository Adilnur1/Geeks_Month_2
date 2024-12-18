class Transport:  # Родительский класс / Супер класс / Основной класс
    def __init__(self, the_model, the_year, the_color):
        # fields  /  attributes
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        # fields  /  attributes
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    counter = 0

    # constructor                      parameters
    def __init__(self, the_model, the_year, the_color, penalties = 0):
        # fields  /  attributes
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    def signal(self, num_of_times, sound):
        while num_of_times > 0:
            print(f'Car {self.model} is signalling: {sound}')
            num_of_times -= 1


class Truck(Car):
    counter = 0

    def __init__(self, the_model, the_year, the_color, penalties = 0, load_capacity = 0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'You successfully loaded the cargo'
                  f' of {product_type} ({weight} kg.)')


my_car = Car(the_model = "BMW X6", the_year = 2020, the_color = "Black")
print(my_car)

print(f'MODEL: {my_car.model} YEAR: {my_car.year} COLOR: {my_car.color} '
      f'PENALTIES: {my_car.penalties}')

best_car = Car(the_year = 2021, the_model = 'Honda Fit', the_color = 'Blue', penalties = 900)

print(f'MODEL:{best_car.model} YEAR: {best_car.year} COLOR: {best_car.color} '
      f'PENALTIES: {best_car.penalties}')

# best_car.color = 'Red' # меняем свет машины.
best_car.change_color('Red')  # меняем свет машины с помощью метода.

print(f'MODEL:{best_car.model} YEAR: {best_car.year} NEW COLOR: {best_car.color} 'f'PENALTIES: {best_car.penalties}')

my_car.drive('Osh')
best_car.drive('Kant')
best_car.drive('Tokmok')
best_car.signal(3, 'Beep')

my_plane = Plane('Boeing 747', 2019, 'White')
print(f'MODEL: {my_plane.model} YEAR: {my_plane.year} COLOR: {my_plane.color}')

truck = Truck('Volvo 300', 2000, 'blue', 500, 30000)
print(
    f'MODEL:{truck.model} YEAR: {truck.year} NEW COLOR: {truck.color} 'f'PENALTIES: {truck.penalties} LOAD CAPACITY {truck.load_capacity}')
truck.load_cargo(35000, 'apples')
truck.load_cargo(25000, 'oranges')
truck.drive('Batken')

print(f'Factory Car produced: {Car.counter} car')
print(f'Factory Truck produced: {Truck.counter} cars')
print('End of Program')
