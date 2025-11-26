#initiliaxe class
class employee:
    #special function/method/dunder method -constructor
    def __init__(self):
        self.__name = "Default"
        #print("Started data fetching....")
        self.id = 123
        self.salary = 50000 
        self.designation = "software development engineer"
       # print("Data fetched!")

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value

    def travel(self,destination):
        print("This travel function was called manually")
        print(f'Employee is now traveling to {destination}')

#creating an object/instance of class employee
#sam = employee()
#print(id(sam))

#print(sam.salary)
#sam.travel("Delhi")

#print(type(sam))
user1 = employee()
print(user1.get_name())
user1.set_name("Agent X")
print(user1.get_name())