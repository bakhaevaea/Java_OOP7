class Human:
    
    def __init__(self, name, sex, year, father, mather):
        """Constructor"""
        self.name = name
        self.sex = sex
        self.year = year
        self.father = father
        self.mather = mather
    def getName(self): 
        return self.name
    
    def getSex(self):
        return self.sex

    def getYear(self):
        return self.year

    def getFather(self):
        return self.father

    def getMather(self):
        return self.mather
    
    def getParents(self):
        return[self.getFather(), self.getMather()]
    
    def getChilds(self, list):
        childs = []
        for i in list:
            if i.getFather() == self or i.getMather() == self:
                childs.append(i)
        return childs

    def toString(self): 
        return "{" + "name ='" + self.name +", sex ='" + self.sex + ", year =" + self.year +'}'


def main():
    grand1 = Human("Александр", "М", "1965", "", "")
    grand2 = Human("Галина", "Ж", "1960", "", "")
    parent1 = Human("Александр", "М", "1987", grand1, grand2)
    child1 = Human("Дарья", "Ж", "2013", parent1, "")
    child2 = Human("Павел", "М", "2018", parent1, "")
    humans = [grand1, grand2, parent1]
    humans.append(child1)
    humans.append(child2)
    print("У чеовека: " + parent1.toString())
    print("родители: " )
    print(list(map(lambda x: x.toString(), parent1.getParents() )))
    print("дети: " )
    print(list(map(lambda x: x.toString(), parent1.getChilds(humans) )))

    # print(list(map(lambda x: x.toString(), humans)))
    


main()

# if __name__ == "__main__":
#     car = Vehicle("blue", 5, 4, "car")
#     print(car.brake())
#     print(car.drive())
 
#     truck = Vehicle("red", 3, 6, "truck")
#     print(truck.drive())
#     print(truck.brake())