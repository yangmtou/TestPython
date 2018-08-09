class Phone():
    def __init__(self):
        self.name = 'iPhone'
        self.color = 'black'
        self.price = 7000

    def print_color(self):
        return self.color

iPhone = Phone()

print(iPhone.color)
print(iPhone.print_color())
#==
print(Phone.print_color(iPhone))
