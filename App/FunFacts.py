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

    def intergrateY(self):
        for i in range(0, len(self.yvelocity))::
                self.ydisplacment.append(dty * self.AccelYtf[j])

    def FunFact1(self):
        print("Your maximum velocity was", max(self.yvelocity))

    def FunFact2(self)  :
        print("Your minimum velcoity was", min(self.yvelocity))

if __name__ == '__main__':
    FunF = FunFacts()
    FunF.getData()
