import os

class XOGAME:
    def __init__(self,user1="X",user2="O") :
        print(" WELCOME TIC-TAC-TOE ".center(100,"*"))
        print(" ")
        self.user1name=input("User 1 Name : ")
        self.user2name=input("User 2 Name : ")
        self.user1=user1
        self.user2=user2
        self.gamelist=["_","_","_","_","_","_","_","_","_"]
        self.gameMoveList=["1","2","3","4","5","6","7","8","9"]
        
    def display(self):
        """
        Game IO.

        """
        print("  Game Display  ".center(50,"*"))
        print(" ")
        print(f"{self.gamelist[0]} {self.gamelist[1]} {self.gamelist[2]}\n".center(50)+f"{self.gamelist[3]} {self.gamelist[4]} {self.gamelist[5]}\n"+f"{self.gamelist[6]} {self.gamelist[7]} {self.gamelist[8]}".center(50))
        print(" ")
        print("*".center(50,"*"))
        print("  Choise Display  ".center(50,"*"))
        print(" ")
        print(f"{self.gameMoveList[0]} {self.gameMoveList[1]} {self.gameMoveList[2]}\n".center(50)+f"{self.gameMoveList[3]} {self.gameMoveList[4]} {self.gameMoveList[5]}\n"+f"{self.gameMoveList[6]} {self.gameMoveList[7]} {self.gameMoveList[8]}".center(50))
        print(" ")
        print("*".center(50,"*"))
        
    def move(self,symbol,choose):
        """
            input = User, User move choose
            output = gamelist and gameMoveList add str.
        """
        self.symbol=symbol
        self.choose=choose
        self.gameMoveList[choose-1]="-"
        self.gamelist[choose-1]=symbol

    def movecheck(self,choose):
        """
        User choose check. 
        Input : Choose
        Output : True/False

        """
        return self.gameMoveList[choose-1]!="-" 

    def wincheck(self,user_symbol):
        """
        winlist = all win
        Input : User Symbol( "x" or "o" )
        Output : True/False

        """
        self.usersymbol = user_symbol
        useranswer=[user_symbol,user_symbol,user_symbol]
        winlist= [self.gamelist[:3],self.gamelist[3:6],self.gamelist[6:],self.gamelist[::3],self.gamelist[2::3],self.gamelist[::4],self.gamelist[2:7:2],self.gamelist[1:8:3]]
        for win in winlist:
            if win == useranswer:
                return True
        return False

    def winnerdisplay(self,username):
        """
        winner display io
        
        """
        os.system('cls')
        XOGAME.display(self=self)
        print(" ")
        print("Tic-Tac-Toe King".center(100,"-"))
        print(" ")
        print(f"Winner :  {username}".center(100))
        print(" ")
        print(" GAME THE END ".center(100,"*"))

    def choosecheck(self,choose):
        """
        Check = Answer Str or diffrent choise
        
        """
        try :
            chose =int(choose)
            if chose <0:
                return False
            if chose>10:
                return False
            else:
                return True        
        except:
            return False
   
              
xo=XOGAME()

for i in range(1,10):
    os.system('cls')
    xo.display()
    if i%2==1:
        user_symbol = xo.user1
        while True:
            choose = input(f"It is yoru turn : {xo.user1name}  \nPlease Choose Number  : ")
            if xo.choosecheck(choose):
                if xo.movecheck(int(choose)):
                    xo.move(user_symbol,choose=int(choose))
                    break
                else:
                    print("The field is full. Choose another area ! ".center(100,"!"))
                    print(" ")
            else:
                    print("Plase enter valid number".center(100,"!"))
                    print(" ")

        if xo.wincheck(user_symbol)==True:
            xo.winnerdisplay(xo.user1name)
            break
    
    else:
        user_symbol=xo.user2
        while True:
            choose = input(f"It is your turn : {xo.user2name}  \nPlease Choose Number  : ")
            if xo.choosecheck(choose):
                if xo.movecheck(int(choose)):
                    xo.move(user_symbol,choose=int(choose))
                    break
                else:
                    print("The field is full. Choose another area ".center(100,"!"))
                    print(" ")
            else:
                    print(" Plase enter valid number ".center(100,"!"))
                    print(" ")

        if xo.wincheck(user_symbol)==True:
            xo.winnerdisplay(xo.user2name)
            break
       
if xo.wincheck(user_symbol)==False: 
    print(" ")
    print(" DRAW ".center(100,"-"))  
    print(" ")

