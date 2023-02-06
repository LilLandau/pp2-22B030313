import math

class myClass:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string)

class Shape():
    def __init__(self):
        self.area = 0
    
    def print_area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, lenght):
            self.lenght = lenght

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def compute_area(self):
        self.area = self.lenght*self.width

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        txt = "Coordinates of the point is ({0}, {1})"
        print(txt.format(self.x, self.y))

    def move(self, dist_x, dist_y):
        self.x += dist_x
        self.y += dist_y

    def dist(self, point):
        diff_x = point.x - self.x
        diff_y = point.y - self.y

        print(math.sqrt(pow(diff_x, 2) + pow(diff_y, 2)))
        
class Acount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

        txt = "Your balance has been replenished by {0} tenge. On the account {1} tenge"
        print(txt.format(amount, self.balance))

        return

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on your balance")
            return
        else:
            self.balance -= amount
            txt = "{0} tenge was withdrawn from your balance. The balance of the account is {1} tenge"
            print(txt.format(amount, self.balance))
            return

