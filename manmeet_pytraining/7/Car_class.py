class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f'I am{self.color} car'

def main():
    obj = Car("blue",77)
    print(obj)
main()
