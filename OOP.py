# Class - like coockie cutter that allows you to
# bake coockies with defined charachteristics

#Instance - individual obj class which have an unique memory adress

class Cookie():
    #__init__ - constructor, called every time when we instantiete an obj
    def __init__(self, name, shape, chips = "chocolate"):
        self.name = name
        self.shape = shape
        self.chips = chips

    def bake(self):
        print(f"this {self.name} in shape of {self.shape} with {self.chips} will be bake soon")

coockie = Cookie("awesome coockie", "coockie-monster")

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

class Human:
    #Constructor
    def __init__(self, name, age, gender):
        # Atributes
        self.name = name
        self.age = age
        self.gender = gender
    # Methods
    def get_name(self):
        return f'Person name is {self.name}'

    def get_age(self):
        return f'Person age is {self.age}'

    def get_gender(self):
        return f'Person gender is {self.gender}'

    def get_full_info(self):
        print(f'Person {self.name}')
        print(f'Age {self.age}')
        print(f'Gender {self.gender}')

# -----------------------INHERITANCE-------------------------


class Parent:
    def __init__(self, param1):
        self.atr = param1
    def parent_method(self):
        return self.atr * 3


class Child(Parent):
    def __init__(self, param1, param2):
        super().__init__(param1)
        self.atr_child = param2

    def child_method(self):
        return self.atr_child * 2


# -----------------------ENCAPSULATION-------------------------
class Worker:
    RIGHTS = "Every worker has rights to get payed for work he/she done"

    def __init__(self, work_class):
        self.__class_salary_map = {
            'A': 100,
            "B": 200,
            "C": 500,
            "D": 1000
        }
        self.__salary = self.__calculate_salary(work_class)

    def __calculate_salary(self, work_class):
        return self.__class_salary_map.get(work_class, 0)

    @property
    def salary(self):
        if not self.__salary:
            return "Undefined"
        return self.__salary


worker1 = Worker(work_class="A")
print(worker1.salary) #100
worker2 = Worker(work_class='B')
print(worker2.salary)  #200
print(worker1.RIGHTS == worker2.RIGHTS) #True
print(worker1.RIGHTS) #Every worker...
worker3 = Worker(work_class='X')
print(worker3.salary) #Undefined

# -----------------------POLYMORPHISM-------------------------


class Car:
    def __init__(self, name):
        self.__name_speed_dict = {
            'Mercedes': 250,
            'BMW': 200
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self.__name_speed_dict.get(name, 0)

    def distance_time_on_max_speed(self, distance):
        if not self._max_speed:
            print("No speed param specified")
            return 0
        return distance/self._max_speed


car_a = Car(name = "BMW")
car_b = Car(name="Mercedes")

print(car_a.distance_time_on_max_speed(distance=160))
print(car_b.distance_time_on_max_speed(distance=160))


# -----------------------ABSTRACTION-------------------------

class Core:
    def __init__(self):
        self._types = {
            'A': 100,
            "B": 300
        }

    def get_salary(self, worker_type):
        return self._types.get(worker_type, 0)


class AccountingInterface:
    def __init__(self, data):
        self._core = Core()
        self._people_class_dict = data

    def get_person_salary(self, name):
        person_class = self._people_class_dict.get(name)
        return self._core.get_salary(person_class)


database = {"John":"A", "Sally":"B"}
accounting = AccountingInterface(data=database)
print(f"John's salary is {accounting.get_person_salary('John')}")


