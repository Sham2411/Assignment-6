class Dog:
    def __init__(self,name,age,coatcolor):
        self.name = name
        self.age = age
        self.coatcolor = coatcolor
    def Description(self):
        print("Name of the dog: ", self.name)
        print("age of the dog:",self.age)
    def get_info(self):
        print("coat color of the dog:",self.coatcolor)
class JackRussellTerrier(Dog):
    def trial1(self):
        pass
    def trial2(self):
        pass
class Bulldog(Dog):
    def trial3(self):
        pass
    def trial4(self):
        pass
Dog1 = JackRussellTerrier("Sher","6 years","Brown")
Dog2 = Bulldog("Rocky","2 years","Black")
Dog1.Description()
Dog1.get_info()
Dog2.Description()
Dog2.get_info()