class Vehicle():
    status = 'For Sale'   
    def __init__(self, brand, model, bodywork, year, mileage, transmission, paintedpart, changedpart, price):
        self.brand = brand
        self.model = model
        self.bodywork = bodywork
        self.year = year
        self.mileage = mileage
        self.transmission = transmission
        self.paintedpart = paintedpart
        self.changedpart = changedpart
        self.price = price
    def showvehicle(self):
        return "This car is {} {}. This car's body is {}. This car was made in {}. It has {} of mileage. It has {} transmission. This car has {} painted parts and {} changed parts. It has a price of {} USD.".format(   
        self.brand,
        self.model,
        self.bodywork,
        self.year,
        self.mileage,
        self.transmission,
        self.paintedpart,
        self.changedpart,
        self.price)
    
    
vehicle1 = Vehicle('Mercedes-Benz', 'E320', 'Sedan', 2007, 190245, 'Automatic', 3, 2, 15000)

vehicle1.showvehicle()