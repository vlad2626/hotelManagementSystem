from typing import Any


class guest:

    def __init__(self, fName,lName,lAge,lPhone,lCC, roomNum):
        self.fName = fName
        self.lName = lName
        self.lAge = lAge
        self.lphone = lPhone
        self.lCC = lCC
        self.roomNum = roomNum

    def getCC(self):
        return  self.lCC

    def setCC(self , num):
        exit

    def encrypt(self , ccNum):
        nums = [1,2,3,4,5,6,7,8,9,0]
        arr= ccNum.split()
        newCC = []
        for i in arr:
            enc = int((i *5)/2)
            newCC.append(enc)
        return newCC
    def decrypt(self, ccNum):
        arr= ccNum.split()
        newCC= []
        for i in arr:
            enc = int((i/5) * 2)
            newCC.append(enc)
        return newCC

    def savePerson(self, object):
        b = object.toStringSave()
        arr = b.split(" ")
        infile = False
        file = open("guestInfo.txt", "r")

        #checks to see if duplucate
        for x in file:
            if x == object.toStringSave():
                infile== True
                file.close()
        if infile== False:
            file = open("guestInfo.txt", "a")
            file.write(object.toStringSave())
            # next save to exel spreadsheet , make headers
            file.close()

    def getFName(self):
        return self.fName
    def getLName(self):
        return self.lName
    def getRoom(self):
        return self.roomNum
    def toStringSave(self):
        return  str(self.fName) + " " + str(self.lName) + " " +  str(self.lAge) + " " + str(self.lphone) + " " + str(self.lCC) + " " + str(self.roomNum) + '\n'

    def toString(self):
        return " First Name: " + self.fName + ", Last Name" + self.lName +  ", Age" + self.lAge + " Phone Number" + self.lphone + ", CC " + self.lCC + " RoomNum " + self.roomNum




