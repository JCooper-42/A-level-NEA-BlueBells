from OpenData import fileManagment

class FunFacts(fileManagment):

    def __init__(self):
        self.xvelocity = []
        self.yvelocity =[]
        self.zvelocity = []

    def getData(self):
        FileM = fileManagment() # Make an instance of FileM in diff class
        data = FileM.getName()
        FileM.openCSV(fileName = data)
        self.xvelocity, self.yvelocity, self.zvelocity, self.time = FileM.formatData() #unpack in to instance vars

    def FunFact1(self): #Top rep speed
        print(self.yvelocity)
        print(f"Your maximum lift speed was {max(self.yvelocity, default=0)}")

    def FunFact2(self):
        print(f"Your minimum lift speed was {min(self.yvelocity)}")

    def FunFact3(self):
        Ek = 0.5 * 10 * {max(self.yvelocity)}
        calories = Ek / 4.81
        print("Lifting 10kg at this speed, you burned roughly", calories)


if __name__ == '__main__':
    FunF = FunFacts()
    FunF.getData()
    print(FunF.FunFact1())
