import random

class Userhandling:

    def __init__(self, username, password, salt):
        self.username = username # user input
        self.password = password # user input
        self.salt = salt # retrived from file from username
        # salt is a random number added to passwords to lower likleyhood of hash function collisions

    @staticmethod
    def calchash(string):
        total = 0 # sum each value for a folding hash
        for i in range(0,len(string)):
            total = total + ord(string[0]) # ord gives ascii value of character
        return total

    def makeaccount(self):
        password = input("What is your password: ")
        salt = random.randint(0, 100) # A random value added to end to make all passwords different
        salt = str(salt) # Make a string so ord can be used
        password = password.join(salt) # join so password is with salt
        password = self.calchash(password) # calculate the modulo 26 hash
        data = password, salt
        file = open("passwords.txt", "a") # File writing
        file.write(str(data))

    def search(self, password):
        file = open("passwords.txt", "r")

