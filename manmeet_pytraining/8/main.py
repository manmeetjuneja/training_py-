import vehicle
def main():
    auto = vehicle.Automobile("A","Car","54.5","$4585455")
    auto.get_make()
    auto.get_model()
    auto.get_mileage()
    auto.get_price()

    car = vehicle.Car("B","Car","45.66","$34637574","5")
    print("----------------------------------")
    #parent class method
    car.get_make()
    car.get_model()
    car.get_mileage()
    car.get_price()
    #child class method
    car.get_doors()

    tr = vehicle.Truck("B","Car","45.66","$34637574","2 way")
    print("----------------------------------")
    #parent class method
    tr.get_make()
    tr.get_model()
    tr.get_mileage()
    tr.get_price()
    #child class method
    tr.get_drive_type()

    sv = vehicle.Suv("B","Car","45.66","$34637574","98")
    print("----------------------------------")
    #parent class method
    sv.get_make()
    sv.get_model()
    sv.get_mileage()
    sv.get_price()
    #child class method
    sv.get_pass_cap()
main()    
