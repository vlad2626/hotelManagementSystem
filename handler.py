import numpy as np
from guest import guest

class Handler:

    def main(self):
        menOp = -1
        blGo = True
        Hdl = Handler()
        rooms=Hdl.createRooms()

        #handle new walk in , new reservation , existing reservation check in .
        while  blGo:
            menOp = Hdl.mainMenu()
            match menOp:
                case "0":
                    blGo = False
                case "1":
                    Hdl.newWalkin()


    def createRooms(self):
        # Creates rooms arranges them into a matrix  and returns it.

        rooms =[]
        for i in range(5):
            rooms.append(i)
            for j in range(5):
                rooms.append(j)

        a= np.array(rooms)
        b=a.reshape(5,6)
        print("Hello world")
        print(b)

        return b



    def mainMenu(self):
        print("Main Menu \n" + ""
                               "1. New Walk in \n"
                               "2. New Arrival \n"
                               "3. Extend \n"
                               "4. Checkout\n"
                               "5. Room stats\n"
                               "6. Checkout all rooms \n"
                               "7. Check in all rooms \n"
                               "0. Exit")
        menOP = input("Menu option: ")
        return menOP



    def newWalkin(self):
        fname = input("First Name:")
        lName= input("Last Name:")
        lAge= input("Age:")
        lPhone = input("Phone:")
        lCC = input("Credit Card")

        newGuest = guest(fname,lName,lAge,lPhone,lCC)

        roomType = input("What kind of Room ?")

        match roomType:
            case "Suite":
                print("s")
            case "King":
                print("k")
            case "Queen":
                print("Queen")
            case "Double":
                print("D")
            case "Single" :
                print("S")
            case _:
                print("please enter valid room. ")

        #1.check empty rooms
        #2. Check guest into one of the empty room s.