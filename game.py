import datetime
import BackEnd


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
        BD = datetime.datetime.strptime(self.BirthDay,'%Y-%m-%d')
        Age = Today.year -BD.year
        print(Age)
        

class Player(Human):
    def __init__(self,Name,LastName,Gender,BirthDay,PlayerID,UserName,Password,Balance):
        super().__init__(Name,LastName,Gender,BirthDay)
        Category = 1
        self.PlayerID = PlayerID
        self.UserName = UserName
        self.PassWord = Password
        self.Balance = Balance
        if Balance < 9999:
            Category = 20
        else:
            Category = 21
        self.Category  = Category
        
    def ChargeCredit(self,Number):
        self.Balance += Number
    
    

class Dealer(Human):
    def __init__(self,Name,LastName,Gender,BirthDay,DelaerID):
        super().__init__(Name,LastName,Gender,BirthDay)
        self.DelaerID = DelaerID
        




            
Player1 = Player("Hamid Reza","Bakhtaki",2,"1985-06-25",1,"HamidRB","2263605",999)
Player1.PrintBasics()
Player1.GetAge()
Dealer1 = Dealer("Vaheh","Davitian",1,'1981-06-01',1)
Dealer1.PrintBasics()
print(Player1.Balance)
Player1.ChargeCredit(1000)
print(Player1.Balance)

