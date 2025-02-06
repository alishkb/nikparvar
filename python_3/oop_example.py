class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(f"{self.name} در حال غذا خوردن است.")

    def sleep(self):
        print(f"{self.name} خوابیده است.")

class Cat(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def meow(self):
        print("میو میو!")

class Dog(Animal):
    def __init__(self, name, age, color, bark_volume):
        super().__init__(name, age, color)
        self.bark_volume = bark_volume

    def bark(self):
        print("واق واق!")

class Bird(Animal):
    def __init__(self, name, age, color, can_fly):
        super().__init__(name, age, color)
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print(f"{self.name} در حال پرواز است.")
        else:
            print(f"{self.name} نمی‌تواند پرواز کند.")

class Fish(Animal):
    def __init__(self, name, age, color, can_swim):
        super().__init__(name, age, color)
        self.can_swim = can_swim

    def swim(self):
        if self.can_swim:
            print(f"{self.name} در حال شنا کردن است.")
        else:
            print(f"{self.name} نمی‌تواند شنا کند.")

# ایجاد اشیاء
cat = Cat("نفس", 2, "سفید", "پرشین")
dog = Dog("هاپو", 5, "قهوه‌ای", "بلند")
bird = Bird("طوطی", 3, "سبز", True)
fish = Fish("دلفین", 10, "آبی", True)

# فراخوانی متدها
cat.meow()
dog.bark()
bird.fly()
fish.swim()
