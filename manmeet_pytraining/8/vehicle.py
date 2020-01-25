class Automobile:
    def __init__(self,make,model,mileage,price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def set_make(self,make):
        self.__make = make

    def set_model(self,model):
        self.__model = model

    def set_price(self,model):
        self.__price = price

    def set_mileage(self,mileage):
        self.__price = price
    
    def get_make(self):
        print("Parent Class "+str(self.__make))   
       
    def get_model(self):
        print("Parent Class "+str(self.__model))
    
    def get_mileage(self):
        print("Parent Class "+str(self.__mileage))

    def get_price(self):
        print("Parent Class "+str(self.__price))

class Car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        Automobile.__init__(self,make,model,mileage,price)
        self.__doors = doors
        
    def set_doors(self,doors):
        self.__doors = doors
        
    def get_doors(self):
        print(self.__doors)
    
class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        Automobile.__init__(self,make,model,mileage,price)
        self.__drive_type = drive_type
        
    def set_drive_type(self,drive_type):
        self.__drive_type = drive_type
        
    def get_drive_type(self):
        print(self.__drive_type)    
    
class Suv(Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        Automobile.__init__(self,make,model,mileage,price)
        self.__pass_cap = pass_cap
        
    def set_pass_cap(self,pass_cap):
        self.__pass_cap = pass_cap
        
    def get_pass_cap(self):
        print(self.__pass_cap)

