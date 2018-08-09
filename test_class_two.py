class Phone():
    def __init__(self,name,color,price):
        self.name = name
        self.color =color
        self.price = price

    def print_color(self):
        return self.color

iPhone = Phone('htc','red',6000)

print(iPhone.color)
print(iPhone.print_color())
#==
print(Phone.print_color(iPhone))
