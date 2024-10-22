import random
import hashlib

class Userhandling:

    def __init__(self, username, password, salt):
        self.username = username # user input
        self.password = password # user input
        self.salt = salt # retrived from file from username
        # salt is a random number added to passwords to lower likleyhood of hash function collisions

    @staticmethod
    def calchash(string):
        hash = hashlib.sha512()
        hash.update(string.encode())
        return hash

    def makeaccount(self):
        password = input("What is your password: ")
        file = open("passwords.txt", "r")
        hash = hashlib.sha512()
        hash.update(password)
        print(hash)

    def search(self, password):
        file = open("passwords.txt", "r")


