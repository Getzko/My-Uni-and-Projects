class Product:
    def __init__(self,name,price,stock,):
        self.name=name
        self.price=price
        self.stock=stock
        self._discount=10
    @property
    def inventory_value(self):
        return self.price * self.stock
    @property
    def discount(self):
        return self._discount
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if value <= 0:
            raise ValueError("Price must be greater than 0.")
        self._price=value

    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self,value):
        if value < 0:
            raise ValueError("Value must be 0 or greater ")
        self._stock=value
    
    def sell(self,change):
        if self.stock < change:
            raise ValueError("You dont have that much to sell")
        else:
            self.stock=self.stock-change
            print(f"Total: {self.stock}")
    def restock(self,change):
        self.stock+=change
        print(f"Total: {self.stock}")

