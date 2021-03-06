class Parent():
    """Parent class as test"""
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name - "+self.last_name)
        print("Eye color - "+self.eye_color)

class Child(Parent):
    """Child class"""
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last name - "+self.last_name)
        print("Eye color - "+self.eye_color)
        print("Number of toys - "+str(self.number_of_toys))

billy_cyrus = Parent("Cyrus", "blue")

miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()
billy_cyrus.show_info()
