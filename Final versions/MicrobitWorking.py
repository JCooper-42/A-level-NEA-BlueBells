from microbit import *
import time as t
import log


class Menu:
    def __init__(self):
        self.mass = 0
        self.weight = 0
        self.queue = []  # Priority queue
        self.running = True  # Changed to boolean for simplicity

    def terminate(self):
        display.clear()
        self.running = False

    def increase_mass(self):
        self.mass += 5
        display.show(str(self.mass))  # Convert to string for display
        t.sleep(0.2)
        display.clear()

    def decrease_mass(self):
        if self.mass > 0:  # Prevent negative mass
            self.mass -= 5
            display.show(str(self.mass))
            t.sleep(0.2)
            display.clear()

    def select_mass(self):
        self.weight = self.mass * 9.81  # Convert mass to weight
        print(self.weight)  # Debugging output
        display.scroll(str(int(self.weight)))  # Convert to int and display
        t.sleep(0.2)
        self.mass = 0  # Reset mass for next use
        self.terminate()
        return 1

    def enqueue(self, button_press):
        if "AB" not in self.queue:  # Prioritize AB
            self.queue.append(button_press)
        else:
            self.queue = ["AB"]  # Clear queue and prioritize AB

    def dequeue(self):
        if self.queue:
            button = self.queue.pop(0)  # Process first item in queue
            if button == "A":
                self.decrease_mass()
            elif button == "B":
                self.increase_mass()
            elif button == "AB":
                self.select_mass()

    def menu_logic(self):
        while not pin_logo.is_touched() and self.running:
            if button_a.was_pressed():
                self.enqueue("A")
            if button_b.was_pressed():
                self.enqueue("B")
            if button_a.is_pressed() and button_b.is_pressed():
                self.enqueue("AB")
            if len(self.queue) > 0:
                self.dequeue()


class DataCollection:
    def __init__(self):
        self.df = DataFilter(self)
        self.time = 0  # Timer for workout
        self.x_Readings = []
        self.y_Readings = []
        self.z_Readings = []
        self.stop_flag = False

    def accelerometer(self):
        while not self.stop_flag:
            t.sleep(1)
            x_acceleration = accelerometer.get_x() / 1000 * 9.81
            self.x_Readings.append(x_acceleration)
            y_acceleration = accelerometer.get_y() / 1000 * 9.81
            self.y_Readings.append(y_acceleration)
            z_acceleration = accelerometer.get_z() / 1000 * 9.81
            self.z_Readings.append(z_acceleration)

            self.time += 1

            if button_a.is_pressed() and self.time > 0:  # Stop condition
                self.stop_flag = True

        self.df.get_values()

    def get_acceleration(self):
        return self.x_Readings, self.y_Readings, self.z_Readings

    def get_time(self):
        print(self.time)
        return self.time


class DataFilter:
    def __init__(self, data_collection):
        self.DataSet = data_collection
        self.AccelXtf = []
        self.AccelYtf = []
        self.AccelZtf = []
        self.time = 0

    def get_values(self):
        self.time = self.DataSet.get_time()
        print("Time:", self.time)
        self.unpack_accel()

    def unpack_accel(self):
        (self.AccelXtf, self.AccelYtf, self.AccelZtf) = self.DataSet.get_acceleration()
        self.LPF()

    def LPF(self):
        self.AccelXtf = [x for x in self.AccelXtf if -28 <= x <= 28]
        self.AccelYtf = [y for y in self.AccelYtf if -28 <= y <= 28]
        self.AccelZtf = [z for z in self.AccelZtf if -28 <= z <= 28]
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
        for i in range(len(self.AccelXtf) - 2):
            values = self.AccelXtf[i:i + 3]
            median = self.calculate_median(values)
            self.AccelXtf[i] = abs(round(median))

        for i in range(len(self.AccelYtf) - 2):
            values = self.AccelYtf[i:i + 3]
            median = self.calculate_median(values)
            self.AccelYtf[i] = abs(round(median))

        for i in range(len(self.AccelZtf) - 2):
            values = self.AccelZtf[i:i + 3]
            median = self.calculate_median(values)
            self.AccelZtf[i] = abs(round(median))

    def tuple_to_export(self):
        return self.AccelXtf, self.AccelYtf, self.AccelZtf  # Export data as tuple


class Integrate:
    def __init__(self, accel_tuple, time):
        self.AccelXtf, self.AccelYtf, self.AccelZtf = accel_tuple  # Unpack tuple
        self.time = time  # Get time from DataFilter
        self.Xvel = []
        self.Yvel = []
        self.Zvel = []
        self.Xdisp = []
        self.Ydisp = []
        self.Zdisp = []

    def left_reimann_integral(self):
        print("Starting integration...")
        dtx = self.time / len(self.AccelXtf) if len(self.AccelXtf) > 0 else 0
        dty = self.time / len(self.AccelYtf) if len(self.AccelYtf) > 0 else 0
        dtz = self.time / len(self.AccelZtf) if len(self.AccelZtf) > 0 else 0

        for i in range(len(self.AccelXtf)):
            self.Xvel.append(dtx * self.AccelXtf[i])
            self.Xdisp.append(dtx * sum(self.Xvel))

        for j in range(len(self.AccelYtf)):
            self.Yvel.append(dty * self.AccelYtf[j])
            self.Ydisp.append(dty * sum(self.Yvel))

        for z in range(len(self.AccelZtf)):
            self.Zvel.append(dtz * self.AccelZtf[z])
        self.Zdisp.append(dtz * sum(self.Zvel))

        print("X Velocity:", self.Xvel)
        print("Y Velocity:", self.Yvel)
        print("Z Velocity:", self.Zvel)

        # Return all velocities
        return self.Xvel, self.Yvel, self.Zvel

    def cut0(self):
        pass  # Cut all the 0's in the list so less memory used

    # Compress???


class Driver(Menu, DataCollection):
    def __init__(self):
        Menu.__init__(self)
        DataCollection.__init__(self)
        self.data_filter = DataFilter(self)  # Create DataFilter instance

    def drive(self):
        self.menu_logic()
        if self.select_mass() == 1:
            self.accelerometer()  # Collect data
            self.data_filter.get_values()  # Filter data
            accel_tuple = self.data_filter.tuple_to_export()  # Export tuple
            time_value = self.data_filter.time  # Get time
            integrator = Integrate(accel_tuple, time_value)
            xresult, yresult, zresult = integrator.left_reimann_integral()
            for i in range(0, len(xresult)):
                log.add({
                    'xresult': xresult[i],
                    'yresult': yresult[i],
                    'zresult': zresult[i]
                })


runner = Driver()
runner.drive()

