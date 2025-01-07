from OpenData import fileManagment

class FunFacts(fileManagment):

    def __init__(self):
        self.xvelocity = []
        self.yvelocity = []
        self.zvelocity = []
        self.ydisplacment = []

    def getData(self):
        FileM = fileManagment() # Make an instance of FileM in diff class
        data = FileM.getName()
        FileM.openCSV(fileName = data)
        self.xvelocity, self.yvelocity, self.zvelocity, self.time = FileM.formatData() #unpack in to instance vars

    def FunFact1(self):
        statment = f"Your maximum velocity was {max(self.yvelocity)}"
        return statment

    def FunFact2(self)  :
        statment = f"Your minimum velcoity was {min(self.yvelocity)}"
        return statment

    def FunFact3(self):
        total = 0
        for i in range(0, len(self.yvelocity) - 1):
            total = total + float(self.yvelocity[i])
        statment = f"Your total velocity was {str(total)}"
        return statment


if __name__ == '__main__':
    FunF = FunFacts()
    FunF.getData()
