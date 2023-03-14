class main:
    def __bills(self):
        print("Assalam-o-Aalikum")
    def __init__(self):
        self.__products=""
        self.__bread=""
        self.__wheat=""
        self.__bills()
        self.__getname()
    def __getname(self):
        return self.__products
        return self.__bread
        return self.__wheat
    def setname(self,product1,bread3,wheat2):
            self.__products=product1
            self.__bread=bread3
            self.__wheat=wheat2

class student(main):
    def __bills(self):
        super().__init__()
        print("Bills")
    def __init__(self):
        self.__honey=" "
        self.__bills()
        self.__getname()
    def __getname(self):
        return self.__honey
    def setname(self,product1,bread3,wheat2,honey3):
            self.__products=product1
            self.__bread=bread3
            self.__wheat=wheat2
            self.__honey=honey3
            print(f" the total bil  is {self.__products} {self.__bread} and {self.__wheat} {self.__honey}")
customer2=student()
customer2.setname(10,70,50,3)


 


