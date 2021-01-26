import datetime
import getpass
import random

from colorama import Fore, Back

Red = [1, 3, 5, 7, 9, 11, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
Black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
Zero = [0]
Odd = [1, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
Even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]


class Human:
    def __init__(self, Name, LastName, Gender, BirthDay):
        self.Name = Name
        self.Family = LastName
        self.Gender = Gender
        self.BirthDay = BirthDay

    def PrintBasics(self):
        print(self.Name + " " + self.Family)

    def GetAge(self):
        Today = datetime.date.today()
        BD = datetime.datetime.strptime(self.BirthDay, '%Y-%m-%d')
        Age = Today.year - BD.year
        print(Age)


class Player(Human):
    def __init__(self, Name, LastName, Gender, BirthDay, PlayerID, UserName, Password, Balance):
        super().__init__(Name, LastName, Gender, BirthDay)
        Category = 1
        self.PlayerID = PlayerID
        self.UserName = UserName
        self.PassWord = Password
        self.Balance = Balance
        if Balance < 9999:
            Category = 20
        else:
            Category = 21
        self.Category = Category

    def ChargeCredit(self, Number):
        self.Balance += Number


class Dealer(Human):
    def __init__(self, Name, LastName, Gender, BirthDay, DelaerID):
        super().__init__(Name, LastName, Gender, BirthDay)
        self.DelaerID = DelaerID


def Wheel():
    WinNumber = random.randint(0, 36)
    return WinNumber


def RegisterPlayer():
    PlayerName = input("Please Enter Your Name: ")
    PlayerLastNameName = input("Please Enter Your LastName : ")
    Playergender = input("Please Enter 1 if you are Man Esle Print 2: ")
    PlayerBirthdate = input("Please Enter Your Birthdate : ")
    PlayerPassword = getpass.getpass("Please Enter Your Password:")
    PlayerUsername = input("Please Select a Useranme: ")
    PlayerCredit = input("Enter Credit")
    NewPlayer = Player(PlayerName, PlayerLastNameName, Playergender, PlayerBirthdate, 1, PlayerUsername, PlayerPassword,
                       PlayerCredit)


class table:
    def __init__(self):
        self.table = [[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],
                      [0, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                      [0, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]]

    def PrintTable(self):
        for i in range(3):
            for j in range(13):
                if self.table[i][j] in Red:
                    print(Fore.RED, self.table[i][j], end='')
                elif self.table[i][j] in Zero:
                    print(Fore.GREEN, self.table[i][j], end='')
                else:
                    print(Fore.BLACK, self.table[i][j], end='')
            print("\n")

    def PrintTableWinner(self, number):
        for i in range(3):
            for j in range(13):
                if self.table[i][j] == number:
                    print(Back.BLACK, Fore.YELLOW, self.table[i][j], end='')
                elif self.table[i][j] in Red:
                    print(Back.RESET, Fore.RED, self.table[i][j], end='')
                elif self.table[i][j] in Zero:
                    print(Back.RESET, Fore.GREEN, self.table[i][j], end='')
                else:
                    print(Back.RESET, Fore.BLACK, self.table[i][j], end='')
            print(Back.RESET, "\n")


# Player1 = Player("Hamid Reza","Bakhtaki",2,"1985-06-25",1,"HamidRB","2263605",999)
# Player1.PrintBasics()
# Player1.GetAge()
# Dealer1 = Dealer("Vaheh","Davitian",1,'1981-06-01',1)
# Dealer1.PrintBasics()
# print(Player1.Balance)
# Player1.ChargeCredit(1000)
# print(Player1.Balance)
Table1 = table()
Winner = Wheel()
Table1.PrintTableWinner(Winner)
