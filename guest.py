from typing import Any


class guest:

    def __init__(self, fName,lName,lAge,lPhone,lCC):
        self.fName = fName
        self.lName = lName
        self.lAge = lAge
        self.lphone = lPhone
        self.lCC = lCC

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
        # next save to exel spreadsheet , make headers

        exit


    def toStringSave(self):
        return  self.fName + " " +self.lName + " " +  self.lAge + " " + self.lphone + " " + self.lCC

    def toString(self):
        return " First Name: " + self.fName + ", Last Name" + self.lName +  ", Age" + self.lAge + " Phone Number" + self.lphone + ", CC " + self.lCC




