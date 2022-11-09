import numpy as np
from guest import guest

class Handler:
    rooms =[]
    currentResidents=[]
    reservations = []
    def main(self):
        menOp = -1
        blGo = True
        Hdl = Handler()
        self.loadGuestInfo()
        self.createRooms()
        #self.readRooms()




        #handle new walk in , new reservation , existing reservation check in .
        while  blGo:
            self.readRooms()
            menOp = Hdl.mainMenu()
            match menOp:
                case "0":
                    blGo = False
                case "1":
                    self.newWalkin()
                case "2":
                    self.newArrival()
                case "3":
                    self.newReservation()
                case "4":
                    self.checkout()
                case "5":
                    print(self.rooms)


    def getEmptyRoom(self, rType):
        match rType:
            case "Suite":
                room = self.getNextRoom(0)
            case"King":
                room = self.getNextRoom(1)
            case "Queen":
                room = self.getNextRoom(2)
            case "Double":
                room = self.getNextRoom(3)
            case "Single":
                room = self.getNextRoom(4)
        return room

    def getNextRoom(self,rType):
        dupRooms = []
        room= []
        floor= int(rType)
        for counter in range(len(self.rooms)):
            status=self.rooms[floor][counter]
            print(self.rooms[floor][counter])
            print(status + "Status")
            if status =="Empty":
                room = [rType, counter]
                break



        # for room in range(len(dupRooms)):
        #     if dupRooms[room]!="empty":
        #         room=[rType,room]
        #
        #         break

        print("Room number" + str(room))
        return room


    def createRooms(self):
        # Creates rooms arranges them into a matrix  and returns it.

        rooms =[]
        for i in range(5):
            for j in range(5):
                rooms.append("Empty")

        a= np.array(rooms)
        b=a.reshape(5,5)
        self.rooms = b
        #print(b)





    def mainMenu(self):
        print("Main Menu \n" + ""
                               "1. New Walk in \n"
                               "2. New Arrival \n"
                               "3. New Reservation\n"
                               "4. Checkout\n"
                               "5. Room stats\n"
                               "0. Exit")
        menOP = input("Menu option: ")
        return menOP



    def newWalkin(self):
        res = input("Do you have a reservation y/n").lower()
        if res=="n":
            fname = input("First Name:")
            lName= input("Last Name:")
            lAge= input("Age:")
            lPhone = input("Phone:")
            lCC = input("Credit Card")
            roomType = input("What kind of Room ?")
            los = input(" how long would you like to stay ")
            rType = self.validateRoom(roomType)
            room = self.getEmptyRoom(rType)
        else:
            #create room type and store it to check in guest
            lName = input("lName")
            for x in self.reservations:
                if x.getLName() == lName:
                    roomType = input("What kind of room would you like?")
                    rType = self.validateRoom(roomType)
                    room = self.getEmptyRoom(rType)
                    break

        #2. Check guest into one of the empty room s.


        if len(room)==0:
            print("Sorry out of rooms")
        else:
            print("Dear " + fname + " You are staying in room: " + str(room[1]) + " on floor " + str(room[0]))
            newGuest = guest(fname, lName, lAge, lPhone, lCC,room)
            newGuest.savePerson(newGuest)
            self.currentResidents.append(newGuest)#adds it to a dict of current guest





    def validateRoom(self,rType):
        match rType:
            case "Suite":
                rType = "Suite"
            case "King":
                rType = "King"
            case "Queen":
                rType = "Queen"
            case "Double":
                rType = "Double"
            case "Single":
                rType = "Single"
            case _:
                rType = input("please enter valid room. ")

        return rType
    def newReservation(self):

        fname = input("First Name: ")
        lName = input("Last Name: ")
        lAge = input("Age: ")
        lPhone = input("Phone: ")
        lCC = input("Credit Card ")
        roomType = input("What kind of Room ? ")
        rType = self.validateRoom(roomType)
        los = input(" how long would you like to stay ")

        checkIn = input("would you like to chekc in now ? Y/N ").lower()

        if checkIn == "y":
            room = self.getEmptyRoom(self,roomType)
            newGuest = guest(fname, lName, lAge, lPhone, lCC, room)
            self.currentResidents.append(newGuest)
        else:
            newGuest = guest(fname, lName, lAge, lPhone, lCC, " ")
            self.reservations.append((newGuest))


        #print(self.rooms)
        print(self.reservations)


    #this method loads the guest info when first running program
    def loadGuestInfo(self):
        file= open("guestInfo.txt", "r")
        for line in file:
            if len(line) != 0:
                arr = line.split(" ")
                newGuest = guest(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5] + arr[6])
                self.currentResidents.append(newGuest)
        file.close()




    #this method reads the current residents change the rooms to their name.
    def readRooms(self):

        # for i in range(len(self.currentResidents)):
        #     #print(self.currentResidents[i].toString())
        #     room =(self.currentResidents[i].getRoom())
        #
        #     arrRooms = []
        #     for i in range(len(room)):
        #         arrRooms.append(room[i])
        #
        #     #print(arrRooms)
        #     if len(arrRooms)>0:
        #         indX = int(arrRooms[1])
        #         indY = int(arrRooms[3])
        #         #print(str(indX) + " index" + str(indY))
        #         self.rooms[indX][indY]=(self.currentResidents[i].getLName())


            #now go in the rooms and set it to taken .
        arrRoomNum=[]
        lName = ""
        indx =-1
        indy=-1
        # chck if its empty or not.
        for x in self.currentResidents:
            #print(x.toString())
            try:
                arrRoomNum = x.getRoom()
                lName = x.getLName()
                indx= arrRoomNum[1]
                indy = arrRoomNum[3]
                indx = int(indx)
                indy = int(indy)
                self.rooms[indx][indy] = lName
            except Exception :
                break

    def checkout(self):
        counter=0
        lName = input("who are you checking out ?")
        try:
            for i in self.currentResidents:
                if lName == i.getLName():
                    room = i.getRoom()
                    indx = int(room[1])
                    indy = int(room[3])
                    print(str(indx) + " " + str(indy))
                    self.rooms[indx][indy]="Empty"
                    break
                counter +=1
            del(self.currentResidents[counter])
            print(self.rooms)
        except IndexError:
            print("Guest not inhouse unable to check out")