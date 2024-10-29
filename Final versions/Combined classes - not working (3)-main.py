from microbit import *
import time as t


class Menu:

    def __init__(self):
        self.mass = 0
        self.weight = 0
        self.queue = []  # Create a list to use as a priority queue ADT
        self.running = "True"

    def termimate(self):
        display.clear()
        self.running = "False"

    def increase_mass(self):
        self.mass += 5
        display.show(self.mass)  # Inbuilt method

    def decrease_mass(self):
        if self.mass > 0:  # So can't have negative mass
            self.mass -= 5
            display.show(self.mass)

    def select_mass(self):
        self.weight = self.mass * 9.81  # mass --> weight
        display.show(self.weight)
        self.mass = 0  # reset for next lift

    def enqueue(self, Button_Press):
        if "AB" not in self.queue:  # AB takes priority
            self.queue.append(Button_Press)

    def dequeue(self):
        if self.queue:
            button = self.queue.pop(0)  # pops first item in queue
            if button == "A":
                self.decrease_mass()
            elif button == "B":
                self.increase_mass()
            elif button == "AB":
                self.select_mass()

    def menu_logic(self):
        while not pin_logo.is_touched() and self.running == "True":
            # Check button presses and enqueue actions
            if button_a.was_pressed():
                self.enqueue("A")
            if button_b.was_pressed():
                self.enqueue("B")
            if len(self.queue) != 0:
                self.dequeue()
        self.select_mass()


class DataCollection:

    def __init__(self):
        self.df = DataFilter(self)
        self.time = 0  # timer for the workout
        self.x_Readings = []
        self.y_Readings = []
        self.z_Readings = []
        self.stop_flag = False

    def timer(self):
        while not self.stop_flag:  # Loop for clock
            # Stops when stop_flag evaluates to true
            t.sleep(1)
            self.time += 1

    def get_time(self):  # returns length of workout
        return self.time

    def accelerometer(self):
        while not self.stop_flag:
            t.sleep(0.1)
            x_acceleration = accelerometer.get_x()
            # Built in getter method
            x_acceleration = x_acceleration / 1000 * 9.81
            # Convert miligs to ms^-1
            self.x_Readings.append(x_acceleration)
            # Write to self.x_Readings for exporting
            y_acceleration = accelerometer.get_y()
            y_acceleration = y_acceleration / 1000 * 9.81
            self.y_Readings.append(y_acceleration)
            z_acceleration = accelerometer.get_z()
            z_acceleration = z_acceleration / 1000 * 9.81
            self.z_Readings.append(z_acceleration)
            self.stop()
        self.df.get_values()

        # 3 plane accelerometer
        # 3 lists used to store a from each plane

    def get_acceleration(self):
        return self.x_Readings, self.y_Readings, self.z_Readings

    def stop(self):  # stop flag
        if button_a.is_pressed():
            self.stop_flag = True
            # Used to show if user is working out or not


class DataFilter:

    def __init__(self, DataCollection):
        self.DataSet = DataCollection
        # Using existing instance of DataCollection
        self.AccelXtf = []
        self.AccelYtf = []
        self.AccelZtf = []
        self.time = 0

    def get_values(self):
        self.time = self.DataSet.get_time()
        self.UnpackAccel()

    def UnpackAccel(self):
        (self.AccelXtf, self.AccelYtf, self.AccelZtf) = self.DataSet.get_acceleration()
        self.LPF()

    def LPF(self):
        print(self.AccelXtf)
        i = len(self.AccelXtf) - 1  # Start from last index
        while i >= 0:  # Go backward to avoid index shifting issues
            if self.AccelXtf[i] < -28 or self.AccelXtf[i] > 28:
                self.AccelXtf.pop(i)  # Remove by index
            if self.AccelYtf[i] < -28 or self.AccelYtf[i] > 28:
                self.AccelYtf.pop(i)
            if self.AccelZtf[i] < -28 or self.AccelZtf[i] > 28:
                self.AccelZtf.pop(i)
            i -= 1  # Decrement index
        self.medianfilter()

    def calculate_median(self, values):
        sortedVals = sorted(values)
        mid_index = len(sortedVals) // 2
        if len(sortedVals) % 2 == 0:
            median = (sortedVals[mid_index - 1] + sortedVals[mid_index]) / 2
        else:
            median = sortedVals[mid_index]
        return median

    def medianfilter(self):
        for i in range(0, len(self.AccelXtf) - 2):
            values = [self.AccelXtf[i], self.AccelXtf[i + 1], self.AccelXtf[i + 2]]
            median = self.calculate_median(values)
            self.AccelXtf[i] = abs(int(round(median)))  # Replace the value with the median

        for i in range(0, len(self.AccelZtf) - 2):
            values = [self.AccelZtf[i], self.AccelZtf[i + 1], self.AccelZtf[i + 2]]
            median = self.calculate_median(values)
            self.AccelZtf[i] = abs(int(round(median)))  # Replace the value with the median

        for i in range(0, len(self.AccelYtf) - 2):
            values = [self.AccelYtf[i], self.AccelYtf[i + 1], self.AccelYtf[i + 2]]
            median = self.calculate_median(values)
            self.AccelYtf[i] = abs(int(round(median)))  # Replace the value with the median


class intergrate(DataFilter):

    def __init__(self):
        self.Xvel = []  # Velocity first intergral
        self.Yvel = []
        self.Zvel = []

        self.Xdisp = []  # Displacment intergral of velocity
        self.Ydisp = []
        self.Zdisp = []
        DataFilter.__init__(self, DataCollection)  # Inherit acceleration

    def leftReinamnnIntergral(self):
        # Define rectangle widths (dt)
        dtx = (self.time) / (len(self.AccelXtf) - 1)
        dty = (self.time) / (len(self.AccelYtf) - 1)
        dtz = (self.time) / (len(self.AccelZtf) - 1)
        for i in range(0, len(self.AccelXtf)):
            self.Xvel.append(dtx * self.AccelXtf[i])
            self.Xdisp.append(dtx * self.AccelXtf[i])

        for j in range(0, len(self.AccelYtf)):
            self.Yvel.append(dty * self.AccelXtf[j])
            self.Ydisp.append(dty * self.AccelXtf[j])

        for z in range(0, len(self.AccelXtf)):
            self.Zvel.append(dtz * self.AccelZtf[z])
            self.Zdisp.append(dtz * self.AccelZtf[z])


class driver(Menu, DataCollection, DataFilter):
    def drive(self):
        self.menu_logic()
        if accelerometer.was_gesture('shake'):
            self.termimate()


runner = driver()
runner.drive()
