#initiliaxe class
class employee:
    #special function/method/dunder method -constructor
    def __init__(self):
        print("Started data fetching....")
        self.id = 123
        self.salary = 50000 
        self.designation = "software development engineer"
        print("Data fetched!")

    def travel(self,destination):
        print("This travel function was called manually")
        print(f'Employee is now traveling to {destination}')

#creating an object/instance of class employee
sam = employee()

#print(sam.salary)
sam.travel("Delhi")

print(type(sam))
