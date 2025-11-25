class chatbook:
    def __init__(self):
        self.UserName = " "
        self.PassWord = " "
        self.LoggedIn = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook! How would u like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press anyother key to exit """)
        if user_input == "1":
            self.SignUp()
        elif user_input == "2":
            self.SignIn()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def SignUp(self):
        email = input("Enter your email here ---> ")
        password = input("Setup your password here --->")
        self.UserName = email
        self.PassWord = password
        print('You have signedup successfully')
        print("\n")
        self.menu()

    def SignIn(self):
        if self.UserName == "" and self.PassWord == "":
            print("Please Signup first by pressing 1 in the main menu!")
        else:
            UserName = input("Enter your email here ---> ")
            PassWord = input("Enter your password here ---> ")
            if self.UserName == UserName and self.PassWord == PassWord:
                print("Your have successfully signedup")
                self.LoggedIn = True
            else:
                print("please enter correct credentials!")
        print("\n")
        self.menu()



obj = chatbook()