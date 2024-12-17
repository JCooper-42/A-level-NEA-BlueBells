from OpenData import fileManagment

class FunFacts(fileManagment):

    def __init__(self):
        self.xdisp = []
        self.ydisp = []
        self.zdisp = []

    def getData(self):
        FileM = fileManagment() # Make an instance of FileM in diff class
        data = FileM.getName()
        FileM.openCSV(fileName = data)
        self.xvelocity, self.yvelocity, self.zvelocity, self.time = FileM.formatData() #unpack in to instance vars


    def left_reimann_integral(self):
        print("Starting integration...")
        dtx = self.time / len(self.xvelocity) if len(self.xvelocity) > 0 else 0
        dty = self.time / len(self.yvelocity) if len(self.yvelocity) > 0 else 0
        dtz = self.time / len(self.zvelocity) if len(self.zvelocity) > 0 else 0

        for i in range(len(self.xvelocity)):
            self.xdisp.append(dtx * self.xvelocity[i])
            self.xdisp.append(dtx * sum(self.xdisp))

        for j in range(len(self.yvelocity)):
            self.ydisp.append(dty * self.yvelocity[j])
            self.ydisp.append(dty * sum(self.ydisp))

        for z in range(len(self.zvelocity)):
            self.zdisp.append(dtz * self.zvelocity[z])
        self.zdisp.append(dtz * sum(self.zdisp))

        print("X Velocity:", self.xdisp)
        print("Y Velocity:", self.ydisp)
        print("Z Velocity:", self.zdisp)

        # Return all velocities
        return self.xdisp, self.ydisp, self.zdisp

def FunFact1(self):
        pass

if __name__ == '__main__':
    FunF = FunFacts()
    FunF.getData()
