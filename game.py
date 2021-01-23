import datetime

class Human:
    def __init__(self,Name,LastName,Gender,BirthDay):
        self.Name = Name
        self.Family= LastName
        self.Gender = Gender
        self.BirthDay = BirthDay
        
    def PrintBasics(self):
        print(self.Name +" "+ self.Family)
    
    def GetAge(self):
        Today = datetime.date.today()
        Age = Today.year -self.BirthDay.

class Player(Human):
    def __init__(self,Name,LastName,Gender,BirthDay,PlayerID,UserName,Password,Balance):
        super().__init__(Name,LastName,Gender,BirthDay)
        Category = 1
        self.PlayerID = PlayerID
        self.UserName = UserName
        self.PassWord = Password
        self.initBalance = Balance
        if Balance < 9999:
            Category = 20
        else:
            Category = 21
        self.Category  = Category
            
Player1 = Player("Hamid Reza","Bakhtaki",1,"1985/06/25",1,"HamidRB","2263605",999)
Player1.PrintBasics()