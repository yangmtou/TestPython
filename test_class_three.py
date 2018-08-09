class Phone():
    #class级别的属性
    shape = 'rectangle'
    def __init__(self,name,color,price):
        self.name = name
        self.color =color
        self.price = price

    def print_color(self):
        return self.color

    @classmethod
    def call(self):
        print('喂喂喂')

iPhone = Phone('htc','red',6000)

print(iPhone.color)
print(iPhone.print_color())
#==
print(Phone.print_color(iPhone))

print(Phone.shape)
print(iPhone.shape)

Phone.call()
iPhone.call()
