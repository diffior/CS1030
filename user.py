class User:
    def __init__(self, firstname, lastname, age, identify, height):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.identify = identify
        self.height = height


#Getters

    def get_DescribeUser(self):
        long_name = f"{self.firstname} {self.lastname} {self.age} {self.identify} {self.height}"
        return long_name.title()



#Setters

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, newvalue):
        self.__age = newvalue

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, newvalue2):
        self.__firstname = newvalue2

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, newvalue3):
        self.__lastname = newvalue3

    @property
    def identify(self):
        return self.__identify

    @identify.setter
    def identify(self, newvalue4):
        self.__identify = newvalue4

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, newvalue5):
        self.__height = newvalue5
